# Segmentación y Etiquetas — COINSA-MATIK

> **Propósito:** Definir qué taxonomías requiere el CRM, evaluar el mecanismo correcto para cada una en Odoo, y documentar los pasos exactos de configuración.

---

## Diagnóstico del estado actual

El sistema ya tiene **45 etiquetas registradas** en CRM, pero mezclan tres categorías incompatibles en el mismo campo:

| Rango | Contenido | Problema |
|---|---|---|
| 1–17 | Sectores/industria del cliente (Minería, Energía, Alimentos, Automotriz…) | Taxonomía válida pero sin prefijo |
| 18–21 | Números de O.C. operacionales (O.C.: 4658, etc.) | No pertenecen al CRM |
| 23–45 | Marcas/productos (Banner, Siemens, Festo, Omron, Dorner, OMEC…) | Taxonomía válida pero mezclada con lo anterior |

Esta mezcla hace que **RPT-02 / RPT-10 (Ventas por marca / línea de producto)** exista técnicamente pero sus datos no sean confiables ni auditables. El reporte agrupa por etiqueta sin distinguir si la barra representa un sector, una marca o un número de orden.

---

## Taxonomías requeridas

De la documentación de diseño, las minutas de sesiones y la definición de reportes se identifican **tres taxonomías** con propósitos distintos:

### TAX-01 · Sector industrial / Segmento de mercado

**Qué clasifica:** el sector económico del cliente, no del producto vendido.
**Relación:** Many-to-many — una oportunidad puede cruzar dos sectores (ej. cliente que opera en Minería y Energía).
**Reportes que lo necesitan:** RPT-02, RPT-10 (ventas por segmento).

Ejemplos confirmados en el sistema:
Minería · Energía · Alimentos · Automotriz · Manufactura · Agua y saneamiento · Farmacéutico · Petroquímica · Construcción · Gobierno

---

### TAX-02 · Marca / Línea de producto

**Qué clasifica:** el fabricante o línea de producto involucrado en la oportunidad.
**Relación:** Many-to-many — una oportunidad puede involucrar varias marcas (ej. integración con Siemens + Festo).
**Reportes que lo necesitan:** RPT-02, RPT-10 (ventas por marca).

Ejemplos confirmados en el sistema:
Banner · Siemens · Festo · Omron · Dorner · OMEC · Beckhoff · SMC · Cognex · SICK

---

### TAX-03 · Tipo de solución (ingeniería)

**Qué clasifica:** la naturaleza del trabajo entregado por el equipo de ingeniería.
**Relación:** Single-select — una oportunidad tiene un solo tipo de solución dominante.
**Reportes que lo necesitan:** RPT-12 (ventas por tipo de solución, ingeniería).

Valores definidos:
- `Venta directa`
- `Servicio / Asesoría`
- `Integración`

---

## Mecanismo correcto para cada taxonomía

La primera impresión de usar etiquetas es **correcta para TAX-01 y TAX-02**, pero **no para TAX-03**.
El campo `tag_ids` en Odoo es Many2many y admite múltiples valores, lo cual encaja perfectamente con la naturaleza de sectores y marcas. Sin embargo, TAX-03 es una selección exclusiva y necesita un campo de tipo Selection para poder hacerse obligatorio por equipo.

| Taxonomía | Mecanismo | Razón |
|---|---|---|
| TAX-01 Sector industrial | Etiquetas CRM con prefijo `SECTOR:` | Many-to-many, un cliente puede operar en varios sectores |
| TAX-02 Marca / Línea producto | Etiquetas CRM con prefijo `MARCA:` | Many-to-many, una oportunidad puede involucrar varias marcas |
| TAX-03 Tipo de solución | Campo personalizado Selection (Odoo Studio) | Single-select, debe ser obligatorio solo para equipo Ingeniería |

---

## Plan de configuración

### Paso 1 — Limpiar etiquetas existentes

Antes de crear nuevas etiquetas, se debe depurar el catálogo actual.

**Navegar a:** CRM → Configuración → Etiquetas

Acciones por categoría:

- **Etiquetas de sector (1–17):** Renombrar agregando prefijo `SECTOR:` — por ejemplo, `Minería` → `SECTOR: Minería`
- **Etiquetas de O.C. (18–21):** Eliminar. Los números de orden de compra no son datos de segmentación; si se necesitan deben ir en el campo Notas de la oportunidad o en un campo personalizado de referencia.
- **Etiquetas de marca (23–45):** Renombrar agregando prefijo `MARCA:` — por ejemplo, `Sensores Banner` → `MARCA: Banner`

> **Nota operativa:** Renombrar una etiqueta en Odoo actualiza automáticamente todas las oportunidades que ya la tienen asignada. No se pierden datos.

---

### Paso 2 — Crear catálogo final de etiquetas

Crear o verificar que existan las siguientes etiquetas con la convención de prefijos:

**Etiquetas SECTOR:**
```
SECTOR: Minería
SECTOR: Energía
SECTOR: Alimentos
SECTOR: Automotriz
SECTOR: Manufactura
SECTOR: Agua y Saneamiento
SECTOR: Farmacéutico
SECTOR: Petroquímica
SECTOR: Construcción
SECTOR: Gobierno
SECTOR: Otros
```

