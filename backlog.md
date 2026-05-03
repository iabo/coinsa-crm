# Backlog — Ideas y Funciones Potenciales

> Ideas identificadas durante el proceso de análisis que **no entran en el alcance inicial** del proyecto, pero podrían implementarse si el tiempo y las restricciones técnicas lo permiten.

---

## CRM / Ventas

- [ ] Integración WhatsApp Business con Odoo CRM (captura automática de leads entrantes)
- [ ] Lead scoring automático por probabilidad de cierre (modelo predictivo de Odoo)
- [ ] Margen estimado por oportunidad / cotización visible en el CRM
- [ ] Metas de visitas mensuales por vendedor y reporte de cumplimiento
- [ ] Módulo de visitas de campo (check-in / check-out con geolocalización)
- [ ] Proceso estructurado de abordaje para clientes nuevos (onboarding comercial)
- [ ] Estrategia formal para clientes existentes: retención, upsell y reactivación
- [ ] Definición de zonas de ventas y asignación territorial con metas por zona

## Cotizaciones / Órdenes de Venta

- [ ] Campo personalizado "Clave Interna COINSA" para identificar clientes sin RFC
- [ ] Campo "Tipo de Cliente" (Público General / Empresa) en la ficha de cliente
- [ ] Eliminar política de entrega predeterminada en cotizaciones (obligar a seleccionar)
- [ ] Eliminar dirección de entrega predeterminada (obligar a seleccionar en cada OV)
- [ ] Adjuntar Orden de Compra del cliente como requerimiento en módulo de entregas
- [ ] Permitir modificar fecha de entrega después de confirmar OV
- [ ] Autolimpieza de cotizaciones inactivas (2–3 años sin movimiento → cancelación automática)

## Crédito y Cobranza

- [ ] Bloqueo automático de nuevas OV cuando el cliente excede su límite de crédito o tiene facturas vencidas
- [ ] Liberación manual del bloqueo por Director Comercial (Pablos) y/o Contadora (Adriana Real)
- [ ] Recordatorio automático de pago a clientes con facturas próximas a vencer
- [ ] Correo automático de cobranza para facturas vencidas (ciclos configurables)

## Correo y Comunicaciones

- [ ] Configuración SMTP para evitar que correos salientes de Odoo vayan a Spam / Junk
- [ ] Grupos de envío por cliente: facturas y transaccionales solo a los contactos designados
- [ ] Plantillas de correo por tipo de actividad (seguimiento, cotización, cierre, postventa)

## Marketing

- [ ] Módulo de Email Marketing con campañas segmentadas por tipo de cliente
- [ ] Generación de leads desde campañas de correo masivo
- [ ] Integración con LinkedIn / redes sociales para captación de prospectos

## Soporte y Postventa

- [ ] Módulo de reclamaciones y quejas (helpdesk o tickets internos)
- [ ] Proceso de captura y seguimiento de incidencias postventa en Odoo

## Clientes Corporativos / Portales

- [ ] Campo seguro para almacenar credenciales del portal de compras del cliente
- [ ] Flujo de alta de cliente corporativo: captura de datos del portal en recepción

## Reportes y Analítica

- [ ] Forecast de ventas automático con el modelo predictivo de Odoo
- [ ] Dashboard ejecutivo con KPIs de pipeline, conversión y actividad por vendedor
- [ ] Reportes BI avanzados (dashboards personalizados de Odoo o integración con herramienta externa)