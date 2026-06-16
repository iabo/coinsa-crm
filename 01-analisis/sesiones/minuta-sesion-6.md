# Sesión de Trabajo 6 — COINSA CRM
**Fecha:** Jueves 9 de abril — 8:00 PM

---

## Configuración de Odoo — Pipeline de Ventas

### Criterios para cada etapa del pipeline

Todas las etapas deben contener:
- Actividades siguientes
- Requisitos
- Equipo responsable

---

## Pipeline definido

```
MQL (fuentes: web, correo, WhatsApp, Expo, Bases de Datos, investigación)

  1. {Lead entrante}         ~1200
          |
          |  (haber realizado el primer contacto, haber calificado el lead, etc.)
          V
  2. {Contacto realizado}    ~450   (haber realizado el primer contacto)
          |
          |-> Seguimiento / mantenimiento
          |
          V
SQL

  3. {Diagnóstico}           (necesidad + presupuesto)
          |
          |-----> Actividad Siguiente: Dimensionar
          V

  4. {Validación técnica}
          |
          |-----> Actividad Siguiente: Dimensionar  [Equipo: Arturo]
          V

  5. Cotización enviada
          |
          |-----> Actividad Siguiente: negociación, objeciones, re-cotizar, etc.
          V

  6. Seguimiento (Negociación, objeciones, etc.)
          |
          |-> Actividad Siguiente: reunión, llamada, correo de seguimiento, etc.
          V

  7. Cierre ganado / perdido
```

---

## Pendientes

- Presentar con Guillermo la propuesta de configuración del pipeline.
- Definir: en el contacto inicial, ¿se captura información o no? En caso de que sí, ¿qué se captura?
