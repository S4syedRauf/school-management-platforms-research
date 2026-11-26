# Part V. Blueprint: "OpenCampus One", an Open-Source Platform Designed to Beat Every Platform in This Report

> **Status:** blueprint only. No development has been started. "OpenCampus One" is a working name; check trademarks and domains before public launch.
> **Design rule:** every feature in this blueprint traces back to a documented competitor gap (gap codes C1–C12 below) found in the 40 dossiers and Appendices A–C.

## V.1 Strategic Thesis: Why a New Platform Can Win

The incumbents are strong on breadth and installed base but weak on the things buyers now care about most. The evidence across the 40 dossiers shows the same pattern:

- **Pricing is opaque.** Almost every enterprise vendor is quote-only (PowerSchool, Ellucian, Workday, Infinite Campus, Skyward, Blackbaud, Jenzabar), and implementations run three to seven months (G2 reviewer averages for PowerSchool and Blackbaud).
- **Satisfaction is mediocre.** The Key's 2025 survey of 961 UK MIS users found an average satisfaction of 6.6/10. Only 47% found their system intuitive for new users, only 54% were satisfied with support, and 21% were considering a switch within a year (35% among SIMS users).
- **Mobile is the weakest layer.** Arbor's parent app scored 1.9/5 and PowerSchool Mobile 2.5/5 on Google Play when checked, even though both cores are highly ranked.
- **Trust has been damaged.** PowerSchool (2024–2025), Blackbaud (2020), Illuminate (2021, with FTC action in 2025) and Frontline (2026) all showed that a school system's support or credential plane can expose millions of student records.
- **Segments are split.** K-12 runs on one vendor class (PowerSchool, Arbor, Fedena) and higher education on another (Ellucian, Workday, Jenzabar, MasterSoft). Groups that own both schools and colleges, which are very common in India, the Gulf and Africa, must buy and integrate two systems.
- **India is underserved on compliance.** Few vendors document UDISE+, APAAR, ABC, DigiLocker, PARAKH HPC or DPDP Act 2023 / Rules 2025 workflows end to end.
- **Open source exists but is stale or narrow.** Fedena's public repository was last pushed in May 2020. openSIS and Gibbon are PHP/MySQL single-tenant designs. OpenEduCat depends on the Odoo stack. None is multi-tenant, RLS-secured, offline-first and multi-segment.

**The thesis.** Build one open-source, cloud-native, offline-capable platform that serves a nursery, a K-12 school, a college and a multi-campus university group from the same core. Then win on four promises that no incumbent can easily copy:

1. **"Switch in a weekend, leave in a click."** Migration tooling for every major competitor, plus a contractual one-click full-data exit.
2. **"Published price, or free forever."** The AGPL core is free to self-host. Hosted plans have public per-student prices with no implementation fee for standard migrations.
3. **"Works on a ₹8,000 phone with no signal."** Offline-first teacher and parent apps, low-bandwidth mode, WhatsApp/SMS fallback and 22 Indian languages plus global languages.
4. **"Security you can audit."** Open code, database-enforced tenant isolation, a public security model, immutable audit logs, just-in-time support access and published penetration-test summaries.

## V.2 Gap Matrix: Competitor Pain Points and the Answer for Each

| Code | Gap cluster | Evidence from this report | Competitors most affected | OpenCampus One answer |
|---|---|---|---|---|
| C1 | Opaque cost, price rises, hidden add-ons | Quote-only pricing at most top-20 vendors; SIMS rises of 25%+ expected from 2025/26 (Somerset Schools Forum); paid extra data copies at offboarding (Bromcom) | PowerSchool, Ellucian, Workday, Skyward, Blackbaud, SIMS, Jenzabar | Free self-hosted core; published hosted price card; all core modules in every plan; no exit fee |
| C2 | Complexity and steep learning curve | G2 themes for PowerSchool and Blackbaud: learning difficulty, complex yearly tasks, unintuitive queries | PowerSchool, Ellucian, Skyward, Infinite Campus, SIMS 7 | Role-based "Today" home screens, command palette, guided year-end rollover wizard, progressive disclosure |
| C3 | Slow support and long implementation | 54% support satisfaction (The Key 2025); 3–7 month implementation averages | Bromcom (42% support satisfaction), SIMS, Ellucian, Workday | Self-serve migration engine, in-product contextual help, community forum, certified partner network, public SLA |
| C4 | Dated UI and poorly rated mobile apps | App ratings: Arbor Parent 1.9/5 (Apple), PowerSchool Mobile 2.5/5 (Play); low UX scores for Synergy, Skyward, Bromcom | Arbor, Bromcom, Synergy, Skyward, MyClassboard, Skolaro | One design system for web, PWA and native; offline-first apps; WCAG 2.2 AA; performance budgets |
| C5 | Rigid reporting and data silos | Review complaints about reports; Ed-Fi case studies show value of live, standard data | PowerSchool, Blackbaud, Infinite Campus, Indian ERPs | Semantic data layer, drag-and-drop report builder, natural-language queries with citations, governed SQL views, Superset embedding |
| C6 | Lock-in and migration pain | Paid SQL copies at exit, gated APIs (Infinite Campus direct API reported as partnership-gated), legacy-to-cloud migrations at Ellucian, Anthology and SIMS | Most incumbents | Importers for 25+ competitor formats, shadow parallel-run, OneRoster/Ed-Fi/CSV exports, one-click exit |
| C7 | Security incidents and support-plane risk | PowerSource compromised credential (Dec 2024); Blackbaud ransomware (2020); Illuminate FTC case (2025); Frontline (2026) | PowerSchool, Blackbaud, Frontline, Infinite Campus (alleged 2026 leak) | RLS tenant isolation, passkeys, just-in-time support access, export anomaly detection, immutable audit, open security model |
| C8 | Weak India and local compliance | Few dossiers document UDISE+, APAAR, ABC, DigiLocker, PARAKH HPC, NAAC/NBA/NIRF/AISHE and DPDP end to end | Global vendors in India; several Indian ERPs partially | India Pack with UDISE+, APAAR/PEN, ABC/NAD, DigiLocker, PARAKH HPC, board adapters, NAAC/NBA/NIRF/AISHE, DPDP consent ledger |
| C9 | Connectivity, low-end devices, language | UNESCO: only 50% of primary schools globally had internet for teaching in 2025; India's 1.47M schools vary widely in connectivity | Cloud-only vendors | Offline-first sync, SMS/WhatsApp/IVR fallback, 2G-friendly mode, IndicTrans2 translations, voice input |
| C10 | Fragmented SIS, LMS, comms and payments | Schools juggle separate SIS, LMS, messaging, payments, transport and library tools; parents need several apps | Almost all; Teachmint dropped standalone admissions and fees | One family app and one staff app; built-in light LMS plus LTI 1.3 to Moodle, Canvas and Google Classroom; built-in UPI and cards |
| C11 | Unsafe or shallow AI | RAND 2025: only 45% of principals report AI policies; UNESCO 2026: 1 in 5 universities have a formal AI policy | Vendors adding closed AI features (Arbor AI, Synergy, Ellucian) | Permission-aware AI copilot with citations, local-model option, human approval for consequential actions, AI audit log, admin kill switch |
| C12 | K-12 and higher education on separate products | K-12 leaders (PowerSchool, Arbor) and HE leaders (Ellucian, Workday) are separate stacks | School-plus-college groups in India, the Gulf and Africa | One canonical model with segment packs (Pre-K to PhD), one identity per learner from nursery to alumni |

