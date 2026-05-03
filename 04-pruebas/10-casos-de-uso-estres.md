# Casos de Uso Incrementales (Pruebas de Estrés del Flujo CRM)

Este documento contiene 10 casos de uso que aumentan progresivamente en complejidad, diseñados para probar la solidez del flujo de ventas diseñado para COINSA y detectar posibles huecos o *gaps* en la configuración y reglas de negocio actuales.

---

## Nivel 1: Flujos Simples (Básicos y Directos)

### Caso de uso 1 - Reposición urgente (Mismo cliente, producto conocido)
**Contexto:** Venta común de sensor de presión a través de WhatsApp. El cliente es una maquiladora recurrente que requiere reposición urgente de un sensor específico. 
**Story:** Luis Ramírez, de Mantenimiento de Maquiladora del Norte, contacta al vendedor vía WhatsApp solicitando un sensor de presión 0–10 bar con rosca 1/2. El vendedor debe gestionar el requerimiento desde la recepción hasta el cierre rápidamente.
**Información del lead:** Empresa: Maquiladora del Norte S.A. de C.V. / Contacto: Luis Ramírez / Tel: 6621458890
**Respuesta esperada en CRM:**
1. Al ser cliente existente, se crea una Oportunidad directa (no lead) vinculada a Maquiladora del Norte.
2. Se coloca directo en Etapa: Propuesta (saltando Diagnóstico por ser urgente).
3. Actividad: Enviar cotización por WhatsApp/Correo.
*⚠️ **GAP DETECTADO:** ¿El CRM tiene integración oficial con WhatsApp para registrar la conversación, o el vendedor debe crear un Lead manual y pegar capturas? El RF-01 no menciona WhatsApp como fuente.*

### Caso de uso 2 - Consulta general desde la Web
**Contexto:** Un prospecto que no conoce a COINSA llena el formulario de la página web solicitando el catálogo de válvulas.
**Story:** Un ingeniero recién egresado busca proveedores de válvulas para su nuevo taller y llena el formulario genérico de contacto web pidiendo el "catálogo completo".
**Información del lead:** Contacto: Carlos Mendoza / Empresa: (No especificada) / Correo: cmendoza99@gmail.com
**Respuesta esperada en CRM:**
1. Creación automática de un Lead desde formulario web (RF-01.1).
2. Asignación "Round-Robin" a un vendedor disponible (RN-04).
3. Actividad generada: "Llamada de calificación" para descubrir la empresa y potencial real.
*⚠️ **GAP DETECTADO:** ¿Qué pasa si el correo es genérico (gmail) y no hay empresa? Odoo exige una empresa para crear un contacto formal. ¿Hay un flujo para descartar leads basura rápidamente sin ensuciar el CRM?*

### Caso de uso 3 - El lead frío que revive
**Contexto:** Un lead capturado en una expo hace 6 meses (marcado como inactivo/perdido) vuelve a contactar por correo.
**Story:** En enero, la Ing. Patricia pidió info sobre tableros de control pero el presupuesto no fue aprobado y se marcó la oportunidad como "Perdida". En agosto, envía un correo sobre el mismo hilo indicando que ya tienen presupuesto.
**Respuesta esperada en CRM:**
1. El correo llega al historial de la oportunidad original perdida.
2. El sistema alerta al vendedor asignado de un nuevo mensaje en una oportunidad cerrada.
3. El vendedor "Restaura" la oportunidad o clona una nueva.
*⚠️ **GAP DETECTADO:** Si el cliente responde un correo de hace 6 meses de una oportunidad Perdida, ¿Odoo cambia la etapa automáticamente a "Nuevo" o requiere intervención manual? Podría perderse en la bandeja.*

---

## Nivel 2: Flujos Intermedios (Aprobaciones y Colaboración)

### Caso de uso 4 - Negociación con descuento agresivo
**Contexto:** Cliente habitual pide un volumen grande de actuadores neumáticos, pero exige un 25% de descuento para cerrar hoy.
**Story:** El Ing. Arturo tiene a Aceros de Occidente listo para comprar $40,000 USD en actuadores, pero están compitiendo por precio. Arturo necesita aplicar un descuento del 25% en la cotización.
**Respuesta esperada en CRM:**
1. Oportunidad en etapa: Negociación.
2. Arturo intenta enviar propuesta con 25% de descuento.
3. La Regla de Negocio alerta a Gerencia (RN-02 adaptada al descuento, no solo al monto).
*⚠️ **GAP DETECTADO:** El RN-02 habla de aprobación por un *monto X*, pero no habla de aprobación por un *margen/descuento X*. Un vendedor podría vender $5,000 USD con un 90% de descuento y saltarse el RN-02.*

