# Requerimientos de Negocio

## Metodología de Levantamiento
- Talleres con usuarios clave: sesiones de trabajo 1-7
- Revisión de procesos documentados: minutas, anexos y diagramas de flujo del repositorio
- Entrevistas individuales: Javier Pablos, Guillermo Velez, Arturo Gil y participantes operativos

---

## RF — Requerimientos Funcionales

### RF-01: Gestión de Leads

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-01.1 | El sistema debe capturar leads desde formulario web | Alta | Guillermo Velez |
| RF-01.2 | El sistema debe capturar leads desde correo electrónico | Alta | Guillermo Velez |
| RF-01.3 | El sistema debe permitir carga masiva de leads por CSV | Media | Javier Pablos |
| RF-01.4 | Los leads deben asignarse automáticamente según reglas | Alta | Guillermo Velez |
| RF-01.5 | El sistema debe calificar leads con puntuación (lead scoring) | Media | Javier Pablos |
| RF-01.6 | Los leads sin actividad deben generar alerta a los 7 días | Alta | Guillermo Velez |

### RF-02: Gestión de Oportunidades

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-02.1 | Conversión de lead a oportunidad con un click | Alta | Guillermo Velez |
| RF-02.2 | Pipeline visual con etapas personalizadas por equipo | Alta | Arturo Gil Armenta |
| RF-02.3 | Registro de probabilidad de cierre por etapa | Alta | Javier Pablos |
| RF-02.4 | Fecha de cierre estimada por oportunidad | Alta | Arturo Gil Armenta |
| RF-02.5 | Motivo de pérdida requerido al marcar oportunidad como perdida | Alta | Guillermo Velez |
| RF-02.6 | Duplicación de oportunidades | Baja | Por confirmar |

### RF-03: Actividades y Seguimiento

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-03.1 | Registro de llamadas con duración y notas | Alta | Guillermo Velez |
| RF-03.2 | Programación de reuniones con sincronización a calendario | Alta | Arturo Gil Armenta |
| RF-03.3 | Creación de tareas asociadas a oportunidades | Alta | Guillermo Velez |
| RF-03.4 | Envío de correos desde la oportunidad con historial | Alta | Arturo Gil Armenta |
| RF-03.5 | Recordatorios automáticos de actividades vencidas | Media | Javier Pablos |

### RF-04: Clientes y Contactos

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-04.1 | Ficha de empresa con datos completos | Alta | Adriana Real |
| RF-04.2 | Múltiples contactos por empresa | Alta | Guillermo Velez |
| RF-04.3 | Historial unificado de interacciones por cliente | Alta | Javier Pablos |
| RF-04.4 | Segmentación de clientes por etiquetas | Media | Javier Pablos |
| RF-04.5 | Vista 360° del cliente (oportunidades, ventas, comunicaciones) | Alta | Arturo Gil Armenta |

### RF-05: Equipos y Usuarios

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-05.1 | Definición de equipos de ventas con líder asignado | Alta | Javier Pablos |
| RF-05.2 | Cada usuario pertenece a uno o más equipos | Alta | Guillermo Velez |
| RF-05.3 | Visibilidad de pipeline propia y del equipo | Alta | Javier Pablos |
| RF-05.4 | Cuotas de ventas por usuario / equipo / período | Media | Javier Pablos |

### RF-06: Reportes y Dashboards

| ID | Requerimiento | Prioridad | Validado por |
|---|---|---|---|
| RF-06.1 | Dashboard personal con actividades y oportunidades del día | Alta | Guillermo Velez |
| RF-06.2 | Reporte de pipeline (valor por etapa) | Alta | Javier Pablos |
| RF-06.3 | Reporte de actividad por vendedor | Alta | Javier Pablos |
| RF-06.4 | Reporte de conversión por etapa del funnel | Alta | Javier Pablos |
| RF-06.5 | Reporte de oportunidades ganadas/perdidas por período | Alta | Javier Pablos |
| RF-06.6 | Forecast de ventas | Media | Javier Pablos |

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
| RN-01 | Un lead sin actividad por más de 7 días genera alerta al supervisor | Ventas |
| RN-02 | Una oportunidad mayor a $250,000 MXN requiere revisión del Director Comercial | Ventas |
| RN-03 | Al perder una oportunidad se debe registrar obligatoriamente el motivo | Ventas |
| RN-04 | Los leads captados por web se asignan round-robin al equipo comercial | Marketing |
| RN-05 | Un cliente no puede tener más de 5 oportunidades activas simultáneas sin revisión comercial | Ventas |
