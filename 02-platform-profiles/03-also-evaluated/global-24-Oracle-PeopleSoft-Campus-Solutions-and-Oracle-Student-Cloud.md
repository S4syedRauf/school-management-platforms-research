# Global #24 (evaluated). Oracle PeopleSoft Campus Solutions and Oracle Student Cloud (Oracle)

| Field | Detail |
|---|---|
| Vendor / owner | Oracle Corporation |
| Headquarters | Redwood Shores, California, United States [1] |
| Company founded (year) | 1977 [1] |
| Product first launched (year or Not publicly disclosed) | Oracle Student Cloud was announced in 2014, with first-phase release planned for 2015; the original Campus Solutions product-line launch year is not publicly disclosed in the reviewed Oracle material (Campus Solutions 9.0 was reported as released in December 2006) [10] |
| Platform classification (Cloud SaaS / Web-based / Desktop / Mobile iOS+Android / On-premise / Hybrid) | Hybrid portfolio: PeopleSoft Campus Solutions is a web-based, on-premise or customer-hosted/IaaS deployment; Oracle Student Management and Student Financial Planning are Oracle Fusion Cloud SaaS; responsive browser/mobile access and a legacy Campus Mobile app are available [2] [5] [12] |
| Primary segments | Colleges, universities, community colleges, continuing-education providers, professional/graduate education, and institutions with complex or multi-entity academic models |
| Market presence (schools, students, countries, with date of claim) | Oracle's cloud-journey blueprint says more than 800 customers have used Campus Solutions over several decades (claim in the undated blueprint, accessed November 24, 2026); Oracle's 2022 release named Bowie State (6,000+ students), Butler Community College (7,000 students), Coppin State, Skidmore, and University of Pittsburgh as higher-education cloud customers [5] [11] |
| Official website (full URL) | https://www.oracle.com/government/education/higher-education/ |
| Product / features page (full URL) | https://www.oracle.com/government/education/higher-education/student-cloud/ |
| Documentation / help center (full URL) | https://docs.oracle.com/en/applications/peoplesoft/campus-solutions/index.html |
| Pricing page (full URL or No public pricing page) | No public pricing page; Oracle publishes list-price PDFs and sells through enterprise quotation/contracting |
| Review ratings (G2, Capterra, App Store, Play Store with score, review count and date viewed) | G2 PeopleSoft Campus Solutions: 3.7/5 from 91 reviews, page updated November 4, 2026; Capterra Oracle PeopleSoft: 4.1/5 from 283 reviews, last updated September 29, 2026; Gartner Peer Insights PeopleSoft Campus Solutions: 3.7/5 from 16 ratings, updated/viewed November 24, 2026; Apple App Store Oracle Fusion Applications: 3.7/5 from 452 ratings, viewed November 24, 2026; no verified Google Play rating for a dedicated Student app found [6] [7] [8] [20] |

### Overview

Oracle's higher-education portfolio deliberately combines two different generations of student technology. PeopleSoft Campus Solutions 9.2 is the mature, deeply configurable student information system (SIS) for recruitment, admissions, academic records, advising, financial aid, student accounts, advancement, and self-service. It can remain on premises or be moved to Oracle Cloud Infrastructure (OCI) as hosted infrastructure. Oracle Student (also called Oracle Student Cloud or Fusion Cloud Student) is the cloud-native direction: Oracle Student Management for admissions, academics, advising, and student financials, plus Oracle Student Financial Planning (SFP) for financial aid [2] [5].

The distinction matters. Campus Solutions gives institutions direct access to code, database tables, and the PeopleSoft Integration Broker, while Student Management is SaaS with configuration, APIs, and Oracle-managed updates rather than customer-owned code. Oracle's 2026 strategy is coexistence rather than a forced migration: PeopleSoft support is rolling ten years through at least 2037, and Oracle Student is intended to earn adoption over time [2] [9]. Oracle acquired PeopleSoft in 2005 for approximately $10.3 billion, preserving a major enterprise-application installed base [1] [17].

### Platform Classification Explained

