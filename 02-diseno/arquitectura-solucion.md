# Arquitectura de la Solución

## Versión Odoo
- **Versión:** Odoo [16/17] Community / Enterprise
- **Tipo de despliegue:** [Cloud / On-premise / Odoo.sh]
- **Base de datos:** PostgreSQL [versión]

---

## Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                     USUARIOS                             │
│  Vendedores │ Supervisores │ Gerentes │ Marketing        │
└──────────────────────┬──────────────────────────────────┘
                       │ HTTPS
┌──────────────────────▼──────────────────────────────────┐
│                  ODOO (CRM + Sales)                      │
│  ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐  │
│  │   CRM   │  │  Sales   │  │  Email   │  │Reports  │  │
│  │ Leads   │  │Quotations│  │Marketing │  │Dashboard│  │
│  │Opportun.│  │  Orders  │  │          │  │         │  │
│  └────┬────┘  └────┬─────┘  └────┬─────┘  └─────────┘  │
│       └────────────┴─────────────┘                      │
│                   Database Layer                         │
│                  (PostgreSQL)                            │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │  Email   │  │[Sistema  │  │  Web     │
  │ Server   │  │    X]    │  │ Forms    │
  │IMAP/SMTP │  │          │  │          │
  └──────────┘  └──────────┘  └──────────┘
```

---

## Stack Tecnológico

| Componente | Tecnología | Versión | Notas |
|---|---|---|---|
| ERP/CRM | Odoo | | Community / Enterprise |
| Base de datos | PostgreSQL | | |
| Servidor web | Nginx / Apache | | Proxy reverso |
| Lenguaje backend | Python | 3.10+ | |
| Frontend | OWL (Odoo Web Library) | | |
| OS del servidor | Ubuntu / Debian | | |
| Caché | Redis | | Opcional |

---

## Módulos Odoo Requeridos

### Módulos Core
| Módulo | Técnico | Descripción |
|---|---|---|
| CRM | `crm` | Gestión de leads y oportunidades |
| Sales | `sale_management` | Cotizaciones y órdenes de venta |
| Contacts | `contacts` | Gestión de empresas y contactos |
| Activities | Incluido en CRM | Seguimiento de actividades |
| Email Marketing | `mass_mailing` | Campañas de email |
| Discuss | `mail` | Comunicación interna y chatter |

### Módulos de Integración
| Módulo | Técnico | Descripción |
|---|---|---|
| Email Gateway | `mail` | Captura de leads desde correo |
| Website CRM | `website_crm` | Formularios web → leads |

### Módulos OCA (si aplica)
| Módulo | Repositorio | Descripción |
|---|---|---|
| | | |

---

## Ambientes

| Ambiente | URL | Propósito | Actualizaciones |
|---|---|---|---|
| Desarrollo | | Desarrollo y pruebas internas del equipo consultor | Continuas |
| Staging | | Pruebas UAT y validación con usuarios clave | Por sprint |
| Producción | | Ambiente productivo de COINSA | Solo go-live y releases aprobados |

---

## Seguridad y Roles

| Rol Odoo | Usuarios | Permisos |
|---|---|---|
| CRM / Usuario | Ejecutivos de ventas | Ver y editar sus propias oportunidades |
| CRM / Líder de equipo | Supervisores | Ver todas las oportunidades del equipo |
| CRM / Administrador | Gerentes + Admin | Acceso completo al CRM |
| Sales / Usuario | Ejecutivos | Crear cotizaciones desde oportunidades |
| Sales / Administrador | Gerentes | Gestión de precios y configuración |

---

## Estrategia de Backup

- Frecuencia: Diaria (automática)
- Retención: 30 días
- Almacenamiento: [Destino de backup]
- Responsable: [Admin de sistemas]
