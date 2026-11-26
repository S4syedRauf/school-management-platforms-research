# School, College and University Management Platforms 2026: Top 20 Worldwide, Top 10 India, Full Dossiers and an Open-Source Blueprint to Beat Them

**Author:** Manus AI
**Date:** November 2026 (evidence checked 24–27 November 2026)
**Scope:** student information systems (SIS), school management information systems (MIS), school ERP and campus/university ERP platforms for K-12 schools, independent and international schools, colleges and universities.

## How to Read This Report

This report has three jobs. First, it ranks the 20 strongest school, college and university management platforms worldwide, plus a separate top 10 of Indian platforms, using one published scoring rubric. Second, it gives a complete dossier for every ranked platform. Each dossier covers the vendor, headquarters, creation year, platform classification (web, cloud, desktop, mobile, on-premise), full feature inventory, advanced features, pricing, integrations, security, strengths, weaknesses, milestones and a numbered reference list. Third, it turns the evidence into a blueprint for a new open-source "one platform for all" that schools, colleges and universities can move to easily.

All links are full, visible URLs, never hidden behind link text. Bracketed numbers such as [3] in each dossier point to that dossier's own numbered reference list.

**Table of contents**

1. How to Read This Report, Executive Summary, Methodology and Ranking Tables (this section)
2. Part I. Top 20 Worldwide Platforms: Full Profiles (#1 to #20)
3. Part II. Top 10 Indian Platforms: Full Profiles (India #1 to India #10)
4. Part III. Also Evaluated: Full Profiles of the 10 Candidates That Did Not Make the Lists
5. Part IV. Backend Teardown of the Top 3 System-of-Record Platforms (REA-assisted)
6. Part V. Blueprint: "OpenCampus One", an Open-Source Platform Designed to Beat Every Platform in This Report
7. Appendix A. Interoperability, Privacy, Accessibility, Security and India Digital Public Infrastructure Requirements
8. Appendix B. Open-Source Technical Approach, Free Tiers and Deployment Costs
9. Appendix C. Market Size, Consolidation, Security Incidents and Buyer Pain Points

## Executive Summary

**Worldwide leaders.** PowerSchool SIS is ranked #1 (weighted score 8.8 out of 10). It has the broadest K-12 feature set and the largest footprint: 15,000+ organizations, 60M+ students and 90+ countries, per company claims. Ellucian is #2 (8.4). It is the dominant higher-education system of record, with about 3,000 institutions in 50 countries, and it absorbed Anthology's SIS/ERP business on 31 December 2025. Arbor is #3 (8.2). It is the fastest-moving cloud MIS and held 53.58% of English state schools in the May 2026 census analysis. Alma, FACTS, Workday Student, Synergy, Veracross, Focus and Blackbaud complete the top 10.

**Indian leaders.** MasterSoft ERP is India #1 (7.9). It has the broadest higher-education and accreditation (NAAC/NBA/OBE) coverage. Camu is India #2 (7.8), with the most modern cloud and mobile experience. Fedena is India #3 (7.6), with the largest claimed footprint (40,000+ institutions) and transparent pricing. NextOS (#4) and Academia ERP by Serosoft (#5) follow.

**Market truth.** Across all 40 platforms reviewed, the same weaknesses keep appearing:

- Enterprise pricing is quote-only and hard to compare.
- Implementation takes months.
- Interfaces are dated, and mobile apps are often poorly rated.
- Reporting is rigid.
- Data lock-in and costly exits are common.
- Recent security incidents include PowerSchool (December 2024), Blackbaud (2020), Illuminate (2021, FTC action in 2025) and Frontline (2026).
- India-specific compliance coverage is weak: UDISE+, APAAR, ABC, DigiLocker and the DPDP Act 2023 with the DPDP Rules 2025.

Part V converts these gaps into a feature-by-feature blueprint. The core rule is that every proposed feature must fix a documented competitor gap.

## Selection and Ranking Methodology

**Candidate pool.** We researched 40 platforms in depth: 25 worldwide and 15 Indian. The pool combines the most-cited global SIS/MIS/ERP vendors, the market-share leaders in the US, UK, Australia and international-school segments, the higher-education ERP leaders, and every candidate in the guide you supplied. Each platform got its own research pass using official vendor pages, documentation, pricing pages, press releases, government procurement documents (for example UK G-Cloud rate cards), app-store listings and review platforms. Pure LMS products such as Canvas, Moodle and Google Classroom were excluded from ranking and treated as integration targets.

**Scoring rubric (0–10 per dimension, fixed weights):**

| Dimension | Weight | What it measures |
|---|---:|---|
| Feature breadth | 30% | Coverage of admissions, records, attendance, timetable, gradebook/exams, LMS, communications, portals, fees/finance, HR/payroll, transport, health, behaviour, special education, analytics and compliance |
| Adoption ("most used") | 30% | Institutions, students and countries served, market share and procurement wins, with dated sources |
| Advanced features | 20% | AI, predictive analytics, early-warning, workflow automation, advanced scheduling, standards certification and other distinctive capabilities |
| UX and mobile | 10% | Interface modernity, native app quality and app-store ratings, accessibility |
| Interoperability | 10% | Open APIs, OneRoster/LTI/Ed-Fi/SIF/CASE, SSO, marketplace and data export |

Weighted score = 0.30 × breadth + 0.30 × adoption + 0.20 × advanced + 0.10 × UX + 0.10 × interoperability. Ties are broken by adoption, then advanced features. The ranking was computed with the deterministic script in the edtech-platform-research skill. Global and Indian lists were ranked separately; an Indian platform appears only in the Indian list.

**Important caveats.** Adoption figures are mostly vendor claims and are labelled as such in each dossier. A low UX score sometimes reflects poorly rated companion apps (for example Arbor, Bromcom and Synergy) rather than a poor core web interface. Most enterprise vendors publish no prices, so pricing is quote-only unless an official figure is cited.

## Global Top 20 Ranking

| Rank | Platform | Vendor / owner | Founded (company) / product origin | Classification | Pricing model | Official website | Score |
|---:|---|---|---|---|---|---|---:|
| 1 | PowerSchool SIS | PowerSchool Group (Bain Capital) | 1997 / 1997 | Cloud SaaS, web, iOS/Android | Quote-only | https://www.powerschool.com/ | 8.8 |
| 2 | Ellucian (Banner, Colleague, Ellucian Student) | Ellucian Company LLC | 1968 (Datatel roots) / Banner and Colleague 1979 | Cloud SaaS, web, hybrid legacy on-premise, iOS/Android | Quote-only; AI included in core subscription | https://www.ellucian.com/ | 8.4 |
| 3 | Arbor MIS | Arbor Education (The Key Group) | 2011 / 2011 | Cloud SaaS, web, iOS/Android | Per pupil + school base fee (G-Cloud) | https://arbor-education.com/ | 8.2 |
| 4 | Alma SIS | Alma Technologies, Inc. | 2014 / 2014 | Cloud SaaS, web, responsive mobile portal | Quote; packages named but unpriced | https://www.getalma.com/ | 8.1 |
| 5 | FACTS SIS | FACTS Management (Nelnet) | 1986 / RenWeb, renamed FACTS SIS in 2018 | Cloud SaaS, web, iOS/Android | Quote-only | https://factsmgt.com/ | 7.9 |
| 6 | Workday Student | Workday, Inc. | 2005 / 2016 (first live 2018) | Cloud SaaS, web, iOS/Android | Quote-only | https://www.workday.com/ | 7.7 |
| 7 | Synergy Education Platform | Edupoint Educational Systems | 2003 / not disclosed | Cloud-hosted web, iOS/Android | Quote-only | https://www.edupoint.com/ | 7.7 |
| 8 | Veracross | Veracross LLC | 2003 / 2002 prototype | Cloud SaaS, web, iOS/Android | Quote-only (pricing page without prices) | https://www.veracross.com/ | 7.6 |
| 9 | Focus School Software | Focus School Software LLC | 2006 / 2006 | Hybrid: cloud SaaS, web, customer-hosted servers, iOS/Android | Quote-only | https://focusschoolsoftware.com/ | 7.6 |
| 10 | Blackbaud K-12 Education Management | Blackbaud, Inc. | 1981 / not disclosed | Cloud SaaS, web, responsive mobile | Quote-only | https://www.blackbaud.com/ | 7.5 |
| 11 | Bromcom | Bromcom Computers plc | 1986 / MIS 2005, cloud MIS 2011 | Cloud SaaS (Azure), web, iOS/Android | Public per-pupil packages + base fee | https://bromcom.com/ | 7.5 |
| 12 | Jenzabar | Jenzabar, Inc. | 1998 / 1998 | Hybrid: cloud SaaS, web, J1 Desktop client, iOS/Android | Quote-only | https://www.jenzabar.com/ | 7.5 |
| 13 | Infinite Campus | Infinite Campus, Inc. | 1993 / 1996 | Cloud SaaS, web, iOS/Android | Quote; per student per year | https://www.infinitecampus.com/ | 7.3 |
| 14 | Skyward (Qmlativ, SMS 2.0) | Skyward, Inc. | 1980 / 1981 | Hybrid: web, cloud hosting, district-hosted legacy, iOS/Android | Quote-only | https://www.skyward.com/ | 7.3 |
| 15 | Compass Education | Compass Education Pty Ltd | 2010 / 2011 | Cloud SaaS, web, iOS/Android | Quote-only | https://www.compass.education/ | 7.3 |
| 16 | Classter | Vertitech S.A. (Banyan Software) | 2015 / 2015 | Hybrid: cloud SaaS, web, on-premise option, iOS/Android | Public example per active student | https://www.classter.com/ | 7.3 |
| 17 | openSIS | Open Solutions for Education (OS4ED) | Not disclosed / 2008 | Hybrid: cloud SaaS, self-hosted open-source Community Edition, iOS/Android | Public staff-based pricing; free Community Edition | https://opensis.com/ | 7.2 |
| 18 | iSAMS | iSAMS Ltd (IRIS Software Group) | 2005 / 2005 | Cloud SaaS, web, iOS/Android | Quote-only | https://www.isams.com/ | 7.0 |
| 19 | Anthology Student | Ellucian (acquired 2025–2026) | 2020 (Campus Management roots 1988) / not disclosed | Cloud SaaS, web, legacy on-premise | Quote-only | https://www.anthology.com/ | 7.0 |
| 20 | SIMS (SIMS 7 and SIMS Next Gen) | Education Software Solutions (ParentPay Group) | 2020 legal entity / 1984 product origin | Hybrid: desktop/on-premise SIMS 7, cloud web Next Gen, iOS/Android | Quote-only | https://www.ess-sims.co.uk/ | 6.9 |

**Dimension scores (global top 20).** Order: breadth / adoption / advanced / UX / interoperability.

| Rank | Platform | Breadth | Adoption | Advanced | UX | Interop | Weighted |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | PowerSchool SIS | 10 | 10 | 8 | 6 | 6 | 8.8 |
| 2 | Ellucian | 8 | 10 | 10 | 4 | 6 | 8.4 |
| 3 | Arbor | 8 | 10 | 10 | 2 | 6 | 8.2 |
| 4 | Alma | 8 | 9 | 8 | 6 | 8 | 8.1 |
| 5 | FACTS | 8 | 9 | 8 | 4 | 8 | 7.9 |
| 6 | Workday Student | 6 | 9 | 10 | 6 | 6 | 7.7 |
| 7 | Synergy | 8 | 9 | 8 | 2 | 8 | 7.7 |
| 8 | Veracross | 8 | 8 | 8 | 6 | 6 | 7.6 |
| 9 | Focus | 8 | 8 | 8 | 4 | 8 | 7.6 |
| 10 | Blackbaud | 6 | 9 | 8 | 6 | 8 | 7.5 |
| 11 | Bromcom | 8 | 9 | 8 | 2 | 6 | 7.5 |
| 12 | Jenzabar | 8 | 7 | 10 | 4 | 6 | 7.5 |
| 13 | Infinite Campus | 8 | 9 | 6 | 4 | 6 | 7.3 |
| 14 | Skyward | 8 | 9 | 6 | 2 | 8 | 7.3 |
| 15 | Compass | 8 | 9 | 6 | 4 | 6 | 7.3 |
| 16 | Classter | 8 | 7 | 8 | 6 | 6 | 7.3 |
| 17 | openSIS | 8 | 8 | 8 | 2 | 6 | 7.2 |
| 18 | iSAMS | 8 | 8 | 6 | 4 | 6 | 7.0 |
| 19 | Anthology Student | 8 | 6 | 8 | 6 | 6 | 7.0 |
| 20 | SIMS | 8 | 9 | 4 | 4 | 6 | 6.9 |

## India Top 10 Ranking

| Rank | Platform | Vendor | Founded (company) / product origin | Classification | Pricing model | Official website | Score |
|---:|---|---|---|---|---|---|---:|
| 1 | MasterSoft ERP | MasterSoft ERP Solutions Pvt. Ltd. (Nagpur) | 1995 / not disclosed | Cloud SaaS, web, Android/iOS | Quote-only; free for qualifying government girls', special-needs, NGO and small Sainik schools | https://www.mastersoft.ai/ | 7.9 |
| 2 | Camu | Octoze Technologies (Chennai) | 2013 / 2014 | Cloud SaaS (multi-tenant), web, iOS/Android | Quote-only | https://camudigitalcampus.com/ | 7.8 |
| 3 | Fedena | Foradian Technologies (Bengaluru) | 2009 / 2009–2010 (open-source release 2010) | Cloud SaaS, web, self-hosted/on-premise option, iOS/Android | Public annual plans (USD) | https://fedena.com/ | 7.6 |
| 4 | NextOS | Next Education India (Hyderabad) | 2007 / not disclosed | Cloud SaaS, web, iOS/Android | Indicative public ranges per student per month | https://www.nextos.in/ | 7.6 |
| 5 | Academia ERP | Serosoft Solutions (Indore) | 2008 / not disclosed | Cloud SaaS, web, Android/iOS; 5-year licence option | Named plans without amounts; SaaS or perpetual licence + AMC | https://serosoft.com/ | 7.4 |
| 6 | Skolaro | Buzzyears Education (New Delhi) | 2012 / not disclosed | Cloud SaaS, web, iOS/Android | Per student; all 50+ modules in base plan | https://www.skolaro.com/ | 7.3 |
| 7 | Vidyalaya School ERP | Sapphire Software Solutions (Ahmedabad) | 2002 / 2002 (Windows origins) | Cloud SaaS, web, iOS/Android | Quote; market range on official FAQ | https://www.vidyalayaschoolsoftware.com/ | 7.2 |
| 8 | MyClassboard | MyClassboard Educational Solutions (Hyderabad) | 2009 / 2009–2010 | Cloud SaaS, web, Android/iOS | Quote-only | https://www.myclassboard.com/ | 7.0 |
| 9 | Entab CampusCare (Entab One) | Entab Infotech (Nelnet, from 1 Oct 2026) | 2000 / not disclosed | Cloud SaaS, web, Android/iOS | Custom by school size, unlimited users | https://www.entab.in/ | 7.0 |
| 10 | LEAD School (Nucleus ERP) | Leadership Boulevard Pvt. Ltd. (Mumbai) | 2012 / ERP from 2016–2017 | Cloud SaaS, web, Android/iOS, classroom hardware bundle | Quote; bundled school system | https://leadschool.in/ | 6.5 |

**Dimension scores (India top 10).**

| Rank | Platform | Breadth | Adoption | Advanced | UX | Interop | Weighted |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | MasterSoft ERP | 10 | 7 | 8 | 8 | 4 | 7.9 |
| 2 | Camu | 8 | 8 | 8 | 8 | 6 | 7.8 |
| 3 | Fedena | 8 | 10 | 6 | 4 | 6 | 7.6 |
| 4 | NextOS | 8 | 10 | 4 | 8 | 6 | 7.6 |
| 5 | Academia ERP | 8 | 6 | 10 | 6 | 6 | 7.4 |
| 6 | Skolaro | 10 | 7 | 8 | 2 | 4 | 7.3 |
| 7 | Vidyalaya | 8 | 8 | 6 | 8 | 4 | 7.2 |
| 8 | MyClassboard | 8 | 8 | 8 | 2 | 4 | 7.0 |
| 9 | Entab CampusCare | 8 | 8 | 6 | 6 | 4 | 7.0 |
| 10 | LEAD School | 6 | 9 | 4 | 8 | 4 | 6.5 |

## Candidates Evaluated but Not Ranked in the Lists

Ten researched candidates scored below the cut-off. Their full dossiers are in Part III, so nothing from the research is lost.

| Pool | Position | Platform | Weighted | Main reason it missed the list |
|---|---:|---|---:|---|
| Global | 21 | Aeries SIS | 6.5 | Strong but concentrated in California (about 1 in 2 California students) |
| Global | 22 | Gradelink SIS | 6.4 | Broad and affordable for small private schools, but few advanced/AI features |
| Global | 23 | ManageBac+ | 6.2 | Excellent IB curriculum/assessment tool, but narrower than a full SIS/ERP and low app scores |
| Global | 24 | Oracle PeopleSoft Campus Solutions / Student Cloud | 5.7 | Large legacy base but slow product momentum and narrower modern scope |
| Global | 25 | Gibbon | 3.6 | Free GPL open-source project with no verifiable adoption figures; used as an architecture reference |
| India | 11 | Teachmint | 6.2 | Large user base, but the standalone admissions and fee modules are officially no longer available |
| India | 12 | Edunext ERP | 6.2 | Clean modern UI, but smaller footprint and fewer advanced features |
| India | 13 | OpenEduCat | 6.0 | Open-source (LGPL-3.0) and highly interoperable, but low verified adoption |
| India | 14 | Toddle | 5.7 | Best-in-class curriculum planning for IB/international schools, but not a full ERP |
| India | 15 | MyClassCampus | 5.4 | Acquired by Teachmint in January 2022; the standalone product site now presents Teachmint X |

## Platform Classification Matrix

Key: **Y** means publicly documented. **N** means not documented in current public material. "Legacy" means an older estate still exists. "Opt." means an optional or add-on route.

| Platform | Web-based | Cloud SaaS | Desktop client | Native mobile (iOS/Android) | On-premise / self-host | Open source |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| #1 PowerSchool SIS | Y | Y | N | Y | N | N |
| #2 Ellucian | Y | Y | N | Y | Legacy/hybrid | N |
| #3 Arbor | Y | Y | Opt. (TimeTabler add-on) | Y | N | N |
| #4 Alma | Y | Y | N | Responsive web only | State-hosted option | N |
| #5 FACTS SIS | Y | Y | N | Y | N | N |
| #6 Workday Student | Y | Y | N | Y | N | N |
| #7 Synergy | Y | Y | N | Y | Not clearly documented | N |
| #8 Veracross | Y | Y | N | Y | N | N |
| #9 Focus | Y | Y | N | Y | Y | N |
| #10 Blackbaud | Y | Y | N | Responsive + third-party apps | N | N |
| #11 Bromcom | Y | Y | N | Y | N | N |
| #12 Jenzabar | Y | Y | Y (J1 Desktop) | Y | Not clearly documented | N |
| #13 Infinite Campus | Y | Y | N | Y | N | N |
| #14 Skyward | Y | Y | N | Y | Y (district-hosted SMS 2.0) | N |
| #15 Compass | Y | Y | N | Y | N | N |
| #16 Classter | Y | Y | N | Y | Y | N |
| #17 openSIS | Y | Y | N | Y | Y | Y (Community Edition, GPL) |
| #18 iSAMS | Y | Y | N | Y | Legacy | N |
| #19 Anthology Student | Y | Y | N | Not verified | Legacy | N |
| #20 SIMS | Y (Next Gen) | Y (Next Gen) | Y (SIMS 7) | Y | Y (SIMS 7) | N |
| India #1 MasterSoft | Y | Y | N | Y | N | N |
| India #2 Camu | Y | Y | N | Y | N | N |
| India #3 Fedena | Y | Y | N | Y | Y | Historic Apache-2.0 release (inactive since 2020) |
| India #4 NextOS | Y | Y | N | Y | N | N |
| India #5 Academia ERP | Y | Y | N | Y | Licence model (vendor-hosted) | N |
| India #6 Skolaro | Y | Y | N | Y | Listed by Capterra only, unverified | N |
| India #7 Vidyalaya | Y | Y | Legacy Windows roots | Y | Not clearly documented | N |
| India #8 MyClassboard | Y | Y | N | Y | N | N |
| India #9 Entab | Y | Y | N | Y | Historic only | N |
| India #10 LEAD School | Y | Y | N (smart-TV/tablet hardware) | Y | N | N |

**Observation.** Every ranked platform is now web-based and cloud-delivered. Only SIMS 7 and Jenzabar J1 still ship real desktop clients. Only openSIS and Fedena (historically) have open-source editions in the ranked lists. No ranked platform combines open source, offline-first mobile, multi-segment coverage (K-12 plus higher education) and India compliance. That gap is the white space Part V targets.

## Pricing Overview

Prices were checked 24–27 November 2026. "Estimate" means a third-party directory figure, not a vendor quote. Full pricing analysis, with sources, is in each dossier.

| Platform | Public pricing evidence |
|---|---|
| PowerSchool SIS | No public price list; quote via sales. A Capterra "$7 flat rate" label is a marketplace estimate without a unit. |
| Ellucian | Core Banner/Colleague/Ellucian Student quote-only. The AI pricing page states AI is included in one core subscription with no per-seat or token charges. |
| Arbor | Official G-Cloud 14 rate card (2024/25): primary £3.15 / £6.30 / £10.50 per student (Core/Comms/Perform) + £2,100 base; secondary £4.20 / £7.35 / £11.55 + £4,200. |
| Alma | No public prices; Foundations, Core and Essentials packages and a District Solutions Package; terms set in a statement of work. |
| FACTS SIS | Quote-only; FACTS Family App listed at $4.99 per family per year (not the SIS licence). |
| Workday Student | Quote-only negotiated institutional subscription. |
| Synergy | Quote-only; subscription generally based on enrolled students or sites (Gartner). |
| Veracross | Quote-only pricing page; Capterra estimate $500/month; third-party full-suite estimates $15,000–$50,000+. |
| Focus | Quote-only for SIS/ERP; hardware prices public (attendance kiosk $569). |
| Blackbaud | Quote-only; Capterra estimate $21,000/year starting. |
| Bromcom | Public per-pupil packages (Standard/Plus/One-Stop-Shop). G-Cloud 14 (Feb 2025) MIS+Finance primary £6.55 / £9.55 / £11.55 per pupil; base fees apply. |
| Jenzabar | Quote-only; modular, enrolment-based, subscription or perpetual. |
| Infinite Campus | Quote-only; subscription typically per student per year. |
| Skyward | Quote-only; Software Advice/Capterra estimate from $30,000/year. |
| Compass | Quote-only. |
| Classter | Official example: €21.50 per active student per year (Core €8.50 + Academics & LMS €6.50 + Surveys & Quizzes €6.50) for a 1,000-student institution = €25,500/year. |
| openSIS | Essential $480/year (5 staff) or $50/month; Advanced $1,440/year (10 staff) or $140/month; 15-day trial; free Community Edition. |
| iSAMS | Quote-only; third-party estimates £5,000–£6,000/year. |
| Anthology Student | Quote-only, now through Ellucian. |
| SIMS | Quote-only; EdTech Impact estimate from £350 + £2–£3 per pupil; Somerset Schools Forum recorded £4.99 per pupil in 2022. |
| MasterSoft ERP | Quote-only; free "M-Initiative" licences for qualifying government girls', special-needs, NGO and small Sainik schools. |
| Camu | Quote-only; directory "₹25/year" figures are nominal and unreliable. |
| Fedena | Standard $800/year, Premium $1,120/year, Ultimate $1,360/year (sale prices displayed 24 Nov 2026; unlimited users). |
| NextOS | Official FAQ ranges: ₹7–₹155 per student per month; ₹60,000–₹2,00,000+ per year for packages. |
| Academia ERP | Pro, Premium, Enterprise plans without amounts; SaaS per user/year or 5-year licence + AMC. |
| Skolaro | Per student, annual or term-wise; all 50+ modules, implementation, training and migration included in base plan. |
| Vidyalaya | Official FAQ market range ₹5–₹50 per student per month; directory listings inconsistent. |
| MyClassboard | Quote-only; 2021 press estimate ₹300–₹500 per student per year. |
| Entab CampusCare | Custom pricing by school size; one subscription, 35+ modules, unlimited users. |
| LEAD School | Quote-only bundle (books, onboarding, platform licence, hardware). |

**Pricing insight.** In the US, prices are enterprise quotes with large implementation projects. UK public procurement shows base fee plus per-pupil pricing (about £3–£12 per pupil per year). In India, flat school plans and per-student tiers dominate, often under ₹100–₹500 per student per year. The blueprint uses this to propose a free self-hosted core plus transparent, published hosted pricing.

## Corrections and Updates to the Guide You Supplied

Your guide was researched candidate by candidate. These differences matter for decisions:

1. **Ranking changes.** Our global top 20 adds Workday Student (#6), Bromcom (#11), Jenzabar (#12) and Anthology Student (#19) because of their adoption and higher-education depth. Aeries, Gradelink, ManageBac+ and Gibbon move to Part III, and their full profiles are kept. Our India top 10 adds MasterSoft ERP (#1) and Academia ERP (#5). Teachmint and Edunext move to Part III.
2. **Infinite Campus** ranks #13 here, not #2. It scores high on adoption (11M students, 46 states) but lower on advanced features and app experience under the rubric. It is still analysed as one of the "top 3" system-of-record backends in Part IV, because its footprint and hosting model are among the most instructive.
3. **Arbor** now leads the English state-school market: 53.58% (11,787 schools) in the May 2026 census analysis, against SIMS 26.28% and Bromcom 17.60%. The guide's G-Cloud 15 (September 2026) price figures could not be independently confirmed in this research. The Arbor dossier uses the official G-Cloud 14 rate card and labels it historical.
4. **Anthology Student** is now owned by Ellucian. The acquisition of Anthology's SIS/ERP business completed 31 December 2025 and was announced 5 January 2026.
5. **Entab** was acquired by Nelnet Business Services effective 1 October 2026. Nelnet's announcement cites 1,000+ schools and 1.5M+ students, lower than Entab's own 2,300–2,500+ school claims.
6. **Teachmint's** official pages state that the standalone admission and fee-management solutions are no longer available. Schools expecting a classic ERP should treat those as discontinued.
7. **MyClassCampus** was acquired by Teachmint in January 2022. Its domain now presents Teachmint X, so it is no longer evaluated as an independent ERP.
8. **Focus School Software:** the guide's "$3,000 SourceForge" figure could not be verified and is not treated as subscription pricing.
9. **Gradelink:** the official calculator showed $106/month + $275 setup on 24 November 2026, matching the guide. The company founding year is reported as 2001 by LinkedIn and Crunchbase, while the homepage implies 2002 ("24 years").
10. **Gibbon** publishes no verified institution or student count, so its adoption score is low despite real worldwide use.