**Browser/web:** Campus Solutions is delivered through PeopleSoft's web and Fluid UI. The Student Homepage is a browser self-service hub for academic progress, records, finances, financial aid, classes, profile, and tasks; the same Fluid home appears when users sign in on a mobile device [13].

**Cloud hosting:** PeopleSoft may run on an institution's infrastructure, an Oracle implementation partner's infrastructure, or OCI. Oracle's own positioning says PeopleSoft can run on premises or in the cloud; OCI is an IaaS hosting option, not the same thing as SaaS [2] [5]. Oracle Student Management and SFP are natively hosted Fusion Cloud SaaS services on Oracle infrastructure. The current Fusion service description measures Student Management by Hosted FTE Student, Student Aid Eligibility by Student Aid Applicant, and SFP by Student Aid Recipient [19].

**Desktop client:** No separate end-user desktop application is required or documented. Administration is web-based; legacy implementation tools and local integration infrastructure may still exist in a customer-managed PeopleSoft deployment.

**Native mobile:** Campus Solutions documentation names **Campus Mobile**, built on Oracle ADF Mobile, with deployment to Android APK and iOS IPA. It supports student-facing mobile functions such as enrollment, schedules, grades, notifications, and progress, subject to licensing and configuration [12] [20]. The newer default is responsive Fluid web rather than a dedicated student-store app. Oracle Fusion Applications is a general native iOS/iPadOS app with 3.7/5 from 452 ratings, but the listing is primarily HCM/ERP and says available mobile flows depend on licensed and implemented applications; it is not evidence of a standalone Oracle Student parent/teacher app [20].

### Complete Feature Inventory

#### Campus Community, identity, and constituent data

The shared person/organization layer stores names, addresses, IDs, demographics, languages, ethnicity, religious preferences, health and identification attributes, participation data, FERPA controls, emergency contacts, and organization data. It includes U.S. SEVIS F/M and J-1 visa processing with DHS submissions/updates, plus the cross-portfolio “3Cs”: Communication Management, Checklist Management, and Comment Management [3] [4].

#### Recruiting, admissions, and enrollment management

Recruiting and Admissions captures requests for information, prospects, recruiters, regions, interests, events, communication plans, test data, transcripts, multiple applications, status history, program-specific requirements, automated evaluation, admission decisions, accept/decline, online deposit payment, Quick Enroll/Admit, and applicant self-service. Enrollment management sets hierarchical targets by institution, career, term, admit type, program, gender, and ethnicity and compares target versus actual enrollment [3] [4].

#### Student information and academic records

Student Records covers academic structure, course catalog, schedule of classes, student programs/plans/subplans, student activation, enrollment, repeat checking, transfer credit, student data tracking, attendance tracking, instructor workload, grades, academic statistics, enrollment verification, transcripts, graduation processing, and LMS integration [3] [4]. Oracle Student Management adds Curriculum Registry, multiple assessment types, credentials, structured learning paths, academic calendars, student results, sponsorships, and dynamic entities for consortia, multi-institution degrees, and exchanges [14].

#### Attendance, timetable, and examination scheduling

Attendance tracking is a delivered Student Records function. Schedule of Classes, meeting patterns, class search, class and exam schedules, enrollment appointments, instructor workload, and faculty schedules are supported. The reviewed documentation does not establish a separate automated master-scheduling engine; institutions can integrate specialist schedulers.

#### Grading, assessment, transcripts, and degree progress

PeopleSoft provides student grading, grade rosters, grade history, academic statistics, unofficial/official transcripts, enrollment verification, graduation application, and degree-progress reporting. Academic Advisement defines course lists, requirement groups, shared courses, exceptions, what-if scenarios, outstanding requirements, and advisement reports. Oracle Student adds configurable result sets and credentials; SFP adds a financial plan alongside academic choices [3] [13] [14] [15].

#### Learning management and homework

Campus Solutions does not present a full native LMS, homework workspace, or content-authoring product. It provides LMS integration and faculty links to LMS sites; homework, lessons, discussion, and content delivery require an external LMS [3] [4].

#### Communications and alerts

