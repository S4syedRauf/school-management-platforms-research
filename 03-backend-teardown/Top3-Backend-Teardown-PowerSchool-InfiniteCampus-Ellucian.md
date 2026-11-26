# Publicly observable backend architecture teardown: PowerSchool SIS, Infinite Campus, and Ellucian Banner/Colleague/Ethos

**As-of date: 27 November 2026.** This report uses only lawful public material: vendor documentation and product pages, public GitHub repositories, NIST’s vulnerability database, public breach reporting, HTTP headers, and passive REA observations of public pages. It does not log in, bypass authentication, scan, fuzz, or access a customer system.

The public record is uneven. PowerSchool publishes unusually concrete administrator documentation for plugins, data events, throttling, and mobile server registration. Infinite Campus publishes clear hosting terms and interoperability claims, but much of its direct API documentation is partner/customer gated. Ellucian publishes strong public evidence for Ethos’s application/resource/change-notification model through its official GitHub organization, while detailed tenant-specific API schemas remain behind the customer center. Where the internal implementation is not public, the report says **Inference** rather than presenting a guess as fact.

## Comparative snapshot

| Platform | Publicly evidenced integration center | Hosting posture visible publicly | Event/data movement | Main architectural liability visible from public evidence |
|---|---|---|---|---|
| PowerSchool SIS | Plugin packages, PowerQuery, REST data exchange, Universal Rostering, SIF, Data Event API | Cloud product; customer deployments also expose server/node/load-balancer concepts in admin docs | Real-time REST roster/grade exchange and configurable data-change events | Powerful legacy customization surface and plugin credentials create a large blast radius; the December 2024 PowerSource incident shows support-plane compromise can reach SIS data [1] [2] |
| Infinite Campus | 1EdTech OneRoster, LTI, partner APIs, ODBC for a designated customer employee | Hosted production instance plus staging option; documented Windows, SQL Server, Apache Tomcat, Java, SSL middleware [3] | OneRoster rostering, grade passback, secure launch; direct API is commercially gated according to an independent integration guide [4] | Integration fragmentation across OneRoster versions and partnership tiers; documented stack is operationally traditional and customer-specific |
| Ellucian Banner/Colleague/Ethos | Ethos REST proxy APIs, versioned EEDM resources, application/resource ownership, API keys/JWT, change notifications/pub-sub | Ellucian Cloud SaaS is the strategic direction; Banner/Colleague also have installed/legacy and hybrid estates [5] [6] | Resource-level create/update/delete notifications, publish/subscribe, low-code orchestration, real-time sync [7] | Strong abstraction improves interoperability but adds schema/version/entitlement complexity; legacy self-service surfaces still produce conventional web vulnerabilities [8] |

## Evidence quality and public-observation checks

The public material supports interface and operating-model conclusions better than database-engine conclusions. None of the vendors publishes a complete production schema, deployment diagram, or authoritative list of all internal services.

I ran the requested REA CLI against one public page per vendor. The PowerSchool homepage yielded nine observed/analyzed scripts, but no verified application routes or API endpoints; two low-confidence query-string candidates were explicitly marked unverified by REA. The Infinite Campus partner page yielded three observed scripts; the Nuxt bundle at `/_nuxt/O9Ss3k2F.js` was marked unavailable because of an analysis deadline, and no routes or endpoints were established. The public Ellucian Ethos GitHub organization page yielded zero captured scripts, so it provides no frontend inference. These are observations about public marketing/community pages, not evidence about the authenticated SIS front ends. [9] [10] [11]

A passive `curl -I` check found PowerSchool returning `x-frame-options: SAMEORIGIN`, HSTS, and `x-content-type-options: nosniff`; Infinite Campus’s public page returned Netlify headers and a detailed CSP; Ellucian’s product page returned a Cloudflare 403 to the head-request path. These headers are perimeter observations only. They do not reveal the SIS backend or prove that customer tenants share the same edge configuration.

# 1. PowerSchool SIS

## Data model and core entities

**Documented fact.** PowerSchool describes SIS as managing student records, enrollment, attendance, grades, scheduling, family communication, reporting, and special programs. Its public Universal Rostering documentation names student, course, and related enrollment data, while its product page names attendance, behavior, health, graduation progress, assets, and student demographics as reportable domains. [12] [13]

