# Global #21 (evaluated). Aeries SIS (Aeries Software)

| Field | Detail |
|---|---|
| Vendor / owner | Aeries Software, Inc. (also shown as AERIES SOFTWARE, LLC in Google Play); Francisco Partners announced a growth investment in 2025, while Aeries said it remained family-operated. [1] [2] |
| Headquarters | Orange, California, USA (770 The City Dr S, Ste 6500, Orange, CA 92868-4923 in the Google Play developer listing). [3] |
| Company founded (year) | 1995 (the official site copyright and company materials use 1995; LinkedIn also says it opened in 1995). [4] |
| Product first launched (year or Not publicly disclosed) | Not publicly disclosed. The company says the SIS has supported K-12 districts for about 30 years, but that does not establish a distinct product-launch year. [4] |
| Platform classification (Cloud SaaS / Web-based / Desktop / Mobile iOS+Android / On-premise / Hybrid) | Cloud-hosted web platform on AWS; web access; self-hosted/non-hosted district deployments are documented; native iOS apps and an Android Aeries Mobile Portal app. No current desktop client was verified. [5] [6] [7] |
| Primary segments | U.S. K-12 public school districts, local education agencies (LEAs), schools, teachers, counselors, district staff, parents, and students; strongest presence in California and growing Texas usage. [4] [5] |
| Market presence (schools, students, countries, with date of claim) | More than 750 districts/LEAs and about 1 in 2 California students according to Aeries’s home page, viewed November 24, 2026; its privacy center says more than 2.5 million students are managed each day. G2 describes Aeries as managing over 45% of California’s student population. U.S.-focused; no verified global-country count. [4] [8] [9] |
| Official website (full URL) | https://www.aeries.com/ |
| Product / features page (full URL) | https://www.aeries.com/aeries-sis/ |
| Documentation / help center (full URL) | https://support.aeries.com/support/home |
| Pricing page (full URL or No public pricing page) | No public pricing page; https://www.aeries.com/pricing/ resolves to general marketing content rather than prices. |
| Review ratings (G2, Capterra, App Store, Play Store with score, review count and date viewed) | G2: 4.1/5 from 35 reviews, last updated November 4, 2026; Capterra: 3.5/5 from 22 reviews, page updated January 7, 2026; Apple Aeries Mobile Portal: 1.5/5 from 25K ratings; Apple Aeries Teacher: 1.9/5 from 43 ratings; Apple Aeries EM2: 2.5/5 from 48 ratings; all app ratings viewed November 24, 2026. Google Play Mobile Portal showed 100K+ downloads but no score/review count in the opened localized listing. [10] [11] [12] [13] [14] |

### Overview

Aeries SIS is a K-12 student information system centered on student records, attendance, scheduling, gradebook/grade reporting, portals, state reporting, and district data operations. Its surrounding product family adds Aeries Online Enrollment, Aeries Enroll Path, Aeries Analytics, Aeries Communications powered by ParentSquare, Aeries Payments, JumpRope, and ActivityHero. It is designed for district-wide data governance, school operations, teacher workflows, family access, and state compliance. [4] [5]

Aeries is particularly important in California because its data model and support content track CALPADS, CAASPP, Civil Rights Data Collection, college-readiness indicators, and other state workflows. It also has Texas PEIMS/TSDS and assessment content, with official customer examples including a Texas ISD. [4] [15] The company traces its present identity to 1995 and was formerly associated with Eagle Software. In 2025, Francisco Partners made a growth investment; Aeries stated that it remained family-operated. [1] [2]

### Platform Classification Explained

**Browser and cloud.** Aeries provides a web-based SIS and portals. Its hosted offering runs on Amazon Web Services, with monitoring, encryption, firewalls, secure transfer protocols, backups, redundancy, and rollback recovery described on the SIS page. [5] The API documentation also explicitly distinguishes districts hosted by Aeries from districts that host their own installations, so the most accurate classification is cloud SaaS plus a hybrid/self-hosted option rather than cloud-only. [6]

**Self-hosted and desktop.** The API documentation says self-hosted customers are responsible for some deployment choices, including HTTPS, and that each customer has an independent Aeries website. This confirms a non-hosted/self-hosted deployment path. I found no current evidence of a separate Windows/macOS desktop client; the former Eagle/Aeries CS desktop history is not a current product mode in the reviewed materials. [6]