## V.3 Target Markets, Institutions and Beachhead Sequence

**Primary beachhead: India private K-12 schools and affiliated colleges (years 1–2).** India has 1,471,473 schools and 246.9M enrolments (UDISE+ 2024–25), plus 45,473 colleges and 1,168 universities (AISHE 2021–22). Private unaided schools alone number 339,583. Indian buyers are price-sensitive, mobile-first and under new compliance pressure (DPDP Rules 2025, APAAR, NEP 2020 HPC). The ranked Indian vendors are fragmented, mostly closed and mostly quote-only. This is the largest addressable base where a free, compliant, offline-first platform has an immediate edge.

**Second wave: UK and international schools (years 2–3).** The UK market switched more than 4,000 schools in 2025 and is in a retention phase. Arbor's app ratings and Bromcom's support scores leave room for a better parent and teacher experience. International and IB schools (iSAMS, ManageBac, Toddle, Veracross territory) need curriculum mapping, multi-language families and multi-country groups.

**Third wave: emerging markets (years 2–4).** The Gulf (GCC private school groups), Southeast Asia, Africa (Kenya, Nigeria, South Africa) and Latin America have strong private-school growth, limited budgets and connectivity constraints, and few modern open options.

**Fourth wave: US private, charter and small public districts (years 3–5).** These buyers need OneRoster 1.2, Ed-Fi, FERPA/COPPA/state-privacy tooling and the published price advantage, positioned against FACTS, Gradelink, Alma and openSIS.

**Higher education throughout.** Small and mid-size colleges and private universities that cannot afford Ellucian, Workday or Jenzabar can adopt the Higher-Ed Pack (CBCS/credits, OBE, NAAC/NBA, examinations, hostels, placements).

**Institution types served from one core:** pre-schools and nurseries; K-12 schools (government, aided, private, charter, independent); international and IB/Cambridge schools; coaching and tuition centres; vocational and ITI/polytechnic institutes; colleges (affiliated and autonomous); universities (state, private, deemed); multi-campus groups, trusts and MATs; government departments and education ministries (state dashboards).

## V.4 One Core, Configurable Segment Packs

The core holds the canonical model: people, organizations, campuses, academic periods, programmes, courses, sections, enrolments, attendance, assessments, results, credentials, finance, consent and audit. Packs add terminology, workflows, rules and compliance outputs without forking the code.

| Pack | Who it is for | Key workflows | Compliance and artefacts generated |
|---|---|---|---|
| Early Years | Nurseries, pre-schools, Pre-K | Daily diary, photo moments, pickup authorization with QR/OTP, developmental milestones, nap/meal logs | Early-years observations, parent consent records, NEP Foundational stage HPC |
| K-12 Core | All schools | Admissions, class/section/house, attendance, timetable, gradebook, report cards, behaviour, homework, fees, transport, library, health | UDISE+ (India), DfE census (UK), state reporting adapters (US), CBSE/ICSE/state-board exports, PARAKH HPC |
| International / IB / Cambridge | International schools | Unit planners, MYP/DP criteria, CAS/service hours, extended essay tracking, predicted grades, university counselling, multi-currency fees | IB and Cambridge exports, transcripts, CASE standards alignment |
| Higher Education | Colleges, universities | Programme and curriculum design, CBCS/credits, semesters, electives, registration, examinations (internal/external, revaluation), results, transcripts, convocation, hostels, placements, research, alumni | ABC credit transfer, APAAR, DigiLocker/NAD, NAAC SSR/AQAR, NBA SAR (CO-PO-PSO attainment), NIRF data mart, AISHE DCF, Samarth migration |
| Coaching / Tuition | Test-prep and tuition centres | Batches, lead CRM, trial classes, instalments, test series, rank lists, doubt-clearing, franchise roll-up | GST invoices, batch performance reports |
| Vocational / Skills | ITIs, polytechnics, skill centres | Trades, practical hours, apprenticeships, competency checklists, industry partners | NCVET/skill-credential exports, Open Badges |
| Multi-Campus Group | Trusts, MATs, chains, university systems | Group dashboards, central admissions, shared staff, consolidated finance, policy templates pushed to campuses, cross-campus benchmarking | Consolidated statutory returns, group-level audit |
| Government / Ministry | State education departments, district offices | Read-only aggregated dashboards, school inspection workflows, scheme tracking (scholarships, mid-day meals, uniforms), grievance portal | Open-data exports, GIGW 3.0 accessibility, state-level UDISE+ reconciliation |

**Terminology toggle.** The same field displays as "pupil / form / Year 7" (UK), "student / homeroom / Grade 7" (US) or "student / class / section / house / Std VII" (India). It is set per tenant and per user language, so staff moving from any competitor see familiar words from day one.

## V.5 Switching-Cost Destroyers: The Migration Engine

Migration pain is the main reason institutions stay with a system they dislike (gap C6). OpenCampus One treats migration as a flagship product, not a services project.

### V.5.1 Competitor importers

Each importer ships as an open-source connector with test fixtures and a published field map.

| Source system | Import method |
|---|---|
| PowerSchool SIS | Data Export Manager CSV, PowerQuery extracts, OneRoster 1.1/1.2 CSV or REST, Universal Rostering |
| Infinite Campus | OneRoster 1.2 REST/CSV, ad hoc report CSV, ODBC extract templates (customer-run) |
| Skyward, Synergy, Aeries, Focus | OneRoster and Ed-Fi ODS, vendor CSV templates |
| FACTS, Blackbaud, Veracross, Alma, Gradelink | SKY API (Blackbaud), vendor CSV/XLSX exports, OneRoster |
| Ellucian Banner/Colleague, Anthology, Workday Student, Jenzabar, Oracle Campus Solutions | Ethos EEDM resources, flat-file extracts, Workday report-as-a-service CSV, PeopleSoft query exports |
| Arbor, Bromcom, SIMS, iSAMS | CTF/ATF (Common Transfer File, UK), census XML, vendor API/CSV, SIMS SQL export via customer-run script |
| Compass, ManageBac, Toddle, Classter | CSV/XLSX exports, OneRoster, ManageBac API |
| Indian ERPs (Fedena, Entab, Teachmint, Camu, MasterSoft, NextOS, Edunext, MyClassboard, Skolaro, Vidyalaya, Academia, OpenEduCat) | Excel/CSV templates, Fedena and OpenEduCat database adapters, UDISE+ data-capture formats, Tally XML/JSON for ledgers |
| Spreadsheets and paper | Smart Excel templates, phone-camera OCR of admission registers and mark sheets with human verification |

