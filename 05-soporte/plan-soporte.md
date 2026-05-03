# Plan de Soporte Post-Implementación

## Modelo de Soporte

### Niveles de Soporte

```
NIVEL 1 — Soporte interno (Key Users / Super Usuarios)
  └── Dudas funcionales básicas, configuraciones menores
  └── Tiempo de respuesta: mismo día
  └── Responsable: Key Users entrenados

NIVEL 2 — Soporte consultor Odoo
  └── Bugs funcionales, configuraciones avanzadas, nuevas necesidades
  └── Tiempo de respuesta: 24-48 horas
  └── Responsable: Equipo consultor (SLA por contrato)

NIVEL 3 — Soporte técnico / desarrollador
  └── Bugs de código, customizaciones, actualizaciones de versión
  └── Tiempo de respuesta: según acuerdo de SLA
  └── Responsable: Consultor técnico / Partner Odoo
```

---

## SLA — Acuerdos de Nivel de Servicio

| Severidad | Descripción | Tiempo de respuesta | Tiempo de resolución |
|---|---|---|---|
| P1 — Crítico | Sistema caído, imposible trabajar | 1 hora | 4 horas |
| P2 — Alto | Función crítica no opera, sin workaround | 4 horas | 24 horas |
| P3 — Medio | Función con desvío, con workaround | 8 horas | 3 días |
| P4 — Bajo | Mejora, cosmético, no urgente | 24 horas | Próximo sprint |

---

## Canal de Soporte

| Canal | Para qué | Disponibilidad |
|---|---|---|
| soporte.crm@coinsa.com | Reportar incidencias y dudas funcionales | 24/7 (respuesta en horario laboral) |
| Backlog / registro de incidencias en Odoo o herramienta acordada | Seguimiento de incidencias y mejoras | Horario laboral |
| WhatsApp corporativo / grupo operativo | Urgencias P1/P2 | Horario laboral |
| [Teléfono] | Solo incidencias críticas P1 | Horario laboral |

---

## Gestión de Mejoras Continuas

### Proceso para solicitar mejoras
1. Usuario identifica mejora o nueva necesidad
2. Key User documenta la solicitud en formato estándar
3. PM evalúa impacto y prioridad
4. Si aprobado: entra al backlog del próximo ciclo de mejoras
5. Consultor diseña e implementa en ambiente de desarrollo
6. Validación en staging
7. Despliegue en producción con release note

### Ciclo de releases
- Mejoras menores: mensual
- Mejoras mayores: trimestral
- Actualizaciones de versión Odoo: según evaluación anual

---

## Indicadores de Salud del Sistema

| KPI | Frecuencia de medición | Meta |
|---|---|---|
| Uptime del sistema | Mensual | > 99.5% |
| Tiempo promedio de resolución de incidencias | Mensual | < SLA |
| Satisfacción del usuario (encuesta) | Trimestral | > 4/5 |
| Adopción: usuarios activos / usuarios totales | Mensual | > 90% |
| Leads sin gestionar > 7 días | Semanal | < 5% |

---

## Revisiones Periódicas

| Revisión | Frecuencia | Participantes | Objetivo |
|---|---|---|---|
| Revisión operativa | Mensual | PM + Key Users | Incidencias, adopción, pendientes |
| Revisión estratégica | Trimestral | PM + Patrocinadores | KPIs de negocio, mejoras, roadmap |
| Health check técnico | Semestral | Admin + Consultor técnico | Performance, seguridad, actualizaciones |