**Native mobile applications.** The named apps are **Aeries Mobile Portal** for parents and students, **Aeries Teacher** for teacher attendance and gradebook work, and **Aeries EM2** (Emergency Management App Version 2) for school-site personnel and offline emergency access. Apple listings verify all three iOS apps. The official support article and Google Play listing verify Aeries Mobile Portal for iOS and Android. Mobile Portal covers grades, attendance, report cards, contacts, demographics, payments, state test scores, notifications, Communications, and supplemental-attendance check-in; full portal functions can open in the phone browser. [7] [12] [13] [14]

### Complete Feature Inventory

#### Admissions and enrollment

Aeries Online Enrollment provides a multilingual, survey-style registration flow, configurable questions, editable pages, sibling-based reuse, save-and-return processing, direct synchronization into Aeries, and reduced manual entry. It supports English, Spanish, Vietnamese, Korean, and Farsi. Aeries Enroll Path adds customizable forms, dashboards, role-based access, audit logs, document uploads, and workflow-style enrollment management. [16] The guide’s paperless multi-student-registration lead is directionally correct, but audit-log details are documented for Enroll Path rather than clearly for Online Enrollment itself.

#### Student information and records

The core SIS stores demographics, addresses and address history, contacts, identifiers, languages, enrollment history, programs, activities and awards, student documents, custom fields/tables, student groups, college/career pathway data, work permits, foster-care records, 504 records, and health-related fields. Its REST API exposes student, staff, program, discipline, test, fee, immunization, medical-insurance, and supplemental-data endpoints. [17] [18]

#### Attendance

Attendance includes daily and class/flexible-period attendance, absence codes, attendance history and summaries, tardies, attendance notes, supplemental-attendance sessions, attendance notifications, attendance logs, Texas attendance-reporting data, and teacher attendance submission. Mobile Portal supports attendance viewing and QR-code supplemental-attendance check-in. [7] [17]

#### Timetable and master scheduling

The scheduling model includes courses, sections, course requests and alternate requests, prerequisites, bell schedules, calendars, tracks, master-schedule data, flexible scheduling, class rosters, section staff, and scheduling wait lists. Teacher and student/parent portals expose relevant class and course-request views. [18] [19]

#### Gradebook, assessment and examinations

Teacher Gradebook supports gradebooks, assignments, assignment types, grading scales, standards-based scores, gradebook terms, scores, backups, transfer scores, custom marks, dashboards, and parent/student visibility. The API supports gradebook and student-grade endpoints. Aeries also maintains exams, exam sections, questions, versions, response data, scoring rules, test administration, state test scores, college test scores, and assessment imports. [18] [20]

#### Report cards, transcripts and graduation

Grade reporting covers marking periods, report-card marks, GPA calculation, grade-report history, report-card printing, standards-based grades, grade snapshots, transcripts, course history, transcript requests, graduation requirements, graduation status summaries, endorsements, pathways, and college entrance requirements. [18] [21]

#### Learning management and homework

Aeries is not presented as a full native LMS or homework platform. It provides gradebook/class tools and integrates with Google Classroom, Canvas, Schoology, HMH, IXL, Renaissance, and other learning products through the ecosystem. The evidence supports interoperability with LMSs, not a bundled Aeries course-content, assignment-delivery, or homework engine. [20] [22]

#### Communication

Aeries Communications, powered by ParentSquare, supports emergency/general messaging, two-way communication, surveys, polls, forms, permission slips, mass notifications, classroom communication, engagement reporting, and automatic translation. Channels include email, voice, SMS text, social, websites, and in-app notifications. A customer statement cites more than 100 languages. WhatsApp was not verified. [23]

#### Parent, student and teacher portals

Parent and Student Portals support account creation and management, portal-group permissions, grades, gradebook, attendance, scheduling, contacts, translations, data confirmation/summer re-registration, digital signatures, document requests, alerts, and weekly progress emails. The Teacher Portal includes attendance and gradebook. Portal usage logs and field-level security controls are documented. [19]

#### Fees, billing, payments and fundraising

