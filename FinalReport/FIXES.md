# Tablero KPI COINSA-MATIK - Fixes & Issues

## Status: v1.1 - Funcional

---

## ✅ Bugs Resueltos

### BUG-01: Logo incorrecto
- **Estado:** 🟡 Pendiente
- **Descripción:** El logo es un SVG generado placeholder, no el logo real de COINSA-MATIK
- **Solución:** Reemplazar con logo real (necesita archivo PNG/SVG del cliente)

### BUG-02: Dropdown "Vistas" texto blanco sobre blanco
- **Estado:** ✅ FIXED
- **Solución:** Agregado `color: var(--text)` al CSS de `.toolbar select`

### BUG-03: Pipeline Activo = 0 cuando hay won/lost
- **Estado:** ✅ FIXED
- **Solución:** Pipeline ahora excluye etapas: cerrado, archivo, terminado, perdido

### BUG-04: Tasa Conversión incorrecta
- **Estado:** ✅ FIXED  
- **Causa raíz:** Odoo marca perdidas como `Active=False`, no se exportaban
- **Solución export:** Usar filtro `Active is Yes OR Active is No` para incluir todo
- **Solución dashboard:** 
  - Detecta `Is Won = "Lost"` correctamente
  - Muestra DOS métricas de conversión:
    - **Conversión (Opps):** count-based (ej: 80.1%)
    - **Conversión (Revenue):** revenue-based (ej: 74.5%)

### BUG-05: Top Clientes muestra cliente inexistente
- **Estado:** 🔍 Pendiente investigar
- **Descripción:** "OPERADORA DE MINAS E INST" no encontrado en Odoo
- **Causa posible:** Nombre truncado en CSV o filtros diferentes

---

## 🟢 Features Implementados

### FEAT-04: Doble métrica de conversión
- **Conversión (Opps):** Ganadas / Total cerradas (por cantidad)
- **Conversión (Revenue):** Revenue ganado / Revenue cerrado total

### FEAT-05: KPIs adicionales
- **Perdidas:** Total revenue perdido con conteo de opps
- **Ciclo Promedio:** Días promedio para cerrar

### FEAT-06: KPIs de enlace Sales/Accounting
Usando el campo `Sum of Orders` del CRM (viene de `sale.order`):
- **Pedidos Generados:** Total de pedidos creados desde opps ganadas
- **Quote-to-Order:** % de conversión entre Expected Revenue y pedidos reales
- **Opps con Pedido:** % de opps ganadas que tienen orden creada (compliance)

---

## 🟡 Mejoras Pendientes

### FEAT-01: Soporte multi-divisa
- **Decisión:** Por ahora todo MXN (usuarios instruidos a usar solo MXN en CRM)

### FEAT-02: Vista por rol funcional
- **Estado:** Pendiente
- **Descripción:** El dropdown de vistas no hace nada actualmente

### FEAT-03: Logo real del cliente
- **Estado:** Pendiente archivo del cliente

---

## Instrucciones de Export

### Filtro correcto para exportar:
```
Active is Yes OR Active is No
```
Esto incluye oportunidades activas + perdidas en un solo archivo.

### Campos clave:
- `Is Won`: "Won", "Pending", "Lost"
- `Stage/Stage Name`: Etapa actual
- `Expected Revenue`: Valor en MXN
- `Active`: True/False (perdidas = False)

---

## Historial de Cambios

| Fecha | Versión | Cambios |
|-------|---------|--------|
| 2026-11-03 | v1.0 | Dashboard inicial |
| 2026-11-03 | v1.1 | Fix conversión, doble métrica, KPIs adicionales |
| 2026-11-03 | v1.2 | KPIs de enlace Sales/Accounting (Sum of Orders) |
| 2026-11-03 | v1.3 | Estados de RPT alineados con reportes-tracker.md; archivos movidos a FinalReport |
| 2026-11-03 | v1.4 | Motivos de pérdida, conversión entre etapas, actividad del pipeline (aging), pronóstico vs real; fix atribución Ingeniería |

---

## v1.4 Detalle
- **Motivos de pérdida:** gráfica de `Lost Reason/Description` (RPT-24)
- **Conversión entre etapas (aprox.):** opps en la etapa o posteriores, y % que pasa a la siguiente (RPT-05)
- **Actividad del pipeline:** sin actividad programada, actividad atrasada (`Kanban State`), última acción >7 y >15 días (RPT-18)
- **Pronóstico vs real:** pronóstico = `Prorated Revenue` por mes de `Expected Closing` (excluye perdidas); real = `Expected Revenue` de ganadas por mes de `Closed Date` (RPT-21)
- **Fix Ingeniería:** antes sumaba el equipo "Sales" como ingeniería; ahora solo equipos que contengan "ingenier" (sin equipo de ingeniería en el export actual, RPT-11 mostrará 0)

### Pendientes conocidos
- BUG-01 logo real
- BUG-05 cliente OPERADORA DE MINAS
- FEAT-02 dropdown de Vista sin función
- Cobranza y margen requieren datos de Contabilidad/costos (fuera de alcance CRM)