### V.5.2 AI-assisted mapping and data-quality report

An "Import Studio" detects the source system from file signatures and proposes column mappings with confidence scores. It runs more than 150 validation rules before anything is written: duplicate students and guardians, sibling and household inference, invalid dates, orphan enrolments, fee balances that do not reconcile, and missing UDISE/APAAR/PEN identifiers. The output is a human-readable data-quality report with one-click fixes, and the person approving the import signs it off. Mapping is deterministic and saved as a reviewable file, so it can be version-controlled and reused by the next school migrating from the same vendor.

### V.5.3 Shadow parallel-run mode

For one term the old system stays the system of record. OpenCampus One syncs nightly or in real time where APIs allow, and staff use it for attendance and communication first. A reconciliation dashboard shows any drift (attendance totals, fee balances, grades) between the two systems. Cut-over is a button press, once the drift report shows zero critical differences.

### V.5.4 Familiarity layer

The terminology toggle (V.4) works alongside "muscle-memory" navigation presets that mirror common menu structures. For example, "Gradebook → Assignments" for PowerSchool users and "Students → Registers" for SIMS users, both mapped to the same underlying pages. Grading scales, attendance codes and report-card templates import as-is: DfE attendance codes, CBSE grading, US letter grades and GPA, and IB 1–7.

### V.5.5 Exit guarantee

A one-click full export produces a signed archive. It contains all data in documented JSON, CSV, OneRoster and Ed-Fi formats, all files, the audit log and the schema documentation. It is free, unlimited and part of the licence promise, which turns the incumbents' exit fees into a sales argument.

### V.5.6 Commercial switching incentives

The hosted service charges nothing for the remaining months of a competitor contract (up to 12 months). Standard migrations are free. Certified partners offer fixed-price migrations for complex universities.

## V.6 Feature Blueprint by Module

**Tier key.** **T** = table stakes (most top-10 competitors have it). **D** = differentiator (only one to three competitors have it). **W** = white space (no ranked competitor offers it as documented). Gap codes are in brackets.

### V.6.1 Admissions, enquiries and enrolment

| Feature | Tier | Detail |
|---|---|---|
| Online multilingual application forms | T | No-code form builder, document upload, sibling reuse, save-and-return, fee payment at submission |
| Lead CRM and counselling pipeline | D | Kanban pipeline, WhatsApp/SMS/email nurture, campus tour booking, source attribution (C10) |
| Seat matrix and quota engine | D | RTE 25% quota (India), sibling/staff priorities, lottery with an auditable random seed, category-based reservations for higher education (C8) |
| Entrance tests and interviews | D | Online test scheduling, proctoring hooks, interview panels with rubrics |
| One-tap enrolment hand-off | T | Admitted applicant becomes a student record without re-keying |
| Document verification with DigiLocker | W | Pulls verified mark sheets and certificates with consent, so they never have to be scanned (C8) |
| Duplicate and fraud detection | W | Cross-campus duplicate detection, document tamper hints, all decisions human-verified (C7) |

### V.6.2 Student and guardian records (360° profile)

| Feature | Tier | Detail |
|---|---|---|
| Unified learner identity, nursery to alumni | W | One person record spans school, college and alumni; segment packs attach context (C12) |
| Household and guardian graph | D | Multiple households, custody restrictions, pickup permissions, communication preferences per guardian |
| Custom fields with typed metadata | T | Versioned, permissioned, exportable custom fields; no arbitrary SQL (Part IV lesson 9) |
| External identifier vault | W | APAAR, PEN, UDISE, UPN (UK), state IDs and SSN-free US IDs stored with provenance, consent and masking (C8, C7) |
| Timeline view | D | Chronological record of attendance, grades, behaviour, health, communications and documents with filters |
| Document wallet | D | Signed certificates, transfer certificates, bonafide letters, generated and verifiable via QR |

### V.6.3 Attendance

| Feature | Tier | Detail |
|---|---|---|
| Period, daily, session and event attendance | T | One-tap registers, configurable codes (DfE, US, Indian) |
| Offline attendance | W | Taken without connectivity and synced later with conflict rules (C9) |
| Multi-modal capture | D | QR ID cards, NFC, RFID gates, face-verification as an optional plug-in with explicit consent, biometric device adapters (C9) |
| Instant absence alerts | T | Push notification, then WhatsApp, then SMS, then IVR voice call in the guardian's language (C9, C10) |
| Chronic-absence early warning | D | Explainable risk flags with suggested interventions; human-reviewed (C11) |
| Staff attendance and leave | T | Geo-fenced check-in, leave workflows, substitution suggestions |

### V.6.4 Timetable and scheduling

| Feature | Tier | Detail |
|---|---|---|
| Constraint-based auto-timetabler | D | Open-source solver (for example OR-Tools CP-SAT) for teacher, room, subject and lab constraints; multi-campus shared staff |
| Cover and substitution manager | T | Absence-driven cover suggestions with fairness balancing |
| Higher-education course scheduling | D | Electives, CBCS baskets, room capacity optimisation, exam timetabling without clashes |
| Calendar sync | T | iCal, Google and Microsoft 365 calendars |

### V.6.5 Learning, assessment, examinations and results

| Feature | Tier | Detail |
|---|---|---|
| Gradebook with any scale | T | Marks, grades, GPA, standards-based, IB criteria, CBSE scholastic and co-scholastic, weighted categories |
| Competency and outcome tracking | D | NEP competencies, CASE standards, CO-PO-PSO attainment for NBA (C8) |
| Holistic Progress Card generator | W | PARAKH HPC with self, peer and parent inputs and evidence links (C8) |
| Examination management | D | Seating plans, hall tickets, invigilation duty, answer-sheet barcoding, moderation, revaluation, grace rules, result processing |
| Report cards and transcripts | T | Drag-and-drop template designer, multilingual, digital signatures, QR verification, DigiLocker/NAD push (C8) |
| Light LMS | T | Assignments, resources, quizzes (QTI import), submissions, rubrics, plagiarism hook |
| LTI 1.3 Advantage | T | Deep linking and grade passback with Moodle, Canvas, Google Classroom and Microsoft Teams (C10) |
| AI-assisted marking | D | Rubric-guided draft feedback on typed or photographed answers; the teacher approves every mark (C11) |

