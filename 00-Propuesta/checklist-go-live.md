# Checklist de Go-Live

> **Aprobación requerida:** Este checklist debe ser completado y firmado por el PM y el patrocinador antes de proceder al go-live.

---

## PRE GO-LIVE — Semana anterior

### Técnico
- [ ] Ambiente de producción configurado y verificado
- [ ] Todos los módulos instalados en producción
- [ ] Configuraciones replicadas de staging a producción
- [ ] Customizaciones desplegadas y probadas en producción
- [ ] Integración con correo electrónico funcionando
- [ ] Integración con [sistema X] funcionando
- [ ] Prueba de backup y restauración exitosa
- [ ] Monitoreo de servidor configurado
- [ ] URLs y dominios configurados correctamente
- [ ] Certificado SSL activo y válido

### Funcional
- [ ] UAT completado y firmado por todos los usuarios clave
- [ ] Todos los hallazgos críticos y altos del UAT corregidos
- [ ] Pipeline de ventas configurado con etapas validadas
- [ ] Equipos de ventas y usuarios creados
- [ ] Roles y permisos verificados por perfil
- [ ] Plantillas de correo revisadas y aprobadas
- [ ] Automatizaciones probadas y validadas
- [ ] Reportes y dashboards verificados

### Datos
- [ ] Migración de datos en staging 100% validada
- [ ] Script de migración de producción ensayado
- [ ] Tiempo de migración estimado documentado
- [ ] Archivos de migración actualizados y listos
- [ ] Plan de rollback documentado y comunicado al equipo

### Capacitación
- [ ] Al menos 80% de usuarios finales capacitados
- [ ] Manuales de usuario distribuidos
- [ ] Guía rápida disponible en el sistema
- [ ] Canal de soporte post go-live comunicado a usuarios

---

## DÍA D — Go-Live

### Ventana de Migración (fuera de horario laboral)

| # | Actividad | Responsable | Hora estimada | Estado |
|---|---|---|---|---|
| 1 | Comunicado de inicio de mantenimiento | PM | | |
| 2 | Backup final de producción (si hay datos previos) | Admin | | |
| 3 | Inicio migración de contactos / empresas | Datos | | |
| 4 | Verificación de conteo de contactos | Datos | | |
| 5 | Inicio migración de oportunidades | Datos | | |
| 6 | Verificación de conteo de oportunidades | Datos | | |
| 7 | Verificación funcional rápida (smoke test) | Consultor | | |
| 8 | Confirmación de go/no-go | PM + Patrocinador | | |
| 9 | Comunicado de apertura a usuarios | PM | | |

### Smoke Test Post-Migración

- [ ] Login exitoso con diferentes perfiles de usuario
- [ ] Crear lead de prueba
- [ ] Convertir lead a oportunidad
- [ ] Mover oportunidad entre etapas del pipeline
- [ ] Registrar actividad (llamada / tarea)
- [ ] Enviar correo desde oportunidad
- [ ] Verificar dashboard de ventas
- [ ] Verificar que los datos migrados son visibles y correctos

---

## POST GO-LIVE — Hipercare (2 semanas)

### Semana 1 — Acompañamiento intensivo
- [ ] Equipo de soporte disponible durante horario laboral completo
- [ ] Reunión diaria de 30 min para revisión de incidencias
- [ ] Resolución de incidencias críticas < 4 horas
- [ ] Registro de todas las incidencias en bitácora

### Semana 2 — Estabilización
- [ ] Reunión cada 2 días para revisión de incidencias
- [ ] Resolución de incidencias críticas < 8 horas
- [ ] Transferencia de conocimiento al equipo de soporte interno

### Cierre de Hipercare
- [ ] Reporte de incidencias del período hipercare
- [ ] Pendientes priorizados para versión siguiente
- [ ] Transición formal al equipo de soporte regular
- [ ] Reunión de lecciones aprendidas del proyecto
- [ ] Firma de acta de cierre del proyecto

---

## Criterios de NO GO-LIVE (rollback automático)

Ejecutar rollback inmediatamente si:
- Migración de datos con error > 5% en registros críticos
- Smoke test falla en funciones core del CRM
- Sistema con tiempo de respuesta > 10 segundos en funciones básicas
- Cualquier incidente de seguridad durante el go-live

---

## Firmas de Aprobación Go-Live

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Project Manager | | | |
| Patrocinador del Proyecto | | | |
| Líder Funcional CRM | | | |
| Administrador de Sistemas | | | |
