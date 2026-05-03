# Configuración del Pipeline de Ventas

## Pipeline Definido — Flujo de Oportunidades

El pipeline de COINSA consta de 7 etapas, cada una con requisitos y actividades específicas:

---

## Etapas del Pipeline

### 1. Lead Entrante (MQL)
**Descripción:** Lead inicial sin calificar, acaba de entrar al sistema

**Origen:** Web, email, WhatsApp, base de datos, referencias

**Requisitos obligatorios:**
- Nombre del contacto
- Empresa (si es negocio)
- Medio de contacto
- Problema/necesidad inicial

**Actividades siguientes:**
- [ ] Contacto inicial (llamada o correo)
- [ ] Calificación del lead

**Responsable:** Equipo de Coordinación (Hermenegildo, Guillermo, Miguel)

**Tiempo estimado en etapa:** 2-3 días

---

### 2. Contacto Realizado (SQL)
**Descripción:** Ya realizamos primer contacto, lead calificado con necesidad identificada

**Requisitos obligatorios:**
- Nombre del contacto
- Empresa
- Necesidad/problema descrito
- Presupuesto estimado (indicativo)

**Actividades siguientes:**
- [ ] Reunión técnica (si aplica)
- [ ] Validación con ingeniería (para proyectos técnicos)

**Responsable:** Vendedor asignado

**Tiempo estimado en etapa:** 3-5 días

---

### 3. Diagnóstico Técnico
**Descripción:** Necesidad validada, presupuesto confirmado, se requiere diseño técnico

**Requisitos obligatorios:**
- Cliente confirmado (ficha completa)
- Descripción detallada de necesidad
- Especificaciones técnicas
- Presupuesto estimado (rango)
- Decisor identificado

**Actividades siguientes:**
- [ ] Dimensionamiento técnico (por Ing. Arturo u equipo técnico)
- [ ] Preparación de propuesta técnica

**Responsable:** Ing. Arturo (equipo técnico)

**Tiempo estimado en etapa:** 5-10 días

---

### 4. Validación Técnica
**Descripción:** Propuesta técnica elaborada, en revisión interna o presentación al cliente

**Requisitos obligatorios:**
- Especificaciones técnicas definidas
- Presupuesto base calculado
- Documentación técnica adjunta

**Actividades siguientes:**
- [ ] Presentación técnica al cliente
- [ ] Revisión y ajustes

**Responsable:** Ing. Arturo

**Tiempo estimado en etapa:** 3-7 días

---

### 5. Cotización Enviada
**Descripción:** Cotización formal enviada al cliente, en espera de respuesta

**Requisitos obligatorios:**
- Cotización generada en Odoo (con número)
- Fecha de envío registrada
- Contacto decisor confirmado
- Condiciones de pago especificadas
- Validez de cotización (plazo)

**Actividades siguientes:**
- [ ] Seguimiento de cotización (llamada/email)
- [ ] Negociación (si hay objeciones)
- [ ] Revisión de contrapropuesta

**Responsable:** Vendedor + Ing. Arturo (soporte técnico)

**Tiempo estimado en etapa:** 5-15 días

---

### 6. Seguimiento / Negociación
**Descripción:** Cliente respondió con objeciones, solicitudes de ajuste o renegociación

**Requisitos obligatorios:**
- Motivo de no aceptación registrado
- Propuesta de ajuste (si aplica)
- Notas de negociación en la oportunidad

**Actividades siguientes:**
- [ ] Llamada de seguimiento
- [ ] Envío de cotización modificada
- [ ] Cierre comercial

**Responsable:** Vendedor + Ing. Arturo

**Tiempo estimado en etapa:** 3-10 días

---

### 7. Cierre (Ganado / Perdido)

#### 7a. GANADO — Cierre Exitoso
**Descripción:** Cliente aceptó la cotización, se procede a generar orden de venta

**Requisitos obligatorios:**
- Fecha de aceptación registrada
- Monto final confirmado
- Orden de venta generada desde la oportunidad
- Condiciones de pago finales registradas

**Actividades posteriores:**
- [ ] Confirmación con cliente
- [ ] Seguimiento post-entrega (en 5 días de entrega)

**Responsable:** Vendedor

---

#### 7b. PERDIDO — Cierre sin Venta
**Descripción:** Cliente rechazó la propuesta, oportunidad cerrada sin venta

**Requisitos obligatorios (OBLIGATORIO):**
- Motivo de pérdida seleccionado (requerido):
  - Precio muy alto
  - Competencia (especificar quién)
  - Cambio de prioridades del cliente
  - Presupuesto insuficiente
  - Especificaciones no ajustan a necesidad
  - Cliente sin contacto (inactivo)
  - Otra razón

**Actividades posteriores:**
- [ ] Documentar lecciones aprendidas
- [ ] Seguimiento futuro (si aplica)

**Responsable:** Vendedor

---

## Configuración Técnica en Odoo

### Campos Obligatorios por Etapa

| Etapa | Cliente | Monto | Vendedor | Descripción | Decisor | Fecha cierre |
|---|---|---|---|---|---|---|
| 1. Lead Entrante | ✗ | ✗ | ✓ | ✓ | ✗ | ✗ |
| 2. Contacto Realizado | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| 3. Diagnóstico | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4. Validación Técnica | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 5. Cotización Enviada | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 6. Seguimiento | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 7. Cierre | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

### Probabilidades por Etapa

| Etapa | % Probabilidad | Justificación |
|---|---|---|
| Lead Entrante | 10% | No calificado aún |
| Contacto Realizado | 25% | Lead calificado pero sin propuesta |
| Diagnóstico | 40% | En análisis técnico |
| Validación Técnica | 50% | Propuesta en revisión |
| Cotización Enviada | 70% | Cliente está evaluando |
| Seguimiento | 50% | Negociando ajustes |
| Cierre Ganado | 100% | Cierre confirmado |
| Cierre Perdido | 0% | Sin venta |

---

## Automatizaciones Configuradas

1. **Alerta de leads inactivos:** Lead sin actividad por 7+ días → notificación al supervisor
2. **Recordatorio de seguimiento:** Oportunidad en etapa 5 (Cotización) por 10+ días → recordatorio automático
3. **Cierre automático de oportunidades:** Oportunidad sin movimiento por 90 días → validación de cierre
4. **Actividad de confirmación post-entrega:** Al validar entrega → crear actividad de seguimiento (Llamada) asignada al vendedor, plazo 2 días hábiles

---

## Validaciones y Controles

- [ ] No permitir cerrar etapa sin campos obligatorios completos
- [ ] Al marcar PERDIDO, requiere motivo obligatorio
- [ ] Al generar cotización, validar que cliente esté completo
- [ ] Sincronización automática de monto entre cotización y oportunidad
- [ ] Historial de cambios de etapa registrado (auditoría)

---

## Actividades de Implementación

- [ ] Crear 7 etapas en Odoo CRM
- [ ] Configurar campos obligatorios por etapa
- [ ] Definir probabilidades
- [ ] Crear automatizaciones
- [ ] Configurar alertas
- [ ] Capacitar a usuarios en el nuevo flujo
- [ ] Validar con líderes de equipo