The 3Cs support targeted incoming/outgoing communications, checklists, comments, notes, due dates, status tracking, and constituent interactions across prospects, applicants, students, staff, alumni, donors, and organizations. Campus Mobile can reuse SMS or email notification; Oracle Student supports automated emails and alerts triggered by dates, actions, or events, while intelligent alerts surface academic and financial tasks. WhatsApp messaging is not documented as native [3] [14].

#### Student, faculty, applicant, and proxy portals

Campus Self Service provides applicant status and admission response; Student Center; Student Planner; enrollment shopping cart; add/drop/swap; class search; grades; transcripts; enrollment verification; graduation application; transfer-credit modeling; financial-aid award accept/decline; account inquiry; credit-card/eCheck payment profiles and payments; and Faculty Center access to rosters, grades, schedules, advisees, catalog, and LMS links. It also supports Community Directory, personal information, FERPA privacy, holds, checklists, and contributor-relations outreach. Oracle Student's Student Central provides personalized widgets, to-dos, applications, finances, academics, program links, and proxy/delegate access for a parent or other authorized person while preserving FERPA controls [4] [14].

#### Fees, billing, payments, and accounting

Student Financials calculates tuition and fees, maintains customer accounts, creates bills, supports payment plans, refunds, cashiering, collections, tax forms, and general-ledger interfaces. Self-service supports credit card and eCheck payments. Student Management extends this with pay-to-enroll, student accounts/invoicing, receipts, sponsorship credits, bills, invoices, learning packages, refunds, direct-bank payments, and population-based fee assessment; it depends on Oracle Financials for enterprise structures, General Ledger, Receivables, Payables, and Payments [3] [4] [14].

#### Financial aid

Campus Financial Aid processes applications, eligibility, need calculations, budgets, awards, packaging, disbursements, Direct Lending, FFELP, CommonLine/Common Record, Pell and Title IV, work-study, Canadian aid, and FISAP. Oracle SFP adds electronic document requests/submission, signatures, automated verification, C-code clearing, ISIR corrections, tailored cost of attendance, federal and non-federal packaging, configurable disbursement, COD/G5/CommonLine communication, credit-balance splitting, automated 10-step Return of Title IV, post-withdrawal and late disbursement, grant overpayment handling, real-time synchronization, and financial-aid analytics [3] [15].

#### Advancement, alumni, and fundraising

Contributor Relations includes constituent information, gifts and pledges, prospect management, events, campaigns, volunteers, memberships, planned giving, matching gifts, tribute/memorial gifts, acknowledgements, giving clubs, strategies, action plans, to-do lists, and outreach analysis. Alumni-facing self-service is included in the broader Campus Self Service audience, while recruiting/engagement/advancement marketing can be extended with Oracle CX [3] [4] [5].

#### Analytics, dashboards, and reporting

Delivered summary pages, enrollment-target reports, advisement reports, academic statistics, outreach reports, configurable queries, and PeopleSoft Insights/Pivot Grids support operational reporting. Oracle Student adds integrated dashboards and real-time insights for retention, recruitment, academic performance, and financial aid. This is strong enterprise reporting, but not a no-code report builder for nontechnical users [2] [5] [8].

#### AI and intelligent automation

Oracle Student markets proactive alerts, intelligent automation, automated financial-aid intervention, and predictive-style retention insights; SFP is marketed as self-correcting and able to automate up to 90% of the aid lifecycle [2] [15]. The June 2026 Quest roadmap says delivered AI agents will not be retrofitted directly into Campus Solutions; customers can use PeopleTools 8.63 MCP capabilities to build AI experiences. Thus, AI is more mature in the cloud direction than in the legacy SIS [9].

#### Government reporting and compliance workflows

Native compliance includes SEVIS/DHS visa processing, U.S. Department of Education financial-aid regulation updates, Direct Loan/Pell/COD, Title IV, FISAP, Canadian aid, and international legislative updates such as HESA, UCAS, TCSI/HEIMS, and other country-specific requirements in the roadmap [3] [5].

#### Integrations, APIs, and interoperability

