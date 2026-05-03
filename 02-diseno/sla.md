# SLA — Propuesta de Acuerdo de Nivel de Servicio

> **Estado:** Propuesta inicial — pendiente de aprobación formal en Sesión 4 (punto 4c).
> **Alcance:** Proceso comercial interno (tiempo de respuesta del equipo de ventas). No cubre logística ni entrega de producto.

---

## Reglas de SLA Propuestas

| # | Métrica | Objetivo | Cómo se monitorea en Odoo |
|---|---|---|---|
| SLA-01 | Primer contacto a lead nuevo | ≤ 24 horas hábiles | Alerta automática de inactividad al cumplirse 1 día sin actividad en etapa «Nuevo Lead» |
| SLA-02 | Envío de cotización desde solicitud | ≤ 3 días hábiles | Fecha de creación de la oportunidad vs. fecha de envío de cotización desde Odoo |
| SLA-03 | Seguimiento post-cotización sin respuesta del cliente | ≤ 5 días hábiles | Actividad de seguimiento programada automáticamente al enviar la cotización |
| SLA-04 | Respuesta interna a solicitud de descuento | ≤ 1 día hábil | Tarea asignada a Coordinación Comercial (Javier Pablos) desde Odoo |
| SLA-05 | Devolución de llamada a prospecto no atendido | ≤ 4 horas hábiles | Recepción registra el contacto en Odoo con actividad de devolución de llamada asignada a Hermenegildo |
| SLA-06 | Captura de datos completos en llamada entrante | 100% de contactos (nombre + teléfono + empresa + motivo) | Revisión semanal de leads con datos incompletos en CRM |

---

## Monitoreo en Odoo

- **Alerta de inactividad:** Configurar regla de automatización en CRM para notificar al vendedor y supervisor cuando una oportunidad lleva `X` días sin actividad registrada.
- **Pipeline visual:** Oportunidades con actividad vencida aparecen en **rojo** en la vista Kanban — revisión diaria recomendada.
- **Reunión semanal:** Revisión del cumplimiento de SLA con el Director Comercial como parte de la reunión de pipeline.

---

## Hallazgos del Diagnóstico Inicial (Marco Jacobo, 02/03/2026)

Pruebas realizadas sobre el proceso de captación real detectaron los siguientes puntos de fuga:

| # | Canal | Hallazgo | Acción correctiva |
|---|---|---|---|
| D-01 | Llamada telefónica (8:00 am) | Sin respuesta; sin personal asignado en ese horario | Definir y publicar horario oficial de atención telefónica |
| D-02 | Llamada telefónica (12:56 pm) | Recepción contestó pero solo capturó el nombre; sin devolución de llamada posterior | Implementar protocolo de captura obligatoria + registro en Odoo (ver SLA-05 y SLA-06) |
| D-03 | Formulario web | Bug con caracteres especiales — correos con signos no se envían correctamente | Reportar al equipo técnico del sitio; canal inhabilitado como fuente confiable hasta corrección |

---

## Notas

- Los tiempos están en **días hábiles** (lunes a viernes, horario laboral COINSA).
- Este SLA es un punto de partida mínimo. Se revisará y ajustará tras los primeros **60 días de operación**.
- No contempla tiempos de entrega de producto (corresponde al módulo de Almacén / Logística).
- El SLA de soporte postventa se gestiona por separado en el plan de soporte (`05-soporte/plan-soporte.md`).