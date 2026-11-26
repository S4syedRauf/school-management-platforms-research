# Global #25 (evaluated). Gibbon (GibbonEdu)

| Field | Detail |
|---|---|
| Vendor / owner | Gibbon Foundation (non-profit overseer; copyright of the codebase transferred from Ross Parker in 2023); extended commercial services are offered by Gibbon Education Limited. Founded by Ross Parker. [2] [3] |
| Headquarters | Hong Kong origin: founded at International College Hong Kong; a separately stated legal headquarters for the Foundation is not publicly disclosed. [2] [13] |
| Company founded (year) | 2010 for the Gibbon project; the Gibbon Foundation was established in 2023. No separate vendor-company founding year is published. [2] [3] |
| Product first launched (year or Not publicly disclosed) | 2010: Gibbon says it was founded in October 2010; the founder’s independent project history records seven versions by December 2013. [2] [13] |
| Platform classification (Cloud SaaS / Web-based / Desktop / Mobile iOS+Android / On-premise / Hybrid) | Web-based, open-source, self-hosted/on-premise; can run on a school server, shared hosting, or cloud server. Responsive/mobile-friendly web interface in recent versions; no official native iOS or Android app found. [5] [6] [14] |
| Primary segments | International, public, home, refugee, primary and secondary schools; also colleges and schools supporting higher-education applications. [1] [4] [8] [13] |
| Market presence (schools, students, countries, with date of claim) | Official pages say Gibbon is used by schools worldwide and provide a voluntary school map, but publish no verified institution, student, or country count. The core is currently described as available in 26 actively translated languages (site checked 24 November 2026); v30 release notes separately reported 29 languages, so language counts vary by page/version. [1] [2] [14] |
| Official website (full URL) | https://gibbonedu.org/ |
| Product / features page (full URL) | https://gibbonedu.org/features/ |
| Documentation / help center (full URL) | https://docs.gibbonedu.org/ |
| Pricing page (full URL or No public pricing page) | https://gibbonedu.com/ |
| Review ratings (G2, Capterra, App Store, Play Store with score, review count and date viewed) | G2: 3.5/5 from 1 review, page updated 17 November 2026; Capterra: 4.5/5 from 2 reviews, last updated 21 July 2026 (ease of use 3.5/5, support 3.5/5, value 4.5/5). No official Gibbon iOS or Android app was found, so App Store/Play Store ratings are not applicable. [11] [12] |

### Overview

Gibbon is a free, GPL-3.0, teacher-created school information and learning platform. It brings student records, lesson planning, homework, assessment, attendance, timetables, communication, library, activities and school finance into one browser application. Teachers, students, parents and administrators use the same installation, with permissions controlling what each role can see and do. [1] [4] [10]

The project began at International College Hong Kong in October 2010. Ross Parker describes building it after finding existing systems too rigid and poorly suited to international/IB-school workflows; the early project grew from a prior system called Muse. In 2023, copyright moved from Parker to the non-profit Gibbon Foundation. Gibbon Education Limited separately sells support, server management, certification and Catalyst. [2] [3] [13]

Gibbon is a self-hosted alternative to SaaS MIS products, but the school owns the infrastructure and operational responsibility. Official materials provide a global-use map but no independently audited adoption totals. [1] [5]

### Platform Classification Explained

* **Browser access:** Gibbon is a PHP, CSS and JavaScript web application using MySQL. Users access the installation through a domain or server URL in a browser. [5] [6]
* **Cloud hosting:** Cloud is an infrastructure choice, not a Gibbon SaaS service. Schools may use a VPS, shared host or cloud server; Gibbon Education Limited can provision and maintain virtual servers as a paid service. [5] [9]
* **Desktop client:** None identified. The product is a server-hosted web application, not a Windows/macOS desktop package. [5]
* **On-premise/self-hosted:** Explicitly supported through Apache 2 or Nginx, PHP and MySQL 8 or compatible MariaDB. [5] [6]
* **Native mobile apps:** No official “Gibbon” iOS or Android app is listed; the current approach is responsive web access. [8] [12] [13]

