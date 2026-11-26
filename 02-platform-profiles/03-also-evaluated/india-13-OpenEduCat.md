# India #13 (evaluated). OpenEduCat (OpenEduCat Inc.)

| Field | Detail |
|---|---|
| Vendor / owner | OpenEduCat Inc.; official leadership page names Parthiv Patel (Founder & CEO) and Neha Patel (Co-Founder) [2] |
| Headquarters | Ahmedabad, Gujarat, India (official About page and GitHub organization location); this differs from the Gandhinagar disambiguation in the brief [2] [7] |
| Company founded (year) | 2014, according to the vendor’s current company history [2] |
| Product first launched (year or Not publicly disclosed) | 2014 in the company’s product history; the public GitHub repository was created on 2013-05-02, so the exact commercial launch date is not separately disclosed [2] [7] |
| Platform classification (Cloud SaaS / Web-based / Desktop / Mobile iOS+Android / On-premise / Hybrid) | Browser/web-based ERP; managed cloud SaaS; self-hosted/on-premise; hybrid; native iOS and Android apps. No separate desktop client was verified [1] [6] [13] |
| Primary segments | K–12 schools, preschools, colleges, universities, vocational/training institutes, boarding schools, and multi-campus education groups [1] [3] [9] |
| Market presence (schools, students, countries, with date of claim) | Vendor claim: 1,000+ institutions, 3M+ users, 90+ countries; checked 24 November 2026. The figure is not independently audited in the sources reviewed [2] |
| Official website (full URL) | https://openeducat.org/ |
| Product / features page (full URL) | https://openeducat.org/features/ |
| Documentation / help center (full URL) | https://newdocs.openeducat.org/ |
| Pricing page (full URL or No public pricing page) | https://openeducat.org/pricing/ |
| Review ratings (G2, Capterra, App Store, Play Store with score, review count and date viewed) | G2 4.6/5 from 154 reviews (viewed 24 Nov 2026); Capterra 3.8/5 from 4 reviews (page last updated 28 Sep 2026; viewed 24 Nov 2026); GetApp 3.8/5 from 4 reviews (last updated Mar 2026); Software Advice 3.8/5 from 4 reviews; SourceForge 4.8/5 from 37 reviews; Google Play “OpenEduCat - Educational ERP” showed 1K+ downloads but no visible score/review count; Apple App Store “OpenEduCat - Educational ERP” said insufficient ratings/reviews to display an overview [15] [16] [17] [18] [19] [21] [22] |

### Overview

OpenEduCat is an open-source education ERP built on Odoo. It combines a student information system with admissions, academics, fees, accounting, HR, learning, campus operations, communications, and higher-education workflows. The Community Edition is free and self-hostable under LGPL-3; the Enterprise Edition adds commercial modules, managed hosting and vendor support [5] [6] [8].

The company says it was founded in 2014, reached 100 institutions in 2016, launched Enterprise in 2017, added LMS in 2018, released native apps in 2021, introduced AI in 2023, and passed 3M users/1,000+ institutions in 2024 [2]. The repository predates that company milestone, having been created in 2013 [7]. I found no verified acquisition or venture-funding history in the reviewed sources.

### Platform Classification Explained

OpenEduCat is web-first, with browser access, APIs and role-based portals. Managed cloud deployment includes updates, backups, scaling and a stated 99.9% uptime SLA; cloud regions are described in North America, Europe or Asia-Pacific [13].

Self-hosting is a core differentiator. The download page offers Windows, Ubuntu/Debian, Red Hat/CentOS, source ZIP and Docker images, with PostgreSQL, Python and Nginx requirements. On-premise keeps data on institutional servers, while hybrid combines local sensitive data with a cloud portal [6] [13]. No standalone desktop client was verified; the Windows package is for deployment.

The native mobile product is named “OpenEduCat - Educational ERP” on both Google Play and Apple’s App Store. The vendor describes branded iOS and Android apps for parents, students, faculty and staff with grades, attendance, timetables, assignments, fee payments, library access, push notifications, offline caching and role-based permissions [4] [21] [22].

### Complete Feature Inventory

#### Admissions and enrollment
Online application intake, applicant stages, document upload, review, merit-list/selection workflows, conversion from applicant to enrolled student, subject-wise admission, e-signature offer letters, mass applicant email, application tracking and drag-and-drop forms are documented. The richer form-builder and e-signature functions are Enterprise additions [3] [8].

