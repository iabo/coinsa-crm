# Sesión de Trabajo 1 — COINSA CRM

---

## Temas tratados

- Ingeniero Pablos comenta sobre gente a la que se les da información técnica en pláticas sobre PSI; es decir, agrupar oportunidades por tipo de equipos y clientes para contactar y vender después, seguimiento, etcétera.

---

## Necesidades definidas para el Módulo CRM

- Visibilidad de oportunidades de venta técnicas (cotizaciones, pipeline técnico-comercial)
- Ayuda a vender más
- Repositorio de información del cliente (contactos, historial de interacciones, etc.)
- Segmentación de clientes y oportunidades (por tipo de equipo, industria, etc.)
- Campañas de marketing por segmento
- Programación de seguimientos y tareas comerciales (por ejemplo cobrar mantenimientos o renovaciones)
- Generación de leads a partir de campañas

---

## Puntos de análisis / acción

- Generar diagrama de swimlanes del proceso actual de ventas con puntos de contacto con Odoo y responsables de cada etapa.
- Definir requerimientos para dar de alta todo tipo de clientes (público en general para cotizar; RFC y datos fiscales para clientes empresariales).
- Cómo se capturarían ~100 clientes interesantes y se generaría un historial, dado que estos clientes no tienen RFC (que es el primer ID utilizado en Odoo). Se debe encontrar una forma de dar de alta clientes sin RFC y aun así identificarlos individualmente para dar seguimiento comercial.
- Reclamaciones y quejas: ¿dónde se capturan?
- SLA: ¿cómo lo vamos a medir?
- Proceso de Odoo para generar DB de clientes para campañas de marketing: ¿cómo se va a hacer?
- Quizás en el scope de esta etapa no se van a cubrir tareas o funciones de marketing porque el departamento no está definido.
- Hay varios temas no definidos en cuanto a atención y recepción, canales de comunicación (correo, WhatsApp, teléfono, etc.).

---

## Canales y responsables de leads

- Hermenegildo (ventas internas) ya está asignado a recibir los leads en Odoo; se le asignaría el ingreso de leads por WhatsApp Business y otros medios.
- Guillermo para Hermosillo, Miguel para Tijuana.
- Herme para otros territorios.

---

## Notas técnicas — Cotizaciones

- En cotizaciones hay un desarrollo custom para agregar 3 campos con información de contacto para poder usar "público en general"; actualmente solo tiene nombre y dirección.
- En las SO hay un montón de campos requeridos que no se están llenando, específicamente en cotizaciones.
- **Política de entrega:** actualmente está una definida por default pero se tiene que quitar el preestablecido, porque luego no se puede modificar; se olvida actualizarlo al vender y hace desorden en almacén. Fecha de entrega y política de entrega son importantísimos dejarlos bien en el módulo de cotizaciones.
- Revisar si la fecha de entrega se puede modificar (actualmente nada se modifica en Odoo, pero podría ser útil actualizarla).
- Obligar a que se adjunte la orden de compra en el módulo de entregas.
- Dirección de entrega también está por default; tampoco debería serlo.
- Configurar un periodo de tiempo para autolimpieza: 2–3 años, con cancelación automática de cotizaciones.
- La confirmación de órdenes de venta tiene un límite de crédito y/o facturas vencidas: se bloquean futuras órdenes hasta que se cumpla o se libere manualmente (Pablos y/o Adriana).
- Automatizar recordatorio de pagos de facturas vencidas: correo automático.
- Revisar configuración de SMTP porque actualmente lo que sale por Odoo va a Junk/Spam.
- Hay procesos externos definidos por el cliente (entrar al portal, subir archivos, capturar info); datos específicos del proceso de compra del cliente (claves, passwords, etc.): ¿dónde se guardan? Quizás en recepción al dar de alta al cliente.

---

## Pendientes para la siguiente reunión

- Acceso a Odoo: cuenta demo, instancia de prueba — contacto con Adriana.
- Documentos en Drive interno y externo.
- Agenda SPM.
- Meter en recepción a los stakeholders y quienes participan en contabilidad, aparte de Adriana. Martita es recepción (posible cambio de recepcionista).
- Desarrollar una corrida de prueba de todos los tipos de flujos con cada variante.
- No se ha mencionado ni trabajado el SLA.
- Email config puede ser complejo.

---

## Próxima junta

Mañana de 11 a 1.
