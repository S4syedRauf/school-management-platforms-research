# Competitive Platform Blueprint Framework

Use after the competitor profiles are finished. The blueprint must be derived from evidence in the profiles (gaps, complaints, pricing pain), not from a generic wish list.

## 1. Gap matrix
Collect every `weaknesses` and `user_pain_points` field. Cluster them (cost, complexity, slow support, dated UI, poor mobile, rigid reports, data lock-in, weak India/state compliance, no offline mode, fragmented LMS/SIS). Each blueprint feature must cite which cluster it fixes.

## 2. Switching-cost destroyers
Schools stay with incumbents because migration is painful. Always specify:
- Importers for each top competitor's export formats (CSV/XLSX templates, OneRoster CSV, Ed-Fi, SIMS/Arbor exports, Tally for India).
- AI-assisted column mapping and data-quality report before cut-over.
- Parallel-run mode (shadow sync) so the old and new systems coexist for a term.
- Familiar-terminology toggle (UK "pupils/forms", US "students/homerooms", India "classes/sections/houses").
- One-click exit export of all data (anti lock-in promise as a selling point).

## 3. Segment packs
Model one core with configurable packs: Pre-K, K-12, International/IB, Higher Ed (credits, CBCS, semesters, OBE), Coaching/tuition, Multi-campus groups, Government schools. Each pack lists compliance artifacts it generates.

## 4. Feature tiers
- Table stakes: what every top-10 competitor has.
- Differentiators: what only 1-3 competitors have.
- White space: what none have, justified by a pain-point cluster.

## 5. Experience principles
Role-based home screens, command palette, mobile-first for teachers and parents, offline-first, low-bandwidth mode, vernacular languages, accessibility (WCAG 2.2 AA), progressive disclosure of complexity.

## 6. Technical architecture checklist
Open-source license choice and rationale; modular monolith vs microservices; multi-tenancy model and data isolation; auth (OIDC/SAML, passkeys); offline sync; event bus and audit log; extension/plugin SDK; AI layer with local-model option; observability; backup; zero-cost and low-cost deployment paths with verified current free-tier limits; security baseline (OWASP ASVS, encryption, RBAC/ABAC, consent management, data residency).

## 7. Go-to-market and sustainability for open source
Open-core vs fully open; hosted offering; community governance; partner implementers; certification; grants.

## 8. Roadmap
Phased releases with exit criteria, starting from the smallest product that can replace an incumbent for one segment.