**Inference.** The observable model is a district/school hierarchy with person-centered records, enrollment/roster relationships, academic offerings and sections, attendance, grading/assessment, and extensible program/health/behavior records. The public documents do not prove whether the underlying transactional store is one relational schema, a service decomposition, or a mixture. The plugin and page-customization model strongly suggests a long-lived transactional core with compatibility layers rather than a pure greenfield microservice model.

## API styles and authentication

**Documented fact.** PowerSchool exposes REST data exchange through plugins. Universal Rostering supports REST GET for roster information and REST PUT for course assignments and grades. PowerSchool also documents Data Event API Services for notifications of changes between PowerSchool and third-party applications, plus a SIF Agent option. [2] [14]

The PowerQuery ecosystem is a distinctive extension path: an installed plugin can include a PowerQuery and the plugin itself is packaged as XML or ZIP. The public administrator docs do not present a public, vendor-hosted OpenAPI contract for the whole SIS. [15]

**Documented fact.** Plugin data exchange uses OAuth 2.0. PowerSchool auto-generates a client ID and secret for a plugin, and administrators can regenerate them when compromise is suspected. [1]

**Not publicly verified.** A general PowerSchool GraphQL API, a general public SOAP API, and Ed-Fi as the primary native SIS API were not established in the public sources reviewed. SIF is explicitly documented; it should not be conflated with REST or GraphQL. SAML/OIDC SSO is a product/deployment capability in the broader ecosystem, but the public administrator pages reviewed do not expose enough detail to state which flows are supported by every SIS release or tenant.

## Extensibility and integration/event architecture

PowerSchool’s extension point is unusually administrator-visible. Plugins are installed from XML/ZIP packages, may register with an external registration server, may add links, and can include PowerQueries. The SIS product page claims administrators can modify interface pages, add or adjust SIS pages, and extend existing pages with new tables and fields without custom development. [12] [15]

Data Event API Services provide change notifications. The administrator can enable event generation separately from, or together with, the SIF agent. PowerSchool also exposes a per-plugin minimum interval between API requests, with throttling enforced at the server and requiring restart after a setting change. [14]

**Architecture reading.** This is a “deep plug-in into a transactional application” model, not only an external integration gateway. It is flexible for districts and partners, but it increases the number of code, credential, and compatibility paths that must be governed. Per-plugin throttling is a useful guardrail, but it is a coarse control compared with a centrally managed quota, tenant-aware rate budget, and asynchronous delivery queue.

## Multi-tenancy, hosting, and frontend observations

PowerSchool publicly calls SIS cloud software, but its administrator documentation still refers to a PowerSchool server, node, remote web traffic, Tomcat or load-balancer SSL, and server arrays. [12] [13] **Inference:** the installed/on-premise and hosted estates likely coexist, with a compatibility-oriented deployment abstraction rather than one uniform SaaS runtime.

The public marketing site’s JavaScript is visibly WordPress/theme/plugin oriented in the REA capture. That says nothing reliable about the SIS UI. The public SIS material supports a browser/mobile web-service model, but no authenticated SIS bundle or public login bundle was analyzed. The safe conclusion is that the frontend framework of the SIS is **not publicly established**.

## Reporting, warehouse, and mobile

PowerSchool positions SIS as providing ad hoc and state/provincial reporting across attendance, behavior, health, graduation progress, assets, and demographics. Its separate Analytics & Insights product advertises role-based dashboards, ad hoc reporting, configurable metrics and filters, and cloud hosting with role- and row-based security. [12] [16]

**Inference.** The product boundary implies an operational SIS plus a reporting/analytics plane, with at least some denormalized or derived data used for dashboards. The public pages do not prove the warehouse technology, ETL cadence, or whether analytics is physically isolated from transactional storage.

Mobile is not merely a responsive web claim. The administrator documentation describes registering a district server with PowerSource, a mobile server address and port, SSL status, and a load-balancer/node deployment option. The product page advertises iOS and Android family access for grades, attendance, schedules, notifications, and payments. [13] [17]

