# Segmentación de Clientes — COINSA CRM

## Decisión de Sesión 3

Los clientes se segmentarán mediante **etiquetas flexibles (tags)** en Odoo. No se adoptó un modelo rígido de categorías excluyentes; la flexibilidad permite que cada área aplique los criterios relevantes para su operación y que los usuarios gestionen y filtren las etiquetas directamente.

**Contexto para la configuración:** Se incluirán etiquetas base como parte de la entrega de configuración inicial.

---

## Criterios de Segmentación Levantados en Sesión 3

Se identificaron tres perspectivas durante la actividad de preguntas:

### Perspectiva Guillermo — Por Valor Comercial y Comportamiento de Crédito

| Segmento | Volumen de compra | Lealtad | Cumplimiento de crédito |
|---|---|---|---|
| ⭐⭐⭐ VIP / Triple AAA | Alto | Alta | Bueno — negociación preferencial |
| ⭐⭐ Recurrentes | Medio-Alto | Media | Medio-Alto |
| ⚠️ Morosos | Medio-Alto | Media | Bajo |
| Regulares | Bajo-Medio | Media | Bajo |
| Esporádicos | Bajo | Baja | Bueno (pago de contado) |

### Perspectiva Adriana — Por Tipo de Relación Comercial

- Triple AAA
- Normal
- Revendedor / Integrador
- Por industria
- Por línea de producto

### Perspectiva Pablos — Por Cobertura Geográfica y Canal

- Locales
- Regionales con vendedor en zona
- Foráneos sin presencia física
- Corporativos / Portales / Mercado digital

---

## Taxonomía de Etiquetas Base Propuesta

Se propone implementar las siguientes etiquetas en la configuración inicial de Odoo CRM. Los usuarios podrán agregar etiquetas adicionales durante la operación.

### Valor / Comportamiento

- `AAA` / `VIP`
- `Recurrente`
- `Esporádico`
- `Moroso`

### Tipo de Cliente

- `Empresa`
- `Público General`
- `Revendedor`
- `Integrador`
- `Corporativo / Portal`

### Cobertura Geográfica

- `Local`
- `Regional`
- `Foráneo`
- `Hermosillo`
- `Tijuana`
- `Nogales`

### Industria (ejemplos iniciales)

- `Industrial`
- `Manufactura`
- `Construcción`
- `Servicios`
- `Gobierno`

### Origen del Lead / Fuente

- `WhatsApp`
- `Correo`
- `Feria / Evento`
- `Plática PSI`
- `Prospección propia`
- `BD Interna`

---

## Notas de Implementación

- Las etiquetas son **multi-valor**: un cliente puede tener `AAA` + `Industrial` + `Hermosillo` simultáneamente.
- Se recomienda limitar la creación libre de etiquetas por usuarios finales para evitar duplicados; revisar el catálogo trimestralmente.
- Usar etiquetas en los reportes de Odoo para filtrar el pipeline por segmento y medir el desempeño por categoría de cliente.
- Los campos de segmentación de cliente en `res.partner` en Odoo se complementan con las etiquetas de `crm.lead` para trazabilidad desde el primer contacto hasta la venta.