### Complete Feature Inventory

#### Planner and learning management

Planner supports Smart Blocks, rich multimedia lesson plans, units, curriculum outcomes, homework assignment, online work collection, attendance within a lesson, notes and teacher feedback. It can expose lessons to students, parents and guests. The Resources database catalogs school-wide materials by category, purpose, tags and year group; Departments organize Learning Areas, scope and sequence, and shared documents. [4]

#### Student information and records

Students consolidates profiles, family links, academic, behavioral, medical and SEN alerts, photographs and a Fast Student Finder. User Admin handles families, enrolment, medical data and updates. Form Groups organize tutor/tutee relationships. Data Updater routes staff and parent personal or medical changes into an administrator review queue. [4]

#### Admissions and enrollment

Application Form provides public online applications, priority-based queues, accept/reject decisions, automatic user-account creation and family links for accepted students. Class Enrolment, an extension, lets parents enroll children into classes; Course Selection supports student course choices and can feed a timetable engine. [4] [8]

#### Attendance

Attendance can be taken for form groups or individual students, with recent/full history, future absences, parent visibility and emergency-evacuation absence reports. Lesson Planner attendance can be compared with school attendance. Activities can generate attendee lists and printable registers. [4]

#### Timetable and master scheduling

Timetable displays individual student and teacher schedules, room location and room telephone information. Timetable Admin defines courses, classes and enrolment, while facilities can be booked. Google Calendar events can overlay school and personal calendars. v29/v30 releases added a redesigned timetable and further timetable improvements. [4] [14]

#### Gradebook, assessment and examinations

Markbook records continuous academic data across subjects, exposes selected results to students and parents, and links to Planner submissions. Teachers can return marked work, rubrics and voice recordings. Rubrics track outcomes over time. Formal Assessment captures internal/external tests, includes CATS by default, supports additional tests and can calculate value-added scores. Crowd Assessment enables peer review and discussion. There is no documented enterprise examination-office suite. [4]

#### Report cards and transcripts

The current core feature catalog emphasizes Markbook, Tracking and Formal Assessment rather than a separately named report-card/transcript module. Tracking graphs data by student or cohort and exports selected assessment data to a spreadsheet. The open-source Mastery Transcript extension can create, track and issue credits with an evidenced portfolio; it is an extension, not evidence of a universal core transcript engine. [4] [8]

#### Communication

Messenger sends targeted email, SMS or Message Wall communications to flexible groups such as classes, forms and activities. Messages can include links, files or HTML from the Resource Bank; the Message Wall can produce individualized daily bulletins. v28 added a mailing-list feature. No native WhatsApp or push-notification channel is documented. [4] [14]

#### Parent, student and teacher portals

There are role-based dashboards for parents, students and staff rather than separate commercial apps. Parents can view attendance, academic progress and calendars; students access lessons, homework, resources and assessment where permissions allow; teachers use planning, profiles, attendance and Markbook. The module framework supports Parent Dashboard, Student Dashboard and Staff Dashboard hooks. [1] [4] [19]

#### Fees, billing, payments and accounting

Finance manages fees, billing schedules and invoicees, and generates/emails invoices, receipts and payment reminders. It tracks payments, lists outstanding family balances, and manages expense requests through approval, payment and reimbursement. The official page does not document a general ledger, payroll accounting, card gateway catalogue or native online payment processor. [4] [20]

#### HR, staff and payroll

Staff supports job openings and applications, conversion of applicants into staff accounts, a staff directory, role-based detail visibility and contract tracking. Staff can update their own personal information through Data Updater. No native payroll, benefits, timekeeping or full HRIS module is listed in the current core feature catalog. [4]

#### Transport and trips

