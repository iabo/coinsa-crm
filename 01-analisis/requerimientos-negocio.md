# Requerimientos de Negocio

## Metodología de Levantamiento
- Talleres con usuarios clave: [fecha]
- Revisión de procesos documentados: [fecha]
- Entrevistas individuales: [fecha]

---

## RF — Requerimientos Funcionales

### RF-01: Gestión de Leads

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-01.1 | El sistema debe capturar leads desde formulario web | Alta | |
| RF-01.2 | El sistema debe capturar leads desde correo electrónico | Alta | |
| RF-01.3 | El sistema debe permitir carga masiva de leads por CSV | Media | |
| RF-01.4 | Los leads deben asignarse automáticamente según reglas | Alta | |
| RF-01.5 | El sistema debe calificar leads con puntuación (lead scoring) | Media | |
| RF-01.6 | Los leads sin actividad deben generar alerta a los X días | Alta | |

### RF-02: Gestión de Oportunidades

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-02.1 | Conversión de lead a oportunidad con un click | Alta | |
| RF-02.2 | Pipeline visual con etapas personalizadas por equipo | Alta | |
| RF-02.3 | Registro de probabilidad de cierre por etapa | Alta | |
| RF-02.4 | Fecha de cierre estimada por oportunidad | Alta | |
| RF-02.5 | Motivo de pérdida requerido al marcar oportunidad como perdida | Alta | |
| RF-02.6 | Duplicación de oportunidades | Baja | |

### RF-03: Actividades y Seguimiento

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-03.1 | Registro de llamadas con duración y notas | Alta | |
| RF-03.2 | Programación de reuniones con sincronización a calendario | Alta | |
| RF-03.3 | Creación de tareas asociadas a oportunidades | Alta | |
| RF-03.4 | Envío de correos desde la oportunidad con historial | Alta | |
| RF-03.5 | Recordatorios automáticos de actividades vencidas | Media | |

### RF-04: Clientes y Contactos

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-04.1 | Ficha de empresa con datos completos | Alta | |
| RF-04.2 | Múltiples contactos por empresa | Alta | |
| RF-04.3 | Historial unificado de interacciones por cliente | Alta | |
| RF-04.4 | Segmentación de clientes por etiquetas | Media | |
| RF-04.5 | Vista 360° del cliente (oportunidades, ventas, comunicaciones) | Alta | |

### RF-05: Equipos y Usuarios

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-05.1 | Definición de equipos de ventas con líder asignado | Alta | |
| RF-05.2 | Cada usuario pertenece a uno o más equipos | Alta | |
| RF-05.3 | Visibilidad de pipeline propia y del equipo | Alta | |
| RF-05.4 | Cuotas de ventas por usuario / equipo / período | Media | |

### RF-06: Reportes y Dashboards

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-06.1 | Dashboard personal con actividades y oportunidades del día | Alta | |
| RF-06.2 | Reporte de pipeline (valor por etapa) | Alta | |
| RF-06.3 | Reporte de actividad por vendedor | Alta | |
| RF-06.4 | Reporte de conversión por etapa del funnel | Alta | |
| RF-06.5 | Reporte de oportunidades ganadas/perdidas por período | Alta | |
| RF-06.6 | Forecast de ventas | Media | |

---

## RNF — Requerimientos No Funcionales

| ID | Requerimiento | Criterio de medición |
|---|---|---|
| RNF-01 | Rendimiento: tiempo de carga < 3 segundos | Prueba de carga con 50 usuarios concurrentes |
| RNF-02 | Disponibilidad: 99.5% uptime en horario laboral | Monitoreo mensual |
| RNF-03 | Seguridad: acceso por roles y perfiles | Verificación de permisos por rol |
| RNF-04 | Compatibilidad: navegadores Chrome, Edge, Safari | Pruebas en cada navegador |
| RNF-05 | Responsive: accesible desde dispositivos móviles | Prueba en iOS y Android |
| RNF-06 | Copias de seguridad diarias de la base de datos | Verificación del proceso de backup |

---

## Reglas de Negocio

| ID | Regla | Área |
|---|---|---|
| RN-01 | Un lead sin actividad por más de [X] días genera alerta al supervisor | Ventas |
| RN-02 | Una oportunidad > $[X] requiere aprobación del gerente de ventas | Ventas |
| RN-03 | Al perder una oportunidad se debe registrar obligatoriamente el motivo | Ventas |
| RN-04 | Los leads captados por web se asignan round-robin al equipo | Marketing |
| RN-05 | Un cliente no puede tener más de [X] oportunidades activas simultáneas | Por definir |