**Etiquetas MARCA:**
```
MARCA: Banner
MARCA: Siemens
MARCA: Festo
MARCA: Omron
MARCA: Dorner
MARCA: OMEC
MARCA: Beckhoff
MARCA: SMC
MARCA: Cognex
MARCA: SICK
MARCA: Otros
```

Pasos para crear cada etiqueta:
1. CRM → Configuración → Etiquetas → **Nuevo**
2. Escribir el nombre con prefijo exacto
3. Asignar color diferente para SECTOR (ej. azul) y MARCA (ej. verde) — esto ayuda a identificarlos visualmente en el kanban
4. **Guardar**

---

### Paso 3 — Crear campo Tipo de solución (Studio)

Este paso requiere acceso a **Odoo Studio** (incluido en Enterprise).

1. Activar modo Studio: menú principal → ícono cuadrado punteado (esquina superior derecha)
2. Navegar a **CRM → Flujo** → abrir cualquier oportunidad
3. En el panel de Studio: **Agregar campo** → tipo **Selección**
4. Configurar el campo:
   - **Nombre del campo:** `Tipo de solución`
   - **Nombre técnico:** `x_tipo_solucion` (se asigna automáticamente)
   - **Opciones de selección:**
     - `Venta directa`
     - `Servicio / Asesoría`
     - `Integración`
5. Colocar el campo en el formulario dentro de la sección de información comercial (junto al campo Equipo de ventas)
6. **No marcar como obligatorio globalmente** — solo debe ser obligatorio para el equipo Ingeniería (ver Paso 4)
7. Guardar y salir de Studio

---

### Paso 4 — Hacer obligatoria la etiqueta de marca y el tipo de solución

Odoo no permite campos obligatorios condicionales por equipo de forma nativa sin desarrollo. La alternativa funcional es:

**Para etiqueta de MARCA (obligatoria en todas las oportunidades):**
- Incluir en la capacitación que toda oportunidad debe tener al menos una etiqueta `MARCA:` al llegar a la etapa **Cotizado**
- El coordinador revisa el campo en la reunión semanal usando el filtro: CRM → Pipeline → Agrupar por Etiquetas → verificar oportunidades sin etiqueta

**Para Tipo de solución (obligatorio solo en equipo Ingeniería):**
- Usar una automatización de Odoo: CRM → Configuración → Automatizaciones → Nueva regla
  - **Modelo:** Lead / Oportunidad
  - **Activador:** Al actualizar el registro
  - **Condición:** Equipo de ventas = INGENIERIA **y** Tipo de solución está vacío **y** Etapa ≠ Nuevo
  - **Acción:** Crear actividad → Tarea asignada al vendedor con descripción "Completar Tipo de solución"

---

### Paso 5 — Ajustar favoritos de reportes

Con las etiquetas limpias, actualizar los favoritos guardados de RPT-02 y RPT-10:

1. CRM → Reportes → Flujo
2. Cargar favorito `RPT-02 Ventas por marca`
3. Agrupar por → **Etiquetas**
4. Verificar que ahora las barras muestran solo etiquetas con prefijo `MARCA:`
5. Si aparecen barras de `SECTOR:` mezcladas, agregar filtro por nombre de etiqueta que contenga `MARCA:`
6. Guardar favorito actualizado

Para RPT-12 (tipo de solución):
1. CRM → Reportes → Flujo
2. Filtro: Equipo de ventas = INGENIERIA + Ganado + Fecha de cierre
3. Agrupar por → **Tipo de solución** (el nuevo campo personalizado)
4. Medidas → Ingreso esperado
5. Guardar como `RPT-12 Ventas por tipo solución`

---

## Referencia rápida — Cuadro resumen

| Taxonomía | Campo Odoo | Tipo | Prefijo / Valores | Reporte |
|---|---|---|---|---|
| Sector industrial | `tag_ids` (etiquetas) | Many2many | `SECTOR: Xxx` | RPT-02, RPT-10 |
| Marca / Línea de producto | `tag_ids` (etiquetas) | Many2many | `MARCA: Xxx` | RPT-02, RPT-10 |
| Tipo de solución | `x_tipo_solucion` (Studio) | Selection | 3 valores fijos | RPT-12 |
| Números O.C. | — (eliminar del CRM) | — | Mover a Notas | — |

---

## Criterios de calidad para datos de etiquetas

La taxonomía solo tiene valor si los datos son consistentes. Estos son los criterios mínimos:

- **Toda oportunidad en etapa Cotizado o superior** debe tener al menos una etiqueta `MARCA:`
- **Toda oportunidad del equipo Ingeniería** debe tener el campo Tipo de solución completado
- **Ninguna oportunidad activa** debe tener etiquetas de número de O.C.
- Las etiquetas `SECTOR:` son opcionales pero recomendadas para enriquecer los reportes de segmento

---

## Estado de implementación

| Paso | Descripción | Estado |
|---|---|---|
| 1 | Limpiar etiquetas existentes (renombrar + eliminar O.C.) | ⏳ Pendiente |
| 2 | Crear catálogo final con prefijos SECTOR / MARCA | ⏳ Pendiente |
| 3 | Crear campo Tipo de solución en Studio | ⏳ Pendiente |
| 4 | Configurar automatización de campo obligatorio (Ingeniería) | ⏳ Pendiente |
| 5 | Actualizar favoritos RPT-02, RPT-10, RPT-12 | ⏳ Pendiente |