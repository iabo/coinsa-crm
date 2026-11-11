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

### BUG-06: Export en español no muestra datos
- **Estado:** ✅ FIXED
- **Causa raíz:** Odoo traduce encabezados y valores al idioma de la UI. 32 de 35 columnas cambian de nombre (`Ganado` → `Is Won`, `Ingreso esperado` → `Expected Revenue`, etc.), además de los valores: `Won/Pending/Lost` ↔ `Ganado/Pendiente/Perdido`, etapas con sufijo de probabilidad (`Cotizado 70%`) y estados de kanban.
- **Solución:** Función `normalizarExport()` en la carga del CSV: mapea encabezados ES→EN, normaliza `Is Won`, `Kanban State` y etapas (elimina sufijo ` NN%`, `Ingeniería` → `Diseño`). Ambos idiomas producen el mismo tablero.

### BUG-07: Número de alertas no cuadraba con la tabla
- **Estado:** ✅ FIXED
- **Causa raíz:** el número grande de alertas contaba TODAS las opps sin actividad (incluidas ganadas/perdidas), mientras la tabla contaba solo opps abiertas — dos fuentes distintas. Además `Last Action` viene vacío en todo el export actual, por lo que ">7 días / >15 días" siempre daba 0.
- **Solución:** única fuente de verdad: alertas calculadas solo para opps abiertas (Pending fuera de etapas cerradas); el número grande = fila "Sin actividad programada" de la tabla. El aging usa `Last Action` o, en su defecto, `Last Stage Update`; filas renombradas a "Sin seguimiento hace >N días".

### BUG-08: Opps perdidas contadas como ganadas
- **Estado:** ✅ FIXED
- **Causa raíz:** `won` se definía como `Is Won = Won` **O** etapa "Cerrado". Había 3 opps perdidas asentadas en la etapa "Cerrado" que se sumaban como ganadas (ventas, conversión y rankings inflados).
- **Solución:** `Is Won` es la fuente autoritativa; se eliminó el fallback a etapa. Aplica también al Mix por Marca.

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

### FEAT-07: Guardar instantánea (Save)
- Botón "Guardar": genera un archivo HTML estático autónomo con los números exactos del dataset cargado — clona el tablero renderizado, congela cada gráfica como imagen (`chart.toBase64Image()`), y agrega banner con rango/período/equipo/meta/fecha de generación. Descarga vía Blob.
- Se eliminó el botón "Exportar PDF" (la instantánea HTML lo reemplaza como salida imprimible).

### FEAT-08: Rango de fechas en topbar + datepicker
- Dos datepickers (Desde/Hasta) arriba a la derecha, auto-llenados con min/max de `Created on` al cargar CSV.
- Editarlos activa el período "Personalizado" y filtra todas las métricas; elegir otro período restaura el rango completo.

### FEAT-09: Ventas por equipo con desglose por vendedor
- Reemplaza "Ventas por Equipo": barras apiladas (eje x = equipo, segmentos = vendedor) + tabla jerárquica (total del equipo + aporte y % de cada vendedor).

### FEAT-10: Instrucciones de carga siempre visibles
- Los pasos de export (antes en tooltip `?`) ahora son un bloque numerado visible en el sidebar, bajo el input de archivo.

### FEAT-11: Metas desde Presupuesto 2026 — ⏸️ PAUSADO (2026-11-10)
- **Estado:** la UI está comentada en el HTML (origen de meta, factor USD→MXN y modal "Ver metas y cálculo") para posible reuso posterior. El JSON `PRESUPUESTO_2026` y las funciones JS quedan embebidos; la rama de presupuesto en `calcularMetaInfo()` queda inactiva (fuente fija en manual). Para reactivar: descomentar el sidebar, el modal, los listeners y restaurar `const source` en `calcularMetaInfo`.
- `parse_presupuesto.py` parsea "Presupuesto Coinsamatik 2026.xlsx" (vendedor × 12 meses) y genera el JSON `PRESUPUESTO_2026` embebido en el dashboard; matching de nombres presupuesto→Odoo (11/13 exactos; MANUEL A. HERNANDEZ y JESUS A. LOPEZ no están en el export actual).
- Select de origen de meta: "Presupuesto 2026" (default) o "Manual". Con presupuesto: meta = suma de los meses que cubre el filtro activo × factor de conversión (default 18, USD→MXN, ajustable); acotada al equipo si hay filtro de equipo. Columnas "Meta" y "vs Meta" por vendedor y equipo en la tabla de FEAT-09.
- Moneda del presupuesto: **USD, confirmado por el cliente**. El factor de conversión a MXN es editable (default 18).
- Botón "Ver metas y cálculo" en el sidebar: modal con el origen de la meta, filtros/ventana activos, explicación del cálculo y tabla vendedor → equipo con presupuesto (USD) y meta (MXN) de la ventana, más el total de compañía.

### FEAT-12: Conversión sobre TODAS las oportunidades
- Nueva tarjeta "Conversión (Todas)": ganadas / total de opps del filtro (incluye abiertas), junto a las existentes por cerradas (opps y revenue).

### FEAT-13: Filtro por vendedor
- Select "Vendedor" en Filtros (sidebar), combinable con equipo y período. Recalcula todas las métricas, KPIs, gráficas y tablas para una sola persona. Incluido en el banner de la instantánea.

---

## 🟡 Mejoras Pendientes

### FEAT-01: Soporte multi-divisa
- **Decisión:** Por ahora todo MXN (usuarios instruidos a usar solo MXN en CRM)

### FEAT-02: Vista por rol funcional
- **Estado:** Pendiente
- **Descripción:** El dropdown de vistas no hace nada actualmente

### Metas de venta (reactivar FEAT-11) — dirección acordada 2026-11-11
- **Decisión:** enfoque híbrido a implementar y evaluar sobre la marcha: **meta global de compañía** (derivada del presupuesto 2026, promediada o por rangos) + **categorías de vendedor** (junior / senior / Sonora / foraneo, etc.) en lugar del presupuesto exacto por vendedor × mes. El mix por marca queda pospuesto.
- El JSON `PRESUPUESTO_2026` embebido y `parse_presupuesto.py` siguen disponibles como fuente para derivar las categorías y la meta de compañía.

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
| 2026-11-10 | v1.5 | Fix BUG-06: normalización de exports de Odoo en español (encabezados, Is Won, Kanban State, etapas) |
| 2026-11-10 | v1.6 | Features reunión stakeholders: instantánea HTML (FEAT-07), rango de fechas + datepicker (FEAT-08), ventas equipo→vendedor (FEAT-09), instrucciones visibles (FEAT-10), metas desde Presupuesto 2026 (FEAT-11) |
| 2026-11-11 | v1.7 | Retro presentación: fix alertas (BUG-07), fix ganadas/perdidas por etapa (BUG-08), Conversión (Todas) (FEAT-12), filtro por vendedor (FEAT-13) |

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
- Tabla vendedor × marca del xlsx podría alimentar metas de "Mix por Marca" (futuro)
