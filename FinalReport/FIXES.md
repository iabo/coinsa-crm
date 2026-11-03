# Tablero KPI COINSA-MATIK - Fixes & Issues

## Status: En progreso

---

## 🔴 Bugs Reportados

### BUG-01: Logo incorrecto
- **Estado:** Pendiente
- **Descripción:** El logo es un SVG generado placeholder, no el logo real de COINSA-MATIK
- **Solución:** Reemplazar con logo real (necesita archivo PNG/SVG del cliente)

### BUG-02: Dropdown "Vistas" texto blanco sobre blanco
- **Estado:** ✅ FIXED
- **Descripción:** El selector de vista (Dirección/Coordinador/Vendedor) tiene texto blanco sobre fondo blanco
- **Solución:** Corregir CSS del `.toolbar select` para usar color de texto oscuro

### BUG-03: Pipeline Activo = 0 cuando hay won/lost
- **Estado:** ✅ FIXED
- **Descripción:** El cálculo de pipeline solo cuenta `Is Won = "Pending"`, pero el valor cae a 0 incorrectamente
- **Causa:** La lógica filtraba mal — también necesita excluir etapas cerradas (Cerrado, Archivo, TERMINADO)
- **Solución:** Revisar lógica de filtrado para pipeline activo

### BUG-04: Tasa Conversión incorrecta
- **Estado:** ✅ FIXED  
- **Descripción:** Mostraba 100% porque el export no incluía oportunidades perdidas
- **Causa:** Odoo marca perdidas como `Active=False`, no se exportan con filtro normal
- **Solución:** 
  - Dashboard ahora soporta 2 archivos CSV: principal + perdidas
  - Detecta `Is Won = "Lost"` del archivo de perdidas
  - Muestra conteo real: "X ganadas / Y cerradas"

### BUG-05: Top Clientes muestra cliente inexistente
- **Estado:** 🔍 Investigar
- **Descripción:** "OPERADORA DE MINAS E INST" aparece como #1 con $1,085,650 pero no se encuentra en Odoo
- **Causa posible:** 
  - Nombre truncado en CSV vs nombre completo en Odoo
  - Oportunidad archivada/eliminada después del export
  - Filtros diferentes en Odoo vs dashboard
- **Solución:** Verificar campo usado (Customer/Name vs Company Name) y comparar con export

---

## 🟡 Mejoras Pendientes

### FEAT-01: Soporte multi-divisa
- **Estado:** Pendiente evaluación
- **Descripción:** ¿Las oportunidades pueden estar en USD además de MXN?
- **Contexto:** Usuarios CRM instruidos a usar solo MXN, pero Sales module usa USD
- **Decisión:** Por ahora asumir todo MXN. Si hay campo de divisa en export, convertir.

### FEAT-02: Vista por rol funcional
- **Estado:** Pendiente
- **Descripción:** El dropdown de vistas no hace nada actualmente
- **Implementación:** Filtrar/ocultar KPIs según rol seleccionado

### FEAT-03: Logo real del cliente
- **Estado:** Pendiente
- **Descripción:** Reemplazar placeholder SVG con logo COINSA-MATIK real

---

## ✅ Fixes Aplicados

| Fix | Fecha | Descripción |
|-----|-------|-------------|
| BUG-02 | 2026-11-03 | CSS color texto dropdown |
| BUG-03 | 2026-11-03 | Lógica pipeline activo |
| BUG-04 | 2026-11-03 | Clarificación fórmula conversión |

---

## Notas Técnicas

### Campos CSV relevantes:
- `Is Won`: valores "Won", "Pending" (no "lost")
- `Stage/Stage Name`: "Cerrado", "Archivo", "TERMINADO" = cerrados
- `Customer/Name` vs `Company Name`: verificar cuál usar para clientes
- `Expected Revenue`: valor en MXN (asumir)
