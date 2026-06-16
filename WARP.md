# WARP.md

This file provides guidance to Oz/Warp when working with this repository.

## What This Repository Is

Documentation-only repository for the COINSA-MATIK Odoo CRM implementation, managed by SPM Consultores. No application code, no build system, no package manager. All files are Markdown (`.md`) except for a few HTML dashboards and one CSV in `000-Anexos/Reportes/`.

## Working With This Repo

- All documents are written in **Spanish**
- Use standard Git workflows (`git add`, `git commit`, `git push`) to version changes
- Mermaid diagrams are used for flowcharts and swimlanes
- Checklist items use `- [ ]` / `- [x]` syntax throughout
- File naming convention for internal-only documents: `.spm.md` (visible only to Marco and Yabo, not delivered to client) and `.csm.md` (internal configuration/setup reference for the consulting team)

## Folder Structure and Purpose

Folders are divided into two categories: **internal** (SPM consulting team only) and **client-facing** (shared with COINSA).

### Internal — SPM Only

| Folder | Purpose | Audience |
|---|---|---|
| `00-Propuesta/` | Commercial negotiation documents: value proposition, scope, roadmap, go-live checklist. Used during the sales and proposal phase of the engagement. | SPM internal |
| `01-analisis/` | Raw notes from requirements gathering sessions (minutas, stakeholder mapping, gap analysis, business rules). Source material used to build the solution design — not finalized deliverables. | SPM internal |
| `000-Anexos/` | Supporting reference material: swimlane diagrams, flow charts, HTML dashboards, pipeline sketches, and working notes that inform other documents. | SPM internal |

### Client-Facing — Shared with COINSA

| Folder | Purpose | Audience |
|---|---|---|
| `02-diseno/` | Agreed solution design documents: SLA rules, segmentation model, reports catalog, data model. Reflects decisions formally validated with the client. | Client + SPM |
| `03-configuracion/` | Instructional documents for configuring and operating the Odoo system: pipeline stages, users, teams, automations, and step-by-step navigation for reports. | Client + SPM |
| `04-pruebas/` | UAT plan, use cases, and stress test scenarios. | Client + SPM |
| `05-soporte/` | Post-go-live support plan, SLA tiers, and FAQ. | Client + SPM |

## Key Files

| File | Description |
|---|---|
| `03-configuracion/pipeline-ventas-v3.md` | Canonical pipeline definition: 7 stages, required fields, probabilities, automations (AUT-01 to AUT-04), loss reasons. v1 and v2 are kept for historical reference. |
| `03-configuracion/equipos-usuarios.md` | All 27 users with emails, Odoo roles, team assignments, and permissions matrix |
| `02-diseno/sla.md` | 6 SLA rules with Odoo monitoring approach |
| `02-diseno/segmentacion.md` | Tag taxonomy for client segmentation |
| `02-diseno/reportes-tracker.md` | Step-by-step navigation for every implemented report (RPT-01 to RPT-26) |
| `01-analisis/stakeholders.spm.md` | Stakeholder map from requirements phase — internal reference only |

## Odoo Technical Context

- **Version:** Odoo 17 Enterprise
- **Deployment:** Cloud / managed instance
- **Modules in scope (Fase 1):** `crm`, `sale_management` only
- **Modules deferred:** `mass_mailing`, `website_crm` (pending web form bug fix)
- **Core models:** `crm.lead`, `res.partner`, `res.users`, `crm.lead.stage_id`, `sale.order`
- **Roles:** CRM/Usuario → CRM/Líder de equipo → CRM/Administrador
- **Sales teams configured:** Ingeniería · Ventas A (Sonora) · Soporte Comercial

## Project Context

- **Client:** COINSA-MATIK — industrial/technical equipment sales company (Hermosillo, Sonora)
- **Consultant team:** Marco (lead consultant) + Yabo
- **Core problem:** Zero pipeline visibility — sales state lived in salespeople's heads, no centralized tracking
- **Current phase:** Re-implementation in new Odoo instance (previous staging instance expired)
- **Sessions completed:** 7 working sessions with the client team
- **Key users:** Arturo Gil (Ingeniería), Guillermo Velez (Key User CRM), Javier Pablos (Director Comercial)