There is no native transport fleet, route, GPS or bus-payment module. Trip Planner supports trip planning and approvals; Activities handles applications, participant lists and off-site attendance registers. [4] [8]

#### Library

Library catalogs books, films, computers, cameras and other loanable items; manages loans and inventory; lets students browse items; and can share reading records with teachers. v29 also improved the Library view in Student Profile. [4] [14]

#### Hostel and boarding

No dedicated native hostel/dormitory or boarding module is documented in the current official core or extension catalog. Capterra’s feature summary does not list it; older user feedback mentioned “dorm” as a feature, so schools should verify whether that reflects an older add-on or local customization rather than current core. [8] [12]

#### Inventory and assets

Library can track and loan items such as computers and cameras, and Resources catalogs teaching materials. No organization-wide asset-register, depreciation or procurement module is documented. [4]

#### Health and medical

Medical information and alerts are part of student profiles, with parent/staff updates through Data Updater. Nurse workflows, immunization schedules and medication administration are not advertised. [2] [4]

#### Behavior, discipline and pastoral care

Behaviour records positive and negative notes, school-defined descriptors and severity, comments, follow-up, form-group summaries and profile alerts. Student Alerts was added as a v30 core module, and v30 introduced a Pastoral heading. House Points is an extension for tracking house awards; Badges supports academic, social and athletic awards. [4] [8] [14]

#### Special education and safeguarding

Individual Needs supports designated learning needs, individual education plans, longitudinal archiving, Planner integration and differentiation indicators. SEN alerts are included in Student Profiles. Gibbon does not publicly claim a dedicated safeguarding case-management, statutory child-protection or formal IEP compliance suite. [4]

#### Alumni and fundraising

The Alumni extension accepts alumni registrations and links them to existing user accounts. There is no native fundraising, donor CRM, campaign, gift-processing or advancement module listed. [8]

#### Analytics, dashboards and reporting

Tracking graphs Markbook and Formal Assessment data for individuals and cohorts and exports selected data for offline analysis. Query Builder creates/runs SQL statements and exports results to Excel; the Catalyst license unlocks 151 maintained queries and 31 commands. Role-based dashboards and Fast Finder provide operational views, but there is no advertised warehouse, predictive analytics layer or executive BI product. [4] [8] [9]

#### AI features

No production AI assistant, generative AI, predictive model or AI writing/reporting feature is documented on the official website, documentation, extensions page or current release notes. Schools can build custom modules, but that is development work, not a native AI capability. [4] [8] [19]

#### Government/state reporting and compliance

No dedicated state-census, Ed-Fi, SIF, OneRoster or government-reporting package is advertised. Query Builder and exports can support local reporting, but statutory mapping and submission remain a school responsibility unless a partner builds a custom module. [8] [19]

#### Mobile web experience

Recent releases replaced older front-end libraries with HTMX and Alpine.js and describe more app-like page loads; the official Extend page lists a responsive, mobile-friendly theme. [8] [14]

#### Integrations and APIs

Google integration supports OAuth-based single sign-on and Google Calendar API overlays. The Moodle module exposes Gibbon users and courses to Moodle through external-database authentication/enrollment and scheduled synchronization. Module hooks, database access, exports and custom PHP modules provide extensibility, but the public materials do not document a versioned REST API or developer marketplace. [17] [18] [19]

#### Security and privacy controls

Schools control data location because Gibbon is self-hosted. The documentation recommends HTTPS, SSH keys, restricted access and production server hardening. Role/action permissions, module enablement, update notifications, backups and a responsible-disclosure process are documented. Gibbon’s security policy says older versions are not directly supported and advises use of the latest stable release. [5] [7] [15]

### Advanced and Distinctive Features

