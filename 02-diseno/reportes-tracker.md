# Reportes COINSA-MATIK

> **Estados:** 🟢 Listo (solo navegar) · 🔧 Config rápida (5-15 min) · ⏳ Pendiente (requiere datos/setup mayor) · ⛔ Fuera de scope hoy

---

## Ola 1 — Implementar hoy (sin configuración)

Estos existen en Odoo ahora mismo. Solo hay que navegar y guardar el favorito/filtro.

- [x] ✅ **[RPT-01](#rpt-01)** · Ventas totales del equipo vs. meta

- [x] ✅ **[RPT-04](#rpt-04)** · Cobranza — facturas cobradas en tiempo

- [x] ✅ **[RPT-09](#rpt-09)** · Ventas individuales por vendedor vs. meta

- [x] ✅ **[RPT-11](#rpt-11)** · Ventas totales (ingeniería)

- [x] ✅ **[RPT-20](#rpt-20)** · Valor del pipeline activo (pipeline coverage)

- [x] ✅ **[RPT-23](#rpt-23)** · Actividades de CRM completadas por vendedor

---

## Ola 2 — Config rápida (hoy o mañana)

Requieren pequeños ajustes en Configuración de Odoo. Ninguno tarda más de 15 min.

- [x] ✅ **[RPT-24](#rpt-24)** · Tasa de cotizaciones perdidas y motivo

- [x] ✅ **[RPT-18](#rpt-18)** · Antigüedad de oportunidades sin actividad

- [x] ✅ **[RPT-17](#rpt-17)** · Tiempo de vida promedio de oportunidad

- [x] ✅ **[RPT-05](#rpt-05)** · Tasa de conversión por etapa del pipeline

- [x] ✅ **[RPT-02/RPT-10](#rpt-02-rpt-10)** · Ventas por marca / línea de producto

- [x] ✅ **[RPT-07](#rpt-07)** · Nuevas oportunidades (clientes nuevos)

- [x] ✅ **[RPT-16](#rpt-16)** · Oportunidades generadas por ingeniería (cross-sell)

---

## Ola 3 — Requiere setup mayor o datos previos

No bloquean la Ola 1/2, pero necesitan decisiones de configuración o que el sistema ya tenga datos reales.

- [ ] ⏳ **RPT-06** · Visitas a clientes — cumplimiento de programa
  - Bloqueante: crear tipo de actividad «Visita» en Odoo (CRM → Configuración → Tipos de actividad) y establecer política de registro obligatorio
  - Reporte disponible una vez haya registros: CRM → Actividades → filtrar por tipo «Visita»

- [ ] ⏳ **RPT-12** · Ventas por tipo de solución (ingeniería)
  - Bloqueante: crear campo selección «Tipo de solución» (venta directa / servicio / integración) en oportunidades de ingeniería
  - Requiere: CRM → Configuración → Campos personalizados (o módulo Studio)

- [ ] ⏳ **RPT-14** · Proyectos entregados en tiempo
  - Bloqueante: módulo Proyectos activo + campo «Fecha compromiso» como obligatorio al crear proyecto
  - Reporte: Proyectos → Análisis → comparar Fecha límite vs. Fecha cierre real

- [ ] ⏳ **RPT-19** · Tiempo de entrega de cotización
  - Ruta: Ventas → Presupuestos → columna «Fecha de envío» – «Fecha de creación»
  - Bloqueante: requiere que los presupuestos ya se estén registrando con fecha de envío

- [ ] ⏳ **RPT-21** · Pronóstico vs. ventas reales (forecast accuracy)
  - Bloqueante: necesita al menos 1 mes de datos de pipeline con probabilidades asignadas
  - Ruta futura: CRM → Ingreso esperado (Σ valor × probabilidad) vs. Ventas → Facturación real

- [ ] ⏳ **RPT-26** · % Proyectos con retraso (DBR)
  - Mismo prerrequisito que RPT-14: módulo Proyectos + fechas compromiso capturadas

---

## Fuera de scope por ahora

Sin fuente de dato definida ni plataforma asignada. No tocar hasta decidir arquitectura.

- ⛔ **RPT-03** · Margen de contribución promedio — requiere costos en Odoo por línea/producto
- ⛔ **RPT-08** · Evaluación cliente externo (NPS) — sin plataforma de encuesta asignada
- ⛔ **RPT-13** · Margen contribución proyectos — sin costos por proyecto en ERP
- ⛔ **RPT-15** · Tasa de garantías — sin proceso de registro (Helpdesk no activo)
- ⛔ **RPT-22** · Evaluación cliente interno (ventas → ingeniería) — Fase II, sin herramienta
- ⛔ **RPT-25** · Tiempo respuesta técnica ingeniería → ventas — requiere Helpdesk interno activo

---

## Detalle de Reportes Implementados

---

### RPT-01
**Ventas totales del equipo vs. meta**

**Estado:** ✅ Implementado — 2026-05-15
**Usuario objetivo:** Coordinador Comercial

**Navegación:**
1. Módulo **CRM** (menú principal)
2. Menú superior → **Reportes** → **Flujo**
3. Quitar cualquier filtro activo por defecto (clic en × de cada pill)
4. **Filtros** → **Ganado**
5. **Filtros** → Fecha de cierre → **[mes en curso]**
6. **Agrupar por** → **Equipo de ventas** (primer nivel)
7. **Agrupar por** → **Vendedor** (segundo nivel, en ese orden)
8. **Medidas** → seleccionar **Ingreso esperado**
9. **Favoritos** → Guardar búsqueda actual → nombre `RPT-01 Ventas equipo → vendedor` → Guardar

**Lógica:**
Nivel 1 muestra el total del equipo — el coordinador ve el número agregado de su equipo.
Nivel 2 desglosa por vendedor individual — permite detectar quién está por encima o por debajo.

**Uso mensual:**
Cambiar filtro de fecha: Filtros → Fecha de cierre → [mes]. Para vista trimestral usar Trimestre 1/2/3/4.

**Vista alternativa — Dashboard vs. Meta (más visual):**
CRM → menú superior → **Ventas** → **Equipos**
Muestra cada equipo con barra de progreso `Facturación: X / Meta`. Es la vista más directa para el coordinador.

Estado de metas configuradas por equipo:
- INGENIERIA → 1M/mes ✅
- VENTAS A (SONORA) → 6M/mes ✅
- ZONA B (FORÁNEOS) → sin meta ⚠️
- VENTA DIGITAL → sin meta ⚠️
- ADMINISTRACION → sin meta ⚠️

Pendiente: definir objetivos para los 3 equipos restantes (clic en «Haga clic para definir un objetivo» en cada tarjeta).

**Medidas disponibles en Análisis de flujo (referencia futura):**
- `Ingreso esperado` — valor de ventas ganadas (principal)
- `Días para el cierre` — ciclo de venta (útil para RPT-17, ver nota en esa sección)
- `Número` — conteo de oportunidades cerradas

---

### RPT-09
**Ventas individuales por vendedor vs. meta**

**Estado:** ✅ Implementado — 2026-05-15
**Usuario objetivo:** Vendedor (vista propia) / Coordinador (comparativa entre vendedores)

**Navegación:**
1. Módulo **CRM** (menú principal)
2. Menú superior → **Reportes** → **Flujo**
3. Cargar favorito `RPT-01 Ventas equipo → vendedor` como base
4. En **Agrupar por** → quitar **Equipo de ventas**, dejar solo **Vendedor**
5. Filtros **Ganado** + **Fecha de cierre → [mes]** se mantienen igual
6. **Favoritos** → Guardar búsqueda actual → nombre `RPT-09 Ventas por vendedor` → Guardar

**Diferencia con RPT-01:**
RPT-01 agrupa primero por equipo (vista coordinador). RPT-09 muestra directamente cada vendedor sin nivel de equipo — útil para comparación directa entre individuos.

**Metas individuales por vendedor:**
Actualmente las metas están configuradas a nivel equipo, no por vendedor. Para metas individuales se requiere el módulo de **Gamificación** o configurar objetivos manualmente. Pendiente evaluar si esta granularidad es necesaria en Fase 1.

---

### RPT-11
**Ventas totales (ingeniería)**

**Estado:** ✅ Implementado — 2026-05-15
**Usuario objetivo:** Líder de Ingeniería / Dirección

**Navegación:**
1. Módulo **CRM** (menú principal)
2. Menú superior → **Reportes** → **Flujo**
3. Quitar filtros activos por defecto (clic en ×)
4. **Filtros** → **Ganado**
5. **Filtros** → Fecha de cierre → **[mes en curso]**
6. En la barra de búsqueda escribir `INGENIERIA` → seleccionar **Equipo de ventas contiene “INGENIERIA”**
7. **Agrupar por** → **Vendedor** (un solo nivel — el equipo ya está aislado por el filtro)
8. **Medidas** → **Ingreso esperado**
9. **Favoritos** → Guardar búsqueda actual → nombre `RPT-11 Ventas ingeniería` → Guardar

**Diferencia con RPT-01/09:**
Mismo reporte de Flujo pero restringido al equipo Ingeniería. No se necesita el nivel de equipo en el agrupador porque el filtro ya lo aísla. Muestra la contribución individual de cada ingeniero.

**Meta del equipo:** MX$1,000,000 / mes (configurada en CRM → Ventas → Equipos → INGENIERIA)
Vista vs. meta: CRM → Ventas → Equipos → tarjeta INGENIERIA → barra `Facturación: X / 1M`

---

### RPT-04
**Cobranza — facturas cobradas en tiempo**

**Estado:** ✅ Implementado — 2026-05-15
**Usuario objetivo:** Coordinador Comercial / Administración

---

**Flujo A — Estado actual de cartera (operativo)**

**Navegación:**
1. Módulo **Contabilidad** (menú principal)
2. Menú superior → **Reportes**
3. Sección «Reportes del contacto» → clic en **Cuenta antigua por cobrar**
4. El reporte se genera automáticamente al día de hoy
5. Opcional: **Opciones** → «Desplegar todo» para ver facturas individuales por cliente
6. Exportar: botones **PDF** o **XLSX** en la esquina superior izquierda
7. Guardar vista: botón **GUARDAR** → nombre `RPT-04 Cobranza`

**Cómo leer:**
- **En fecha** = facturas abiertas que aún no vencen
- **1-30, 31-60, 61-90, 91-120** = días vencidas sin pagar
- **Antiguos** = +120 días (zona crítica)
- **Total** = cartera total pendiente

Cálculo del KPI: `En fecha / Total × 100` (meta ≥80%)

---

**Flujo B — Historial de facturas cobradas (para % real pagado a tiempo)**

**Navegación:**
1. Módulo **Contabilidad** → menú superior → **Clientes** → **Facturas**
2. **Filtros** → **Pagado**
3. **Filtros** → Fecha de factura → **[mes en curso]**
4. Activar columnas adicionales: clic en el ícono de columnas (esquina superior derecha, junto a los iconos de vista) → marcar **Vendedor** y **Equipo de ventas**
5. Exportar: botón **SUBIR** (ícono descarga, junto a N/C) → seleccionar **XLSX**
6. En Excel: calcular `filas donde Fecha pago ≤ Fecha vencimiento / total filas × 100`

---

**⚠️ Observación crítica — Fecha de vencimiento no utilizada**
Al revisar las facturas pagadas, la columna **Fecha de vencimiento aparece en blanco en todos los registros**. Esto significa que actualmente el KPI real de «cobrado a tiempo» no es calculable de forma precisa.

Workaround temporal: usar `Fecha de pago – Fecha de factura` como proxy del tiempo de cobro.

Acción requerida: configurar **términos de pago** en los registros de clientes y/o en las facturas para que Odoo calcule automáticamente la fecha de vencimiento. Esto desbloquea tanto el Flujo B como las alertas automáticas.

---

**🔔 Pendiente revisar — Alerta automática 5 días antes del vencimiento**
Odoo tiene un módulo nativo de seguimiento de pagos. Verificar si está activo:
Contabilidad → Clientes → **Seguimiento** (o «Seguimiento de pagos»)

Si existe, permite configurar niveles de recordatorio con email automático al cliente:
- Nivel 1: -5 días antes del vencimiento (aviso preventivo)
- Nivel 2: día 0 (recordatorio de vencimiento)
- Nivel 3: +7, +15 días (cobranza activa)

**Prerrequisito:** que las facturas tengan Fecha de vencimiento configurada (ver observación arriba).

---

### RPT-20
**Valor del pipeline activo (pipeline coverage)**

**Estado:** ✅ Implementado — 2026-05-15
**Usuario objetivo:** Coordinador Comercial / Dirección

**Vista principal — Dashboard de Equipos:**

**Navegación:**
1. Módulo **CRM** (menú principal)
2. Menú superior → **Ventas** → **Equipos**
3. Cada tarjeta de equipo muestra en la parte superior derecha el **ingreso esperado del pipeline activo** (oportunidades abiertas)
4. En la parte inferior de cada tarjeta: barra `Facturación: X / Meta` como referencia de cobertura

**Cómo leer:**
- El valor en la tarjeta = suma de ingreso esperado de oportunidades abiertas del equipo
- Cobertura saludable = pipeline activo ≥3× la meta mensual
- Si el pipeline es menor a 2× la meta → alerta de riesgo de ventas

**Vista alternativa — Análisis de flujo:**

**Navegación:**
1. CRM → **Reportes** → **Flujo**
2. Sin filtro de Ganado/Perdido (dejar solo oportunidades **Activo**)
3. **Filtros** → **Activo**
4. **Agrupar por** → **Equipo de ventas**
5. **Medidas** → **Ingreso esperado**
6. El total = valor del pipeline activo por equipo

**Favorito guardado:** `RPT-20 Pipeline activo` (guardar desde la vista Análisis de flujo alternativa)

**Cálculo del KPI:**
`Cobertura = Σ Ingreso esperado (oportunidades abiertas) / Meta mensual del equipo`
Meta recomendada: ratio ≥3.0x. Por debajo de 2.0x = riesgo.

---

### RPT-23
**Actividades de CRM completadas por vendedor**

**Estado:** ✅ Implementado — 2026-05-15
**Usuario objetivo:** Coordinador Comercial / Líder de ventas

**Navegación:**
1. Módulo **CRM** (menú principal)
2. Menú superior → **Reportes** → **Actividades**
3. Vista lista activa por defecto
4. **Filtros** → buscar y seleccionar **Hecho** (actividades marcadas como completadas)
5. **Filtros** → agregar rango de fecha: **Fecha de vencimiento → [semana o mes actual]**
6. **Agrupar por** → **Asignado a** (para ver totales por vendedor)
7. **Favoritos** → Guardar búsqueda actual → nombre `RPT-23 Actividades por vendedor` → Guardar

**Cómo leer:**
- Cada grupo = un vendedor con el conteo de actividades completadas en el período
- Tipos de actividad que cuenta: llamadas, emails, visitas, demos, tareas
- Un vendedor con 0 actividades en la semana = sin seguimiento activo

**Cálculo del KPI:**
`Actividades completadas / Actividades programadas × 100`
Meta: definir mínimo semanal por rol (ej. 10 actividades/semana por vendedor).

**Nota:** Este reporte mide disciplina de actividad, no resultados. Complementa RPT-01 — un vendedor puede tener muchas actividades pero pocas ventas (problema de calidad) o pocas actividades y muchas ventas (cliente clave recurrente).

---

### RPT-24
**Tasa de cotizaciones perdidas y motivo**

**Estado:** ✅ Implementado — 2026-05-15
**Usuario objetivo:** Coordinador Comercial / Dirección

**Configuración previa (ya aplicada):**
CRM → Configuración → **Motivos de pérdida** → agregar razones relevantes para COINSA-MATIK.
Nota: el feature ya estaba habilitado en esta instancia, no requirió activación en Ajustes.

**Navegación:**
1. Módulo **CRM** (menú principal)
2. Menú superior → **Reportes** → **Flujo**
3. Quitar filtros activos por defecto (clic en ×)
4. **Filtros** → **Perdido**
5. **Agrupar por** → **Motivo de pérdida**
6. **Medidas** → **Número** (conteo de oportunidades perdidas por motivo)
7. **Favoritos** → Guardar búsqueda actual → nombre `RPT-24 Pérdidas por motivo` → Guardar

**Cómo leer:**
- Cada barra = un motivo de pérdida con su conteo de oportunidades
- El motivo más alto = el cuello de botella comercial principal
- Oportunidades sin motivo asignado = registros incompletos (disciplina pendiente)

**Cálculo del KPI:**
`% pérdidas = Oportunidades perdidas / Total oportunidades cerradas × 100`
Para desglose: cambiar Medidas a **Ingreso esperado** para ver valor económico perdido por motivo.

**Nota importante:** El reporte estará vacío o con datos incompletos hasta que los vendedores adopten el hábito de seleccionar el motivo al marcar una oportunidad como perdida. El dato se vuelve confiable después de 30-60 días de uso consistente.

**Acción de adopción requerida:** Comunicar al equipo que al cerrar una oportunidad como perdida, el campo **Motivo de pérdida es obligatorio**. Sin este dato el reporte no tiene valor.

---

### RPT-18
**Antigüedad de oportunidades sin actividad**

**Estado:** ✅ Implementado — 2026-05-15
**Usuario objetivo:** Coordinador Comercial / Líder de ventas

**Navegación:**
1. Módulo **CRM** → vista **Flujo** → cambiar a **Vista lista** (icono de lista, esquina superior derecha)
2. **Filtros** → **Oportunidades abiertas**
3. **Filtros** → **Agregar filtro personalizado**
   - Campo: **Fecha límite de la siguiente actividad**
   - Operador: **no está establecido**
   - Clic en **Aplicar**
4. Ordenar por columna **Última acción** (clic en el encabezado) → ascendente (más antiguo primero)
5. **Favoritos** → Guardar búsqueda actual → nombre `RPT-18 Sin actividad` → Guardar

**Cómo leer:**
- Cada fila = oportunidad activa sin ninguna actividad futura programada
- Las filas al inicio (ordenadas por Última acción asc.) = las más abandonadas
- Columna **Última acción** indica cuándo fue el último contacto registrado

**Umbrales de alerta:**
- ⚠️ Amarillo: sin actividad >7 días
- 🔴 Rojo: sin actividad >15 días

**Cálculo del KPI:**
`Nº oportunidades abiertas sin actividad programada`
Meta ideal: 0. En la práctica, cualquier número >0 requiere acción inmediata del coordinador.

**Nota:** Este es el indicador más directo de abandono del CRM. Una oportunidad sin actividad = nadie la está trabajando. Revisar este reporte debe ser parte de la reunión semanal del equipo comercial.

---

### RPT-17
**Tiempo de vida promedio de oportunidad (ciclo de venta)**

**Estado:** ✅ Implementado — 2026-05-15
**Usuario objetivo:** Coordinador Comercial / Dirección

**Navegación:**
1. Módulo **CRM** (menú principal)
2. Menú superior → **Reportes** → **Flujo**
3. Quitar filtros por defecto (clic en ×)
4. **Filtros** → **Ganado**
5. **Filtros** → Fecha de cierre → **[mes en curso]**
6. **Agrupar por** → **Equipo de ventas**
7. **Medidas** → activar **Días para el cierre** + **Número** (ambas simultáneamente)
8. Cambiar a **vista pivote** (icono de tabla)
9. **Favoritos** → Guardar búsqueda actual → nombre `RPT-17 Ciclo de venta` → Guardar

**Cómo leer:**
- Columna **Días para el cierre** = suma total de días de todas las oportunidades del grupo
- Columna **Número** = cantidad de oportunidades ganadas en el período
- **Promedio real = Días para el cierre / Número** (calcular por fila)
- Ignorar filas con Días = 0.00 (etapas sin fecha de cierre registrada)

Ejemplo con datos reales de staging (2026, ganadas):
- INGENIERIA: 36 días / 1 deal = **36 días promedio**
- VENTAS A (SONORA): 385 días / 12 deals = **32.1 días promedio**
- Total: 421 días / 13 deals = **32.4 días promedio**

**Cálculo del KPI:**
`Ciclo promedio (días) = Σ Días para el cierre / Nº oportunidades ganadas`
Odoo muestra la suma, no el promedio. La división es manual o vía exportación XLSX.

**Observación técnica — campo descartado:** El campo **Días a convertir** dio 0.00 en todos los registros porque las oportunidades se crean directamente sin pasar por etapa de lead.

**Limitación de Odoo:** El gráfico de barras muestra SUMA de días (no promedio). No usar el gráfico para este KPI — usar exclusivamente la vista pivote con ambas medidas.

---

### RPT-05
**Tasa de conversión por etapa del pipeline**

**Estado:** ✅ Implementado — 2026-05-15
**Usuario objetivo:** Coordinador Comercial / Dirección

**Navegación:**
1. Módulo **CRM** (menú principal)
2. Menú superior → **Reportes** → **Flujo**
3. Quitar todos los filtros activos (clic en ×)
4. **Agrupar por** → **Etapa**
5. **Medidas** → **Número**
6. Vista **gráfico de barras**
7. **Favoritos** → Guardar búsqueda actual → nombre `RPT-05 Embudo por etapa` → Guardar

**Cómo leer:**
- Cada barra = número de oportunidades activas en esa etapa
- Barras decrecientes de izquierda a derecha = forma de embudo normal
- Una barra desproporcionadamente alta en una etapa = cuello de botella

**Cálculo del KPI:**
`Tasa de conversión etapa N→N+1 = Oportunidades en etapa N+1 / Oportunidades en etapa N × 100`

Datos reales de staging (pipeline activo 2026):
- **Nuevo → Diagnóstico:** ~75 / 360 = **21% conversión**
- **Diagnóstico → Cotizado:** ~15 / 75 = **20% conversión**
- **Conversión total (Nuevo → Cotizado):** 15 / 360 = **4.2%**

**Cuello de botella identificado:** La mayor caída ocurre en Nuevo → Diagnóstico. La mayoría de oportunidades se quedan sin avanzar de la primera etapa.

**Nota:** Este reporte muestra el pipeline **activo** (oportunidades abiertas). Para ver conversión histórica (cerradas), agregar filtro **Ganado** + rango de fecha y comparar el conteo por etapa en la que estaban al cerrarse.

---

### RPT-02 / RPT-10
**Ventas por marca / línea de producto**

**Estado:** ✅ Implementado (funcional con limitación) — 2026-05-15
**Usuario objetivo:** Coordinador Comercial / Vendedor individual

**Navegación:**
1. Módulo **CRM** (menú principal)
2. Menú superior → **Reportes** → **Flujo**
3. Quitar filtros por defecto (clic en ×)
4. **Filtros** → **Ganado** + **Fecha de cierre → [mes en curso]**
5. **Agrupar por** → **Etiquetas**
6. **Medidas** → **Ingreso esperado**
7. Vista **gráfico de barras**
8. **Favoritos** → Guardar búsqueda actual → nombre `RPT-02 Ventas por marca` → Guardar

**Cómo leer:**
- Cada barra = suma de ingreso esperado de oportunidades ganadas con esa etiqueta
- La barra más alta = la marca/línea con mayor volumen de ventas en el período

**Estado actual de las etiquetas (45 registradas):**
Las etiquetas mezclan tres categorías distintas sin separación:
- **Sectores/industria** (1-17): Minería, Energía, Alimentos, Automotriz, etc.
- **Números de O.C.** (18-21): etiquetas operacionales (O.C.: 4658, etc.)
- **Marcas/productos** (23-45): Sensores Banner, HMI SIEMENS, Festo, Omron, Dorner, etc.

---

**⚠️ Recomendación de consultoría — Limpieza de taxonomía de etiquetas**

El reporte es técnicamente funcional pero los resultados son poco confiables mientras las etiquetas mezclen sectores, marcas y números de orden en el mismo campo.

Acción requerida antes de usar este reporte en producción:
1. **Definir qué es una etiqueta de marca** en COINSA-MATIK (ej. Banner, Siemens, Festo, Omron, Dorner, OMEC)
2. **Separar las etiquetas** en dos grupos con convención de nombres:
   - Prefijo `SECTOR:` para industrias (ej. `SECTOR: Automotriz`)
   - Prefijo `MARCA:` para productos (ej. `MARCA: Siemens`, `MARCA: Banner`)
3. **Eliminar etiquetas de O.C.** (números de orden no deberían ser etiquetas en CRM)
4. **Asignar etiqueta de marca obligatoria** en toda oportunidad nueva

Hasta que se haga esta limpieza, el reporte existe pero sus datos no son comparables ni auditables.

---

### RPT-07
**Nuevas oportunidades / clientes nuevos**

**Estado:** ✅ Implementado (dos flujos) — 2026-05-15
**Usuario objetivo:** Coordinador Comercial

---

**Flujo A — Nuevas oportunidades por cliente (este mes)**

**Navegación:**
1. Módulo **CRM** → **Reportes** → **Flujo**
2. Quitar filtros por defecto (clic en ×)
3. **Filtros** → Creado el → **[mes en curso]**
4. **Agrupar por** → **Cliente**
5. **Medidas** → **Número**
6. Vista **gráfico de barras**
7. **Favoritos** → Guardar → `RPT-07 Nuevas oportunidades por cliente`

Cómo leer: cada barra = número de oportunidades nuevas abiertas para ese cliente en el mes. No distingue si el cliente es nuevo o recurrente.

---

**Flujo B — Clientes nuevos registrados (primera vez en Odoo)**

**Navegación:**
1. Módulo **CRM** → menú superior → **Ventas** → **Clientes**
2. **Filtros** → **Agregar filtro personalizado** → Campo: **Creado el** → Operador: **entre** → rango: primer y último día del mes
3. **Agrupar por** → **Vendedor**
4. **Favoritos** → Guardar → `RPT-07 Clientes nuevos`

Cómo leer: cada grupo = vendedor con sus clientes nuevos del período.

---

**⚠️ Observación — Clientes sin vendedor asignado**
En el Flujo B se detectó el grupo **«Ninguno» con 42 clientes** sin vendedor asignado creados en el período abril–mayo 2026. Estos clientes no están siendo seguidos por ningún vendedor específico. Acción requerida: revisar y asignar vendedor a cada contacto.

**Diferencia entre flujos:**
- Flujo A = actividad comercial nueva (oportunidades abiertas por cliente)
- Flujo B = base de datos de clientes nueva (contactos registrados por primera vez)

---

### RPT-16
**Oportunidades generadas por ingeniería (cross-sell)**

**Estado:** ✅ Implementado (proxy con limitación) — 2026-05-15
**Usuario objetivo:** Líder de Ingeniería / Coordinador Comercial

**Qué mide:**
Oportunidades de venta identificadas por el equipo de ingeniería durante su trabajo en campo. Cuando un ingeniero detecta una necesidad adicional del cliente, debería crear una oportunidad en Odoo y pasarla a ventas. Este reporte muestra cuántas de esas oportunidades existen.

**Navegación:**
1. Módulo **CRM** (menú principal)
2. Menú superior → **Reportes** → **Flujo**
3. En la barra de búsqueda escribir `INGENIERIA` → seleccionar **Equipo de ventas contiene “INGENIERIA”**
4. **Agrupar por** → **Vendedor** (para ver quién genera más oportunidades) o **Etapa** (para ver estado del pipeline)
5. **Medidas** → **Número**
6. **Favoritos** → Guardar búsqueda actual → nombre `RPT-16 Cross-sell ingeniería` → Guardar

**Cómo leer:**
- Número total de oportunidades del equipo Ingeniería = proxy de actividad de cross-sell
- Comparar mes a mes: si el número crece, ingeniería está generando más negocio para ventas

**Observación del staging:** La mayoría de oportunidades aparecen como **“Indefinido”** (sin fecha de cierre definida). Esto indica que el equipo de ingeniería no está asignando fecha de cierre a sus oportunidades — acción correctiva requerida.

**⚠️ Limitación — Sin proceso formal de cross-sell definido**
Este reporte muestra TODAS las oportunidades del equipo Ingeniería, no solo las que explicitamente son cross-sell pasadas a ventas. No hay forma de distinguir entre:
- Oportunidades propias de ingeniería (sus propias ventas)
- Oportunidades generadas para el equipo comercial (cross-sell real)

**Mejora recomendada para producción:**
1. Crear etiqueta **`CROSS-SELL`** en CRM → Configuración → Etiquetas
2. Establecer política: cuando ingeniería identifica una oportunidad comercial, la crea en Odoo con esa etiqueta
3. Filtrar el reporte por esa etiqueta para obtener la métrica real de cross-sell
