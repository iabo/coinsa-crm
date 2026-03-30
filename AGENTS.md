# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## What This Repository Is

A **documentation-only** project management repository for the COINSA Odoo CRM implementation. There is no application code, no build system, no package manager, and no test runner. All files are Markdown.

## Working With This Repo

- All documents are written in **Spanish**
- Use standard Git workflows (`git add`, `git commit`, `git push`) to version documentation changes
- Mermaid diagrams are used for flowcharts (e.g., `flujo-atencion-cliente.md`)
- Checklist items use `- [ ]` / `- [x]` syntax throughout

## Repository Structure

The folders are numbered by project phase:

| Folder | Phase | Key File(s) |
|---|---|---|
| `00-estrategia/` | Strategy | `objetivos-negocio.md` (problem statement, KPIs), `alcance-proyecto.md` (scope), `roadmap.md` (4-phase timeline), `stakeholders.md` |
| `01-analisis/` | Analysis | `analisis-gap.md` (AS-IS vs TO-BE with Ing. Arturo's process), `requerimientos-negocio.md` (RF/RNF/business rules) |
| `02-diseno/` | Design | `arquitectura/arquitectura-solucion.md` (Odoo modules, stack, roles, environments) |
| `03-configuracion/` | Configuration | `pipelines/pipeline-ventas.md` (6-stage pipeline, lead sources, loss reasons, automations) |
| `04-implementacion/` | Implementation | (empty — sprint plans go here) |
| `05-migracion-datos/` | Data Migration | `plan-migracion.md` (field mappings to Odoo models, quality rules, 5-step process) |
| `06-pruebas/` | Testing | `uat/plan-uat.md` (UAT scenarios keyed as UAT-L##, UAT-O##, UAT-A##, UAT-R##) |
| `07-capacitacion/` | Training | (empty) |
| `08-go-live/` | Go-Live | `checklist-go-live.md` (pre/day-of/post checklists, rollback criteria) |
| `09-soporte-postimplementacion/` | Post-Implementation Support | `plan-soporte.md` (3-tier support model, SLA table P1–P4) |

`flujo-atencion-cliente.md` (root level) contains the full Mermaid swimlane diagram of the end-to-end sales/order flow — the canonical process reference.

## Key Technical Context (Odoo)

- **Stack:** Odoo CRM + Sales modules, PostgreSQL, Python 3.10+, OWL frontend, Nginx reverse proxy
- **Core Odoo models referenced:** `crm.lead`, `res.partner`, `res.users`, `crm.lead.stage_id`, `sale.order`
- **Odoo modules in scope:** `crm`, `sale_management`, `contacts`, `mass_mailing`, `mail`, `website_crm`
- **Three environments:** Desarrollo (dev), Staging (UAT), Producción
- **Roles:** CRM/Usuario → CRM/Líder de equipo → CRM/Administrador

## Project Context

- **Client:** COINSA — industrial/technical equipment sales company
- **Primary user being onboarded:** Ing. Arturo (Ventas e Ingeniería) — currently operates entirely outside Odoo
- **Core problem:** Sales pipeline has zero visibility; all state lives in the salesperson's head
- **Odoo version and deployment type:** TBD (placeholder in architecture doc)
- **Current project phase:** Planificación

## README Notes

The `README.md` contains a large block of raw, informal meeting notes (starting at "notas para claudio") that are working notes, not finalized documentation. These capture open questions and pending decisions (SMTP config, client registration without RFC, delivery policy defaults, credit limit controls, etc.) that have not yet been formalized into the structured documents.
