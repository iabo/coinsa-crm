#!/usr/bin/env python3
"""Parsea "Presupuesto Coinsamatik 2026.xlsx" y emite el JSON compacto que se
embebe en CoinsaDashboard.html (var PRESUPUESTO_2026).

Uso:
    python3 parse_presupuesto.py [ruta_xlsx] [ruta_csv_odoo]

- Tabla 1 de la hoja "Presupuesto Coinsamatik": vendedor × 12 meses (+ fila
  VENTAS TOTALES como total de compañía).
- El CSV de Odoo (export en inglés o español) se usa para hacer el matching
  de nombres de vendedor entre presupuesto y Odoo.
- Salida stdout: JSON compacto (para embeber). Salida stderr: reporte del
  matching para revisión manual.
"""
import sys
import json
import re
import csv
import unicodedata

import openpyxl

XLSX = sys.argv[1] if len(sys.argv) > 1 else 'Presupuesto Coinsamatik 2026.xlsx'
CSV = sys.argv[2] if len(sys.argv) > 2 else 'Juev53.csv'
ANIO = 2026

MESES = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO',
         'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']


def norm(name):
    """Uppercase, sin acentos ni puntuación, espacios colapsados."""
    s = unicodedata.normalize('NFD', str(name or '').upper())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = re.sub(r'[^A-Z0-9 ]+', ' ', s)
    return ' '.join(s.split())


def tokens(name):
    """Tokens significativos (longitud > 1, ignora iniciales como 'A.')."""
    return [t for t in norm(name).split() if len(t) > 1]


def read_odoo_sellers(path):
    with open(path, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit('CSV vacío: ' + path)
    vcol = next((k for k in rows[0] if 'endedor' in k or 'alesperson' in k), None)
    if vcol is None:
        raise SystemExit('No se encontró columna de vendedor en ' + path)
    out = []
    for r in rows:
        v = (r.get(vcol) or '').strip()
        if v and v not in out:
            out.append(v)
    return out


def main():
    wb = openpyxl.load_workbook(XLSX, data_only=True)
    ws = wb['Presupuesto Coinsamatik']

    # Localizar tabla 1: fila cuyo encabezado en col B sea 'VENDEDOR'
    header_row = None
    for r in range(1, 30):
        v = ws.cell(row=r, column=2).value
        if v and str(v).strip().upper() == 'VENDEDOR':
            header_row = r
            break
    if header_row is None:
        raise SystemExit('No se encontró la tabla vendedor × meses')

    vendedores = []
    company = None
    r = header_row + 1
    while r <= ws.max_row:
        name = ws.cell(row=r, column=2).value
        if name is None or str(name).strip() == '':
            break
        name = str(name).strip()
        meses = [float(ws.cell(row=r, column=c).value or 0) for c in range(3, 15)]
        if name.upper().startswith('VENTAS TOTALES'):
            company = meses
            break
        vendedores.append({'presupuesto': name, 'meses': meses})
        r += 1

    if not vendedores:
        raise SystemExit('No se leyeron vendedores del presupuesto')
    if company is None:
        company = [sum(v['meses'][i] for v in vendedores) for i in range(12)]

    calc = [sum(v['meses'][i] for v in vendedores) for i in range(12)]
    drift = max(abs(calc[i] - company[i]) for i in range(12))

    # Matching de nombres presupuesto -> Odoo
    odoo = read_odoo_sellers(CSV)
    for v in vendedores:
        tv = tokens(v['presupuesto'])
        matches = [o for o in odoo if norm(o) == norm(v['presupuesto'])]
        if not matches and tv:
            # primer token presente + casi todos los tokens restantes
            # (tolera typos como ESPINOSA/ESPINOZA y iniciales intermedias)
            need = max(2, len(tv) - 1)
            matches = [o for o in odoo
                       if tv[0] in norm(o).split()
                       and sum(1 for t in tv if t in norm(o).split()) >= need]
        if len(matches) > 1:
            print(f'AVISO: "{v["presupuesto"]}" coincide con varios vendedores Odoo: {matches}',
                  file=sys.stderr)
        v['odoo'] = matches[0] if matches else None

    data = {
        'anio': ANIO,
        'meses': MESES,
        'company': [round(x, 2) for x in company],
        'vendedores': [
            {'presupuesto': v['presupuesto'], 'odoo': v['odoo'],
             'meses': [round(x, 2) for x in v['meses']]}
            for v in vendedores
        ],
    }
    print(json.dumps(data, ensure_ascii=False, separators=(',', ':')))

    # Reporte legible para revisión
    print('\n== Matching presupuesto -> Odoo ==', file=sys.stderr)
    for v in vendedores:
        print(f"  {v['presupuesto']:<45} -> {v['odoo'] if v['odoo'] else '(sin match)'}",
              file=sys.stderr)
    unmatched = [v['presupuesto'] for v in vendedores if not v['odoo']]
    if unmatched:
        print('\nSin match en Odoo (no tendrán meta por vendedor):', file=sys.stderr)
        for u in unmatched:
            print('  - ' + u, file=sys.stderr)
    print(f"\nCompañía (VENTAS TOTALES): {[round(x) for x in company]}", file=sys.stderr)
    print(f"Drift max vs suma de vendedores: {drift:.2f}", file=sys.stderr)


if __name__ == '__main__':
    main()
