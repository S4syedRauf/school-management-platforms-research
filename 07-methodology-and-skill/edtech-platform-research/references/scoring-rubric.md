# Scoring Rubric (0-10 per dimension)

Anchor every score to evidence. When evidence is missing, score conservatively and state why in `score_rationale`. Do not score from marketing adjectives.

## Dimensions and weights

| Dimension | Weight | What it measures |
|---|---|---|
| feature_breadth | 0.30 | Native coverage of the 24 standard modules in `profile-template.md` |
| adoption | 0.30 | Verified institutions, students and countries served |
| advanced_features | 0.20 | AI, predictive analytics, workflow automation, configurable forms/workflows, open API, offline/mobile depth |
| ux_mobile | 0.10 | Review ease-of-use scores, native mobile apps, modern UI evidence |
| interoperability | 0.10 | Standards (OneRoster, LTI 1.3, Ed-Fi, SIF), SSO, marketplace, documented API |

Weighted score = sum(score x weight). Rank by weighted score; break ties by adoption, then advanced_features.

## Anchors

feature_breadth: 10 = 21-24 modules native; 8 = 17-20; 6 = 13-16; 4 = 9-12; 2 = 5-8; 0 = fewer.

adoption: 10 = more than 20M students or 15,000 institutions; 9 = 5M-20M students or 5,000-15,000 institutions; 8 = 1M-5M students or 2,000-5,000 institutions; 7 = 500-2,000 institutions; 6 = 200-500; 5 = 100-200; 4 = under 100 but established; 2 = unverified claims only.

advanced_features: 10 = production AI assistants plus predictive analytics plus no-code workflow builder plus public API; 8 = three of these; 6 = two; 4 = one; 2 = none beyond reporting.

ux_mobile: 10 = average review ease-of-use 4.6+ and full-featured native apps for parents, students and staff; 8 = 4.3-4.5 with native apps; 6 = 4.0-4.2 or limited apps; 4 = dated UI or web-only mobile; 2 = widespread usability complaints.

interoperability: 10 = certified on 3+ 1EdTech/Ed-Fi standards plus SSO plus marketplace plus public API; 8 = two standards plus API; 6 = one standard or rich API; 4 = basic integrations only; 2 = closed system.

## Script

Run `python3 scripts/rank_platforms.py <results.json> --out ranking.md` where `results.json` is a list of item objects containing `id`, `name` and `scores`. The script writes a ranked Markdown table and a `ranking.json` with weighted scores and ranks.