PeopleSoft provides Integration Broker, web services, EDI Manager, LMS integration, Oracle Integration Cloud options, and delivered integration to SFP. The 2025 release made Campus Solutions the first SIS certified on 1EdTech Edu-API, initially provisioning persons, classes, programs, academic periods/sessions, organizations, and class enrollments for LMS, parking, housing, and other ecosystem applications [16]. Oracle Student Management has a public REST API with OAuth, JSON, batch actions, CORS, JWT, metadata, SOAP support, and hundreds of documented resource families [18].

#### Security, privacy, and accessibility

PeopleSoft supports role-based security, FERPA privacy controls, data masking/privacy frameworks, configurable security, and mobile service-operation security. Student Management uses abstract/job/data roles, LDAP synchronization, role mappings, access history, and Security Console controls [5] [17]. Oracle's cloud compliance catalogue lists ISO/IEC 27001/27017/27018/27701, SOC 1/2/3, PCI DSS and other frameworks, but warns that attestations are service- and region-specific; this should not be read as a product-specific certification without contract evidence [17]. Oracle pages reviewed did not provide a dedicated COPPA, India DPDP, or product-specific FERPA certification claim. No public product security incident was identified in the sources reviewed through November 24, 2026.

#### Modules not native to the reviewed product scope

There is no documented native transport routing, library, hostel/boarding, inventory/asset, behavior/discipline, pastoral-care, or special-education/safeguarding module. Health and medical data can be stored as Campus Community attributes, but this is not a clinical or school-nurse system. HR, staff, and payroll are separate PeopleSoft HCM/Oracle Cloud HCM products, not Campus Solutions modules [2] [3].

### Advanced and Distinctive Features

- **Two-speed modernization:** Institutions can retain customized Campus Solutions while adopting Oracle Student Financial Planning or OCI hosting incrementally rather than replacing the SIS in one “big bang” project [5].
- **1EdTech Edu-API certification:** The 2025 certification creates a standards-based path for exchanging person, class, program, term, organization, and enrollment data [16].
- **Dynamic entities:** Oracle Student can model systems, consortia, multi-institution degrees, and exchanges without re-implementing the student system [2] [14].
- **Highly automated financial aid:** SFP combines rule-based packaging, document automation, reconciliation, disbursement, and Return of Title IV workflows [15].
- **Configuration over customization:** Student Cloud's core frameworks let business users maintain rules and workflows; Campus Solutions supplies extensibility through PeopleTools, Fluid, Activity Guides, notification, search, and configuration frameworks [2] [5].
- **Lifelong-learning support:** Oracle Student spans traditional degrees, continuing education, non-credit programs, variable course lengths, credentials, and multiple academic models [2] [14].
- **FERPA-aware proxy access:** Delegates can complete selected transactions for a learner while the institution retains privacy control [2] [14].

### Pricing Details

There is no public Oracle pricing webpage with tiers, implementation bundles, or a standard SaaS quote. The official **PeopleSoft Component Global Price List dated June 11, 2026** lists Campus Solutions at **245** for the component license and **53.90** for software update and support, measured per **FTE Student**; the PDF table does not explicitly label a currency, so these are list-price figures rather than a guaranteed USD contract price. Oracle defines FTE Student as each full-time student plus each part-time student counted as 25% of an FTE [19].

Oracle's current Fusion service description is also unit-based, not a public rate card: Student Management is per Hosted FTE Student, Student Aid Eligibility per Student Aid Applicant, and Student Financial Planning per Student Aid Recipient, with separate test environments and optional services. Implementation, integration, data conversion, training, support level, OCI hosting, Oracle Financials/HCM/CX dependencies, and local tax/contract terms are quote-based [19]. G2 says pricing is unavailable; Gartner reports subscription pricing varies with users, modules, support, customization, integration, training, and implementation but gives no reliable numeric range [6] [8]. Checked November 24, 2026.

### Integrations, Standards and Interoperability

