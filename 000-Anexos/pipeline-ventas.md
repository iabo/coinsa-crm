# Diseño del Pipeline de Ventas

## Proceso Comercial General

```
[LEAD]
  │
  ▼ (calificación)
[NUEVO LEAD]
  │
  ▼ (primer contacto)
[CONTACTADO]
  │
  ▼ (reunión / demo agendada)
[REUNIÓN AGENDADA]
  │
  ▼ (propuesta enviada)
[PROPUESTA ENVIADA]
  │
  |   Ganado-Perdido 
  ▼ (negociación)
[EN NEGOCIACIÓN]
  │
  ├──────────────────► [GANADO]
  │
  └──────────────────► [PERDIDO]
```

---

## Etapas del Pipeline

| # | Etapa | Probabilidad | Descripción | Acciones mínimas para avanzar |
|---|---|---|---|---|
| 1 | Nuevo Lead | 10% | Lead recién captado, aún sin contacto | Verificar datos de contacto |
| 2 | Contactado | 20% | Primer contacto realizado, interés confirmado | Registrar resultado del primer contacto |
| 3 | Reunión Agendada | 40% | Reunión / demo programada con el prospecto | Preparar presentación |
| 4 | Propuesta Enviada | 60% | Cotización o propuesta formal enviada | Enviar propuesta desde Odoo |
| 5 | En Negociación | 80% | Propuesta recibida, negociando términos | Registrar objeciones y contrapropuestas |
| 6 | Ganado | 100% | Contrato firmado / pedido confirmado | Crear orden de venta |
| — | Perdido | 0% | Oportunidad no prosperó | Registrar motivo de pérdida (obligatorio) |

---

## Campos Clave por Oportunidad

| Campo | Tipo | Obligatorio | Cuándo se completa |
|---|---|---|---|
| Nombre de la oportunidad | Texto | Sí | Al crear |
| Empresa / Cliente | Many2one | Sí | Al crear |
| Contacto responsable | Many2one | Sí | Al crear |
| Vendedor asignado | Many2one | Sí | Al crear (automático) |
| Equipo de ventas | Many2one | Sí | Al crear (automático) |
| Valor estimado | Monetario | Sí | Al pasar a "Propuesta" |
| Fecha de cierre esperada | Fecha | Sí | Al pasar a "Reunión Agendada" |
| Probabilidad | % | Automático | Por etapa |
| Fuente del lead | Selección | Sí | Al crear |
| Notas internas | Texto | No | Cuando aplique |
| Motivo de pérdida | Selección | Condicional | Solo si se marca como "Perdido" |

---

## Fuentes de Lead

| Fuente | Canal |
|---|---|
| Web Orgánico | Formulario del sitio web |
| Referido | Recomendación de cliente existente |
| Llamada en frío | Prospección activa del vendedor |
| Email entrante | Correo de interés directo |
| LinkedIn / Redes Sociales | Prospección digital |
| Evento / Feria | Contacto en evento presencial |
| Base de datos interna | Minado de clientes existentes o inactivos en Odoo |
| Plática PSI / Evento técnico | Contacto captado en presentación técnica (PSI u otros eventos) |

---

## Motivos de Pérdida

| Motivo | Categoría |
|---|---|
| Precio fuera de presupuesto | Económico |
| Se fue con la competencia | Competencia |
| No hay presupuesto este año | Timing |
| El proyecto fue cancelado | Decisión interna |
| No logramos contactarlo | Sin respuesta |
| Requerimiento no cubierto | Producto |
| [Motivo X] | [Categoría] |

---

## Automatizaciones del Pipeline

| Automatización | Trigger | Acción |
|---|---|---|
| Asignación de lead | Lead nuevo entra al sistema | Asignar al vendedor según regla round-robin |
| Alerta de inactividad | Sin actividad en 5 días | Notificación al vendedor y supervisor |
| Recordatorio de seguimiento | Actividad vencida | Email al vendedor |
| Notificación de oportunidad ganada | Etapa cambia a "Ganado" | Email al supervisor del equipo |
| Solicitud de feedback | Etapa cambia a "Perdido" | Tarea automática: registrar motivo |

---

## Variante de Pipeline — Ventas Técnicas (Ing. Arturo)

> Pendiente de decisión en Sesión 4 (punto 5).
> Para oportunidades de ingeniería, se evalúa agregar una etapa intermedia de **Diseño Técnico** antes de la propuesta formal.

| # | Etapa | Probabilidad | Descripción |
|---|---|---|---|
| 1 | Nuevo Lead | 10% | Lead recibido |
| 2 | Contactado | 20% | Primer contacto confirmado |
| 3 | **Diseño Técnico** | **40%** | **Arturo diseña la solución y registra especificaciones en la oportunidad de Odoo** |
| 4 | Propuesta Enviada | 60% | Cotización con especificaciones técnicas enviada al cliente |
| 5 | En Negociación | 80% | Negociando términos y condiciones |
| 6 | Ganado | 100% | Orden de venta confirmada |
| — | Perdido | 0% | Registrar motivo (obligatorio) |

**Consideración:** Esta variante puede configurarse como pipeline independiente para el equipo de ventas técnicas en Odoo, manteniendo el pipeline estándar para ventas internas (Hermenegildo, Guillermo, Miguel).
