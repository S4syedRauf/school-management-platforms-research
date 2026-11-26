# Platform Profile Template

Use this exact section order for every platform profile so profiles can be concatenated into one ranked document. Replace `{...}` placeholders. Write every URL in full and visible (for example `https://www.example.com/pricing`), never as `[text](url)`. Percent-encode `(` and `)` inside URLs as `%28` and `%29`.

```markdown
## {Rank placeholder: leave as "{{RANK}}"}. {Platform name} ({Vendor})

| Field | Detail |
|---|---|
| Vendor / owner | {company, parent company if acquired} |
| Headquarters | {city, country} |
| Company founded | {year} [n] |
| Product first launched | {year, or "Not publicly disclosed"} [n] |
| Platform classification | {Cloud SaaS / Web-based / Desktop / Mobile (iOS, Android) / On-premise / Hybrid} |
| Primary segments | {Pre-K, K-12, private/independent, international/IB, higher education, coaching, multi-campus groups} |
| Market presence | {schools, students, countries, with the date of the claim} [n] |
| Official website | {full URL} |
| Product / features page | {full URL} |
| Documentation / help center | {full URL} |
| Pricing page | {full URL, or "No public pricing page"} |
| Review ratings | {G2 x.x/5 (n reviews), Capterra x.x/5 (n reviews), App Store / Play Store, with date} [n] |

### Overview
{2-3 short paragraphs: what it is, who uses it, why it matters, history including acquisitions.}

### Platform Classification Explained
{Explain each delivery mode with evidence: browser access, cloud hosting provider if known, desktop client, on-premise option, native mobile apps and their names.}

### Complete Feature Inventory
{One `####` subsection per module the product actually has. Cover, where present: admissions and enrollment; student information and records; attendance; timetable and master scheduling; gradebook, assessment and examinations; report cards and transcripts; learning management and homework; communication (SMS, email, push, WhatsApp); parent, student and teacher portals; fees, billing, payments and accounting; HR, staff and payroll; transport; library; hostel and boarding; inventory and assets; health and medical; behavior, discipline and pastoral care; special education and safeguarding; alumni and fundraising; analytics, dashboards and reporting; AI features; state/government reporting and compliance; mobile apps; integrations and APIs; security and privacy. Name actual sub-features, not generic phrases.}

### Advanced and Distinctive Features
{Bulleted list of the genuinely advanced or unique capabilities, each with one sentence of explanation.}

### Pricing Details
{Official prices with currency, unit (per student/year, per school/month), tier names, setup fees and what each tier includes, with the date checked. If quote-only, say so plainly, then give third-party reported ranges clearly labeled as estimates with sources.}

### Integrations, Standards and Interoperability
{OneRoster, LTI, Ed-Fi, SIF, Clever/ClassLink, Google Workspace, Microsoft 365, payment gateways, accounting tools, open API, marketplace.}

### Security, Privacy and Compliance
{Certifications and laws: SOC 2, ISO 27001, FERPA, COPPA, GDPR, India DPDP Act, regional data hosting. Note publicly reported security incidents with dates.}

### Strengths
{Short paragraph or bullets.}

### Weaknesses and Common User Complaints
{From reviews and press, cited.}

### Key Milestones
{Year-by-year bullets: founding, launches, acquisitions, funding.}

### References
1. {Descriptive title} — {full URL}
2. ...
```

## Required structured fields (return with the profile)

`id, name, vendor, country, company_founded, product_launched, official_website, features_page_url, docs_url, pricing_page_url, platform_types[], segments[], market_presence, pricing_summary, modules[], advanced_features[], differentiators, weaknesses, user_pain_points, review_ratings, integrations_standards, compliance, scores{feature_breadth, adoption, advanced_features, ux_mobile, interoperability}, score_rationale, profile_path`.

Score each dimension with `references/scoring-rubric.md`.