## Security incident and architectural lesson

PowerSchool states that on 28 December 2024 it became aware of unauthorized exfiltration from certain SIS environments through the PowerSource customer support portal. It says a single compromised credential was used, that the activity was limited to selected Students and Teachers tables, and that it found no evidence of system-layer access, malware, or compromise of other products. [18]

The lesson is architectural, not merely procedural: support, community, registration, and operational data planes must be treated as separate trust zones. A support credential should not yield a path to bulk SIS-table extraction. A modern design should require phishing-resistant MFA, short-lived scoped credentials, per-tenant and per-resource authorization, just-in-time support access, immutable audit trails, export anomaly detection, and hard separation between support tooling and production data paths. PowerSchool’s documented plugin credential-regeneration control is useful, but rotation after suspected compromise is reactive rather than a substitute for least privilege. [1]

## Specific weaknesses visible from public evidence

* Plugin XML/ZIP installation, page customization, PowerQueries, external registration, and OAuth secrets form a broad compatibility surface. The public record does not show a signed-package policy, sandbox, or capability manifest.
* Data Event API and REST exchange are valuable, but the public docs do not show durable event IDs, replay semantics, dead-letter handling, consumer offsets, or schema evolution rules.
* The coexistence of server/node/load-balancer concepts and cloud marketing suggests migration and deployment variance. That improves compatibility but complicates patch consistency, observability, and incident containment.
* Reporting, mobile, family engagement, and payments are marketed as connected, but public material does not show a canonical identity graph or an explicit consent/purpose ledger for cross-product data movement.

# 2. Infinite Campus

## Data model and core entities

**Documented fact.** Infinite Campus describes Campus SIS as covering enrollment, scheduling, grading, state reporting, and roles for staff, teachers, students, parents, administrators, and technology teams. Its partner program explicitly supports roster movement and score passback. A public integration guide identifies OneRoster services for results, resources, and enrollments; OneRoster 1.2 adds role/org/account mappings, preferred names, master IDs, scoped endpoint access, standards-based grading fields, and localized OpenAPI service discovery. [19] [4]

**Inference.** The core model is an institutional hierarchy with organizations/schools, users and multiple roles, courses/classes/sections, enrollments, results/grades, resources, and sessions. The OneRoster 1.2 shape is an interoperability projection, not proof of the internal Campus schema.

## API styles and authentication

The vendor’s public partner page says it was the first SIS certified for both 1EdTech OneRoster and CASE, and lists OneRoster provisioning, gradebook/score passback, assessments, and LTI secure launch/content selection across partners. [19]

A public integration analysis says Infinite Campus supports multiple OneRoster implementations, including 1.1 and 1.2, and that developers encounter OAuth 1.0, OAuth 2.0, and JSON depending on the implementation. It also says direct API access typically requires a partnership-level commitment, leaving OneRoster as the practical path for many developers. This is an independent integration source, not an Infinite Campus contract; the commercial-gating claim should therefore be treated as **reported external evidence**, not a universal vendor policy. [4]

**Not publicly verified.** The reviewed public sources do not establish a general GraphQL API, public SOAP contract, native Ed-Fi API, or a vendor-published OpenAPI file covering every Campus deployment. SAML/OIDC details are not public enough to characterize by tenant. The clear public interoperability center is OneRoster plus LTI, with partner-specific APIs layered alongside it.

## Extensibility and integration/event architecture

Infinite Campus publicly emphasizes standards-first partner connections: real-time rostering, grade passback, secure launch, and 1EdTech certification. [19] This is a comparatively constrained, contract-driven extension model. It is safer and easier to certify than arbitrary in-process plugins, but less expressive for partners needing non-roster domains.

**Not publicly established.** No public vendor page reviewed documents a general custom-field schema, page/plugin runtime, webhook delivery contract, or durable event bus. The absence may reflect customer-gated documentation rather than product absence. OneRoster’s fixed service model, version variants, and endpoint scoping are the observable integration boundaries.

## Multi-tenancy, hosting, and frontend observations

