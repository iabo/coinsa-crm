# Tablero KPI COINSA-MATIK - Fixes & Issues

## Status: v1.1 - Funcional

---

## ✅ Bugs Resueltos

### BUG-01: Logo incorrecto
- **Estado:** 🟡 Pendiente
- **Descripción:** El logo es un SVG generado placeholder, no el logo real de COINSA-MATIK
- **Solución:** Reemplazar con logo real (necesita archivo PNG/SVG del cliente)

### BUG-02: Dropdown "Vistas" texto blanco sobre blanco
- **Estado:** ✅ FIXED
- **Solución:** Agregado `color: var(--text)` al CSS de `.toolbar select`

### BUG-03: Pipeline Activo = 0 cuando hay won/lost
- **Estado:** ✅ FIXED
- **Solución:** Pipeline ahora excluye etapas: cerrado, archivo, terminado, perdido

### BUG-04: Tasa Conversión incorrecta
- **Estado:** ✅ FIXED  
- **Causa raíz:** Odoo marca perdidas como `Active=False`, no se exportaban
- **Solución export:** Usar filtro `Active is Yes OR Active is No` para incluir todo
- **Solución dashboard:** 
  - Detecta `Is Won = "Lost"` correctamente
  - Muestra DOS métricas de conversión:
    - **Conversión (Opps):** count-based (ej: 80.1%)
    - **Conversión (Revenue):** revenue-based (ej: 74.5%)

### BUG-05: Top Clientes muestra cliente inexistente
- **Estado:** 🔍 Pendiente investigar
- **Descripción:** "OPERADORA DE MINAS E INST" no encontrado en Odoo
- **Causa posible:** Nombre truncado en CSV o filtros diferentes

---

## 🟢 Features Implementados

### FEAT-04: Doble métrica de conversión
- **Conversión (Opps):** Ganadas / Total cerradas (por cantidad)
- **Conversión (Revenue):** Revenue ganado / Revenue cerrado total

### FEAT-05: KPIs adicionales
- **Perdidas:** Total revenue perdido con conteo de opps
- **Ciclo Promedio:** Días promedio para cerrar

---

## 🟡 Mejoras Pendientes

### FEAT-01: Soporte multi-divisa
- **Decisión:** Por ahora todo MXN (usuarios instruidos a usar solo MXN en CRM)

### FEAT-02: Vista por rol funcional
- **Estado:** Pendiente
- **Descripción:** El dropdown de vistas no hace nada actualmente

### FEAT-03: Logo real del cliente
- **Estado:** Pendiente archivo del cliente

---

## Instrucciones de Export

### Filtro correcto para exportar:
```
Active is Yes OR Active is No
```
Esto incluye oportunidades activas + perdidas en un solo archivo.

### Campos clave:
- `Is Won`: "Won", "Pending", "Lost"
- `Stage/Stage Name`: Etapa actual
- `Expected Revenue`: Valor en MXN
- `Active`: True/False (perdidas = False)

---

## Historial de Cambios

| Fecha | Versión | Cambios |
|-------|---------|--------|
| 2026-11-03 | v1.0 | Dashboard inicial |
| 2026-11-03 | v1.1 | Fix conversión, doble métrica, KPIs adicionales |