### Caso de uso 5 - Asignación cruzada entre equipos
**Contexto:** Un cliente nacional con plantas en dos zonas geográficas requiere equipos para ambas.
**Story:** Grupo Bimbo (Planta CDMX y Planta Monterrey) pide una cotización global. El vendedor de Monterrey recibe el lead, pero la instalación pesada será en CDMX, territorio de otro equipo.
**Respuesta esperada en CRM:**
1. Creación de una Oportunidad Padre.
2. ¿Se debe compartir la oportunidad entre dos vendedores de distintos equipos?
*⚠️ **GAP DETECTADO:** Odoo por defecto asigna UNA oportunidad a UN vendedor. ¿Cómo se manejan comisiones o visibilidad (RF-05.3) si dos vendedores de dos regiones deben trabajar la misma oportunidad?*

### Caso de uso 6 - Reemplazo de vendedor (Baja laboral temporal/definitiva)
**Contexto:** El Ing. Arturo reporta una incapacidad médica de 3 semanas en cierre de mes.
**Story:** Arturo tiene 15 oportunidades activas en etapa de Negociación. El Supervisor debe reasignar temporalmente estas oportunidades al Ing. Roberto para no perder los negocios.
**Respuesta esperada en CRM:**
1. El Supervisor filtra todas las oportunidades activas de Arturo.
2. Realiza una reasignación masiva a Roberto.
3. Roberto recibe notificaciones de las actividades vencidas de Arturo.
*⚠️ **GAP DETECTADO:** ¿Se deben reasignar los clientes (contactos) también, o solo las oportunidades? ¿Qué pasa cuando Arturo regresa? Falta un procedimiento operativo para "Takeover" de cartera.*

---

## Nivel 3: Flujos Complejos (Casos Borde e Integraciones)

### Caso de uso 7 - Cliente con crédito bloqueado
**Contexto:** Un cliente acepta la propuesta técnica y comercial, y manda su Orden de Compra, pero Administración de Ventas frena el proceso porque el cliente tiene facturas vencidas por 90 días.
**Story:** Arturo cierra exitosamente la venta de 3 bombas centrífugas ($15,000 USD). Pasa la oportunidad a "Ganada", pero al intentar pasar a Orden de Venta en el ERP, el sistema le bloquea el avance.
**Respuesta esperada en CRM:**
1. Oportunidad arrastrada a "Ganada".
2. Odoo (integrado con el módulo contable) arroja una alerta de límite de crédito excedido.
*⚠️ **GAP DETECTADO:** Las Reglas de Negocio actuales (RN) solo abarcan el flujo comercial. No hay validación financiera en CRM. Arturo podría trabajar 2 meses un negocio que finanzas va a rechazar el último día. ¿Cómo sabe el CRM el estatus crediticio del cliente?*

### Caso de uso 8 - Duplicidad de Leads por diferentes canales
**Contexto:** Un mismo cliente de una corporación grande entra por dos canales diferentes el mismo día y se asigna a dos vendedores distintos.
**Story:** El Gerente de Compras de CEMEX manda un correo al alias general pidiendo cotización de motores (se asigna a Vendedor A). Una hora después, el Ingeniero de Mantenimiento de la misma planta llena el formulario web pidiendo soporte técnico sobre los mismos motores (se asigna a Vendedor B). Ambos vendedores empiezan a llamar a CEMEX.
**Respuesta esperada en CRM:**
1. Odoo detecta que el dominio `@cemex.com` ya existe o que el nombre de la empresa coincide.
2. Alerta de "Posible duplicidad de oportunidad" (RF-02.6).
*⚠️ **GAP DETECTADO:** ¿Quién es el dueño del cliente? Si el Vendedor A gana la oportunidad comercial, ¿se le asigna permanentemente la cuenta? ¿El Vendedor B pasa su lead de soporte al equipo de servicio técnico? Falta definir la regla de "Dueño de Cuenta".*

### Caso de uso 9 - Licitación a largo plazo (Oportunidad Pausada)
**Contexto:** COINSA entra a una licitación gubernamental. El ciclo de venta puede durar de 8 a 12 meses y requiere pausas largas.
**Story:** Arturo participa en una licitación de PEMEX. Entrega la documentación técnica en febrero. El fallo se dará hasta noviembre.
**Respuesta esperada en CRM:**
1. La oportunidad avanza a "Propuesta Entregada".
2. Arturo agenda una actividad para octubre.
*⚠️ **GAP DETECTADO:** Según la RN-01 (Alerta de inactividad), esta oportunidad estará "muerta" por 8 meses y generará ruido en los reportes semanales del pipeline. ¿Falta una etapa llamada "En Espera/Standby" o "Licitación" que congele el SLA de inactividad?*

