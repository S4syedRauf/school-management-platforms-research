---
name: edtech-platform-research
description: "Research, rank and document education-management software (school management systems, SIS, school ERP, MIS, campus/university ERP, LMS-adjacent platforms) and turn the competitive evidence into a blueprint for a better platform. Use when asked for top-N lists or comparisons of school/college/university management platforms, per-platform dossiers with features, pricing, founding year, platform type (web/cloud/desktop/mobile) and full reference links, country-specific edtech landscapes (e.g. India), or a product/feature/technical blueprint to beat incumbent edtech platforms."
---

# Edtech Platform Research

Produce an evidence-based, ranked landscape of education-management platforms with one complete dossier per platform, then derive a competitive product blueprint from the gaps found.

## Workflow

1. **Scope the item set.** Define the category (school management/SIS/ERP; exclude pure LMS such as Canvas, Moodle or Google Classroom unless the user asks, and treat them as integration targets). Cover segments the user cares about: K-12, private/international, higher education. For country lists, pick vendors headquartered in that country. State selection criteria in the report.
2. **Fan out one research agent per platform** (workflow-composer, `collect` failure policy). Embed the full text of `references/profile-template.md` and `references/scoring-rubric.md` in every item prompt, give each a unique profile path such as `profiles/G01-<id>.md` or `profiles/IN01-<id>.md`, and require the structured fields listed in the template. Add separate agents for cross-cutting topics the blueprint needs (standards and regulation; free/open-source tech stack and current free-tier limits).
3. **Rank deterministically.** Save structured results to `results.json` and run `scripts/rank_platforms.py`. Rank global and country lists separately. Review outliers; if a score contradicts the profile evidence, correct the score and note why rather than re-researching.
4. **Assemble the document** in ranked order: ranking overview table, classification matrix (web/cloud/desktop/mobile/on-premise), pricing overview, then every full profile, then the blueprint. Replace `{{RANK}}` placeholders with final ranks.
5. **Write the blueprint** using `references/blueprint-framework.md`. Every proposed feature must trace back to a competitor gap or pain-point cluster.
6. **Enforce link format.** Users of these reports usually want full visible URLs. Run `scripts/lint_links.py report.md`, then `--fix` if needed. Write the References lists as `1. Title — https://full.url`, not hidden reference definitions.
7. **Render** to PDF (typst-pdf-maker Markdown route) and keep the Markdown source.

## Accuracy rules

- Distinguish company founding year from product launch year; many products were renamed or acquired (e.g. RenWeb became FACTS SIS; Capita SIMS became ESS SIMS).
- Pricing: quote official numbers with currency, unit and date checked. Most enterprise SIS vendors are quote-only; say so, and label third-party estimates as estimates with their source.
- Adoption figures: cite the source and the date of the claim; prefer vendor annual reports, press releases and filings over listicles.
- Review ratings change; record platform, score, review count and the date viewed.
- Never invent URLs. Use pages actually opened. Prefer official domains for website, features, docs and pricing links.

## Resources

- `references/profile-template.md`: section order and required structured fields for each dossier.
- `references/scoring-rubric.md`: anchored 0-10 scales and weights for ranking.
- `references/blueprint-framework.md`: gap matrix, switching-cost destroyers, segment packs, architecture checklist and roadmap structure.
- `scripts/rank_platforms.py`: weighted ranking to Markdown and JSON.
- `scripts/lint_links.py`: detects hidden or malformed links and rewrites embedded links as visible URLs.