#### Student information and records
The core SIS stores student, parent/contact, demographic, academic-history, health, document, program, course, batch, subject, department and faculty records. It supports portals, student badges, configurable terminology, academic plans, activity logs and multi-campus data [3] [8].

#### Attendance
Basic attendance supports marking and reporting by class/date, with student leave requests, absence alerts and attendance-linked reporting. Enterprise pages add biometric, fingerprint, RFID and face-recognition capture, kiosk check-in, offline mobile marking and parent notifications [3] [4] [8].

#### Timetable and master scheduling
The timetable module creates sessions and conflict-free schedules, allocates rooms and faculty, supports timetable changes, lesson/session planning, study-material allocation and calendar synchronization. Live-class integrations can generate meeting links from scheduled sessions [3] [8] [14].

#### Gradebook, assessment and examinations
The Enterprise stack includes a central gradebook, marks and letter grades, GPA/CGPA, CBCS credits, outcome-based education with CO–PO attainment, question banks, auto-graded quizzes, weighted scoring, multiple exam versions, negative marking, OMR scanning and anti-cheating/proctoring. Community has basic exams, configurable letter grades and marksheets, but not the central gradebook or full LMS [3] [8].

#### Report cards and transcripts
OpenEduCat generates marksheets, progress/report cards, result publications and transcripts. Enterprise secure-transcript workflows add QR verification, digital signatures, watermarks, batch processing, self-service ordering, online payment and financial-hold enforcement. AI-generated report-card comments are described as an Enterprise AI use case [3] [8].

#### Learning management and homework
The Enterprise LMS provides course authoring, video/content delivery, quizzes, forums, surveys, gamification, certificates, H5P/SCORM content and learning analytics. Assignments support submission, marks, feedback and gradebook linkage; Enterprise adds inline annotation, rubrics, multiple attempts and late-submission rules [3] [8].

#### Communication (SMS, email, push, WhatsApp)
Communication includes email, notices, news/blog publishing, forums, announcements, surveys, push notifications and in-app messaging. Enterprise integrations send attendance alerts, fee reminders, exam/result notifications and emergency broadcasts through Twilio/Vonage SMS or WhatsApp Business API; WhatsApp supports approved templates, broadcasts, two-way replies and logged responses [3] [11] [12].

#### Parent, student and teacher portals
Student, parent, faculty and staff portals expose role-specific records. The parent portal covers grades, attendance, fee balances, messages and circulars; the student portal covers courses, timetable, assignments, results and documents; faculty views include schedules, attendance, grading, leave and substitutions [3] [4] [8].

#### Fees, billing, payments and accounting
Fee structures, tuition/program/hostel/exam/lab charges, discounts, installments, invoices, receipts, scholarships, refunds, online payment, fee reminders and automated reconciliation are supported. The accounting layer provides double-entry books, chart of accounts, journals, AP/AR, bank reconciliation, budgets, cost centers, fund-level tracking and fee-to-ledger posting [3] [8] [10].

#### HR, staff and payroll
Faculty/staff profiles can include qualifications, skills, degrees, prior employment, workload, substitutions, attendance, timesheets, recruitment, appraisals and performance reviews. Payroll covers salary calculations, taxes, benefits and payslips, with attendance and contracts as inputs [3]. Indian PF/ESI is claimed in a comparison page search result but was not substantiated by a page opened for this profile; treat it as unverified.

#### Transport
Enterprise transport manages routes, vehicles, student stops and allocations, driver certifications, tracking/operations and transport-fee billing linked to student records, attendance and parent portals [3] [8].

#### Library
The library module covers catalogs, members, circulation, barcode-enabled lending, fines and collection reports. Enterprise adds barcode-scanner workflows and a digital/e-book library tied to courses and student records [3] [8].

#### Hostel and boarding
Enterprise hostel management handles room/bed allocation, occupancy, check-in/check-out, visitors and IDs, gate passes, facility maintenance, inventories and fee linkage [3] [8].

#### Inventory and assets
Inventory tracks supplies, lab chemicals, IT equipment and campus assets across buildings and stockrooms, with barcode scanning, reorder points, lot/expiry alerts and valuation. Asset requests add budget approvals, acquisition-to-disposal lifecycle, warranties, maintenance and procurement/accounting linkage [3].

