# Plan de Pruebas de Aceptación de Usuarios (UAT)

## Objetivos del UAT

- Validar que el sistema cumple los requerimientos de negocio aprobados
- Identificar desviaciones antes del go-live
- Obtener la aceptación formal de los usuarios clave
- Generar confianza y familiaridad con el sistema

## Participantes

| Rol | Nombre | Área | Escenarios a probar |
|---|---|---|---|
| Líder UAT | | | Todos |
| Key User — Ventas | | Ventas | Pipeline, leads, oportunidades |
| Key User — Supervisión | | Ventas | Reportes, equipo, asignaciones |
| Key User — Gerencia | | Dirección | Dashboards, forecast |
| Key User — Marketing | | Marketing | Leads, campañas |

## Fechas UAT

| Actividad | Fecha | Duración |
|---|---|---|
| Preparación del ambiente UAT | | |
| Carga de datos de prueba | | |
| Sesión UAT — Ventas | | ~3 horas |
| Sesión UAT — Supervisores | | ~2 horas |
| Sesión UAT — Gerencia | | ~1 hora |
| Corrección de hallazgos | | |
| Re-prueba de correcciones | | |
| Sign-off UAT | | |

---

## Escenarios de Prueba

### Módulo: Gestión de Leads

| ID | Escenario | Pasos | Resultado esperado | Resultado real | Estado |
|---|---|---|---|---|---|
| UAT-L01 | Crear lead manualmente | 1. Ir a CRM > Leads. 2. Nuevo. 3. Completar datos. 4. Guardar | Lead creado correctamente | | |
| UAT-L02 | Captura de lead por email | Enviar email a alias configurado | Lead aparece en CRM automáticamente | | |
| UAT-L03 | Asignación automática de lead | Crear lead sin vendedor | Sistema asigna vendedor según regla | | |
| UAT-L04 | Convertir lead a oportunidad | Abrir lead > Convertir a oportunidad | Oportunidad creada en pipeline | | |
| UAT-L05 | Alerta de lead inactivo | Lead sin actividad > 5 días | Notificación enviada al vendedor | | |

### Módulo: Gestión de Oportunidades

| ID | Escenario | Pasos | Resultado esperado | Resultado real | Estado |
|---|---|---|---|---|---|
| UAT-O01 | Crear oportunidad | CRM > Nuevo > Completar datos | Oportunidad en primera etapa | | |
| UAT-O02 | Mover oportunidad entre etapas | Drag & drop en kanban | Oportunidad cambia de etapa, probabilidad actualizada | | |
| UAT-O03 | Registrar oportunidad ganada | Marcar como ganada | Oportunidad cierra, % = 100 | | |
| UAT-O04 | Registrar oportunidad perdida | Marcar como perdida | Sistema solicita motivo, obligatorio | | |
| UAT-O05 | Filtrar pipeline por vendedor | Aplicar filtro de vendedor | Solo aparecen sus oportunidades | | |
| UAT-O06 | Vista Kanban del pipeline | Entrar a CRM | Vista por columnas de etapa visible | | |

### Módulo: Actividades y Seguimiento

| ID | Escenario | Pasos | Resultado esperado | Resultado real | Estado |
|---|---|---|---|---|---|
| UAT-A01 | Registrar llamada en oportunidad | Oportunidad > Actividades > Nueva | Llamada registrada con fecha y notas | | |
| UAT-A02 | Programar reunión | Actividad tipo Reunión + fecha | Aparece en calendario del usuario | | |
| UAT-A03 | Enviar correo desde oportunidad | Oportunidad > Enviar mensaje | Correo enviado y registrado en historial | | |
| UAT-A04 | Recibir correo en historial | Responder al correo | Respuesta aparece en el chatter | | |

### Módulo: Reportes y Dashboards

| ID | Escenario | Pasos | Resultado esperado | Resultado real | Estado |
|---|---|---|---|---|---|
| UAT-R01 | Dashboard de ventas | Ir a Reporting > CRM | Dashboard carga con datos correctos | | |
| UAT-R02 | Pipeline por etapa | Reporting > Pipeline | Valor total por etapa visible | | |
| UAT-R03 | Actividades por vendedor | Reporting > Actividades | Actividades del período por usuario | | |
| UAT-R04 | Forecast de ventas | Reporting > Forecast | Proyección de cierre del mes | | |

---

## Clasificación de Hallazgos

| Severidad | Descripción | Plazo de corrección | ¿Bloquea go-live? |
|---|---|---|---|
| Crítico | El sistema no funciona, pérdida de datos | 24 horas | Sí |
| Alto | Funcionalidad incorrecta, sin workaround | 48-72 horas | Sí |
| Medio | Funcionalidad con desvío pero con workaround | Antes del go-live | No |
| Bajo | Cosmético o mejora de usabilidad | Post go-live | No |

---

## Bitácora de Hallazgos

| ID | Severidad | Descripción | Reportado por | Asignado a | Estado | Resolución |
|---|---|---|---|---|---|---|
| BUG-001 | | | | | | |

---

## Aprobación UAT

Al firmar, el usuario confirma que el sistema cumple los requerimientos de negocio para su área.

| Área | Key User | Firma | Fecha | Observaciones |
|---|---|---|---|---|
| Ventas | | | | |
| Supervisión Comercial | | | | |
| Gerencia | | | | |
| Marketing | | | | |