### Caso de uso 10 - El "Deal" que se divide (Split Opportunity)
**Contexto:** El cliente acepta el presupuesto total, pero decide comprarlo en tres fases separadas a lo largo del año por temas de flujo de caja.
**Story:** Arturo cotiza el equipamiento completo de una nave industrial por $100,000 USD. El cliente firma, pero emite una Orden de Compra (PO) hoy por $30,000 USD (Fase 1), y avisa que en julio comprará $40,000 (Fase 2) y en octubre los $30,000 restantes.
**Respuesta esperada en CRM:**
1. Arturo tiene una oportunidad de $100,000. Si la marca Ganada ahora, ensucia el "Forecast" (RF-06.6) porque cobrará ese dinero meses después.
2. Si la deja abierta, no puede reportar la Fase 1 como ganada en este mes.
*⚠️ **GAP DETECTADO:** Odoo estándar requiere ganar la oportunidad completa. Arturo tendría que duplicar/dividir manualmente la oportunidad en 3 (Fase 1, Fase 2, Fase 3) ajustando los montos y fechas de cierre estimadas para no alterar el Forecast del mes. ¿Se ha capacitado a los usuarios para manejar "Partial Wins" (ganancias parciales)?*

---

## Nivel 4: Flujos Críticos (Conflictos de Negocio y Edge Cases Severos)

### Caso de uso 11 - Conflicto de comisiones por registro tardío (Canibalización)
**Contexto:** Dos vendedores están trabajando la misma cuenta sin saberlo, uno por relación personal y otro porque recibió un lead web.
**Story:** El vendedor de Monterrey (Vendedor A) lleva 3 semanas visitando a "Manufacturas Delta", negociando un proyecto de $80,000 USD, pero no lo registró en el CRM por falta de tiempo. Hoy, el Gerente de Compras de Delta llena un formulario en la web pidiendo una cotización formal. El sistema asigna el lead "Round-Robin" al Vendedor B (CDMX). El Vendedor B contacta a Delta, envía la cotización y registra la oportunidad en el CRM.
**Respuesta esperada en CRM:**
1. El Vendedor A intenta registrar la oportunidad finalmente, pero Odoo alerta que ya existe una activa a nombre del Vendedor B.
2. El Vendedor A reclama la comisión porque él hizo el trabajo de campo.
*⚠️ **GAP DETECTADO:** ¿Existe una regla de negocio de "Protección de Cuenta"? Si un vendedor no registra la oportunidad en el CRM en X tiempo, ¿pierde el derecho sobre el cliente ante un lead entrante? Odoo no puede resolver conflictos políticos, requiere una política de ventas clara sobre "quién registra primero, se lo queda".*

### Caso de uso 12 - Cambio abrupto de la moneda de negociación
**Contexto:** Volatilidad cambiaria durante una negociación larga que obliga a recalcular todo el pipeline.
**Story:** Arturo inicia una oportunidad en enero por $2,000,000 MXN para un proyecto de automatización. En marzo, debido a la fluctuación del dólar, el cliente y COINSA acuerdan que el contrato final se firmará en USD ($110,000 USD) para protegerse.
**Respuesta esperada en CRM:**
1. Arturo abre la oportunidad y cambia la moneda de la cotización esperada de MXN a USD.
2. Los reportes de Forecast y Pipeline deben reflejar este cambio sin distorsionar los totales consolidados.
*⚠️ **GAP DETECTADO:** ¿Odoo está configurado con multimoneda activa y tasas de cambio actualizadas automáticamente (vía Banxico/Banamex)? Si el dashboard gerencial (RF-06.1) suma MXN y USD sin convertir, reportará cifras infladas o erróneas. Además, ¿se congela la tasa de cambio al momento de cotizar o al momento de ganar?*

### Caso de uso 13 - El cliente que es también proveedor (Conflicto de entidad)
**Contexto:** Una empresa que le vende insumos a COINSA ahora quiere comprar equipos industriales, mezclando roles en el sistema ERP.
**Story:** "Logística y Transportes Rápidos" es el proveedor principal de fletes de COINSA. Un día, su gerente de mantenimiento se interesa en comprar un compresor a COINSA. Arturo quiere crear la Oportunidad.
**Respuesta esperada en CRM:**
1. Arturo intenta crear el contacto, pero Odoo le advierte que ya existe en el sistema (creado por Compras/Contabilidad como Proveedor).
2. Arturo asocia su oportunidad al perfil existente.
*⚠️ **GAP DETECTADO:** ¿Están separados los flujos de "Partners" (Contactos) en Odoo para evitar que Ventas modifique datos bancarios o fiscales que usa Contabilidad para pagarles? En Odoo, un "Contact" es universal. Si Arturo modifica la dirección fiscal porque el gerente de mantenimiento le dio la de la planta, podría causar que Contabilidad envíe los cheques al lugar equivocado.*