#### Health and medical
Health information is a documented SIS field and the Enterprise student-welfare suite adds institutional health records. The reviewed pages do not substantiate a full clinical/medical-records module, electronic medication administration, or a certified school-nurse workflow [3] [8].

#### Behavior, discipline and pastoral care
Enterprise welfare covers discipline, grievances, leave, mentoring, feedback, achievements, skills assessment, progress, withdrawal and basic pastoral lifecycle records. Community exposes only a basic activity log [8].

#### Special education and safeguarding
Third-party listings tag “Special Education,” but I found no opened official feature or documentation page proving IEP/504-style plans, safeguarding case management, or child-protection workflows. Score this capability as not publicly verified rather than assuming the generic student-welfare tools are special-education functionality [16] [18].

#### Alumni and fundraising
Enterprise alumni management covers graduate records, reunions/events, an alumni job board and alumni blog. Email marketing can target alumni and donors, but a dedicated fundraising, donation ledger or campaign-management module was not clearly documented [3] [8].

#### Analytics, dashboards and reporting
KPI dashboards cover enrollment yield, retention, graduation, staffing, attendance, class capacity, fees and budget utilization. Advanced reporting produces academic, financial and compliance reports on demand or on schedule with CSV/Excel export; Microsoft 365 integration advertises Power BI export [3] [14].

#### AI features
Enterprise AI covers essay/assignment grading, rubric and quiz generation, lesson planning, note summarization, report-card comments, at-risk alerts and predictive performance/enrollment insights. The model-agnostic layer supports OpenAI, Claude, Gemini, Llama and Mistral, with quotas, guardrails, audit logs and REST APIs. G2 additionally lists an AI chat assistant and AI-enhanced search; those claims are not independently verified [14] [15].

#### Government/state reporting and compliance
The India page explicitly markets CBSE, ICSE/ISC and state-board schools, 22 official Indian languages, Indian fee workflows and school/university reporting [9]. The platform has generic compliance-report and advanced-reporting capabilities, but no reviewed official page confirms ready-made UDISE+, APAAR ID, NEP 2020 holistic progress card, NAAC, NBA, NIRF or AISHE exports. GST-specific invoicing, Tally integration and Paytm as a distinct gateway are also not publicly confirmed; Razorpay supports UPI and Paytm as a wallet/UPI method [10] [11].

#### Mobile apps
The exact app name is “OpenEduCat - Educational ERP.” iOS/iPadOS and Android versions offer role-based access, attendance, grades, schedules, assignments, payments, library, messaging, push notifications and offline synchronization. Google Play showed 1K+ downloads but no visible score; Apple reported insufficient ratings/reviews [4] [21] [22].

#### Integrations and APIs
The integrations directory advertises 29 integrations, including Google Workspace/Classroom/Drive/Calendar/Gmail, Microsoft 365/Teams/OneDrive/Outlook/Azure AD, Zoom, Google Meet, BigBlueButton, WhatsApp, SMS, 19 payment gateways, SAML/LDAP and LTI/SCORM. The platform also advertises REST APIs and webhooks [14].

#### Security and privacy
Security controls described by the vendor include AES-256 at rest, TLS 1.3 in transit, tenant database isolation, encrypted backups, RBAC, record-level rules, MFA, SAML/OIDC, LDAP/AD, Google/Microsoft SSO, API keys/OAuth/JWT, rate limiting, audit trails, anomaly monitoring and configurable retention [13].

### Advanced and Distinctive Features

- **Open-source and self-hosted:** LGPL-3 Community source code can be audited, modified and deployed without per-student licensing [5] [6] [7].
- **Odoo data model:** Academic, finance, HR and campus data share one database rather than requiring separate SIS/LMS products [1] [7].
- **No-code customization:** Enterprise No Code Studio provides drag-and-drop apps, forms, workflows and reports [3].
- **AI plus local-model option:** AI tools can use cloud providers or self-hosted Llama/Mistral endpoints, with quotas, guardrails and audit logs [14].
- **Indian fee collection:** Razorpay handles UPI, net banking, cards, wallets, EMI, payment links and student-ledger reconciliation [10].
- **Higher-education depth:** CBCS, OBE, CO–PO attainment, thesis management, convocation and placement are unusual in school-first products [3] [8].