Infinite Campus’s public Cloud Hosting Services terms are unusually specific. A hosted customer receives a single production instance; computing hardware, system software, database software, and storage are located at Infinite Campus facilities. The documented middleware includes Windows OS, Microsoft SQL Server, Apache Tomcat, Java, drivers, and SSL certificates. Infinite Campus describes backups retrieved each business day, backup servers intended to restore service within 24 hours after catastrophic disruption, and an optional staging environment. [3]

The same terms permit ODBC access to one designated customer employee, subject to approval. That is a powerful operational escape hatch, but it exposes a coupling risk: ODBC can become an unofficial integration surface that bypasses versioned API governance. [3]

The public partner page is a modern Nuxt-rendered site; REA observed the Nuxt bundle URL but could not analyze that particular bundle before its deadline. This is a marketing-site observation only. The Campus SIS frontend framework is not established by public evidence. The product pages do establish a family mobile app for grades, assignments, attendance, food service, announcements, fees, stores, and activity registration. [20]

## Reporting and data products

Infinite Campus markets built-in state reporting and a Campus Analytics Suite that uses attendance, behavior, academic, curriculum, classroom performance, and stability signals. It advertises daily risk predictions, embedded operation without imports/exports, visualizations, and customizable reports. [21]

**Inference.** The analytics product likely consumes derived/feature data within or alongside the SIS rather than relying exclusively on external batch exports. The public record does not establish the warehouse engine, whether the transactional and analytical stores are separate, or the exact retention and lineage model.

## Security incident and architectural lesson

As of the report date, HIBP records a March 2026 incident in which data alleged to be from Infinite Campus was published, describing roughly 137,000 email addresses and names, phone numbers, physical addresses, and support tickets. HIBP says subsequent notifications characterized much of the exposure as staff directory information. [22] UpGuard described the incident as alleged, reported through dark-web monitoring, with PII categories unconfirmed and no formal vendor response available at its publication date. [23]

This is not equivalent to a vendor-confirmed production SIS breach. It is nevertheless an important public security signal: support and corporate-contact datasets can be valuable even when they are not student records. The design lesson is to minimize support-ticket data, separate corporate CRM/support identity from SIS tenant identity, enforce MFA and conditional access, and make incident scope auditable. For customers, ODBC and partner credentials should be treated as privileged data paths, not convenience interfaces.

## Specific weaknesses visible from public evidence

* Multiple OneRoster versions and authentication variants increase connector branching and testing cost. Version negotiation and capability discovery must be first-class.
* A standards-first surface is predictable but narrow. Non-roster domains such as health, behavior, finance, and local custom entities may require partner-specific work.
* ODBC access is useful for controlled reporting but can undermine API governance, auditability, and forward compatibility if used for operational writes or large extracts.
* The hosting terms describe a traditional Windows/SQL/Tomcat/Java stack and customer-specific production instances. That can simplify isolation and change management, but it may constrain elastic scaling and make fleet-wide patch/observability uniformity harder than in a fully multi-tenant SaaS control plane.

# 3. Ellucian Banner/Colleague and Ethos

## Data model and core entities

Ethos publicly exposes a resource-oriented model rather than a table-oriented contract. The official Ellucian Ethos Community repository describes an **application** that owns resources and a subscribing application that consumes resource change notifications. Its example resources include students, courses, grades, parking tickets, and finance objects. The official Java and C# repositories describe invoking Ethos APIs and consuming or publishing change notifications. [7] [24] [25]

**Documented fact.** Ellucian’s public platform positioning covers the full higher-education lifecycle: recruiting, enrollment, retention, finance, HCM, advancement, and alumni engagement. Its public analytics page describes unified SIS, ERP, CRM, and third-party data, with a governed data lake/single data warehouse. [5] [26]

**Inference.** Ethos is a canonical integration/data-contract layer over heterogeneous Banner and Colleague domains. It is not evidence that Banner and Colleague share one physical database or one internal domain model. Versioned resource schemas and tenant-enabled resources are a more defensible design target than direct table replication.

## API styles and authentication

The publicly observable Ethos style is REST/JSON proxy APIs with resource versioning and application/resource authorization. The official Python pub/sub example says Ethos applications obtain API keys, use those keys to obtain JWTs, and that JWTs expire after five minutes; the Java examples explicitly cover getting an access token, invoking the proxy API, and consuming/publishing change notifications. [7] [25]

