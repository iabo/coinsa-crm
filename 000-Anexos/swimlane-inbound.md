# Swimlane — Proceso Inbound (Flujo de Compra / Atención al Cliente)

> Mermaid no soporta swimlanes nativos. Este diagrama aproxima el formato usando subgráficos coloreados por actor (carril).
> Para la lógica de decisión completa ver [`flujo-Indbound.md`](./flujo-Indbound.md).

---

```mermaid
flowchart TD

  subgraph LANE_C["👤  CLIENTE"]
    CL1([Inicia contacto])
    CL2{Acepta la cotización?}
    CL3([Recibe entrega])
  end

  subgraph LANE_VI["📞  VENTAS INTERNAS — Hermenegildo"]
    VI1[Recibe contacto\nRegistra en CRM + etiqueta el canal]
    VI2{Venta comun\no compleja?}
    VI3[Elabora cotización en Odoo]
    VI4[Envia cotizacion por correo / Odoo]
    VI5{Motivo de\nno aceptacion?}
    VI6[Solicita autorizacion\nde descuento]
    VI7[CRM: marca como\nPostergado o Perdido]
  end

  subgraph LANE_VC["🏭  VENDEDOR DE CAMPO — Guillermo · Miguel"]
    VC1[Recibe oportunidad\ncompleja asignada]
    VC2[Visita tecnica\ncon el cliente]
    VC3[Diseno de solucion\nregistra notas en CRM]
  end

  subgraph LANE_CO["📊  COORDINACION COMERCIAL — Javier Pablos"]
    CO1[Revisa y aprueba\nla solicitud de descuento]
  end

  subgraph LANE_BO["📦  BACK OFFICE — Compras / Facturacion / Almacen"]
    BO1{Hay material\nen inventario?}
    BO2[COMPRAS genera OC\na proveedor]
    BO3[Recibe material\ny da entrada en Odoo]
    BO4[Confirma OV en Odoo\nGenera orden de salida]
    BO5[MARTHA emite factura\nAdjunta OC en Odoo]
    BO6[ALMACEN envia\npor paqueteria]
  end

  %% Handoffs entre carriles
  CL1 --> VI1
  VI1 --> VI2
  VI2 -->|Comun| VI3
  VI2 -->|Compleja tecnica| VC1
  VC1 --> VC2 --> VC3 --> VI3
  VI3 --> VI4
  VI4 --> CL2
  CL2 -->|Si confirma| BO1
  CL2 -->|No acepta| VI5
  VI5 -->|Pide descuento| VI6
  VI6 --> CO1 --> VI3
  VI5 -->|Postergado Perdido| VI7
  BO1 -->|No hay stock| BO2 --> BO3 --> BO4
  BO1 -->|Hay stock| BO4
  BO4 --> BO5 --> BO6 --> CL3

  %% Estilos de carriles
  style LANE_C fill:#e3f2fd,stroke:#1976d2,color:#000
  style LANE_VI fill:#e8f5e9,stroke:#4caf50,color:#000
  style LANE_VC fill:#fff3e0,stroke:#ff9800,color:#000
  style LANE_CO fill:#fce4ec,stroke:#e91e63,color:#000
  style LANE_BO fill:#f3e5f5,stroke:#9c27b0,color:#000

  %% Nodos Odoo
  style VI1 fill:#6a0dad,color:#fff
  style VI3 fill:#6a0dad,color:#fff
  style VI4 fill:#6a0dad,color:#fff
  style BO4 fill:#6a0dad,color:#fff
  style BO5 fill:#6a0dad,color:#fff

  %% Inicio Fin
  style CL1 fill:#2d7a2d,color:#fff
  style CL3 fill:#4169e1,color:#fff
  style VI7 fill:#c0392b,color:#fff

  %% Decisiones
  style VI2 fill:#f0c040,color:#000
  style CL2 fill:#f0c040,color:#000
  style VI5 fill:#f0c040,color:#000
  style BO1 fill:#f0c040,color:#000
```