### Pricing Details

The official pricing page, checked 24 November 2026, says Community is free and LGPL v3. Enterprise starts at **$79 per module per year**, uses user packs from 25 to 10,000+ for cloud or unlimited users for an on-premise one-time option, and has no per-student fee. It advertises cloud or on-premise deployment, a 15-day trial, no setup fees, and “buy 2 years + get the 3rd year free.” The live configurator is required for a final quote; the public page does not show INR prices, so an INR equivalent is **not publicly listed** and should not be treated as a fixed rupee price [4].

The TCO calculator gives illustrative group prices from $299/year for Core SIS to $1,999/year for all modules. Its example shows implementation/training of $7,000 for Community and $13,000 for Enterprise, plus Community hosting; these are scenario estimates, not contractual prices [23].

Official mobile pricing on the feature page lists the Android app at **$889/year** and iOS app at **$1,179/year**, unlimited users, licensed separately. Independent directories display inconsistent prices: G2 and Capterra/GetApp/Software Advice show a $59/year starting figure, while SourceForge lists $79/month and much higher plan examples. These should be treated as directory/listing data, not authoritative Enterprise quotes [4] [15] [16] [17] [18] [19].

### Integrations, Standards and Interoperability

OpenEduCat has a public REST API/webhook story, SSO through SAML 2.0, OIDC/OAuth, LDAP/Active Directory, Azure AD and Google authentication, plus a maintained integrations directory [12] [13] [14]. LTI 1.3, SCORM 1.2/2004 and xAPI are explicitly documented, including grade passback and a learning-record store [25]. Google Workspace syncs Classroom rosters, Drive, Calendar, Gmail and Meet; Microsoft 365 connects Teams, OneDrive, Outlook, Azure AD, SharePoint and Power BI [26] [27].

Razorpay, Stripe, PayPal and other gateways are documented; India-specific payment methods include UPI, net banking, RuPay, cards, EMI and wallets including Paytm [10] [11]. I found no evidence of certification for OneRoster, Ed-Fi or SIF, and no verified Clever or ClassLink connector. Therefore interoperability is strong for an Odoo/API platform but should not be described as standards-certified.

### Security, Privacy and Compliance

The vendor claims FERPA, GDPR and COPPA readiness through access controls, audit logging, consent workflows, portability/deletion tools and parental-consent controls [13]. It says SOC 2 reports and DPAs are available on request, but no public SOC 2 report or ISO 27001 certificate was provided on the reviewed page. No explicit India Digital Personal Data Protection Act readiness statement was found. On-premise deployment can keep data in an institution’s network; cloud regions are described as North America, Europe and Asia-Pacific [13].

The product page claims AES-256, TLS 1.3, isolated databases, daily backups, RPO under one hour and RTO under four hours. No public security incident was located in reviewed sources through 24 November 2026; app-store privacy disclosures should still be validated against institution-configured processing [13] [21] [22].

### Strengths

- Broad academic, financial, HR, campus and higher-education coverage in one Odoo-based data model.
- Free LGPL-3 Community Edition and genuine self-hosting reduce lock-in and permit code inspection.
- Strong deployment choice: managed cloud, self-hosted or hybrid.
- Good Indian payment fit through Razorpay, UPI, SMS/WhatsApp links and automatic reconciliation.
- Native mobile apps, LTI/SCORM/xAPI, Google/Microsoft integrations and public API/webhook claims.
- Enterprise differentiators include CBCS/OBE, OMR, AI, no-code workflows, thesis, placement and convocation.

### Weaknesses and Common User Complaints

- Setup and configuration can be difficult: G2 users praise centralization but repeatedly mention learning curve, setup difficulty, technical issues and limited customization [15].
- Independent reviews are less enthusiastic than G2: GetApp and Software Advice show 3.8/5; Software Advice gives 3.5 for ease of use and 3.25 for support [17] [18].
- Users report too many menus/icons, language terminology barriers, a dated student profile, and library shortcomings; one review wanted a glossary and fewer menus [18].
- Reviewers say grading-period and multi-teacher workflows can be closed or cumbersome, and support/documentation may be insufficient for non-technical integrations [18] [19].
- SourceForge feedback cites limited out-of-box customization, incomplete documentation, occasional performance slowdowns and weak state-reporting coverage [19].
- India-specific government identifiers/reporting and Tally/GST/DPDP claims are not sufficiently evidenced in public documentation, so local implementation effort may be material.