Campus Solutions supports PeopleSoft Integration Broker, REST/JSON and SOAP web services, EDI Manager, Oracle Integration Cloud, Oracle Financials/ERP/HCM/CX, Student Financial Planning, payment processing, and LMS links. Edu-API is the clearest verified open standard and was certified in 2025. Oracle Student Management documents public REST resources, OAuth, JWT, JSON, batch actions, CORS, metadata, and SOAP. The reviewed sources do not verify OneRoster, LTI certification, Ed-Fi, SIF, Clever, ClassLink, Google Workspace, Microsoft 365, or a dedicated marketplace; these should be treated as possible partner integrations rather than native certifications. Payment support is documented for credit cards, eCheck/direct bank payments, and Oracle Payments, but no named third-party gateway was verified [4] [16] [18].

### Security, Privacy and Compliance

Role- and data-based security, LDAP synchronization, Security Console, role mappings, access history, FERPA privacy flags, proxy access, and configurable mobile-service security are documented. Oracle's cloud compliance catalogue includes ISO 27001-family controls and SOC reports, but availability depends on service and region. PeopleSoft's strongest compliance coverage is operational: SEVIS/DHS, U.S. Department of Education aid rules, Title IV, Pell/COD, FISAP, Canadian aid, and international reporting. Oracle does not publicly publish a single Student Cloud data-hosting region list or a product-specific COPPA/DPDP certification on the reviewed pages; GDPR/DPDP suitability remains a customer/contract assessment. No publicly reported incident was found in this review set through November 24, 2026 [3] [5] [17].

### Strengths

- Unusually broad higher-education lifecycle coverage, including admissions, records, advising, aid, billing, advancement, and self-service.
- Mature academic and regulatory depth for large universities and multi-campus institutions.
- Extensive configuration/customization, integration, and data-model control in Campus Solutions.
- A credible incremental cloud route: OCI, SFP, Oracle Student, ERP, HCM, CX, and Edu-API can be adopted in stages.
- Strong financial-aid automation and complex-program support in Oracle Student Financial Planning.
- Long support horizon through at least 2037 reduces forced-migration risk [9].

### Weaknesses and Common User Complaints

G2 users praise breadth, reliability, customization, and centralization but report a steep learning curve, outdated-feeling interface, upgrade complexity, and integration difficulty; its overall rating was only 3.7/5 as viewed November 24, 2026 [6]. Capterra reviewers cite unintuitive navigation, slow or peak-load performance, costly/effort-heavy customization, glitches after upgrades, limited mobile ease, and dependence on specialist IT support [7]. Gartner reviewers like the integrated student lifecycle but say reporting is too technical for ordinary users and that navigation/training costs erode value [8]. The biggest strategic weakness is portfolio complexity: institutions must choose between maintaining a heavily customized legacy SIS and adopting a newer SaaS product that is still maturing, while HR, LMS, transport, library, housing, and safeguarding capabilities require separate systems.

### Key Milestones

- **1977:** Larry Ellison, Bob Miner, and Ed Oates found Software Development Laboratories, Oracle's predecessor [1].
- **1989:** Oracle moves headquarters to Redwood Shores, California [1].
- **2004:** Oracle announces a definitive agreement to buy PeopleSoft for approximately $10.3 billion [17].
- **2005:** Oracle completes the PeopleSoft acquisition and adds the PeopleSoft enterprise application portfolio [1] [17].
- **2006:** PeopleSoft Enterprise Campus Solutions 9.0 is reported as released in December 2006; Oracle Student Cloud had not yet been announced [10].
- **2013:** Oracle adds Campus Solutions mobile capabilities for enrollment, schedules, grades, notifications, and academic progress [20].
- **2014:** Oracle announces Oracle Student Cloud; first phase was planned for calendar 2015 with enrollment, payment, and assessment [10].
- **2019:** St. Petersburg College moves Campus Solutions and related PeopleSoft applications from on premises to OCI [4].
- **2022:** Oracle names higher-education cloud customers including Bowie State, Butler Community College, Coppin State, Skidmore, and University of Pittsburgh [11].
- **2025:** Campus Solutions becomes the first SIS announced as certified on the 1EdTech Edu-API standard [16].
- **2026:** Oracle extends rolling PeopleSoft support through at least 2037; the June 2026 roadmap emphasizes security, regulatory updates, Fluid UX, cloud readiness, and configuration [2] [9].
- **2026:** Oracle's current Fusion service description prices Student Management, Student Aid Eligibility, and SFP by hosted student/applicant/recipient units, while the PeopleSoft global list publishes Campus Solutions per FTE Student [19].