* **Teacher-designed workflows:** The product originated inside a school and models planning, teaching and assessment. [13]
* **Role/action permission model:** Each module action can be assigned to roles, enabling granular configuration without changing core code. [19]
* **Module and theme extensibility:** Schools can install, update, uninstall or build modules and themes, with hooks into dashboards, Student Profile and Planner. [7] [8] [19]
* **Catalyst Query Builder:** A paid license supplies 151 maintained queries and 31 commands, while the free Query Builder supports SQL execution and Excel export. [8] [9]
* **Internationalization:** The project supports right-to-left text, UTF-8 and a volunteer translation system; the current homepage says 26 actively translated languages. [1] [2]
* **Self-hosted ownership:** Schools choose server, backups and data location. [5]
* **Open-source sustainability model:** The 2023 Foundation transfer separates non-profit core stewardship from optional paid support and hosting. [3]

### Pricing Details

The core Gibbon software is free to download and licensed under GNU GPL-3.0. Schools pay their own server, domain, backup, administration and implementation costs unless they contract for help. [5] [10]

The official Gibbon Education Limited page, checked 24 November 2026, lists a **Gibbon Catalyst License at USD $150 per installation for one year**. Multi-site discounts are automatically applied. Catalyst unlocks the Query Builder library of 151 useful queries and 31 commands. Server provisioning, installation, configuration, maintenance, contract support and ad hoc support are quote-based; no public hosting rate card or implementation fee is shown. [9]

### Integrations, Standards and Interoperability

Documented integrations are Google OAuth/SSO and Google Calendar API, and a Moodle module that syncs users and courses through Moodle’s external database authentication and enrollment functions. Gibbon’s module hooks and GPL source support custom connectors, CSV/spreadsheet import/export and local database integration. [17] [18] [19]

No public evidence was found for 1EdTech certification, OneRoster, LTI, Ed-Fi, SIF, Clever, ClassLink, Microsoft 365, WhatsApp, payment-gateway certification or an official public REST API; the extension page is a curated catalogue rather than a commercial integration marketplace.

### Security, Privacy and Compliance

Gibbon publishes no SOC 2, ISO 27001, FERPA, COPPA, GDPR or India DPDP Act certification claim. Self-hosting can help a school meet data-residency and privacy obligations, but compliance depends on configuration, contracts, access controls, backups, subprocessors and local law. [5] [15]

The security policy provides responsible disclosure guidance, supports the current stable version and uses a six-month release cycle, with mid-version patches for high-severity issues. NIST’s NVD lists nine Gibbon CVE records through 27 May 2025, including CSRF, XSS, PHP deserialization, server-side template injection, directory traversal, arbitrary file write and session-fixation issues affecting older versions. [15] [16]

The v30.0.02 and v30.0.03 GitHub releases in November 2026 were explicitly marked essential security updates. The v30.0.03 notice says Gibbon had no known data breach, credits responsible-disclosure researchers and advises PHP 8.2+ preparation for the next patch. [14]

### Strengths

* Free GPL-3.0 core removes license and per-student fees and permits modification and self-hosting. [1] [10]
* Strong teacher-centric breadth across planning, homework, assessment, attendance, communication and timetables. [4] [13]
* Granular permissions, multilingual support and extensible modules suit international and resource-constrained schools. [1] [19]
* Schools retain control of data location, backups and upgrade cadence rather than being locked into a SaaS tenancy. [5]
* A Foundation, active GitHub development and paid support ecosystem support ongoing maintenance. [3] [8] [14]

### Weaknesses and Common User Complaints

* Adoption scale is not publicly quantified; the official map is voluntary. [1]
* Self-hosting transfers installation, hardening, backups, upgrades and monitoring to the school; documentation says an administrator is normally required. [5]
* There is no native iOS/Android app, no documented push or WhatsApp channel, and no public evidence of a full state-reporting or standards-certified interoperability layer. [8] [13]
* Current core documentation does not show payroll, transport fleet, hostel, fundraising, enterprise asset management or dedicated report-card/transcript operations. [4] [8]
* Independent review evidence is thin. G2 has one review (3.5/5), whose reviewer praised usability/UX but reported that the system was slow and “somewhat frozen.” [11]
* Capterra’s two reviews average 4.5/5 for overall value, but the weaker sub-scores are ease of use 3.5/5 and customer service 3.5/5. One reviewer said learning it was somewhat difficult; another said the frontend, finance workflow and mobile experience could be improved. [12]
* Security maintenance requires discipline: NIST records vulnerabilities in older versions, and November 2026 notices called for essential patching. [14] [16]