### Key Milestones

- **2013:** Public OpenEduCat GitHub repository created on 2 May 2013 [7].
- **2014:** Vendor’s stated founding year; began as an open-source education-management project [2].
- **2016:** Vendor says it reached 100 institutions across 20 countries [2].
- **2017:** Enterprise Edition launched with advanced modules and support [2].
- **2018:** Full LMS and online course delivery/grade synchronization added [2].
- **2019:** Vendor says it passed 500 institutions and 1M users [2].
- **2020:** Remote-learning and virtual-classroom support expanded [2].
- **2021:** Native Android and iOS apps released [2].
- **2022:** Vendor says it reached 2M users and added multi-campus/advanced analytics; a contemporaneous press release reported 300k installations and 2M users [2] [20].
- **2023:** Vendor says AI course-generation, quiz-generation and predictive-analytics features were introduced [2].
- **2024:** Vendor says it passed 3M users and 1,000+ institutions in 90+ countries [2].
- **2025:** Platform modernization, UI/security refresh and expanded API capabilities claimed [2].
- **2026:** Current pages emphasize global expansion, 73+ features, 29 integrations, AI, no-code tools and Indian-market workflows [3] [9] [14].
- **Acquisitions/funding:** No verified acquisition or funding event was found in the opened sources.

### References

1. OpenEduCat official home page - https://openeducat.org/
2. OpenEduCat About Us: mission, leadership and milestones - https://openeducat.org/about/
3. OpenEduCat complete feature catalog - https://openeducat.org/features/
4. OpenEduCat official pricing page - https://openeducat.org/pricing/
5. OpenEduCat documentation home - https://newdocs.openeducat.org/
6. OpenEduCat Community Edition download and deployment page - https://openeducat.org/download/
7. OpenEduCat official GitHub repository - https://github.com/openeducat/openeducat_erp
8. OpenEduCat Community versus Enterprise comparison - https://openeducat.org/compare-editions/
9. OpenEduCat education software for India - https://openeducat.org/education-software-india/
10. OpenEduCat Razorpay school fee payment integration - https://openeducat.org/integrations/razorpay/
11. OpenEduCat payment gateway integrations - https://openeducat.org/integrations/payment-gateways/
12. OpenEduCat SMS provider integrations - https://openeducat.org/integrations/sms-providers/
13. OpenEduCat security and compliance - https://openeducat.org/security/
14. OpenEduCat integrations directory - https://openeducat.org/integrations/
15. G2 OpenEduCat reviews and product details - https://www.g2.com/products/openeducat/reviews
16. Capterra OpenEduCat review and pricing - https://www.capterra.com/p/182870/OpenEducat/
17. GetApp OpenEduCat reviews and pricing - https://www.getapp.com/education-childcare-software/a/openeducat/
18. Software Advice OpenEduCat review - https://www.softwareadvice.com/gradebook/openeducat-profile/
19. SourceForge OpenEduCat reviews, pricing and user feedback - https://sourceforge.net/software/product/OpenEduCat/
20. Business Standard/ANI OpenEduCat press release, 4 January 2022 - https://www.business-standard.com/content/press-releases-ani/openeducat-s-open-source-educational-management-system-creates-an-industry-buzz-122010400615_1.html
21. Google Play OpenEduCat - Educational ERP listing - https://play.google.com/store/apps/details?id=com.inc.openeducat&hl=en
22. Apple App Store OpenEduCat - Educational ERP listing - https://apps.apple.com/us/app/openeducat-educational-erp/id1631506740
23. OpenEduCat education software total-cost-of-ownership calculator - https://openeducat.org/tco-calculator/
24. OpenEduCat WhatsApp integration - https://openeducat.org/integrations/whatsapp/
25. OpenEduCat LTI and SCORM integration - https://openeducat.org/integrations/lti-scorm/
26. OpenEduCat Google Workspace integration - https://openeducat.org/integrations/google-workspace/
27. OpenEduCat Microsoft 365 integration - https://openeducat.org/integrations/microsoft-365/
28. OpenEduCat AI how-it-works page - https://openeducat.org/ai/how-it-works/