Aeries Payments (formerly Aeries Financials) processes fees, fines, tuition, debit/credit transactions, monthly payment schedules, online stores, and district-controlled crowdfunding campaigns. It reports transactions, arrears, donor/campaign statistics, and financial statements. The current page names PayPal and Stripe as processors. The guide’s budgeting/accounting wording is broader than the verified emphasis on payments, tuition, stores, and fundraising. [24]

#### Health and medical

The data model includes health problems/notes, immunizations, medical insurance, dental records, health tests, and medical/health/student-wellness support content. EM2 exposes medical information to authorized school personnel and can cache it for offline emergency use. [14] [17]

#### Behavior, discipline and pastoral/counseling care

Aeries includes discipline and assertive-discipline records, offenses and dispositions, expulsions, behavioral emergency reports, discipline notifications, counselor conferences/notes, at-risk indicators, interventions, student wellbeing fields, and career/academic planning. These are records and intervention-management capabilities, not a marketed standalone pastoral-care suite. [17] [18]

#### Special education, 504 and safeguarding

The data model contains special-education demographics, disability services, infant services, student services, alternate assessments, suspensions, secondary transition, preschool outcomes, 504 plans/accommodations, foster-care legal cases, placements, education rights holders, meetings, goals, hearings, and notes. It also supports data permissions and red-flag indicators. The reviewed sources do not claim a separate child-safeguarding case-management product. [18]

#### Inventory, assets and resource management

Aeries’s data model includes district resource titles, items, course assignments, checkout assignments, documents, and custom tables. The ecosystem integrates with GreenLight Locker and other resource/asset products. This is narrower than a full standalone procurement and asset-management suite. [18] [22]

#### Analytics, dashboards and reporting

Aeries Analytics provides ready-to-use and custom dashboards, interactive drill-down charts, dynamic student groups, indicators, permissions, exports to Excel, and early-warning monitoring. Indicators can use grades, discipline, interventions, college-admission requirements, attendance, program participation, and other data. The published LCAP example includes 25+ dashboards, 50+ charts, 100+ indicators, and subgroup analysis. Robust queries, custom reports, ad-hoc reporting, and state/federal extracts are core strengths. [25]

#### Government/state reporting and compliance

The product has deep California CALPADS and assessment/reporting support, including CAASPP, CTE, college/career indicators, CRDC, Civil Rights calculations, and physical-fitness extracts. Texas support covers PEIMS/TSDS, Texas attendance reporting, STAAR/TELPAS-related imports and regulatory changes. Documentation is release-driven, with current 2026/27 CALPADS and Texas regulatory notes. [15]

#### Mobile apps

Aeries Mobile Portal is the family/student app; Aeries Teacher is the staff app for attendance, lunch count, assignments, grades, imports/exports, class tools, and Communications; Aeries EM2 is an authorized school-personnel emergency/offline app for student, contact, discipline, medical, class, and attendance information. Ratings indicate that functional breadth does not equal consistent mobile reliability. [12] [13] [14]

#### Integrations and APIs

The Aeries Ecosystem lists Ed-Fi, Clever, ClassLink/OneSync, Google and Google Classroom, Microsoft, Canvas, Schoology, ParentSquare, Follett Destiny, Frontline, Renaissance, MySchoolBucks, SchoolCash, nutrition systems, transportation providers, safety tools, and many other partners. The REST API is version 5, outputs JSON or XML, supports SSO, and exposes student, staff, scheduling, gradebook, attendance, grades, transcripts, fees, medical, discipline, and reporting-related endpoints. Updates are restricted to selected datasets and require district-issued certificates and permissions. [22] [26]

#### Security and privacy

Aeries states that AWS hosting uses encryption, firewalls, secure transfer protocols, monitoring, regular backups, redundancy, and disaster recovery. The June 18, 2026 privacy policy defines Aeries as a school official/service provider under district control, prohibits selling student PII, limits processing to contracted educational purposes, and provides return or secure destruction on termination. [5] [27]

There is no publicly documented native hostel/boarding, transport-management, payroll/HR, alumni-management, or university administration module. Transport, HR, library, nutrition, and LMS functionality is primarily represented by ecosystem integrations, not by Aeries-native modules. No production generative-AI assistant was found in the reviewed materials.

### Advanced and Distinctive Features