### V.6.6 Communication and engagement

| Feature | Tier | Detail |
|---|---|---|
| Unified inbox | T | Announcements, two-way chat, read receipts, office hours, quiet hours for staff |
| Channel waterfall | W | Push first, then WhatsApp Business API, then SMS, then voice IVR, with cost-aware routing and delivery proof (C9, C10) |
| Auto-translation | D | Every message translated into the guardian's language with IndicTrans2 or a self-hosted model; original text kept (C9) |
| Parent-teacher conference booking | T | Slots, video links (Jitsi or BigBlueButton), reminders |
| Digital forms and e-consent | D | Trips, medical, photo consent; DPDP-grade consent artefacts (C8) |
| Emergency broadcast | D | One-tap lockdown or closure alert across all channels with roll-call |

### V.6.7 Fees, finance and accounting

| Feature | Tier | Detail |
|---|---|---|
| Fee structures and instalments | T | Class, category, transport and hostel components; concessions; scholarships; late fees |
| Family wallet and UPI AutoPay | W | One wallet per household covering every child and every campus; UPI AutoPay mandates, cards, net-banking, BBPS; pluggable gateways (Razorpay, Cashfree, PayU, Stripe, Paystack) (C10) |
| GST-ready invoicing and receipts | D | GST invoices, e-receipts, credit notes (C8) |
| Double-entry ledger | D | Immutable journal, cost centres, bank reconciliation; Tally and QuickBooks/Xero export (C10) |
| Defaulter intelligence | D | Gentle-nudge sequences and payment plans; privacy-preserving, so children are never shamed in class |
| Payroll | T | Indian statutory payroll (PF, ESI, PT, TDS), UK/US export adapters, payslips in the app |
| Budget and procurement | D | Purchase requests, approvals, vendor management, asset capitalisation |

### V.6.8 Staff and HR

| Feature | Tier | Detail |
|---|---|---|
| Staff records, contracts, documents | T | Qualifications, background-check tracking, safeguarding training expiries |
| Recruitment | D | Job posts, applicant tracking, interview scorecards |
| Appraisal and CPD | D | Goals, lesson observations, CPD hours (NEP 50-hour CPD tracking), peer review |
| Workload analytics | W | Teaching load, marking load and cover fairness dashboards to reduce burnout (C2) |

### V.6.9 Campus operations

| Feature | Tier | Detail |
|---|---|---|
| Transport | T | Routes, stops, GPS tracking with live ETA in the parent app, boarding scans, driver app, fuel and maintenance |
| Hostel and residence | T | Room allocation, mess, leave and out-pass with guardian approval, visitor log |
| Library | T | Catalogue (MARC import), barcode/RFID circulation, OPAC, e-resources, Koha connector |
| Inventory and assets | T | Stores, issue and returns, asset tags, depreciation, maintenance tickets |
| Canteen and cashless | D | Pre-paid cards via the family wallet, allergy alerts at the point of sale |
| Visitor management | D | Pre-registration, QR passes, ID capture with retention limits |
| Health and wellbeing | T | Medical records, allergies, immunisations, infirmary visits, counselling notes with restricted access |

### V.6.10 Behaviour, pastoral care, safeguarding and inclusion

| Feature | Tier | Detail |
|---|---|---|
| Behaviour points and incidents | T | Positive and negative behaviour, configurable sanctions, parent notification |
| Safeguarding case management | D | Restricted-access chronology, multi-agency referrals, need-to-know permissions (UK KCSIE, POCSO in India) |
| Special education and IEPs | D | IEP/EHCP/504 plans, accommodations that flow into exams and timetables, progress monitoring |
| MTSS and interventions | D | Tiered interventions, intervention groups, outcome tracking |
| Anonymous concern reporting | W | Students report bullying or wellbeing concerns safely; routed to trained staff with an audit trail |

### V.6.11 Higher-education specifics

| Feature | Tier | Detail |
|---|---|---|
| Programme and curriculum management | T | Regulations, credit rules, CBCS baskets, prerequisites, versioned syllabi |
| Online registration and add/drop | T | Seat limits, waitlists, advisor approval |
| Degree audit and "what-if" planner | D | Students see remaining requirements and simulate a change of major or minor |
| ABC credit bank integration | W | Credits push to and pull from the Academic Bank of Credits with learner consent (C8) |
| Accreditation workspace | D | NAAC criteria evidence vault (binary and maturity-based models), AQAR cycles, NBA SAR, NIRF data mart with lineage (C8) |
| Research and publications | D | Faculty research profiles, grants, publication import (ORCID, Crossref), IPR tracking |
| Placements and alumni | D | Recruiter portal, drives, offers, alumni directory, mentoring, giving |

### V.6.12 Analytics, reporting and AI

| Feature | Tier | Detail |
|---|---|---|
| Role dashboards | T | Principal, teacher, finance, registrar, group CEO; KPIs with freshness indicators |
| Drag-and-drop report builder | T | Any entity, any filter, saved and shared reports, scheduled email/WhatsApp delivery (C5) |
| Semantic layer and governed SQL | D | Read-only analytical replica with row-level security, published data dictionary and Superset embedding; production is never queried directly (Part IV lesson 2) |
| "Ask OpenCampus" copilot | W | Natural-language questions answered only from data the user may see, with citations to source records; drafts letters, comments and summaries; consequential actions need explicit human approval (C11) |
| Local AI mode | W | AI runs on a self-hosted small model (via Ollama or llama.cpp) so no student data leaves the institution; cloud models optional per tenant (C7, C11) |
| Early-warning system | D | Explainable risk scores for attendance, grades, behaviour and fees; bias monitoring; no automated punitive decisions (C11) |
| Benchmarking | W | Opt-in, anonymised, differentially private benchmarks across participating schools |

### V.6.13 Government and statutory reporting

| Feature | Tier | Detail |
|---|---|---|
| UDISE+ adapter | W | Versioned data-capture formats, validation, submission tracker, reconciliation (C8) |
| APAAR / PEN workflow | W | Consent capture for minors, generation status, mismatch resolution, never used as the primary key (C8) |
| UK DfE census, CTF/ATF | T (UK) | School census returns, Common Transfer Files, workforce census |
| US state reporting and Ed-Fi | T (US) | Ed-Fi ODS/API sync, state-specific extracts, CRDC support |
| AISHE, NIRF, NAAC, NBA | D | Year-specific schemas, evidence lineage, approval workflow (C8) |