The public sources reviewed do not prove GraphQL or a general SOAP surface for Ethos. Legacy Banner/Colleague estates have older web/API and transaction integration mechanisms, but the evidence supports Ethos REST as Ellucian’s preferred modern integration boundary. SAML/OIDC may be used for human user SSO in campus deployments, but Ethos machine-to-machine authentication is the API-key-to-short-lived-JWT pattern shown in the public examples.

## Extensibility and integration/event architecture

Ethos’s extensibility model is explicit and useful: an application can own a resource, subscribe to another application’s resource, and publish or consume create/update/delete change notifications. The public Python demo models a parking-ticket authoritative application and a finance subscribing application, and shows polling for notifications in addition to publishing. [7]

Ellucian’s product page adds a low-code data-orchestration capability, pre-built connectors and APIs, serverless scalable APIs, real-time data sync, and custom transformations. These are vendor product claims rather than a public implementation diagram, but they demonstrate a deliberate move from point-to-point integrations toward a governed integration plane. [5]

**Not publicly verified.** The public sources do not show the complete webhook delivery contract, ordering guarantee, replay window, dead-letter policy, schema registry internals, or whether every Banner/Colleague resource is event-enabled. The official examples show change-notification semantics and a polling consumer; do not infer exactly-once delivery from them.

## Multi-tenancy, hosting, and frontend observations

Ellucian’s Trust Center describes SaaS capabilities across the student lifecycle and lists SOC 2, ISO 27001, UK Cyber Essentials Basic, and NIST 800-171, while also publishing links for a Cloud Disaster Recovery Plan and shared-responsibility materials. It says a UK certification covers segregated AWS networks, but that statement should not be generalized to every Ellucian product or tenant. [27]

Ellucian’s public platform pages describe a central workspace that unifies student, finance, and HCM systems with personalized, role-based dashboards and one access point. [28] The marketing/product frontend is publicly visible, but no authenticated Banner/Colleague/Ethos UI bundle was inspected. The safe conclusion is a SaaS, role-based workspace approach around APIs; the exact client framework is not publicly established.

Banner and Colleague remain relevant as installed or hybrid systems. Ethos reduces direct coupling, but an institution migrating from local Banner/Colleague to Ellucian Cloud still has identity, data-quality, version, and operational boundary problems. The public docs’ customer-center gating is itself evidence that the detailed schema/entitlement surface is controlled rather than openly discoverable.

## Reporting, warehouse, and mobile approach

Ellucian Reporting & Analytics claims pre-built dashboards, role-specific analytics, a single data warehouse, a governed data lake, and data orchestration/custom transformations. [26] The platform’s central workspace exposes dashboards, reports, KPIs, and role-based experiences, while Ellucian’s product portfolio includes transcript exchange and process automation. [28]

**Inference.** Ellucian has made the analytical and experience layers explicit platform products, rather than treating reporting as SQL access to the ERP. That is a good separation of operational, integration, and analytical concerns. It also creates governance requirements: lineage, resource-level consent, cross-module identity resolution, and clear freshness indicators.

The public central-workspace material supports responsive, cross-device access, but does not prove a native mobile architecture. Public app-store listings show Ellucian-branded mobile apps, yet the backend contract and offline behavior are not public. Treat mobile as an API consumer of the same role-aware platform unless tenant-specific evidence says otherwise.

## Security incidents and architectural lesson

NIST’s NVD records CVE-2026-47106 for Banner Self-Service before the April T2 release dated 23 April 2025: stored XSS in course search, where authenticated Banner ERP write access could place payloads in faculty/course fields and an unauthenticated API response could serve them to viewers. NVD describes a medium CVSS-B score and identifies the affected Banner Self-Service line. [8]

This is not an Ethos cloud breach, but it demonstrates the risk of legacy/self-service surfaces adjacent to ERP data. A canonical integration API does not remove the need for output encoding, API-specific authorization, content security policy, and security regression tests in every presentation layer. The architectural lesson is to keep untrusted descriptive fields typed and encoded at every render boundary, and to avoid allowing an unauthenticated read endpoint to become a payload delivery path merely because the underlying fields were written by an authenticated user.