### References

1. About Oracle and corporate history - https://www.oracle.com/corporate/
2. Oracle Student Cloud - Higher Education - https://www.oracle.com/government/education/higher-education/student-cloud/
3. Campus Solutions Overview - https://docs.oracle.com/en/applications/peoplesoft/campus-solutions/9.2.038/campus-solutions-application-fundamentals/campus-solutions-overview.html
4. Campus Self Service Business Processes - https://docs.oracle.com/en/applications/peoplesoft/campus-solutions/9.2.038/campus-self-service/campus-self-service-business-processes.html
5. Campus Solutions: Blueprint for Journey to the Cloud - https://www.oracle.com/a/ocom/docs/applications/erp/campus-solution-blueprint-for-journey-to-the-cloud.pdf
6. PeopleSoft Campus Solutions Reviews and Product Details, G2 - https://www.g2.com/products/peoplesoft-campus-solutions/reviews
7. Reviews of Oracle PeopleSoft, Capterra - https://www.capterra.com/p/155958/Oracle-PeopleSoft/reviews/
8. PeopleSoft Campus Solutions Reviews and Ratings, Gartner Peer Insights - https://www.gartner.com/reviews/product/peoplesoft-campus-solutions
9. How Oracle Is Evolving PeopleSoft Campus Solutions for the Future of Higher Education - https://questoraclecommunity.org/learn/blogs/bp4d26-how-oracle-is-evolving-psft-campus-solutions/
10. Oracle Bringing Student Cloud to Education and Research Cloud - https://campustechnology.com/articles/2014/03/11/oracle-bringing-student-cloud-to-education-and-research-cloud.aspx
11. Oracle Cloud Helps Schools Embrace the Next Era of Higher Education - https://www.prnewswire.com/news-releases/oracle-cloud-helps-schools-embrace-the-next-era-of-higher-education-301463482.html
12. Setting Up Campus Mobile Within Campus Solutions - https://docs.oracle.com/cd/E56917_01/cs9pbr4/eng/cs/lsss/task_SettingUpCampusMobileWithinCampusSolutions-667ffe.html
13. Using the Student Homepage - https://docs.oracle.com/en/applications/peoplesoft/campus-solutions/9.2.038/campus-solutions-application-fundamentals/using-student-homepage.html
14. Oracle Student Management Data Sheet - https://www.oracle.com/a/ocom/docs/industries/higher-education/edu-student-management-ds.pdf
15. Oracle Student Financial Planning Data Sheet - https://www.oracle.com/a/ocom/docs/industries/higher-education/student-financial-planning-ds.pdf
16. Oracle First to Achieve 1EdTech Certification for its Student Information System - https://www.oracle.com/news/announcement/oracle-first-to-achieve-1edtech-certification-for-its-student-information-system-2025-10-28/
17. Oracle Buys PeopleSoft - https://www.oracle.com/corporate/pressrelease/oracle-buys-peoplesoft-121304.html
18. REST API for Oracle Fusion Cloud Student Management - https://docs.oracle.com/en/cloud/saas/student-management/farsm/index.html
19. PeopleSoft Component Global Price List and Fusion Cloud Service Descriptions - https://www.oracle.com/ng/a/ocom/docs/corporate/pricing/peoplesoft-price-list-070612.pdf ; https://www.oracle.com/contracts/docs/oracle-fusion-cloud-service-desc-1843611.pdf
20. Oracle Fusion Applications, Apple App Store - https://apps.apple.com/us/app/oracle-fusion-applications/id1361813677
21. Oracle Cloud Compliance - https://www.oracle.com/corporate/cloud-compliance/