### V.6.14 Platform services

| Feature | Tier | Detail |
|---|---|---|
| No-code workflow builder | W | Visual approvals (leave, fee waivers, TC requests, admissions) built on an Apache-licensed engine; no n8n dependency because of its Sustainable Use License (C2) |
| Plugin marketplace | D | Signed, capability-scoped plug-ins running out-of-process (Part IV lesson 4); community and commercial plug-ins |
| Public API and webhooks | D | OpenAPI 3.1, GraphQL read gateway, durable webhooks with replay and dead-letter queues (Part IV lesson 5) |
| SSO and identity | T | OIDC, SAML, Google, Microsoft, passkeys, LDAP, SCIM provisioning |
| Multi-language and RTL | D | 22 Indian scheduled languages plus Arabic, French, Spanish, Portuguese, Swahili, Indonesian and others; RTL support (C9) |
| White-label apps | D | Institution-branded mobile apps from one codebase for groups that want their own app listing |

## V.7 Signature Features: Ten Ideas No Incumbent Offers Together

1. **Shadow Switch.** The parallel-run migration of V.5.3. A school trials OpenCampus One for a full term without risk, and the reconciliation report proves readiness. It addresses C6, the biggest switching barrier.
2. **Family Super-App.** One parent login covers every child at every campus, from nursery to university. It includes attendance, homework, fees through the family wallet with UPI AutoPay, bus ETA, canteen balance, consent forms, conferences and auto-translated chat. It addresses C4 and C10, where competitors force several apps.
3. **Offline Classroom Mode.** Teachers take attendance, enter marks and write behaviour notes in a basement lab with no signal. Records sync with deterministic conflict rules when the device reconnects, and offline edits are always auditable. It addresses C9.
4. **Channel Waterfall with Delivery Proof.** A message tries push, then WhatsApp, then SMS, then a voice call in the guardian's language, and stops at the first confirmed delivery. The cost of every channel is shown up front. It addresses C9 and C10.
5. **Consent Ledger (DPDP-native).** Each data purpose (admissions, photos, AI, transport tracking, APAAR) has a versioned notice in the guardian's language and verifiable parental consent with DigiLocker-token support. Withdrawal propagates to processors, and an evidence pack is ready for the Data Protection Board. It is built to the DPDP Rules 2025 phased schedule, with child-consent rules (Rules 3 and 5–16) due 18 months after the 14 November 2025 notification, around May 2027. Comparable GDPR, FERPA and COPPA packs exist for other markets. It addresses C7 and C8.
6. **Accreditation Autopilot.** The NAAC, NBA, NIRF and AISHE evidence vault fills itself from operational data, with lineage back to the source record. It replaces the spreadsheet scramble before every accreditation cycle. It addresses C5 and C8.
7. **Ask OpenCampus with Receipts.** The AI copilot answers questions such as "Which Grade 9 students have below 75% attendance and an unpaid term fee?" Every answer links to the records it used. It never acts without approval and can run fully on-premise. It addresses C11.
8. **One Learner, One Lifetime Record.** A single identity follows the learner from nursery to alumni across campuses in a group. It exports as a verifiable credential (W3C Verifiable Credentials, Open Badges 3.0, CLR) and pushes to DigiLocker/ABC. It addresses C12.
9. **Trust Center in the Product.** Each institution can see who accessed what and when, every export, every API token, every support session (just-in-time and approved by the school), and backup-restore test results. It addresses C7 and is a direct answer to the PowerSource-style support-plane breach.
10. **Leave in One Click.** A full, free, signed export in open formats at any time, written into the licence and the hosted terms. It addresses C6 and turns lock-in into a reason to choose OpenCampus One.

## V.8 UX Principles: Simple, Clean, Classic, Feature-Rich Underneath

1. **"Today" home screen per role.** A teacher sees the next class, an attendance button, unmarked work and messages. A principal sees attendance, fee collection and alerts. A parent sees each child's day. No menus are needed for the 80% of daily tasks.
2. **Command palette (Ctrl/Cmd+K) and universal search.** Type "Aarav fee" or "Grade 7B timetable" and go straight there, with typo-tolerant search.
3. **Progressive disclosure.** Simple defaults with an "Advanced" layer for power users, so the platform is easy for a 200-student school and deep enough for a 40,000-student university.
4. **Classic, calm visual language.** A neutral palette with one accent colour per institution, generous whitespace, a clear type scale (Inter or Noto Sans for Indic scripts), consistent tables, keyboard-first data entry and no visual clutter.
5. **Mobile-first for teachers and parents, desktop-optimised for office staff.** Bulk tasks such as fee posting, timetabling and exam processing get dense desktop layouts.
6. **Accessibility as a gate, not a feature.** WCAG 2.2 AA, screen-reader tested, large-touch targets, dyslexia-friendly font option, reduced motion, high contrast. GIGW 3.0 mapping for Indian government tenants.
7. **Low-bandwidth mode.** Under 200 KB per first screen, image-free option, works on 2G/3G and on low-end Android phones with 2 GB RAM.
8. **Vernacular everywhere.** The UI, notifications, report cards and voice prompts are available in the user's language, with voice input for teachers who prefer speaking to typing.
9. **Guided wizards for rare but critical tasks.** Year-end rollover, promotion, timetable generation, census and UDISE submission, and exam result publication all have a preview, an undo window and a checklist.
10. **In-product learning.** Contextual tips, 60-second videos, a sandbox copy of the institution for safe practice, and a "what changed" panel after each release.

## V.9 Technical Architecture: Lessons from the Top 3 Backends

Part IV shows what to copy and what to avoid:

- PowerSchool has deep in-process plugins and a support portal that became a breach path.
- Infinite Campus has per-customer Windows/SQL Server/Tomcat instances, an ODBC escape hatch and fragmented OneRoster versions.
- Ellucian Ethos has a strong canonical resource and event layer, but complex versioning and legacy self-service surfaces.

The blueprint architecture:

```text
                Cloudflare (DNS, CDN, WAF, TLS)  -- static PWA, docs, edge cache
                                 |
   Web PWA (SvelteKit or Next.js)  |  Mobile (Expo/React Native)  |  Desktop kiosk (Tauri, optional)
                                 |
                   API gateway (rate limits, auth, OpenAPI 3.1)
                                 |
 +-------------------------------+--------------------------------+
 | Modular monolith (TypeScript/NestJS or Python/Django)          |
 |  identity | people | admissions | academics | attendance |     |
 |  assessment | finance | HR | operations | comms | compliance  |
 +-------------------------------+--------------------------------+
        |                |                  |                |
 PostgreSQL 17 + RLS   Outbox -> queue   Object storage    Keycloak / ZITADEL
 (system of record)    (workers, webhooks, (R2 / Garage)    (OIDC, SAML, passkeys)
        |               search, notifications)
 Read replica -> analytics store (Superset, semantic layer)
        |
 Offline sync (PowerSync or Electric) -> SQLite on devices
        |
 OpenTelemetry -> Grafana / Loki / Tempo / Prometheus
 AI service (Ollama/llama.cpp local; vLLM GPU; optional cloud) via permission-aware retrieval
```