- California-first compliance depth: current CALPADS, CAASPP, CRDC, and Texas PEIMS/TSDS support is maintained in the public release/support system. [15]
- Early-warning analytics: Aeries Analytics creates indicators, dynamic groups, drill-down dashboards, and intervention/supplemental-attendance records for at-risk students. [25]
- No-code enrollment configuration: Online Enrollment and Enroll Path let districts configure questions, pages, forms, documents, permissions, and audit-oriented workflows without building a separate application. [16]
- Interoperability as a product strategy: Aeries maintains a large integration lineup and a documented REST API rather than forcing every district workflow into a single suite. [22] [26]
- District-controlled family communications: ParentSquare-powered messaging unifies email, voice, SMS, web, social, in-app notifications, translation, surveys, and permission slips. [23]
- Offline emergency access: EM2 caches authorized student, contact, discipline, medical, class, and attendance records for situations without network access. [14]
- California-scale student data operations: the vendor reports more than 2.5 million students managed daily and more than 750 districts/LEAs. [4] [8]

### Pricing Details

Aeries publishes no official prices, tiers, per-student rate, implementation fee, or setup fee. The official pricing URL reviewed did not present a pricing schedule, and both G2 and Capterra direct buyers to contact the vendor; Capterra explicitly says no free trial and no free version are available. [10] [11] The commercial model should therefore be treated as sales-led, district-level quoting for the core SIS and selected add-ons, with hosting, implementation, training, support, and integrations potentially scoped in the contract. No credible public third-party numeric range was found, so no estimate is supplied.

### Integrations, Standards and Interoperability

Aeries is a member of the Ed-Fi Alliance and says it adheres to Ed-Fi data standards. It also lists Clever, ClassLink, Google/Google Classroom, Microsoft, Canvas, Schoology, ParentSquare, Follett Destiny, MySchoolBucks, SchoolCash, nutrition, transport, HR, safety, assessment, and analytics partners. The API is REST-based, version 5, with JSON/XML output, SSO support, district-issued certificates, and endpoint-level permissions. OneRoster, LTI, SIF, and a public app marketplace were not verified; the ecosystem page is an integration catalog. [5] [22] [26]

### Security, Privacy and Compliance

AWS cloud documentation describes encryption, firewalls, secure transfer protocols, advanced monitoring, automatic backups, redundancy, and rollback recovery. The privacy center states that Aeries does not share student information with advertisers or marketers, does not own district-tracked data, and is compliant with FERPA, COPPA, HIPAA, SOPIPA, and California Education Code 49073.1. The June 18, 2026 policy adds school-official obligations, subprocessor controls, customer audit rights, and data return/destruction terms. [5] [8] [27]

Public materials reviewed did not verify SOC 2, ISO 27001, GDPR, India DPDP Act, or a specific AWS data-hosting region. Self-hosted customers make some security choices themselves, including HTTPS configuration, according to the API documentation. I found no publicly reported Aeries security incident in the reviewed official releases, support pages, or independent listings; that is not evidence that no incident has ever occurred. [6] [26]

### Strengths

- Exceptional California state-reporting and data-model depth, with growing Texas regulatory coverage.
- Broad K-12 operational coverage around student records, attendance, scheduling, gradebook, grade reporting, portals, analytics, enrollment, communications, and payments.
- Large reported installed base: more than 750 districts/LEAs and over 2.5 million students managed daily.
- Strong REST API and integration philosophy, with Ed-Fi, SSO, Clever, ClassLink, Google, Microsoft, LMS, assessment, nutrition, safety, and transportation connections.
- Flexible district configuration through custom fields/tables, dashboards, forms, permissions, portals, and reporting.
- AWS-hosted option plus a documented self-hosted path gives districts deployment flexibility.

### Weaknesses and Common User Complaints

- Usability is inconsistent. Capterra is 3.5/5 overall, with 3.4/5 ease of use, 3.0/5 value for money, and 2.7/5 customer service as of its January 7, 2026 update. [10]
- Capterra reviews report excessive clicks, clunky navigation, slow or frustrating workflows, difficult training materials, ticket-based support, and separate enrollment/admin portals that can require imports. [10]
- G2’s otherwise stronger 4.1/5 average still identifies gradebook complexity, hard-to-find options, confusing reports, and gaps in parent/teacher grade transfer as recurring issues. [11]
- Mobile experience is a major risk: Apple ratings were 1.5/5 for Mobile Portal, 1.9/5 for Aeries Teacher, and 2.5/5 for EM2, with reviews citing crashes, login failures, loading errors, locked attendance, and limited in-app functionality. [12] [13] [14]
- The product is U.S.-centric and especially California-oriented; there is no verified international-country footprint or higher-education feature set.
- Several enterprise functions are ecosystem integrations rather than native modules, so total cost, implementation effort, and data-governance complexity can rise across partners.
- No public pricing makes competitive budgeting difficult, and no production AI assistant was verified.

