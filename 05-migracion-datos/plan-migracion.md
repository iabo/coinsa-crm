# Plan de Migración de Datos

## Principios de Migración

1. **Clean first, migrate later:** Los datos se limpian ANTES de migrar, no después
2. **Staging primero:** Toda migración se prueba en staging antes de producción
3. **Sin retorno sucio:** Si la validación falla en producción, se ejecuta el rollback
4. **Trazabilidad:** Cada registro migrado lleva referencia del origen

---

## Inventario de Datos a Migrar

| Entidad | Fuente | Formato | Volumen estimado | Prioridad |
|---|---|---|---|---|
| Contactos / Empresas | [Sistema actual] | Excel / CSV | ~ registros | Alta |
| Clientes activos | [Sistema actual] | Excel / CSV | ~ registros | Alta |
| Oportunidades activas | Excel de ventas | Excel | ~ registros | Alta |
| Historial de oportunidades | Excel de ventas | Excel | ~ registros | Media |
| Leads sin calificar | [Fuente] | Excel | ~ registros | Media |
| [Datos adicionales X] | [Fuente] | [Formato] | ~ registros | Baja |

---

## Mapeo de Campos

### Contactos y Empresas

| Campo Origen | Campo Odoo | Transformación | Regla de validación |
|---|---|---|---|
| Nombre empresa | `res.partner.name` | Ninguna | No nulo |
| RUC / NIT | `res.partner.vat` | Formatear sin guiones | Único |
| Email | `res.partner.email` | Minúsculas | Formato email válido |
| Teléfono | `res.partner.phone` | Normalizar formato | |
| Dirección | `res.partner.street` | | |
| Ciudad | `res.partner.city` | | |
| [Campo X] | `res.partner.[campo]` | | |

### Oportunidades

| Campo Origen | Campo Odoo | Transformación | Regla de validación |
|---|---|---|---|
| Nombre / descripción | `crm.lead.name` | | No nulo |
| Cliente | `crm.lead.partner_id` | Mapear a res.partner | Empresa debe existir |
| Vendedor responsable | `crm.lead.user_id` | Mapear a res.users | Usuario debe existir |
| Valor estimado | `crm.lead.expected_revenue` | Parsear número | ≥ 0 |
| Etapa actual | `crm.lead.stage_id` | Mapear a nueva etapa | Etapa debe existir |
| Fecha de cierre | `crm.lead.date_deadline` | Formato YYYY-MM-DD | Fecha válida |
| Estado (ganado/perdido) | `crm.lead.probability` | 100 o 0 | |

---

## Reglas de Calidad de Datos

| Regla | Campo | Acción si falla |
|---|---|---|
| Email único por contacto | `email` | Marcar como duplicado, revisar manualmente |
| Empresa no puede estar vacía | `partner_id` | Crear empresa genérica "Sin empresa" si no existe |
| Valor de oportunidad > 0 | `expected_revenue` | Poner 0 y marcar para revisión |
| Vendedor debe existir en Odoo | `user_id` | Asignar al administrador si no existe |
| Fecha de cierre no puede ser pasada | `date_deadline` | Actualizar a fecha +30 días si es pasada |

---

## Proceso de Migración

### Paso 1 — Extracción (Fase 1)
- [ ] Exportar datos de cada fuente en formato CSV/Excel
- [ ] Documentar estructura y cantidad de registros extraídos
- [ ] Archivar los archivos fuente originales (inmutables)

### Paso 2 — Limpieza y Transformación
- [ ] Eliminar duplicados por email / RUC
- [ ] Normalizar formatos de teléfonos y correos
- [ ] Completar campos obligatorios faltantes
- [ ] Mapear valores al catálogo de Odoo (etapas, usuarios, etc.)
- [ ] Validar integridad referencial (oportunidades → empresas)
- [ ] Generar reporte de calidad antes de cargar

### Paso 3 — Carga en Staging
- [ ] Cargar contactos / empresas primero
- [ ] Cargar oportunidades (dependen de contactos)
- [ ] Cargar leads sin calificar
- [ ] Verificar conteos: registros cargados vs. esperados
- [ ] Validación funcional por usuarios clave

### Paso 4 — Aprobación de Migración (UAT de datos)
- [ ] Key users verifican muestra representativa de datos
- [ ] Confirmar que historiales críticos están completos
- [ ] Sign-off de aprobación de datos

### Paso 5 — Carga en Producción (Go-Live)
- [ ] Repetir pasos 1–4 con datos actualizados al día del go-live
- [ ] Ventana de migración: [fecha y hora] (fuera de horario laboral)
- [ ] Tiempo estimado de migración: [X horas]
- [ ] Punto de no retorno: [hora] — después de este punto, se avanza

---

## Plan de Contingencia

| Escenario | Acción |
|---|---|
| Error en migración de contactos | Detener proceso, corregir y reintentar |
| Pérdida de datos críticos > 5% | Ejecutar rollback y reagendar |
| Tiempo de migración excede ventana | Extender ventana o reagendar go-live |
| Error de integridad en producción | Restaurar backup y reagendar |