**Architecture decisions and why:**

1. **Canonical education model plus projections.** Internal entities are stable. OneRoster 1.2, Ed-Fi, CEDS, UDISE+ and DfE census are adapters with conformance tests, so no standard dictates the internal schema. This is the Ethos lesson without Ethos's licensing barrier.
2. **Modular monolith first.** It is one deployable unit with strict module boundaries, which makes it easy to self-host on a €6 VPS and to secure. Modules can be extracted to services later where load demands it. This avoids the per-customer instance sprawl visible at Infinite Campus.
3. **Multi-tenancy in the database.** Every row carries `tenant_id`, PostgreSQL row-level security enforces isolation, and the application never connects as a table owner. A dedicated-database tier is available for universities and governments that need it.
4. **Durable events.** A transactional outbox gives every event an immutable ID, tenant ID, schema version, actor, causation ID and replay window. Webhooks have retries and dead-letter queues, and connectors have reconciliation endpoints. This fixes the undocumented replay and ordering gaps seen in PowerSchool's and Ellucian's public event models.
5. **Capability-scoped plug-ins.** Plug-ins are signed manifests that declare scopes, events, UI slots and rate limits. They run out-of-process (WebAssembly sandbox or separate container) and never get database superuser access. This keeps PowerSchool-style flexibility without its blast radius.
6. **Separated planes.** The operational, integration, analytical and support planes are separate. Support staff use just-in-time, tenant-approved, time-boxed, read-only-by-default access with full audit. That is the direct lesson of the PowerSource incident.
7. **One policy-aware API for every client.** Web, mobile, partners, reports and AI all receive the same authorization decisions. There is no weaker "mobile API".
8. **Selective offline.** Attendance, mark drafts, behaviour notes, timetables and messages work offline. Fee settlement, result publication and identity changes require online confirmation.
9. **Reconciliation as a feature.** Every connector has full sync, delta sync, cursor recovery, dry run and human-readable error reports.
10. **Evidence by default.** Audit logs, export logs, token inventory, event-delivery health, dependency inventory (SBOM) and backup-restore results are visible to each tenant. There is also a public status page.

## V.10 Open-Source Stack and Licensing

| Layer | Choice | Licence | Why |
|---|---|---|---|
| Database | PostgreSQL 17 (+ pgvector, pg_trgm) | PostgreSQL License | RLS, JSONB, full-text search, mature operations |
| Backend | TypeScript + NestJS (alternative: Django) | MIT / BSD | Large talent pool, typed domain modules |
| Web | SvelteKit or Next.js PWA | MIT | Installable, offline caching, fast first load |
| Mobile | Expo / React Native | MIT | Shares TypeScript and UI logic; native push and camera |
| Desktop (optional) | Tauri | MIT / Apache-2.0 | Lightweight kiosk and exam-hall client |
| Offline sync | PowerSync open-source components or ElectricSQL | Apache-2.0 / MIT | PostgreSQL-aware partial replication to SQLite |
| Auth | Keycloak (alternative: ZITADEL) | Apache-2.0 | OIDC, SAML, LDAP, passkeys, multi-realm |
| Search | PostgreSQL FTS first; Meilisearch Community Edition | MIT | Typo-tolerant search; enterprise edition avoided |
| Object storage | Cloudflare R2 (hosted) or Garage (self-hosted) | Service / AGPL-3.0 (Garage) | Low egress; MinIO avoided because its community edition is frozen |
| Workflow | Outbox + workers; Temporal for long processes | MIT | Durable timers and approvals; n8n avoided (Sustainable Use License) |
| BI | Apache Superset + semantic layer | Apache-2.0 | Open dashboards on a read replica |
| Video | Jitsi Meet / BigBlueButton | Apache-2.0 / LGPL-3.0 | Self-hostable conferences and classes |
| AI | Ollama / llama.cpp, vLLM; IndicTrans2 for translation | MIT / Apache-2.0 / MIT | Local, private inference; 22 Indian languages |
| Timetabling | Google OR-Tools CP-SAT | Apache-2.0 | Proven constraint solver |
| Observability | OpenTelemetry + Grafana LGTM | Apache-2.0 / AGPL-3.0 | Portable telemetry |
| Deployment | Docker, Coolify or Dokploy; Helm charts for Kubernetes | Apache-2.0 | One-click self-hosting |

**Project licence.** The core platform is AGPL-3.0, so anyone can use, modify and self-host it for free, including commercially. Anyone offering a modified version as a network service must publish their changes, which protects the community from closed SaaS forks. SDKs, connector templates, the design system and API clients are Apache-2.0, so vendors and institutions can build proprietary integrations without copyleft concerns. Documentation is CC BY 4.0. There is no source-available bait and switch: every feature in the core stays OSI-licensed. Contributions use the Developer Certificate of Origin (DCO), and the trademark is held by a non-profit foundation to protect the name.

**Licensing cautions found in this research.** n8n uses the Sustainable Use License (not OSI). MinIO's AGPL community edition is frozen, and AIStor is commercial. Meilisearch Enterprise is BUSL. The Vercel Hobby plan is for personal, non-commercial use. Open-weight AI models each carry their own licence terms. All of these are excluded from the core or flagged in the dependency policy.

## V.11 Security, Privacy and Compliance by Design

**Baseline standards.** OWASP ASVS 5.0 Level 2 for the whole application, with Level 3 for authentication, finance and the support plane. The ISO/IEC 27001:2022 ISMS and SOC 2 Type II evidence model is built into the hosted service from day one.

**Identity.** Passkeys (WebAuthn Level 3) and phishing-resistant MFA are mandatory for staff. Parents can sign in with an OTP or a passkey. Sessions are short-lived and refresh tokens rotate. Admins can revoke any device.

**Isolation.** PostgreSQL RLS is tested in CI with negative tests, and the application has no superuser connections. Each tenant gets its own encryption key (envelope encryption) for sensitive fields such as health, safeguarding, identifiers and bank details.

**Support plane.** Support access is just-in-time, approved by the institution, time-limited, reason-coded and recorded. Bulk export by support staff is impossible without dual approval. Anomaly detection runs on exports and API usage.

