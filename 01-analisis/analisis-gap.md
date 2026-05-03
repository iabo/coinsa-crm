# Análisis de Brechas (Gap Analysis)

## AS-IS — Estado Actual

### Herramientas utilizadas hoy

| Herramienta | Para qué se usa | Problemas identificados |
|---|---|---|
| Correo electrónico | Envío directo de cotizaciones (Ing. Arturo) | Sin historial centralizado, sin trazabilidad de estado |
| [Sistema de cotización / Excel] | Generación de cotizaciones técnicas | No conectado a ningún pipeline, sin seguimiento post-envío |
| WhatsApp | Seguimiento informal | No hay registro, no escalable |
| [Sistema actual X] | [Uso actual] | [Problemas] |

### Procesos documentados por usuario

#### Ing. Arturo — Ventas e Ingeniería
**Proceso actual (AS-IS):**
```
Necesidad del cliente
       │
       ▼
Ing. Arturo diseña la solución técnica
       │
       ▼
Envía cotización directamente al cliente
       │
       ▼  ← ⚠️ SIN VISIBILIDAD NI SEGUIMIENTO AQUÍ
       ▼
Facturación (si el cliente acepta)
```
**Problemas identificados:**
- No existe registro de cuántas cotizaciones están en proceso
- No hay seguimiento estructurado entre cotización enviada y respuesta del cliente
- Sin visibilidad para gerencia de qué está "en juego" comercialmente
- El conocimiento del estado de cada venta vive solo en la cabeza de Arturo
- No hay historial de cotizaciones previas por cliente en un sistema centralizado

### Dolor del proceso actual

- **[Arturo]** No hay visibilidad de qué cotizaciones están activas y en qué estado
- **[Arturo]** El proceso salta directo de cotización a facturación, sin etapa de seguimiento
- No existe visibilidad centralizada del pipeline de ventas para gerencia
- La información de clientes está dispersa, no centralizada
- No hay seguimiento sistemático post-cotización
- Falta trazabilidad del historial de interacciones por cliente
- Dificultad para medir KPIs comerciales (tasa de conversión, valor en pipeline)

---

## TO-BE — Estado Futuro con Odoo CRM

### Proceso TO-BE: Ing. Arturo en Odoo
> **Decisión tomada en Sesión 1:** Arturo operará dentro de Odoo CRM para dar visibilidad total a su proceso de venta técnica.

```
Necesidad del cliente
       │
       ▼
[Odoo CRM] Arturo crea Oportunidad
       │  (cliente, descripción, valor estimado, fecha cierre)
       ▼
[Odoo CRM] Diseña solución técnica → registra notas en la oportunidad
       │
       ▼
[Odoo Sales] Genera cotización formal desde la oportunidad
       │
       ▼
[Odoo CRM] Seguimiento: registra actividades, mueve etapa del pipeline
       │
       ├──► [GANADO] → Odoo genera orden de venta → Facturación
       │
       └──► [PERDIDO] → Registra motivo → queda en historial
```

**Beneficio inmediato:** Gerencia ve en tiempo real cuántas cotizaciones hay activas, en qué etapa están y qué valor total representa el pipeline.

| Capacidad | AS-IS | TO-BE con Odoo |
|---|---|---|
| Proceso de venta de Arturo | Invisible, en su cabeza | Visible en CRM en tiempo real |
| Cotizaciones activas | Sin registro centralizado | Oportunidades en pipeline de Odoo |
| Seguimiento post-cotización | No existe | Actividades registradas en la oportunidad |
| Historial de comunicaciones | Correos dispersos | Historial unificado en la oportunidad |
| Reportes de ventas | No existen | Dashboard: pipeline por etapa, valor, vendedor |
| Visibilidad gerencial | Nula | Dashboard ejecutivo en tiempo real |
| Flujo cotización → facturación | Salto directo sin tracking | Trazado completo en Odoo CRM + Sales |

---

## Análisis de Brechas Funcionales

### BRECHA-01: Sin gestión centralizada de leads
- **Estado actual:** Leads en Excel, sin asignación sistemática
- **Estado deseado:** Leads capturados y asignados automáticamente en Odoo
- **Solución Odoo:** Módulo CRM — Leads + reglas de asignación
- **Complejidad:** Baja (configuración estándar)
- **Tipo:** Configuración

### BRECHA-02: Proceso comercial no estandarizado
- **Estado actual:** Cada vendedor gestiona su pipeline de forma diferente
- **Estado deseado:** Proceso unificado con etapas definidas y obligatorias
- **Solución Odoo:** Pipeline CRM + etapas + campos obligatorios por etapa
- **Complejidad:** Baja
- **Tipo:** Configuración

### BRECHA-03: Sin historial unificado de comunicaciones
- **Estado actual:** Correos en inbox personal, notas en papel/Excel
- **Estado deseado:** Toda comunicación registrada en la ficha de la oportunidad
- **Solución Odoo:** Chatter + integración de correo electrónico
- **Complejidad:** Media (requiere configuración IMAP/SMTP)
- **Tipo:** Configuración + Integración

### BRECHA-04: Reportes manuales que consumen tiempo
- **Estado actual:** Reportes generados manualmente cada semana
- **Estado deseado:** Dashboards automáticos actualizados en tiempo real
- **Solución Odoo:** Dashboards CRM + reportes estándar
- **Complejidad:** Baja
- **Tipo:** Configuración

### BRECHA-05: Sin integración con [sistema X]
- **Estado actual:** Datos duplicados entre sistemas
- **Estado deseado:** Sincronización automática entre Odoo y [sistema X]
- **Solución Odoo:** API REST / conector dedicado
- **Complejidad:** Alta
- **Tipo:** Desarrollo / Integración

### BRECHA-06: Sin seguimiento formal post-entrega
- **Estado actual:** No existe proceso formal. El vendedor decide discrecionalmente si da seguimiento al cliente tras el envío, y no se registra si el material llegó correctamente ni en qué condición. (Confirmado por Guillermo Vélez, correo 27/02/2026.)
- **Estado deseado:** Actividad automática de confirmación de recepción asignada al vendedor tras completar la entrega, con registro del resultado en la orden de venta.
- **Solución Odoo:** Regla de automatización: al validar la orden de entrega (stock.picking), crear actividad de tipo «Llamada de seguimiento» asignada al vendedor responsible, con plazo de 2 días hábiles.
- **Complejidad:** Baja
- **Tipo:** Configuración

---

## Funcionalidades Standard vs. Customización

| Requerimiento | ¿Cubierto por Odoo estándar? | Acción requerida |
|---|---|---|
| Gestión de leads | Sí | Configuración |
| Pipeline de ventas | Sí | Configuración |
| Seguimiento de actividades | Sí | Configuración |
| Lead scoring | Parcial | Configuración avanzada |
| Asignación automática | Sí | Configuración de reglas |
| Reportes y dashboards | Sí | Configuración |
| Integración con correo | Sí | Configuración IMAP/SMTP |
| [Requerimiento X] | No | Desarrollo custom |
| [Requerimiento Y] | Parcial | Módulo OCA / desarrollo |