## Specific weaknesses visible from public evidence

* Resource abstraction hides legacy complexity, but versioned schemas and entitlement-dependent resources can become a compatibility matrix that is difficult for open-source adopters to test locally.
* API keys that mint short-lived JWTs are better than long-lived bearer secrets, but public examples do not show per-resource scopes, key rotation UX, or workload identity federation.
* Pub/sub examples show polling and notification semantics, but public evidence does not establish ordering, replay, backpressure, or delivery durability. Integrators must assume they need idempotency and reconciliation.
* Low-code transformations and custom resources improve time-to-value but can create opaque data lineage and “integration logic outside version control” unless every mapping is exportable, reviewable, and testable.
* Legacy Banner/Colleague and modern SaaS surfaces coexist. The migration boundary is a product strength but an operational weakness when identity, audit, and data semantics differ between estates.

# Architecture lessons for a new open-source platform

1. **Use a canonical education domain model plus projections.** Define stable entities and relationships for person, organization, campus/school, academic period, course, section, enrollment, attendance, assessment, grade, credential, program, support plan, finance, and consent. Expose standards projections such as OneRoster and Ed-Fi without allowing either projection to become the only internal model. Preserve source IDs, effective dates, and provenance.

2. **Separate operational, integration, and analytical planes.** Keep the transactional system authoritative for writes. Publish an outbox-backed event stream for integrations. Build a governed analytical store with lineage and freshness metadata. Do not grant reporting users arbitrary database access to production; provide read models, SQL views, or a controlled query service.

3. **Make multi-tenancy explicit in every identifier and policy.** Tenant, institution, campus, and organizational scope should be first-class claims and database partition keys. Enforce row-level authorization at the service boundary and again in analytics. Provide an auditable support plane with just-in-time, tenant-scoped access rather than a support credential that can bulk-read unrelated customer data.

4. **Prefer capability-based extensions over arbitrary plugins.** Offer signed, declarative manifests with named capabilities, scopes, event subscriptions, UI slots, custom fields, and rate limits. Run extension code out of process or in a sandbox. Make every extension install, upgrade, credential rotation, and data export observable. This keeps PowerSchool-like flexibility without allowing a plugin to become an implicit database superuser.

5. **Treat events as a durable contract.** Every event needs an immutable event ID, tenant ID, resource type/version, actor, occurred-at and observed-at timestamps, causation/correlation IDs, before/after or patch semantics where permitted, and a schema URL. Provide replay from a documented retention window, consumer offsets, idempotency keys, dead-letter queues, backoff, reconciliation endpoints, and an explicit ordering guarantee per aggregate.

6. **Support standards with version negotiation and conformance tests.** Implement OneRoster 1.2 and Ed-Fi/other required standards as adapters over the canonical model. Publish OpenAPI documents, JSON Schemas, examples, capability discovery, and a local conformance test suite. Accept that districts will expose multiple versions and make the connector choose capabilities rather than branching on undocumented behavior.

7. **Use modern workload identity and least privilege.** For machine integrations, support OAuth 2.0 client credentials with private-key JWT or mTLS, short-lived access tokens, narrow resource scopes, rotation without downtime, and secretless workload identity where possible. For people, support OIDC and SAML federation, phishing-resistant MFA, SCIM or equivalent lifecycle provisioning, and explicit separation of support/admin identities from customer users.

8. **Design reconciliation as a first-class operation.** Real-time events fail, tenants pause integrations, and standards versions drift. Every connector needs a bounded full sync, delta sync, cursor recovery, conflict policy, dry run, and human-readable error report. Track per-field provenance and never silently overwrite a more authoritative value.

9. **Make custom fields safe and portable.** Store custom definitions as typed, versioned metadata with validation, access policy, retention, export/import, and migration hooks. Do not allow arbitrary SQL or unescaped HTML into core UI paths. Encode at output, sanitize rich text, and maintain security tests for every custom page, report, import, and API projection.

