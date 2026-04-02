# Minuta — Sesión 4 | COINSA CRM
**Fecha:** Lunes 30 de marzo, 2026
**Horario:** 3:30 – 5:30pm
**Modalidad:** Por definir

---

## Objetivo de la sesión
Cerrar los temas bloqueantes del análisis y alinear a Marco (consultor) con los avances de sesiones anteriores.

---

## Agenda

### 1. Apertura y seguimiento — 10 min
- Recapitulación de acuerdos de Sesión 3
- Presentación de avances a Marco (quien no estuvo presente en sesiones anteriores)

---

### 2. Recap: Segmentación de clientes — 10 min
> *Tema ya resuelto en Sesión 3. Se toca brevemente para alinear a Marco.*

Se definió en Sesión 3 que los clientes se segmentarán mediante **etiquetas flexibles** que los propios usuarios podrán gestionar y filtrar. Se incluirán etiquetas base como parte de la entrega final de configuración.

**Contexto para Marco:** No se decidió un modelo rígido; se optó por etiquetas para dar flexibilidad operativa al equipo comercial.

---

### 3. Validación: Usuarios y roles de acceso en Odoo — 20 min
> *Avanzado en sesiones anteriores. Sesión 4 = validación final.*

| Persona | Área | Rol Odoo propuesto |
|---|---|---|
| Arturo | Ventas Técnicas | Vendedor (CRM + Sales) |
| Guillermo | Ventas | Vendedor (CRM + Sales) |
| Hermenegildo | Ventas Internas / Leads | Vendedor (CRM) |
| Miguel (Hermosillo / Tijuana) | Ventas | Vendedor (CRM) |
| Martha Molina | Recepción / Facturación | Facturación + Vista CRM |
| Adriana Real | Contabilidad | Contabilidad |
| Javier Pablos | Dirección Comercial | Gerente / Líder de equipo |
| Edna / Melissa / Valeria | Compras | Compras (sin acceso CRM) |
| Irma / Jesús | Almacén | Inventario (sin acceso CRM) |

**Entregable:** Tabla de usuarios + roles aprobada.

---

### 4. Temas bloqueantes — 45 min

#### 4a. Alta de clientes sin RFC — decisión requerida
> *COINSA tiene ~100 clientes interesantes sin RFC. Odoo usa RFC como identificador principal.*

**Propuesta a validar:** Crear campo opcional "Clave Interna COINSA" como identificador alterno + campo "Tipo de cliente" (Público General / Empresa).

#### 4b. Canales de entrada de leads — confirmación y estrategia de prospección
Todos los canales de comunicación (WhatsApp Business, correo, llamadas) convergen en **Hermenegildo** como punto de captura de leads. Esto ya fue definido.

**Punto nuevo a explorar:** Ferias, eventos y pláticas técnicas como fuentes de prospección (ej. pláticas sobre PSI mencionadas por Ing. Pablos en Sesión 1).
- ¿Qué estrategias de prospección existen actualmente en COINSA para estos eventos?
- ¿Cómo se capturan hoy los contactos obtenidos en ferias o pláticas?
- **Propuesta:** Definir un proceso de carga de prospectos post-evento (CSV o captura manual) directamente al CRM, para dar seguimiento comercial desde el primer contacto.
- Prospeccion por parte del vendedor. 
- Desarrollo de territorio de ventas con visitas en campo. (Definir metas de visitas mensuales por vendedor, zonas geográficas, etc).
- Estrategias de minado o busqueda. 
- Definir parametros de atencion, tiempos y contactos por parte del vendedor, empezar con objetivos y medir capacidad. Diferenciar entre clientes nuevos y existentes.
- Procesos de abordaje para clientes nuevos.
- Estrategia para clientes existentes...



#### 4c. SLA — primer acuerdo formal
> *Mencionado como pendiente en múltiples sesiones. Necesitamos al menos un acuerdo base.*

Preguntas a resolver:
- ¿Tiempo máximo para primer contacto a un lead nuevo? (ej. 24–48 hrs)
- ¿Tiempo máximo para enviar cotización? (ej. 3–5 días hábiles)
- ¿Cómo lo monitorea Odoo? → alerta de inactividad en pipeline

**Entregable:** Al menos 2–3 reglas de SLA definidas y aprobadas por el equipo.

---

### 5. Validación del pipeline de ventas — 15 min


Etapas propuestas:
```
Nuevo Lead → Contactado → Reunión Agendada → Propuesta Enviada → En Negociación → Ganado / Perdido
```

Preguntas abiertas para la sesión:
- ¿El flujo aplica igual para Arturo (técnico) y para los vendedores internos, o se necesita una variante?
- ¿Se requiere una etapa específica para "Diseño Técnico" en el pipeline de Arturo?

---

### 6. Acuerdos y próximos pasos — 10 min
- Resumen de decisiones tomadas en la sesión
- Responsables y fechas de cada entregable
- Fecha de Sesión 5

---

## Pendientes en backlog (no entran en esta sesión)

- Configuración SMTP / correo saliente
- Campos custom de cotizaciones (política de entrega, OC adjunta, fecha de entrega)
- Módulo de visitas
- Proceso de portales de clientes corporativos
- Autolimpieza de cotizaciones y bloqueo por límite de crédito