### Key Milestones

* **2010:** Ross Parker founded Gibbon in October at International College Hong Kong after finding existing school systems too rigid and difficult to use. [2] [13]
* **2013:** The public project history recorded v7.1.00, the seventh version, released in December. [13]
* **2014:** An independent project history described 24 core modules, five free add-ons and active use at Parker’s college and partner school. [13]
* **2023:** The Gibbon Foundation was established; copyright of the codebase transferred from Parker to the Foundation. [3]
* **2024:** v28 refreshed the front end with HTMX and Alpine.js, added Activities registration and mailing lists, and moved core-module ownership visibly to the Foundation. [14]
* **2025:** v29 redesigned the timetable, improved Student Profile library views, added Petty Cash and Behaviour observations, and strengthened CSRF/nonce handling. [14]
* **2025–2026:** Foundation-maintained extensions expanded, including Alumni, Query Builder, Trip Planner, Higher Education and Flexible Learning. [8]
* **20 November 2026:** v30.0.00 marked 15 years of development, added Calendar and Student Alerts as core modules and reported 29 production languages in its release notes. [14]
* **13–18 November 2026:** v30.0.02 and v30.0.03 were released as essential security updates; the latter said v31 work was paused while security work continued. [14]

### References

1. Gibbon official homepage - https://gibbonedu.org/
2. Gibbon About and Foundation page - https://gibbonedu.org/about/
3. Gibbon Documentation Welcome and Foundation history - https://docs.gibbonedu.org/get-started/welcome
4. Gibbon official feature inventory - https://gibbonedu.org/features/
5. Gibbon system requirements and self-hosting model - https://docs.gibbonedu.org/reference/system-requirements
6. Gibbon installation guide - https://docs.gibbonedu.org/guides/install/installing-gibbon
7. Gibbon documentation: Managing Modules - https://docs.gibbonedu.org/guides/administration/modules
8. Gibbon official Extend catalogue - https://gibbonedu.org/extend/
9. Gibbon Education Limited services and Catalyst pricing - https://gibbonedu.com/
10. GibbonEdu core GitHub repository and GPL-3.0 license - https://github.com/GibbonEdu/core
11. G2 Gibbon reviews - https://www.g2.com/products/gibbon/reviews
12. Capterra Gibbon Software review - https://www.capterra.com/p/164210/Gibbon/
13. OpenSource.com: In search of a flexible, open education management system - https://opensource.com/education/14/2/gibbon-project-story
14. GibbonEdu core GitHub releases - https://github.com/GibbonEdu/core/releases
15. GibbonEdu core security policy - https://github.com/GibbonEdu/core/security/policy
16. NIST National Vulnerability Database Gibbon search results - https://nvd.nist.gov/vuln/search?resultType=records&cpeFilterMode=cpe&cpeName=cpe:2.3:a:gibbonedu:gibbon:8.2.00:*:*:*:*:*:*:*
17. Gibbon documentation: Connecting to Moodle - https://docs.gibbonedu.org/tutorials/configuring-gibbon/integrations/connecting-to-moodle
18. Gibbon documentation: Google Integration - https://docs.gibbonedu.org/tutorials/configuring-gibbon/integrations/google-integration
19. Gibbon documentation: Module Development - https://docs.gibbonedu.org/explanation/development/module-development
20. Gibbon official Finance feature page - https://gibbonedu.org/features/other/finance/