**Software supply chain.** Signed releases (Sigstore), SBOM per release, dependency scanning, secret scanning, SAST and DAST in CI, reproducible builds, a public vulnerability disclosure policy, a bug bounty and an annual external penetration test with a published summary.

**Data protection packs.** These are versioned and dated per jurisdiction:

- **India:** DPDP Act 2023 and Rules 2025 with the phased commencement correctly labelled. Verifiable parental consent, no behavioural tracking or targeted ads for children, a breach workflow with a 72-hour detail window, grievance officer tooling and retention and erasure orchestration.
- **US:** FERPA, COPPA (2025 amendments), PPRA and state student-privacy laws such as California SOPIPA.
- **EU and UK:** GDPR, UK GDPR and the Age Appropriate Design Code.
- **Australia:** Privacy Act and the Children's Online Privacy Code.

**Data residency.** The hosted service runs in-region (India, EU, UK, US) and every subprocessor is listed publicly.

**Resilience.** Encrypted off-site backups, point-in-time recovery, quarterly restore drills with results shown to tenants, RPO of 15 minutes or less and RTO of 4 hours or less on hosted plans.

## V.12 Deployment Paths: Zero Cost to Low Cost

| Path | Who | Monthly cost (estimate) | Components |
|---|---|---:|---|
| Developer and demo | Contributors, evaluators | $0 | GitHub Free (code, CI, Pages docs), Cloudflare Pages/Workers Free (PWA, docs), Neon Free or Supabase Free with synthetic data only, Cloudflare R2 free tier (10 GB) |
| Single school self-hosted | One school with an IT teacher or partner | €6–€20 | One Hetzner cloud VM (from €5.49–€5.99/month excl. VAT), Coolify or Dokploy, PostgreSQL, Garage or R2, nightly encrypted off-site backups, Cloudflare DNS/WAF free |
| School group or small college | 5–20 institutions | €25–€75 | Two VMs (app + database), R2, monitoring, separate backup target |
| Hosted SaaS by the project | Institutions that want no IT | $25–$300+ infrastructure per region | Managed PostgreSQL with replicas, autoscaled app nodes, search, observability, paid messaging |
| Government or university on-premise | Ministries, large universities | Own data centre | Helm charts on Kubernetes, air-gapped AI option, dedicated database tier |

Free tiers are used only for development, documentation, demos and public assets, never as the system of record for real student data. Oracle Cloud Always Free can host a zero-cost pilot when capacity is available, but it must have off-provider backups. WhatsApp, SMS and voice traffic, payment-gateway fees, app-store fees and GPU inference are pass-through costs shown transparently to institutions.

## V.13 Business Model, Go-to-Market and Sustainability

**Revenue model (open core without crippleware):**

1. **Hosted OpenCampus Cloud** with a public price card. Indicative targets, to be validated with pilots:
   - India: free up to 100 students, then ₹15–₹30 per student per year for schools and ₹60–₹120 for higher education.
   - UK: £2–£4 per pupil per year.
   - US private schools: $1–$2 per student per month.
   - All core modules are included in every plan.
2. **Usage pass-through** for messaging, payments and AI at cost plus a small published margin.
3. **Enterprise services** for universities and governments: dedicated tenancy, SLAs, accreditation consulting and integration projects.
4. **Certified partner network.** Local implementers in every state and country earn the migration and training revenue, which builds the support capacity that incumbents lack (C3).
5. **Marketplace revenue share** on paid community plug-ins (70/30 in favour of developers).
6. **Grants and public funding.** Digital public goods registration (Digital Public Goods Alliance), education-ministry partnerships, CSR funding for government schools and philanthropic grants for offline and low-resource features.

**Go-to-market:**

- Start with 50 lighthouse schools and 5 colleges in two Indian states (for example Telangana and Maharashtra), migrated free from Fedena, Teachmint, Entab, Excel and paper.
- Publish the case studies and the migration time for each.
- Run a "Switch Season" campaign before every academic year: April–June in India, June–August in the UK and US.
- Give government schools a free hosted tier funded by CSR and grants. This builds massive adoption (the adoption score drives 30% of the ranking) and creates a reference base for private schools.
- Build developer community through hackathons on connectors and plug-ins, and student contributors through university open-source programmes.
- Use analysts and review sites: proactively collect G2, Capterra and app-store reviews from day one, since UX/mobile ratings are where incumbents are weakest.

**Governance.** A non-profit foundation holds the trademark and roadmap. A technical steering committee includes institution representatives. Public RFCs cover major changes, with a long-term-support release every 12 months.

## V.14 Phased Roadmap with Exit Criteria

| Phase | Timeline (indicative) | Scope | Exit criteria |
|---|---|---|---|
| 0. Foundations | Months 0–3 | Threat model, canonical data model, tenancy with RLS tests, auth (Keycloak + passkeys), audit log, design system, CI/CD, licence and governance set-up | RLS negative tests pass; ASVS L2 checklist for the foundation; public repository and docs live |
| 1. School MVP ("replace the register") | Months 3–9 | People, admissions, classes/sections, attendance (offline), timetable viewer, gradebook, report cards, announcements and chat, fees with UPI, parent and teacher apps, Excel/Fedena/Teachmint importers, India terminology | 20 lighthouse schools fully live for a term; under 2 days migration per school; parent app at least 4.5 stars; zero critical security findings in external test |
| 2. India compliance and ERP depth | Months 9–15 | UDISE+, APAAR, DigiLocker, PARAKH HPC, DPDP consent ledger, transport GPS, library, inventory, HR and payroll, GST ledger, Tally export, channel waterfall, auto-translation, auto-timetabler | 200 schools; UDISE+ submission completed from the platform; DPDP evidence pack reviewed by external counsel |
| 3. Higher education and global | Months 15–24 | Higher-Ed Pack (CBCS, exams, ABC, NAAC/NBA/NIRF/AISHE), UK pack (census, CTF), OneRoster 1.2 and LTI 1.3 certification, Ed-Fi adapter, PowerSchool/SIMS/Arbor/Ellucian importers, Shadow Switch, plug-in SDK, marketplace beta | 10 colleges and 2 universities live; 1EdTech certification obtained; first UK schools migrated from SIMS |
| 4. Intelligence and scale | Months 24–36 | Ask OpenCampus copilot (local and cloud), early-warning analytics, Superset semantic layer, benchmarking, multi-campus group console, white-label apps, Kubernetes HA, SOC 2 Type II, ISO 27001 | 2,000+ institutions; SOC 2 Type II report; AI copilot audited for bias and privacy |
| 5. Ecosystem leadership | Year 3+ | Government/ministry pack, Gulf/Africa/SEA localisations, US state reporting, verifiable credentials wallet, research and alumni suites, partner certification at scale | 10,000+ institutions in 10+ countries; top-3 app-store rating in category; recognised as a Digital Public Good |

