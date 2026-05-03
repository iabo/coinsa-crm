# Configuración de Equipos de Ventas y Usuarios

## Equipos de Ventas

### Equipo 1: Ventas Directas (Técnico-Comercial)
- **Líder del equipo:** Javier Pablos (Director Comercial)
- **Integrantes:** Ing. Arturo Gil Armenta (Ventas e Ingeniería)
- **Responsabilidad:** Cotizaciones técnicas, diseño de soluciones, pipeline técnico-comercial
- **Procesos:** Oportunidades técnicas, cotizaciones, seguimiento de diseño → cierre

### Equipo 2: Coordinación Comercial
- **Líder del equipo:** Guillermo Velez Sabag (Coordinación de Ventas)
- **Integrantes:** Hermenegildo (Recepción de leads), Guillermo (Hermosillo), Miguel (Tijuana)
- **Responsabilidad:** Captación de leads, calificación, asignación y coordinación
- **Procesos:** Leads → oportunidades, coordinación con equipo técnico

### Equipo 3: Soporte Comercial
- **Líder del equipo:** Rosa Estrada Nambo (Soporte Comercial)
- **Integrantes:** [A confirmar]
- **Responsabilidad:** Seguimiento post-entrega, atención al cliente, reclamaciones
- **Procesos:** Confirmación de recepción, soporte postventa, incidencias

---

## Usuarios y Permisos

### Usuarios Finales (Ejecutivos de Ventas)

| Nombre | Área | Email | Rol Odoo | Equipo |
|---|---|---|---|---|
| Ing. Arturo Gil Armenta | Ventas e Ingeniería | arturo@coinsa.com | CRM / Usuario | Ventas Directas |
| Hermenegildo | Recepción/Ventas | herm@coinsa.com | CRM / Usuario | Coordinación |
| Guillermo (Hermosillo) | Ventas Regional | guillermo.hmo@coinsa.com | CRM / Usuario | Coordinación |
| Miguel (Tijuana) | Ventas Regional | miguel.tj@coinsa.com | CRM / Usuario | Coordinación |
| Rosa Estrada Nambo | Soporte Comercial | rosa@coinsa.com | CRM / Usuario | Soporte Comercial |

### Supervisores (Líderes de Equipo)

| Nombre | Área | Email | Rol Odoo | Equipo |
|---|---|---|---|---|
| Javier Pablos | Director Comercial | pablos@coinsa.com | CRM / Líder de equipo | Ventas Directas |
| Guillermo Velez Sabag | Coordinación de Ventas | gvelez@coinsa.com | CRM / Líder de equipo | Coordinación |
| Rosa Estrada Nambo | Soporte Comercial | rosa@coinsa.com | CRM / Líder de equipo | Soporte Comercial |

### Administradores

| Nombre | Área | Email | Rol Odoo |
|---|---|---|---|
| [Admin TI] | Tecnología | [email] | CRM / Administrador |
| Adriana Real | Contabilidad/Administración | adriana@coinsa.com | CRM / Administrador |

---

## Matriz de Permisos por Rol

| Función | Usuario | Supervisores | Administrador |
|---|---|---|---|
| Ver/Editar propias oportunidades | ✓ | ✓ | ✓ |
| Ver oportunidades del equipo | ✗ | ✓ | ✓ |
| Ver todas las oportunidades | ✗ | ✓ | ✓ |
| Crear leads | ✓ | ✓ | ✓ |
| Asignar leads | ✓ | ✓ | ✓ |
| Generar cotizaciones | ✓ | ✓ | ✓ |
| Crear reportes | ✓ | ✓ | ✓ |
| Configurar pipeline | ✗ | ✗ | ✓ |
| Gestionar usuarios | ✗ | ✗ | ✓ |

---

## Asignación de Oportunidades

### Reglas de Asignación Automática

1. **Leads por web:** Round-robin entre Hermenegildo, Guillermo, Miguel (según zona)
2. **Leads por referencia técnica:** Asignado a Ing. Arturo (equipo técnico)
3. **Leads de cliente existente:** Asignado al vendedor histórico
4. **Escalamientos:** Supervisor asigna manualmente según carga de trabajo

---

## Actividades de Configuración

- [ ] Crear 3 equipos en Odoo CRM
- [ ] Crear usuarios para cada persona listada
- [ ] Asignar roles según matriz de permisos
- [ ] Configurar territorios/zonas (si aplica)
- [ ] Definir reglas de asignación automática
- [ ] Validar con líderes de equipo
