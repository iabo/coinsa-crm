# Swimlane — Proceso Outbound (Captación de Prospectos)

> Mermaid no soporta swimlanes nativos. Este diagrama aproxima el formato usando subgráficos coloreados por actor (carril).
> Para la lógica de decisión completa ver [`flujo-Outbound.md`](./flujo-Outbound.md).

---

```mermaid
flowchart TD

  subgraph LANE_F["📡  CANALES / FUENTES DE ENTRADA"]
    F1["📱 WhatsApp · 📧 Correo · 📞 Telefono"]
    F2["🎪 Feria / Exposicion / Platica PSI"]
    F3["🙋 Prospeccion propia del vendedor"]
    F4["🔍 Minado de base de datos interna"]
  end

  subgraph LANE_VC["🏭  VENDEDOR DE CAMPO — Guillermo · Miguel · Arturo"]
    EV1[Recopila contactos\ndurante el evento]
    EV2{Volumen de contactos?}
    EV3[Carga masiva CSV a Odoo]
    EV4[Captura manual en Odoo]
    EV5[Etiqueta origen:\nFeria / Platica / PSI]
    PR1[Identifica prospecto:\nvisita / referido / red de contactos]
    PR2[Crea Lead en Odoo CRM\nEtiqueta: Prospeccion propia]
  end

  subgraph LANE_MD["🔍  VENTAS / DATOS — Mineria BD Interna"]
    MD1[Identifica clientes inactivos\no potenciales en Odoo]
    MD2[Filtra y exporta lista\ndesde Odoo Contactos]
    MD3[Crea Leads en CRM\nEtiqueta: BD Interna]
  end

  subgraph LANE_HM["📞  VENTAS INTERNAS — Hermenegildo"]
    HM1[Recibe contacto entrante]
    HM2[Crea Lead en CRM\nEtiqueta canal de origen]
    SLA_N[SLA: primer contacto en 24-48 hrs]
    HM3{Califica como\nprospecto real?}
    HM4[Registra motivo\ny archiva lead]
    HM5[Convierte a\nOportunidad en CRM]
  end

  subgraph LANE_AS["🎯  ASIGNACION — Coordinacion Comercial"]
    AS1{Tipo de venta?}
    AS2[Hermenegildo\nda seguimiento directo]
    AS3[Asigna vendedor de campo\npor zona geografica]
    NOTE_Z["📍 Hermosillo: Guillermo\n📍 Tijuana: Miguel\n📍 Otros: Hermenegildo"]
    PIPE([Pipeline de Ventas])
  end

  %% Canales directos hacia Herme
  F1 --> HM1

  %% Eventos: vendedor recopila y carga en Odoo
  F2 --> EV1
  EV1 --> EV2
  EV2 -->|6 o mas contactos| EV3
  EV2 -->|1 a 5 contactos| EV4
  EV3 --> EV5
  EV4 --> EV5
  EV5 --> HM2

  %% Prospeccion propia: vendedor crea lead, va directo a calificacion
  F3 --> PR1 --> PR2 --> HM3

  %% Minado BD: crea leads, pasa por SLA
  F4 --> MD1 --> MD2 --> MD3 --> SLA_N

  %% Flujo principal de Herme
  HM1 --> HM2
  HM2 --> SLA_N
  SLA_N --> HM3
  HM3 -->|No califica| HM4
  HM3 -->|Si califica| HM5
  HM5 --> AS1
  AS1 -->|Comun| AS2
  AS1 -->|Compleja o tecnica| AS3
  AS3 -.-> NOTE_Z
  AS2 --> PIPE
  AS3 --> PIPE

  %% Estilos de carriles
  style LANE_F fill:#f8f9fa,stroke:#dee2e6,color:#000
  style LANE_VC fill:#fff8e1,stroke:#ff9800,color:#000
  style LANE_MD fill:#e8eaf6,stroke:#5c6bc0,color:#000
  style LANE_HM fill:#e8f5e9,stroke:#4caf50,color:#000
  style LANE_AS fill:#e3f2fd,stroke:#1976d2,color:#000

  %% Nodos de canal
  style F1 fill:#546e7a,color:#fff,stroke:none
  style F2 fill:#ff7043,color:#fff,stroke:none
  style F3 fill:#e91e63,color:#fff,stroke:none
  style F4 fill:#5c6bc0,color:#fff,stroke:none

  %% Nodos Odoo
  style HM2 fill:#6a0dad,color:#fff
  style EV3 fill:#6a0dad,color:#fff
  style EV4 fill:#6a0dad,color:#fff
  style PR2 fill:#6a0dad,color:#fff
  style MD3 fill:#6a0dad,color:#fff
  style HM5 fill:#6a0dad,color:#fff

  %% Otros
  style HM4 fill:#c0392b,color:#fff
  style PIPE fill:#2d7a2d,color:#fff
  style SLA_N fill:#fff3cd,color:#856404,stroke:#ffc107,stroke-width:2px
  style HM3 fill:#f0c040,color:#000
  style EV2 fill:#f0c040,color:#000
  style AS1 fill:#f0c040,color:#000
  style NOTE_Z fill:#fff3cd,color:#856404,stroke:#ffc107,stroke-dasharray:5 5
```