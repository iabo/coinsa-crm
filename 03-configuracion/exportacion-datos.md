# Campos `crm.lead` — Odoo 16 · Referencia para Exportación CSV

> Documento técnico de referencia para alimentar el **Tablero Comercial COINSA-MATIK**.
> Fuente: código fuente oficial `odoo/odoo` rama 16.0 (`addons/crm/models/crm_lead.py`).

---

## 1. Estado actual del CSV extraído

El archivo `Lead  oportunidad (crm.lead).csv` contiene las siguientes columnas
y sus nombres técnicos reales en Odoo:

| Columna en CSV exportado | Campo técnico Odoo | Tipo | Notas |
|---|---|---|---|
| Oportunidad | `name` | Char | Nombre del registro |
| Etapa | `stage_id` → `stage_id/name` | Many2one | Exporta el nombre de la etapa |
| Ingreso esperado | `expected_revenue` | Monetary | Monto bruto sin ponderar |
| Probabilidad | `probability` | Float | 0–100% |
| Nombre del contacto | `contact_name` | Char | Persona de contacto |
| Correo electrónico | `email_from` | Char | Email principal |
| Teléfono | `phone` | Char | |
| Vendedor | `user_id` → `user_id/name` | Many2one | |
| Equipo de ventas | `team_id` → `team_id/name` | Many2one | |
| Etiquetas/Nombre de etiqueta | `tag_ids/name` | Many2many | Industria / segmento |
| Última acción | `date_action_last` | Datetime | Última acción registrada |
| Fecha límite de mi actividad | `my_activity_date_deadline` | Date | Solo del usuario activo |
| Actividades | `activity_summary` | Char | Resumen de actividad pendiente |
| Actividades/Asignada a | `activity_ids/user_id/name` | Relación | Sub-campo actividades |
| Actividades/Acción | `activity_ids/activity_type_id/name` | Relación | Sub-campo actividades |
| Actividades/Fecha de vencimiento | `activity_ids/date_deadline` | Relación | Sub-campo actividades |
| Motivo de pérdida/Descripción | `lost_reason_id/name` | Many2one | Solo si está perdida |

---

## 2. Campos críticos FALTANTES para el tablero

Estos campos **no están en el CSV actual** pero son necesarios para los KPIs,
el embudo, el ranking por vendedor y la lectura ejecutiva:

### 2.1 Pipeline y estado

| Campo técnico | Etiqueta UI (es) | Tipo | Para qué se usa en el tablero |
|---|---|---|---|
| `active` | Activo | Boolean | Distinguir activas vs archivadas (perdidas) |
| `type` | Tipo | Selection | `lead` vs `opportunity` |
| `won_status` | Es ganado | Selection | `won` / `lost` / `normal` |
| `kanban_state` | Estado Kanban | Selection | Alerta: `grey`=sin actividad, `red`=vencida |
| `priority` | Prioridad | Selection | `0`=normal, `1`=bajo, `2`=alto, `3`=muy alto |

### 2.2 Ingresos y métricas financieras

| Campo técnico | Etiqueta UI (es) | Tipo | Para qué se usa |
|---|---|---|---|
| `prorated_revenue` | Ingreso ponderado | Monetary | Pipeline activo = `expected_revenue × probability/100` |
| `sale_amount_total` | Suma de pedidos | Monetary | Ventas confirmadas reales (desde `sale.order`) |
| `quotation_count` | Número de cotizaciones | Integer | Actividad comercial |

### 2.3 Fechas esenciales

| Campo técnico | Etiqueta UI (es) | Tipo | Para qué se usa |
|---|---|---|---|
| `create_date` | Fecha de creación | Datetime | Edad del lead, tendencia mensual |
| `date_deadline` | Cierre esperado | Date | Forecast, oportunidades vencidas |
| `date_closed` | Fecha de cierre | Datetime | Cuándo se ganó o perdió |
| `date_last_stage_update` | Últ. actualiz. de etapa | Datetime | Alertas de inactividad (AUT-03) |
| `date_open` | Fecha de asignación | Datetime | Tiempo de respuesta |
| `day_open` | Días para asignar | Float | Velocidad de respuesta |
| `day_close` | Días para cerrar | Float | Ciclo de ventas |