## V.15 Success Metrics and Key Risks

**North-star metrics:**

- Weekly active teachers and parents as a share of enrolled users
- Median migration time per institution
- Net Promoter Score by role
- App-store rating (target at least 4.6)
- Support first-response time
- Share of institutions using offline mode
- Cost per student compared with the incumbent replaced
- Security: zero cross-tenant incidents, mean time to patch critical CVEs under 72 hours

**Key risks and mitigations:**

| Risk | Mitigation |
|---|---|
| Scope is too broad for a new team | Strict phase gates; the school MVP must replace an incumbent for one segment before HE work begins |
| Open-source sustainability | Hosted revenue, partner network, grants and foundation governance; AGPL protects against closed forks |
| Incumbent response (price cuts, bundling) | Compete on exit freedom, offline, compliance and transparency, which closed vendors cannot match quickly |
| Regulatory change (DPDP rules, state laws) | Dated policy packs with a public change log; legal review per release |
| Security of a public codebase | Defence in depth, bug bounty, signed releases and external audits; openness speeds discovery and fixes |
| AI errors or bias | Retrieval with citations, human approval, bias monitoring, admin kill switch, no autonomous high-stakes decisions |

## V.16 Projected Position Against the Ranked Platforms

Applying the same rubric to the planned capabilities at the end of Phase 4 gives this result. It is a design target, not a measured result.

| Dimension | Weight | Target score | Basis |
|---|---:|---:|---|
| Feature breadth | 30% | 10 | All modules in V.6 across K-12 and higher education; segment packs |
| Adoption | 30% | 6 (year 3) to 9 (year 5) | Free core plus government-school programme plus switching engine |
| Advanced features | 20% | 10 | Permission-aware copilot, early warning, auto-timetabler, accreditation autopilot, verifiable credentials |
| UX and mobile | 10% | 10 | Offline-first apps, Today screens, accessibility, vernacular |
| Interoperability | 10% | 10 | OneRoster 1.2, LTI 1.3, Ed-Fi, CASE, Open Badges, UDISE+, ABC, DigiLocker, open API and events, one-click exit |
| **Weighted** | | **8.8 (year 3) to 9.7 (year 5)** | Year 3 already ties PowerSchool's 8.8; year 5 would rank #1 worldwide and in India |

The decisive factor is adoption, which carries 30% of the score. That is why the plan pairs a free open-source core with a migration engine and a government-school programme: features alone will not win the ranking unless institutions can switch easily.

## V.17 Blueprint References

Evidence for this blueprint comes from the 40 dossiers (Parts I–III), the backend teardown (Part IV) and Appendices A–C. The main external sources are:

1. The Key Group, What Do Schools Really Think About Their MIS in 2025? - https://thekeygroup.com/news-insights/4zr7dmj85i8urkohb1w0fxcjsr8stt
2. WhichMIS, MIS Stats from the May 2026 Census Returns - https://www.whichmis.com/mis-stats-from-the-may-2026-census-returns/
3. Finnemore Consulting, The UK School MIS Market 2026 - https://finnemoreconsulting.com/uk-school-mis-market-2026/
4. PowerSchool Security Incident: SIS Incident - https://www.powerschool.com/security/sis-incident/
5. FTC action against Illuminate Education (December 2025) - https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-takes-action-against-education-technology
6. Frontline Education Notice of Data Breach - https://www.frontlineeducation.com/news/frontline-education-notice-of-data-breach/
7. BBC, Blackbaud hack: more UK universities confirm breach - https://www.bbc.com/news/technology-53528329
8. UDISE+ Ministry of Education portal - https://udiseplus.gov.in/
9. AISHE Final Report 2021–22 - https://aishe.gov.in/document/aishe-final-report-2021-22/
10. APAAR: One Nation, One Student ID - https://apaar.education.gov.in/
11. Academic Bank of Credits - https://www.abc.gov.in/
12. PARAKH Holistic Progress Cards - https://parakh.ncert.gov.in/hpc/
13. Digital Personal Data Protection Rules 2025 (MeitY) - https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf
14. National Assessment and Accreditation Council - https://www.naac.gov.in/
15. National Board of Accreditation - https://www.nbaind.org/
16. National Institutional Ranking Framework - https://www.nirfindia.org/home
17. 1EdTech OneRoster - https://www.1edtech.org/standards/oneroster
18. 1EdTech Learning Tools Interoperability - https://www.1edtech.org/standards/lti
19. Ed-Fi Alliance data standard - https://docs.ed-fi.org/getting-started/provider-playbook/project-planning/why-support-the-ed-fi-data-standard/
20. W3C Web Content Accessibility Guidelines 2.2 - https://www.w3.org/TR/WCAG22/
21. W3C Web Authentication Level 3 - https://www.w3.org/TR/webauthn-3/
22. OWASP Application Security Verification Standard - https://owasp.org/www-project-application-security-verification-standard/
23. PostgreSQL row security policies - https://www.postgresql.org/docs/current/ddl-rowsecurity.html
24. PowerSync open-source components - https://powersync.com/open-source
25. Electric Sync documentation - https://electric.ax/docs/sync/
26. Keycloak - https://www.keycloak.org/
27. Apache Superset - https://superset.apache.org/
28. AI4Bharat IndicTrans2 - https://github.com/AI4Bharat/IndicTrans2
29. Google OR-Tools - https://developers.google.com/optimization
30. n8n Sustainable Use License - https://docs.n8n.io/n8n-community-license
31. MinIO pricing and community-edition status - https://www.min.io/pricing
32. Coolify pricing and self-hosting - https://coolify.io/pricing
33. Hetzner Cloud - https://www.hetzner.com/cloud/
34. Cloudflare Workers pricing - https://developers.cloudflare.com/workers/platform/pricing/
35. Cloudflare R2 pricing - https://developers.cloudflare.com/r2/pricing/
36. GNU Affero General Public License v3.0 - https://www.gnu.org/licenses/agpl-3.0.html
37. Digital Public Goods Alliance - https://www.digitalpublicgoods.net/
38. RAND, AI Use in Schools Is Quickly Increasing but Guidance Lags Behind - https://www.rand.org/pubs/research_reports/RRA4180-1.html
39. UNESCO, Higher education global trends release - https://www.unesco.org/en/articles/number-students-higher-education-more-doubled-20-years-inequalities-remain
40. Ellucian Ethos Community on GitHub - https://github.com/ellucianEthos
