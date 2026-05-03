# Historia de Usuario: Gestión del Ciclo de Vida de una Oportunidad de Venta

**Como** Vendedor (Ing. Arturo)  
**Quiero** gestionar visualmente el progreso de mis oportunidades de venta desde el primer contacto hasta el cierre  
**Para** tener control total sobre mis negociaciones, asegurar el seguimiento oportuno, dejar de depender de mi memoria y reportar automáticamente mis métricas a gerencia.

---

## 1. El Problema (Contexto del Negocio)
Actualmente en COINSA, el Ing. Arturo maneja las ventas de equipo industrial basándose en su experiencia y libretas personales. Cuando un cliente potencial (ej. Industrias Metalúrgicas SA) muestra interés, Arturo anota los detalles, pero no existe un registro centralizado. 
Esto provoca que a veces se olviden seguimientos críticos en cotizaciones enviadas, no haya visibilidad del valor del *pipeline* para la gerencia, y si Arturo no está disponible, el estado de la negociación es un completo misterio para el resto del equipo. 

Con la implementación de Odoo CRM, el objetivo es que Arturo tenga un **asistente digital** que centralice la información, le recuerde qué hacer y documente cada paso de forma natural sin trabajo administrativo excesivo.

---

## 2. El Flujo Principal (El "Camino Feliz")

### A. El Descubrimiento y Captura
Arturo recibe una llamada de un prospecto interesado en renovar equipos industriales. Mientras habla con el cliente, abre el CRM y crea rápidamente una nueva **Oportunidad**. Ingresa el nombre del cliente, un título claro para el negocio (ej. "Renovación Equipos Planta Norte") y un valor monetario inicial estimado (ej. $50,000 USD).

### B. Visibilidad Inmediata
Al colgar, la oportunidad ya aparece como una tarjeta en la primera columna ("Nuevo") de su tablero visual (vista Kanban). Arturo puede ver el valor total de su *pipeline* sumado en la parte superior de cada columna.

### C. Planificación del Siguiente Paso
Arturo sabe que debe enviar información técnica mañana por la mañana. Ahí mismo, en la tarjeta de la oportunidad, programa una actividad: *"Enviar ficha técnica y cotización preliminar"* con fecha de vencimiento para el día siguiente.

### D. Evolución del Negocio
A los pocos días, Arturo envía la cotización formal desde el sistema. Vuelve a su tablero y simplemente arrastra la tarjeta de la oportunidad a la columna "Propuesta Enviada". Automáticamente, el sistema entiende que la probabilidad de cierre ha aumentado (ej. del 10% al 50%).

### E. El Cierre
Tras un par de reuniones (cuyas minutas quedaron registradas en el historial de la oportunidad), el cliente acepta la oferta. Arturo celebra arrastrando la tarjeta a la etapa "Ganada". La oportunidad se cierra exitosamente, actualizando en tiempo real sus métricas de ventas del mes en el dashboard gerencial.

---

## 3. Escenarios Alternativos y Casos de Uso Reales (Flujos Borde)

### Escenario 1: El cliente se enfría (Alerta de Inactividad)
Arturo envió una cotización, pero tuvo una semana muy ocupada visitando plantas y olvidó dar seguimiento a esta propuesta en particular. 
* **Qué sucede:** El sistema detecta que la oportunidad lleva 7 días en la etapa "Propuesta Enviada" sin ninguna actividad completada o programada a futuro. 
* **Resolución (RN-01):** Arturo recibe una notificación automática (y un correo) recordándole que esta oportunidad de alto valor está "estancada". Arturo retoma el contacto inmediatamente.

### Escenario 2: Negociación Perdida por Precio
El cliente informa que la competencia ofreció un precio 20% menor que COINSA no puede igualar operativamente.
* **Qué sucede:** Arturo arrastra la tarjeta a la etapa "Perdida" (o hace clic en el botón de perder).
* **Resolución (RN-03):** El sistema **no** le deja simplemente borrarla o cerrarla sin más; le exige seleccionar un "Motivo de Pérdida" (en este caso, "Precio muy alto") y permite agregar una nota. Esto es vital para que a fin de año la gerencia sepa cuántos negocios se pierden por precio frente a otros factores.

### Escenario 3: Escalamiento por Alto Valor (Regla de Negocio)
El cliente solicita un volumen inusualmente grande, elevando el valor de la oportunidad a $250,000 USD.
* **Qué sucede:** Arturo actualiza este monto en la oportunidad.
* **Resolución (RN-02):** Debido a una regla interna de validación, el sistema alerta a la Gerencia de Ventas. Arturo no puede marcarla como "Ganada" o aplicar un descuento mayor al permitido sin que el gerente apruebe primero la viabilidad comercial, técnica y de inventario.

### Escenario 4: Colaboración Interna (Chatter)
Arturo necesita apoyo técnico de un especialista interno para validar la compatibilidad de un equipo antes de enviar la propuesta formal.
* **Qué sucede:** En lugar de enviar un correo externo o un mensaje de WhatsApp perdiendo el hilo del cliente, Arturo usa la sección de comentarios (Chatter) dentro de la misma oportunidad y etiqueta al ingeniero de soporte (`@JuanSoporte`).
* **Resolución:** Juan recibe la notificación, entra directo a la oportunidad leyendo todo el contexto y necesidades del cliente, y responde ahí mismo. Toda la conversación técnica queda unida permanentemente a la oportunidad de venta.

---

## 4. Criterios de Aceptación Técnicos
Para considerar esta Historia de Usuario como "Terminada" y lista para el Go-Live, el sistema configurado debe cumplir con:

- [ ] **Creación ágil:** El vendedor puede crear una oportunidad en menos de 1 minuto con los datos mínimos requeridos.
- [ ] **Pipeline estructurado:** El tablero Kanban refleja exactamente las etapas reales del proceso de ventas de COINSA.
- [ ] **Probabilidad automática:** El cambio de etapa actualiza la probabilidad de éxito de forma automática según la configuración definida.
- [ ] **Motivo de pérdida:** Es campo obligatorio registrar el motivo si la oportunidad se marca como "Perdida".
- [ ] **Historial 360°:** Toda actividad (llamada, correo, tarea) queda ligada al historial del cliente y la oportunidad en un solo hilo de comunicación.
- [ ] **Alertas de inactividad:** Las notificaciones a supervisores/vendedores se disparan correctamente cuando se excede el tiempo máximo sin contacto.