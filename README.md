# COINSAMATIK — Implementación CRM Odoo

## Visión del Proyecto
Implementación del módulo CRM de Odoo para centralizar la gestión de clientes, oportunidades de venta y pipeline comercial de COINSA.

## Estructura del Repositorio

| Carpeta | Contenido |
|---|---|
| `00-estrategia/` | Objetivos de negocio, alcance, stakeholders y roadmap |
| `01-analisis/` | Análisis AS-IS / TO-BE, requerimientos y gap analysis |
| `02-diseno/` | Arquitectura técnica, modelo de datos e integraciones |
| `03-configuracion/` | Guías de configuración de módulos y pipelines |
| `04-implementacion/` | Plan de fases y entregables por sprint |
| `05-migracion-datos/` | Inventario, mapeo y plan de migración de datos |
| `06-pruebas/` | Plan de pruebas, casos de prueba y UAT |
| `07-capacitacion/` | Plan de capacitación y manuales de usuario |
| `08-go-live/` | Checklist de salida a producción y plan de rollback |
| `09-soporte-postimplementacion/` | Plan de soporte, incidencias y mejora continua |

## Estado del Proyecto

- **Fase actual:** Planificación
- **Versión Odoo:** Por definir
- **Fecha inicio estimada:** Por definir
- **Fecha go-live estimada:** Por definir

## Equipo

| Rol | Responsable |
|---|---|
| Project Manager | |
| Consultor Odoo | |
| Líder Técnico | |
| Líder Funcional CRM | |
| Responsable de Datos | |

## Links Importantes

- Instancia Odoo (staging): 
- Instancia Odoo (producción): 
- Repositorio de código (customizaciones): 



# notas para claudio : 

- ingeniero pablos comenta de gente que se les da informacion tecnica de platicas que dan sobre PSI, es decir agrupar oportunidades por tipo de equipos y clientes . 
para contactar y vender despues, seguimiento etcetera

- Se definen las siguientes necesidades para el Modulo :: 
 - Visisbilidad de oportunidades de venta técnicas (cotizaciones, pipeline técnico-comercial)
 - Ayuda a Vender màs 
 - Repositorio de infomacion de mi cliente (contactos, historial de interacciones, etc)
 - Segmentacion de clientes y oportunidades (por tipo de equipo, industria, etc)
 - Campañas de marketing por segmento
 - Programacion de seguimientos y tareas comerciales (por ejemplo cobrar mantenimientos o renovaciones)
 - Generacion de leads a partir de campañas 
 - 


 - Generar diagrama de swimlanes del proceso actual de ventas con puntos de contacto con Odoo y responsables de cada etapa.

 - Defninir requerimientos para almentar el sistema, que se ocupa para dar de alta todo tipo de clientes (publico en general para cotizar y RFC y datos fiscales para clientes empresariales) 

 - Como se capturarian 100 clientes interesantes y general un historial pero estos clientes no tienen RFC que es el primer ID  utilizado en Odoo , debemos encontrar una forma de dar de alta clientes sin RFC y aun asi identificarlos induvidualmente para dar seguimiento comercial.

 - Reclamaciones y quejas , donde se capturan ? 

 - SLA , como lo vamos a medir ? 

 - Quizas en el scope de esta etapa de no vamos a cubrir tareas o funciones de marketing porque el departamento 

 - Proceso de Odoo para generar DB de lciuentes para generar campañas de marketing, como se va a hacer ?

 - Parece que hay varios temas que no estan definidos en cuestion de atencion y recepcion, canales de comunicacion , correo, whatsapp, telefono, etc.

 - Hermenegildo (ventas internas) yya esta asignado a recibir los leads en odoo, por lo tanto se le asignaria el ingreso de leads por whatsapp business y talvez otro tipo de medio. 
 - Guillermo para Hermosillo Miguel Para Tijuana 
 - Herme para OTROS territorios 

 - En cotizaciones se hizo un desarrollo custom para agregar 3 campos para agregar la informacion de contacto para poder usar publico en general, actualemtne solo tiene para porner nombre y direccion 

 - en las SO hay un monton de campos que son requeridos y no se estan llenando, especificamente las cotizaciones 

  - En las cotiaciones es un tema importante , la politica de entrega, actualmente esta una definida por default, pero se tiene que quital el prestablecido, porque luego no se puede modificar , se tiene que qiitar el dafaul porque se les ovida actualizarlo al vender , y hace un desmadre en almacen, entonces, fecha de entrrga y politicas de entrega  son importantizimos dejarlas bien en el modulo de cotizaciones 

  - revisar si la fecha de entrega se puede modificar , actualmente nada se modifica en odoo, pero este podria ser util poder actualizar ese 

  - Otra cosa que hay que obligar a que se adjuente es la orden de compra en el modulo de entregas 

  - Direccion de entrega tambien esta por default , tampoco deberia ser por dejault  

  - configurar 

  - Configurar un periodo de tiempo par autolimpieza , con un tiempo de 2-3 años y que automaticamente se cancelen solos 

  - La confirmacion del las ordenees de venta tienen un limite de credito y/o facturas vencidas _ , se bloquean furturas ordenes de ventas hasta que se cumpla o se libere manualmente por parte de pablos y/o adriana 

  - Automatizar el recordatorio de pagos de facturas vencidas , correo automatico 

  - checar la configuracion de SMTP porque actualemtne los que sale por Odoo se va a Junk/spam 

  - hay un problema porque hay algunos procesos externos definidos por el cliente, por ejemplo entra al portal del cliente y realiza ciertas actuvidades , sube rchivos corretea infos y lo captura para el cliente , pero pues no se hace. 
 - sobre lo mismo, hay datos especificos del proceso de compra del cliente, como claves passwords etc. donde se van a guardar ? 
 - tal vez en recepcion al dar de alta del cliente se puede tomar la oportunidad para captuar esta informacion. 

 - Temas para la siguente reunion antes :: 

 - acesso a Odoo , cuenta demo, instacia de prubea contacto con Adriana
 - Documentos en Drive interno y exteno
 - Agenda SPM 
 - 

 - meter a recepcion a los steakholders y quienes participan en conta aparte de Adriana , martita es recepcion , posioble cambio de recepcionista

 - desarrollar una corrida de prueba de todos los tipos de flujos , con cadia variante 

 -  Mañana de 11 a 1 siguiente Junta 

 - No se ha mencionado ni trabajado el SLA 

  - Email config puede ser todo un show 

  - 


S2 >> 

 - Implementar un configuracion predeterminada para el envio de correos por grupos de interes, es decir, que la informacion de facturas solo se envie a ciertos contactos. Asignar por cliente los contactos importantes para envio de correos y los que no son necesarios para el envio de correos automaticos transaccionales. 

 - Posible idea >> agregar al CRM el margen por oportunidad/cotizacion, no final. 



another test 


 Meeting MArco :: 

- Actividades 
- Etapas 


- modulo de visitas . 






