### Key Milestones

- **1972:** The guide claims an Aeries founder created an early SIS in this year; I found no primary-source confirmation, so it remains unverified.
- **1995:** Aeries Software’s current site and app materials identify 1995 as the company/copyright origin. [4]
- **2014:** Aeries API documentation records the original public API release and SSO release in its revision history. [26]
- **2015–2017:** API additions expanded student programs, test scores, enrollment history, transcripts, graduation requirements, report cards, fees/fines, discipline, scheduling, and gradebook coverage. [26]
- **2020:** API versions were consolidated toward v5, adding flexible scheduling support and broader endpoint coverage. [26]
- **2025:** Aeries announced a growth investment from Francisco Partners while stating that the company remained family-operated. [1] [2]
- **2026:** Aeries materials show ongoing CALPADS, Texas regulatory, CRDC, mobile, enrollment, API, privacy, and product-release activity; the current privacy policy took effect June 18, 2026. [15] [27]

### References

1. A Message from CEO and President Brent Lloyd - https://aeries.com/welcome-2025/
2. Aeries Software LinkedIn company profile - https://www.linkedin.com/company/aeries-software
3. Aeries Mobile Portal Google Play listing - https://play.google.com/store/apps/details?id=com.aeries.mobile.psp
4. Aeries Software official home page - https://www.aeries.com/
5. Aeries SIS product page - https://www.aeries.com/aeries-sis/
6. Aeries API Full Documentation - https://support.aeries.com/support/solutions/articles/14000077926-aeries-api-full-documentation
7. Aeries Mobile Portal App overview - https://support.aeries.com/support/solutions/articles/14000070433-aeries-mobile-portal-app-overview
8. Aeries Privacy Center - https://www.aeries.com/privacy-center/
9. Aeries SIS G2 product details and reviews - https://www.g2.com/products/aeries-sis/reviews
10. Aeries SIS Capterra review and pricing listing - https://www.capterra.com/p/5544/Aeries/
11. Aeries SIS G2 reviews - https://www.g2.com/products/aeries-sis/reviews
12. Aeries Mobile Portal Apple App Store listing - https://apps.apple.com/us/app/aeries-mobile-portal/id1261483635
13. Aeries Teacher Apple App Store listing - https://apps.apple.com/us/app/aeries-teacher/id1479356035
14. Aeries EM2 Apple App Store listing - https://apps.apple.com/us/app/aeries-em2/id1188123025
15. Aeries Support home and state-reporting release/support categories - https://support.aeries.com/
16. Aeries Online Enrollment product page - https://www.aeries.com/aeries-sis/aeries-online-enrollment/
17. Aeries API student-related endpoints - https://support.aeries.com/support/solutions/articles/14000113683-aeries-api-student-related-end-points
18. Aeries Table Names and Descriptions - https://support.aeries.com/support/solutions/articles/14000075603-aeries-table-names-and-descriptions
19. Parent and Student Portals support category - https://support.aeries.com/support/solutions/14000072540
20. Aeries API Full Documentation, gradebook and assessment endpoint history - https://support.aeries.com/support/solutions/articles/14000077926-aeries-api-full-documentation
21. Aeries Support knowledge base - https://support.aeries.com/support/solutions
22. Aeries Ecosystem integration lineup - https://www.aeries.com/aeries-sis/aeries-ecosystem/
23. Aeries Communications product page - https://www.aeries.com/aeries-sis/aeries-communications/
24. Aeries Payments product page - https://www.aeries.com/aeries-sis/payments/
25. Aeries Analytics product page - https://www.aeries.com/aeries-sis/aeries-analytics/
26. Aeries API Full Documentation and revision history - https://support.aeries.com/support/solutions/articles/14000077926-aeries-api-full-documentation
27. Aeries Privacy Policy, effective June 18, 2026 - https://www.aeries.com/privacy-policy/