### 2.4 Cliente / empresa

| Campo técnico | Etiqueta UI (es) | Tipo | Para qué se usa |
|---|---|---|---|
| `partner_id` → `partner_id/name` | Cliente | Many2one | Nombre del cliente vinculado |
| `partner_name` | Nombre de empresa | Char | Empresa cuando no hay partner_id |

### 2.5 Marketing (UTM / fuentes)

| Campo técnico | Etiqueta UI (es) | Tipo | Para qué se usa |
|---|---|---|---|
| `source_id/name` | Origen | Many2one | Fuente del lead (web, referido, etc.) |
| `medium_id/name` | Medio | Many2one | Canal (email, evento, redes…) |
| `campaign_id/name` | Campaña | Many2one | Campaña de marketing |
| `referred` | Referido por | Char | Empresa/contacto que refirió |

---

## 3. Configuración de exportación recomendada (Odoo 16)

### Cómo exportar en Odoo UI

1. **CRM → Pipeline** (vista lista)
2. Seleccionar todos los registros
3. **Acción → Exportar**
4. Desmarcar *"Solo campos que pueden importarse"*
5. Agregar los campos de la lista de abajo
6. Guardar plantilla como `"Tablero Comercial COINSA"`
7. Exportar como **CSV**

### Lista completa de campos a exportar

```
name
stage_id/name
type
active
won_status
kanban_state
priority
expected_revenue
prorated_revenue
sale_amount_total
probability
partner_id/name
partner_name
contact_name
email_from
phone
user_id/name
team_id/name
tag_ids/name
create_date
date_deadline
date_closed
date_last_stage_update
date_action_last
date_open
day_open
day_close
lost_reason_id/name
source_id/name
medium_id/name
campaign_id/name
referred
activity_summary
my_activity_date_deadline
```

---

## 4. Notas importantes sobre campos relacionales (Many2one / Many2many)

- **Many2one** (`stage_id`, `user_id`, `team_id`): en el exportador de Odoo, agregar
  el sub-campo `/name` para obtener el texto legible. Sin `/name` se exporta el ID numérico.
- **Many2many** (`tag_ids`): Odoo exporta los valores separados por coma en una sola celda.
  Si una oportunidad tiene múltiples etiquetas, aparecerán así: `MANUFACTURA,MINERIA`.
- **`active`**: las oportunidades perdidas tienen `active = False` y no aparecen en vistas
  normales. Para exportarlas hay que activar el filtro **"Archivadas"** antes de exportar,
  o exportar desde **CRM → Análisis → Pipeline** con el filtro de perdidas.
- **`won_status`**: valores posibles — `won` (ganada), `lost` (perdida), `normal` (en progreso).
- **`type`**: valores posibles — `lead` (lead sin calificar), `opportunity` (oportunidad activa).

---

## 5. Campos adicionales útiles para reportes RPT específicos

| Campo técnico | RPT relacionado | Notas |
|---|---|---|
| `day_close` | Ciclo de venta promedio | Días entre asignación y cierre |
| `recurring_revenue` | MRR / contratos | Solo si se usa módulo de ingresos recurrentes |
| `description` | Notas internas | HTML; puede contener texto largo |
| `color` | — | Índice de color en kanban (0–11) |
| `calendar_event_count` | Reuniones por oportunidad | Número de reuniones agendadas |

---

## 6. Campos de cobranza (modelo `account.move`)

El tablero tiene una sección de **Cobranza** que **no viene del modelo `crm.lead`**.
Para esa sección se requiere una exportación separada desde **Contabilidad → Clientes → Facturas**:

| Columna necesaria | Campo técnico (`account.move`) |
|---|---|
| Número de factura | `name` |
| Cliente | `partner_id/name` |
| Fecha de factura | `invoice_date` |
| Fecha de vencimiento | `invoice_date_due` |
| Monto total | `amount_total` |
| Monto pendiente | `amount_residual` |
| Estado | `payment_state` (`not_paid` / `partial` / `paid`) |
| Vendedor relacionado | `invoice_user_id/name` |

---

*Fuentes: `github.com/odoo/odoo` rama 16.0 · `addons/crm/models/crm_lead.py` · Documentación oficial Odoo 16.0*