10. **Build mobile and frontend on the same policy-aware API.** A web app, native mobile app, partner integration, and reporting job should receive the same authorization decisions and consistent resource representations. Add offline-safe sync tokens only for data that has an explicit mobile policy. Do not create a second “mobile API” with weaker authorization or untracked fields.

11. **Ship tenant-visible security and operations evidence.** Provide audit logs, export logs, API token inventory, event delivery health, dependency/version inventory, backup-restore tests, and a public status page. Publish security advisories and a supported-version matrix. The PowerSchool and Infinite Campus incidents show why support data, credentials, and operational metadata deserve the same controls as student records.

12. **Keep the open-source boundary honest.** Document what is core, what is an adapter, and what is an optional hosted service. Provide a reference single-node deployment, a horizontally scalable deployment, and migration tooling. An open platform wins not by pretending every institution has one schema, but by making variation explicit, testable, observable, and reversible.

## References

1. PowerSchool administrator documentation: View OAuth Client Credentials - https://ps.powerschool-docs.com/pssis-admin/latest/view-oauth-client-credentials
2. PowerSchool administrator documentation: Universal Rostering - https://ps.powerschool-docs.com/pssis-admin/latest/universal-rostering
3. Infinite Campus Cloud Hosting Services Terms - https://www.infinitecampus.com/terms/cloud-hosting-services-terms
4. Edlink: What data can the Infinite Campus API access? - https://ed.link/community/what-data-can-the-infinite-campus-api-access/
5. Ellucian: Data Orchestration for Higher Education - https://www.ellucian.com/products/platform/data-orchestration
6. Ellucian: Ellucian Platform - https://www.ellucian.com/products/platform
7. Ellucian Ethos Community: Python publish-subscribe demo - https://github.com/ellucianEthos/python-pubsub-demo
8. NIST National Vulnerability Database: CVE-2026-47106 - https://nvd.nist.gov/vuln/detail/CVE-2026-47106
9. PowerSchool public homepage used for REA observation - https://www.powerschool.com/
10. Infinite Campus Digital Learning Partners page used for REA observation - https://www.infinitecampus.com/about/partners/digital-learning-partners
11. Ellucian Ethos Community GitHub organization used for REA observation - https://github.com/ellucianEthos
12. PowerSchool SIS product page - https://www.powerschool.com/products/student-information/sis/
13. PowerSchool administrator documentation: Mobile Apps Setup - https://ps.powerschool-docs.com/pssis-admin/latest/mobile-apps-setup
14. PowerSchool administrator documentation: Configure Global API and SIF Settings - https://ps.powerschool-docs.com/pssis-admin/latest/configure-global-api-and-sif-settings
15. PowerSchool administrator documentation: Install Plugins - https://ps.powerschool-docs.com/pssis-admin/latest/install-plugins
16. PowerSchool Analytics & Insights - https://www.powerschool.com/products/analytics-and-insights/
17. PowerSchool public mobile and family-access claims in SIS product page - https://www.powerschool.com/products/student-information/sis/
18. PowerSchool Security Incident: SIS Incident - https://www.powerschool.com/security/sis-incident/
19. Infinite Campus Digital Learning Partners - https://www.infinitecampus.com/about/partners/digital-learning-partners
20. Infinite Campus Student Information System - https://www.infinitecampus.com/products/student-information-system
21. Infinite Campus Campus Analytics Suite - https://www.infinitecampus.com/products/extension-marketplace/campus-analytics-suite
22. Have I Been Pwned: Infinite Campus Data Breach - https://haveibeenpwned.com/breach/InfiniteCampus
23. UpGuard: Data breach reported for Infinite Campus - https://www.upguard.com/news/infinite-campus-data-breach-2026-03-25
24. Ellucian Ethos Community: C# examples - https://github.com/ellucianEthos/csharp-examples
25. Ellucian Ethos Community: Java examples - https://github.com/ellucianEthos/java-examples
26. Ellucian Reporting & Analytics - https://www.ellucian.com/products/platform/reporting-analytics
27. Ellucian Trust Center - https://trust.ellucian.com/
28. Ellucian Central Workspace - https://www.ellucian.com/products/platform/central-workspace
