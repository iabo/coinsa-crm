# Flujo de Captación — Prospectos y Clientes Nuevos

> Cubre el camino desde el primer contacto o evento de prospección hasta la apertura de la oportunidad en el pipeline de ventas.

```mermaid
flowchart TD

    subgraph CANALES["📡 Canales de Entrada"]
        C1["📱 WhatsApp Business"]
        C2["📧 Correo Electrónico"]
        C3["📞 Llamada Telefónica"]
        C4["🎪 Feria · Exposición · Plática PSI"]
        C5["🙋 Prospección propia\ndel vendedor"]
        C6["🔍 Minado de base\nde datos interna"]
    end

    subgraph EVENTO["Flujo Post-Evento  (Vendedor responsable del evento)"]
        E1["Recopila contactos\ndurante el evento"]
        E2{"¿Volumen\nde contactos?"}
        E3["Carga masiva\nCSV → Odoo CRM"]
        E4["Captura manual\nen Odoo CRM"]
        E5["📌 Etiqueta origen:\nFeria · Plática · PSI"]
    end

    subgraph PROPIA["Prospección Autogestionada  (Vendedor)"]
        P1["Identifica prospecto:\nvisita · referido · red de contactos"]
        P2["Crea Lead directamente\nen Odoo CRM"]
        P3["📌 Etiqueta origen:\nProspección propia"]
    end

    subgraph MINADO["Minería de Base de Datos Interna  (Ventas / Datos)"]
        M1["Filtra clientes inactivos\no sin actividad reciente en Odoo"]
        M2["Genera lista de\nprospectos candidatos"]
        M3["📌 Crea Leads en CRM\nEtiqueta: BD Interna"]
    end

    subgraph HERME["Ventas Internas — Hermenegildo"]
        H1["Recibe contacto\nentrante"]
        H2["Crea Lead en Odoo CRM\n+ etiqueta canal de origen"]
        SLA["⏱ SLA: Primer contacto\nen ≤ 24–48 hrs"]
        H3{"¿Califica como\nprospecto real?"}
        H4["Registra motivo\ny archiva"]
        H5["Convierte a\nOportunidad en CRM"]
    end

    subgraph ASIG["Asignación de Vendedor"]
        A1{"¿Venta común\no compleja?"}
        A2["Hermenegildo\nda seguimiento"]
        A3["Asigna vendedor\nde campo por zona"]
        NOTE_Z["📍 Hermosillo: Guillermo\n📍 Tijuana: Miguel\n📍 Otros: Hermenegildo"]
    end

    %% Canales directos → Hermenegildo
    C1 & C2 & C3 --> H1

    %% Canal de evento → flujo especial
    C4 --> E1

    %% Canal de prospección propia → flujo autogestionado
    C5 --> P1
    C6 --> M1
    M1 --> M2
    M2 --> M3
    M3 --> SLA
    P1 --> P2
    P2 --> P3
    P3 --> H3
    E1 --> E2
    E2 -->|"≥ 6 contactos"| E3
    E2 -->|"1–5 contactos"| E4
    E3 --> E5
    E4 --> E5
    E5 --> H2

    %% Flujo principal de captura
    H1 --> H2
    H2 --> SLA
    SLA --> H3
    H3 -->|"No califica"| H4
    H3 -->|"Sí califica"| H5
    H5 --> A1
    A1 -->|"Común"| A2
    A1 -->|"Compleja / Técnica"| A3
    A3 -.-> NOTE_Z

    %% Salidas
    A2 --> PIPE([▶ Pipeline de Ventas])
    A3 --> PIPE
    H4 --> ARCH([🗄 Archivado · Sin seguimiento activo])

    %% Estilos
    style CANALES fill:#f8f9fa,stroke:#dee2e6
    style EVENTO fill:#fff8e1,stroke:#ffc107
    style PROPIA fill:#fce4ec,stroke:#e91e63
    style HERME fill:#e8f5e9,stroke:#4caf50
    style ASIG fill:#e3f2fd,stroke:#1976d2

    style C1 fill:#25d366,color:#fff,stroke:none
    style C2 fill:#1a73e8,color:#fff,stroke:none
    style C3 fill:#546e7a,color:#fff,stroke:none
    style C4 fill:#ff7043,color:#fff,stroke:none
    style C5 fill:#e91e63,color:#fff,stroke:none

    style P2 fill:#6a0dad,color:#fff
    style P3 fill:#fff3cd,color:#856404,stroke:#ffc107,stroke-dasharray:5 5

    style E3 fill:#6a0dad,color:#fff
    style E4 fill:#6a0dad,color:#fff
    style E5 fill:#fff3cd,color:#856404,stroke:#ffc107,stroke-dasharray:5 5

    style H2 fill:#6a0dad,color:#fff
    style SLA fill:#fff3cd,color:#856404,stroke:#ffc107,stroke-width:2px
    style H3 fill:#f0c040,color:#000
    style H4 fill:#e8d5d5,color:#721c24
    style H5 fill:#6a0dad,color:#fff

    style A1 fill:#f0c040,color:#000
    style A3 fill:#1976d2,color:#fff
    style NOTE_Z fill:#fff3cd,color:#856404,stroke:#ffc107,stroke-dasharray:5 5

    style PIPE fill:#2d7a2d,color:#fff
    style ARCH fill:#c0392b,color:#fff
    style C6 fill:#5c6bc0,color:#fff,stroke:none
    style MINADO fill:#e8eaf6,stroke:#5c6bc0
    style M3 fill:#6a0dad,color:#fff
```

---

## Notas del diagrama

### Canales activos
| Canal | Responsable de captura | Herramienta |
|---|---|---|
| WhatsApp Business | Hermenegildo | Odoo CRM (manual o integración) |
| Correo electrónico | Hermenegildo | Odoo CRM (alias de correo) |
| Llamada telefónica | Hermenegildo | Odoo CRM (actividad manual) |
| Feria / Exposición / Plática PSI | Vendedor asistente | CSV post-evento → Odoo CRM |
| Prospección propia del vendedor | Vendedor (autogestionado) | Captura directa en Odoo CRM |
| Minado de base de datos interna | Ventas / Administración | Filtrado en Odoo Contactos → creación de Leads con etiqueta «BD Interna» |

### Regla de carga post-evento
- **≥ 6 contactos:** carga masiva por CSV para agilizar el ingreso.
- **1–5 contactos:** captura manual directamente en Odoo CRM.
- En ambos casos se etiqueta la fuente del evento para trazabilidad y métricas de prospección.

### SLA de primer contacto
> Pendiente de aprobación formal en Sesión 4 (punto 4c).
> Propuesta inicial: primer contacto en ≤ 24–48 hrs desde la creación del lead.
