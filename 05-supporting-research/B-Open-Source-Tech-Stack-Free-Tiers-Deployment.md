# Open-source technical approach for a modern multi-tenant school and higher-education platform

**Evidence checked: 27 November 2026.** Prices, quotas, plan names, repository metadata, and licensing can change. The provider figures below are transcribed from the official pages opened for this report; GitHub stars and activity were read from the GitHub API on 27 November 2026.

## Recommendation in one sentence

Build a modular monolith around PostgreSQL with database-enforced row-level security, an explicit tenant and institution model, an append-only audit/event log, OIDC/WebAuthn authentication, object storage, a queue, and a PWA-first frontend; deploy the same containers on a VPS with Coolify or Dokploy for production, while using Cloudflare Pages/Workers for the public edge and static assets. Do not make a free-tier provider the system of record for student data, and do not choose a source-available component merely because its repository is public.

## What “fully open source” should mean here

For this product, “open source” should mean software under an OSI-approved license that permits commercial use, modification, redistribution, and operation as a hosted service, subject to notice and copyleft obligations. MIT, Apache-2.0, BSD, and MPL-2.0 are normally the easiest licenses for a proprietary or open-core application. LGPL permits linking with fewer obligations than GPL, while changes to the LGPL library itself must remain available under the license. GPL-3.0 and AGPL-3.0 are commercial-use licenses, not non-commercial licenses: they require preservation of freedoms and, for AGPL software offered over a network, source availability for the covered work and modifications.

AGPL is an application-level compliance choice, not a reason to avoid a component. It becomes a problem when the team wants to hide modifications to an AGPL application or combine it with proprietary code without taking advice. The safe practice is to keep copyleft applications as separately deployed services, publish required source and notices, and inventory every dependency.

BSL, FSL, Sustainable Use License, “community license,” and other source-available terms are not OSI open source when they restrict production or commercial use. They can still be useful, but they must be approved as a separate commercial dependency. n8n is explicit that its Sustainable Use License restricts use to internal business or non-commercial use and requires a commercial agreement for some productized or customer-facing uses.[38] PowerSync’s open-source components are Apache-2.0/MIT, but some enterprise features are separate; Zero’s client and server are Apache-2.0.[30] [31]

## Platform design principles

### Tenant model and data isolation

Use one logical PostgreSQL cluster and one shared schema for the normal SaaS deployment. Every business table should carry `tenant_id` and, where relevant, `institution_id`, `campus_id`, `academic_year_id`, and `data_classification`. Use composite unique keys such as `(tenant_id, student_number)`, never a global student number. Put tenant context in a short-lived, signed token and set a transaction-local database setting before queries. Enable RLS on every tenant table; use both `USING` and `WITH CHECK` policies and test them with non-owner database roles. PostgreSQL documents that enabled RLS becomes default-deny when no policy exists, but table owners, superusers, and `BYPASSRLS` roles can bypass it, so the application must not connect as an owner or superuser.[27]

Keep a small, privileged control plane for tenant provisioning, billing, feature flags, schema migrations, and support access. Support impersonation must be time-limited, explicitly consented, reason-coded, read-only by default, and recorded in an immutable audit log. For a high-assurance institution, offer a dedicated database or cluster as an isolation tier rather than forcing every customer into database-per-tenant.

### Core domain boundaries

The minimum domain modules are identity and organizations; student/learner and guardian records; admissions and enrollment; programs, courses, sections, and timetables; attendance; assessment and gradebook; transcripts and credentials; fees, invoices, payments, refunds, and concessions; HR and payroll; library, hostel, transport, inventory, and assets; communications; workflow and approvals; learning content and video integrations; reports; and platform administration.

Use an event/outbox table for changes that must reach search, notifications, analytics, or an offline client. A worker consumes the outbox, publishes idempotent messages, and records a delivery key. Avoid distributed transactions: commit domain data and its outbox record together, then retry external work. Use temporal or versioned academic data so changes to a timetable or grade are auditable rather than destructive.

### Security baseline

Use OIDC/OAuth 2.1 for web and mobile sessions, short-lived access tokens, rotating refresh tokens, device/session revocation, MFA for staff, and phishing-resistant passkeys where supported. WebAuthn Level 3 became a W3C Recommendation on 25 August 2026 and defines public-key credentials scoped to a relying party; it is the right standard for passkeys, but recovery and cross-device enrollment still need careful product design.[46]

Use secure, same-site cookies for browser sessions; CSRF protection for cookie-authenticated mutations; strict origin and content-security policies; input validation; rate limits on login, OTP, exports, and bulk imports; encrypted backups; application-level envelope encryption for particularly sensitive fields; and tenant-aware access logs. Never put a service-role key in a browser or mobile bundle. Treat uploaded identity documents and student photographs as sensitive objects with private buckets, short-lived signed URLs, malware scanning, retention policy, and deletion workflows.

## Best open-source application stack

### Web and API

**Recommended default:** TypeScript with Next.js or SvelteKit for the web/PWA, Hono for small edge APIs, and a conventional Node.js service for long-running jobs. Next.js has the broadest React hiring and integration ecosystem; SvelteKit is a clean alternative for a smaller, fast frontend; Nuxt is the analogous Vue option. React Router is a good routing/data layer when the team wants a deliberately assembled React app rather than a framework-owned full stack. Hono is especially attractive for Cloudflare Workers.

For a large, strongly structured backend, NestJS provides a familiar module/decorator architecture. Django is an excellent alternative when Python reporting, education integrations, or AI is central; Laravel is productive for PHP teams and interoperates naturally with the existing education ERP ecosystem; Go is a good fit for high-throughput, small operational services. Do not split a school ERP into microservices at the start: a modular monolith with explicit boundaries is easier to secure, migrate, and deploy.

### Mobile, PWA, and desktop

Make the browser/PWA the primary client. It gives schools and universities the widest reach, supports installability and offline caching, and avoids app-store delays for most administrative workflows. Use Expo/React Native when the web team is TypeScript/React-oriented and native push, camera, biometrics, or background work matter. Use Flutter when a strong single UI codebase across Android/iOS is more important than sharing React code. Capacitor is the lowest-friction route from a polished web app to app-store shells, but native background behavior can require plugins and platform-specific work.

Use Tauri for an optional lightweight desktop shell with a Rust core and system webview. Use Electron only when the team needs its mature Chromium runtime, broad native ecosystem, or guaranteed rendering consistency and accepts larger binaries and memory usage. A desktop client should be an offline kiosk or local-agent enhancement, not a second source of business rules.

### Database

PostgreSQL is the system of record. It gives transactions, constraints, JSONB, full-text search, extensions, logical replication, mature backup tools, and RLS. Add `pgvector` only for semantic features; ordinary SIS queries should use relational indexes and materialized reporting tables.

SQLite is excellent for a local client, a kiosk, a small deployment, or an embedded cache. SQLite is an in-process, serverless, zero-configuration SQL engine, which makes it ideal for offline-first local state but not a network multi-tenant primary database.[26] libSQL/Turso-style SQLite extensions and embedded replicas are worth evaluating for edge/local workloads, but they do not replace PostgreSQL’s RLS and operational ecosystem for the authoritative shared record.

### Authentication choices

Keycloak is the conservative default for a multi-application, self-hosted institution: OIDC, OAuth 2.0, SAML, LDAP/AD federation, identity brokering, admin console, and fine-grained authorization are documented capabilities.[41] It is Java-based and operationally heavier than an in-process library. Authentik is a flexible self-hosted IdP with OAuth2, SAML, LDAP, and SCIM and an explicit forever-free open-source core plus source-available enterprise features.[42] ZITADEL is API-first and multi-tenant at the organization/project level, with passkeys and self-hosting; verify the exact edition license and enterprise boundary before embedding it into a resold SaaS.[43] Ory provides modular open-source components and an enterprise license/cloud split, which is powerful but demands license review for production features.[44]

Better Auth is the best fit when the application wants auth to live in TypeScript and in the same database. Its plugin model includes organizations, two-factor authentication, passkeys, OAuth, and sessions, but its hosted dashboard/enterprise add-ons are separate from the core library.[45] For a serious education platform, prefer Keycloak or ZITADEL at the institution boundary and Better Auth only when the product intentionally owns the entire auth surface.

## Offline and local-first synchronization

Offline mode should be selective. Attendance taking, grading drafts, timetable viewing, messaging drafts, and field-work forms are good candidates; fee settlement, final result publication, identity changes, and destructive administration should require online confirmation.

Electric Sync is a read-path sync engine for PostgreSQL: it sends authenticated subsets (“Shapes”) over HTTP into local clients and provides self-hosting guidance.[29] PowerSync provides SQLite-based client sync and a broad set of Apache-2.0/MIT SDKs, including Flutter, React Native, web, Node, Capacitor, Tauri, Kotlin, Swift, and .NET.[30] Zero is Apache-2.0 and integrates with Postgres, React, and React Native.[31] Replicache is a proven client-sync model but should be license-checked for current commercial terms before adoption. RxDB is a useful local database with sync plugins and a commercial professional layer; do not assume every plugin is MIT.

Use Yjs or Automerge only for genuinely collaborative documents, such as shared lesson plans or collaborative notes. Yjs is a high-performance CRDT whose shared types merge concurrent changes without conflicts and whose network provider is intentionally separate from the CRDT.[32] CRDTs do not solve authorization, academic conflict policy, or auditability; define server-side acceptance rules and preserve the original operations.

## Search, storage, notifications, and media

**Search:** Start with PostgreSQL full-text search and trigram indexes. Add Meilisearch Community Edition when student/course/document search needs typo tolerance and faceting; Community Edition is MIT, while its enterprise edition is BUSL and cannot be freely used in production.[33] Typesense is an alternative with GPL-3.0, self-hosting, scoped API keys, typo-tolerant/vector/hybrid search, and Raft clustering; the GPL obligation should be isolated as a service and reviewed for the intended distribution model.[34]

**Object storage:** Use S3-compatible storage behind an application-owned abstraction. Cloudflare R2 is attractive for public-edge deployments because its standard tier includes 10 GB-month storage, 1 million Class A operations, 10 million Class B operations, and free internet egress per month.[3] For a self-hosted stack, Garage is a lightweight S3 implementation designed for small hardware, with a single binary, 1 GB RAM guidance, and three-zone replication as its design target.[36] SeaweedFS is another strong S3/file storage option for a larger cluster. Treat MinIO carefully: as of the checked 2026 page, MinIO says the original AGPLv3 community edition is frozen and no longer receives fixes, while AIStor is commercially licensed; AIStor Free is single-node and redistribution is prohibited.[35] That makes MinIO a poor new dependency for a fully open, redistributable platform.

**Notifications:** Use an application notification table plus a queue and provider adapters. Web Push is the baseline for the PWA; FCM/APNs are needed for native mobile delivery. ntfy is a simple self-hostable topic-based push option for operational alerts, not a complete student-notification workflow. Novu can provide templates, inboxes, and channel orchestration, but its self-hosting edition and current license boundary need review. Keep SMS, WhatsApp, and email adapters replaceable because the carrier/provider cost is not open-source infrastructure.

**Video:** Jitsi Meet is a good meeting component; BigBlueButton is education-oriented and explicitly allows educational or commercial integration under LGPL, with trademark conditions separate from code.[40] LiveKit is a strong programmable WebRTC server/SDK for embedded live classes and events; budget for TURN, recording, and egress. Video should be a linked service with its own retention and consent policies rather than a core SIS table.

## Workflow, reporting, AI, and observability

Temporal is the strongest open-source durable-workflow choice for admissions pipelines, scheduled fee reminders, transcript generation, imports, and long-running approvals. Its official self-host guide covers Docker/Kubernetes/manual deployment, namespaces, TLS/mTLS, authorization, monitoring, archival, and multi-cluster replication.[37] It is more operationally demanding than a queue plus idempotent worker. Use a simple outbox/worker first and adopt Temporal for workflows that genuinely need durable timers, compensation, or human-in-the-loop state.

n8n is excellent for internal integration automation, but its Sustainable Use License is not OSI open source and restricts customer-facing productized use. Do not expose an n8n editor to each institution or make n8n the licensed core of the SaaS without a commercial agreement.[38]

For BI, expose a read-only reporting database or warehouse. Apache Superset is Apache-licensed and supports SQL exploration, dashboards, caching, templating, and many databases.[39] Metabase is easier for non-technical staff but has an open-core/edition boundary that should be checked for embedding and commercial redistribution. Prefer Superset for a broad open-source posture and a custom, tenant-filtered reporting API for the most sensitive dashboards.

For AI, use retrieval over institution-approved documents with tenant-filtered search and explicit citations. Qwen, Llama, Gemma, and Mistral model families have different model-specific terms; “open weights” is not the same as OSI open source. Confirm the exact checkpoint license, acceptable-use policy, attribution, and redistribution conditions before shipping. Serve a small quantized model through Ollama or llama.cpp for local development and offline pilots; use vLLM for GPU-backed concurrent serving. IndicTrans2 from AI4Bharat supports all 22 scheduled Indian languages and is a practical translation layer for UI, notices, and search, subject to its repository/model/data licenses.[57] Bhashini can provide Indian-language services where an external government/API dependency is acceptable. Keep AI optional, auditable, and incapable of changing grades, attendance, or financial records without a human-authorized workflow.

Use OpenTelemetry instrumentation in the web, API, workers, database exporter, and mobile client. A self-hosted Grafana LGTM stack—OpenTelemetry Collector, Grafana, Loki, Mimir/Prometheus, and Tempo—is a reasonable starting point; Grafana documents a Docker OTEL-LGTM image for development/demo and self-managed environments.[58] For production, separate tenant-safe logs from high-cardinality traces, redact student data at source, keep audit events in the database/object store, and define retention by data class.

## Current free and nearly-free deployment options

The following figures were checked on 27 November 2026. Free plans are useful for prototypes, demos, CI, and non-sensitive public components. They are not a substitute for backups, a recovery plan, or a contractual production service.

| Provider | Current free/entry facts from official pages | Commercial/production warning | Fit |
|---|---|---|---|
| Cloudflare Workers/Pages | Workers Free: 100,000 requests/day and 10 ms CPU/invocation; static assets are free/unlimited. KV: 100,000 reads/day, 1,000 writes/deletes/lists/day, 1 GB, 1,000 namespaces. Queues: 10,000 operations/day, 10,000 queues, 24-hour retention. D1: 5m rows read/day, 100k rows written/day, 5 GB total, 10 databases. SQLite Durable Objects: 100k requests/day, 13,000 GB-s/day, plus D1-like SQLite storage limits. Paid Workers starts at $5/month.[1] [2] [4] [5] [6] | Free quotas stop operations at the limit. D1/DO are SQLite-oriented and do not replace Postgres RLS. Check commercial use in the account terms; the main risk is quota/operational fit, not an advertised non-commercial restriction. | Excellent edge, PWA/static delivery, webhooks, cache, small queues; keep the authoritative SIS in Postgres. |
| Cloudflare R2 | 10 GB-month, 1m Class A, 10m Class B, and free egress monthly on Standard storage.[3] | Usage is metered beyond the tier; no managed relational semantics. | Excellent uploads and downloads with egress-sensitive media. |
| Supabase | Free: 2 active projects, 500 MB database, 50k MAU, 5 GB egress, 1 GB file storage, unlimited API requests; projects pause after one week inactivity. Pro starts at $25/month with 8 GB disk/project, 250 GB egress, 100 GB storage, daily backups, and $10 compute credits.[7] | The free plan is not a production backup/SLA tier and pauses. RLS must be designed correctly; platform keys must stay server-side. | Fastest managed Postgres/Auth/Storage prototype; production path at $25+ or self-hosted Postgres. |
| Neon | Free is permanent: 100 projects, 100 CU-hours/project, 1 GB/project, 20 GB account total, 5 GB public transfer/project, scale-to-zero; no card required. Paid Launch is usage-based; the page gives an example of about $15/month for intermittent load.[8] | Free limits suspend compute or block writes when hit. A database-per-tenant prototype is possible, but 100 projects is not a production tenancy promise. | Strong database branching and prototyping; excellent for isolated demo tenants. |
| Vercel Hobby | $0; 1m CDN requests/month, 100 GB transfer, 4 CPU-hours, 360 GB-hours memory, 1m function invocations, 200 projects, 100 deployments/day. Hobby has no billing cycle and exhausted features wait for reset; Pro is $20/month.[9] [10] | The Hobby plan is intended for personal/non-commercial use in Vercel’s plan terms; do not use it as the production home of a commercial school SaaS without confirming the current terms. | Frontend previews and static/SSR prototypes; use Cloudflare or self-hosted production for a commercial open stack. |
| Netlify | New accounts use credit pricing: Free is $0 with a 300-credit limit, custom domains/SSL, previews, functions, database/blob features, and CDN; production deploys cost 15 credits, compute 10 credits/GB-hour, bandwidth 20 credits/GB, web requests 2 credits/10k.[11] | The new credit model replaced legacy plans for new accounts from 4 Sep 2025. Credit exhaustion and account behavior must be monitored; do not assume old 100 GB/300 build-minute figures. | Static/PWA hosting and previews; not a database or core backend. |
| Render | Hobby workspace is $0 plus compute; Free compute is 512 MB and includes 750 free instance hours/workspace/month. Free web services sleep after 15 minutes, have ephemeral files, and free Postgres is 1 GB, expires after 30 days, has no backups/pooling, and should not be used for production.[12] [13] | Render explicitly says free instances are for testing/hobby/preview, not production. | Good test environment and review apps. |
| Fly.io | Personal Free plan: $1 one-time credit without a card, $5 monthly usage after adding a card, max 3 Machines, 5 GB volumes, one Developer Managed Postgres, and one member. A 256 MB always-on shared Machine is $2.19/month in listed regions; egress rates vary and India is listed at $0.12/GB.[14] [15] | When $5 is exhausted, the organization moves to Pay As You Go and bills the month from the first cent. | Small self-managed production edge or worker if billing is watched; not the cheapest database HA. |
| Railway | Free: $1 monthly usage credit, services wake on request, up to 1 vCPU/0.5 GB per service and 0.5 GB volume, no card required; first 30-day trial has $5 credits. Hobby is $5 minimum and includes $5 credits.[16] | Usage-based and sleep/wake behavior can surprise interactive workloads; check current plan terms before selling it as production infrastructure. | Very convenient demos and small internal services. |
| Oracle Cloud Always Free | Always Free services are unlimited in time; the account also offers $300 for 30 days. The catalog includes AMD and Ampere compute, block/object/archive storage, load balancers, databases, networking, monitoring, logging, vault, notifications, and more.[17] | Capacity is not guaranteed, one free account per person, idle accounts may be suspended/terminated, and one account is allowed per person. | Best zero-cost VM opportunity when capacity is available; design for region loss and backup elsewhere. |
| Google Cloud | New customers receive $300 credit; 20+ products have monthly free quotas not charged against the credit. The exact free limits vary by product and region; free-tier docs must be consulted per service.[18] | Card/billing setup and quota boundaries matter; free quotas are not a production SLA. | CI, Cloud Run experiments, and selected edge/stateless services. |
| GitHub | GitHub Free personal accounts include 500 MB Packages storage, 120 Codespaces core hours and 15 GB storage/month, $12 included compute/month, and GitHub Pages for public repositories.[19] Actions standard runners are free for public repositories and self-hosted runners; private free accounts have 500 MB artifact/package storage and $12 compute/month.[20] Codespaces Free is 120 hours and 15 GB-month; Pro is 180 hours/20 GB.[21] | GHCR/Packages shares storage allowances with Actions artifacts; public packages are appropriate for open images, but private packages consume quota. Pages is static/public-oriented, not an app backend. | Source control, CI, Pages docs/demo, public container images, and reproducible releases. |
| Hetzner | Cloud entry pages list Cost-Optimized from €5.99/month and Regular Performance from €5.49/month excluding VAT; dedicated General Purpose starts at €36.99/month. IPv4 is an additional €0.50/month in the docs, IPv6 is free, firewalls are free, and the platform offers private networks, volumes, backups, API, and one-click apps.[22] | You operate backups, patching, abuse response, database HA, and incident response. Price varies by location and plan changes; confirm checkout price. | Best value for a small production cluster or single-server Coolify deployment. |

### Commercial-use conclusion for hosted free tiers

The safest commercial posture is to treat free tiers as development, public assets, previews, or a temporary pilot unless the provider’s current terms clearly permit the specific commercial workload. Vercel Hobby is the clearest “do not assume commercial SaaS” case. Render explicitly excludes production. Oracle, Fly, Railway, Supabase, Neon, Cloudflare, GitHub, Netlify, and Google are primarily quota, capacity, billing, and account-policy questions, but legal terms and acceptable-use policies still govern. Record the plan page and terms URL in an infrastructure bill of materials and recheck quarterly.

## Self-hosted PaaS choices

Coolify is the default recommendation for a small team: self-hosted is free forever with all features, while Coolify Cloud is $5/month for two connected servers plus $3 per additional server.[24] It deploys containers, databases, services, domains, TLS, backups, and environment variables, but the operator still owns the server, patches, backups, and monitoring.

Dokploy’s January 2026 announcement says the current codebase is Apache-2.0 and freely usable, modifiable, redistributable, and resellable outside future `proprietary/` source-available components.[25] It is a good option when a simpler Docker deployment surface is preferred, but future enterprise boundaries must be watched.

CapRover is a mature Docker/Swarm-oriented self-hosted app platform with 300+ one-click apps, automatic HTTPS, deployment history, workers, and Compose stacks; its docs state a 1 GiB RAM minimum.[26] It is lightweight but less opinionated about the full production operating model than Coolify. For a single VPS, choose Coolify or Dokploy; for a tiny constrained host, CapRover remains viable.

## Existing open-source education systems: useful reference, not a turnkey foundation

The current repository landscape shows that mature products tend to be PHP/Rails/Python monoliths with valuable domain workflows, but none is a drop-in answer for a modern multi-tenant, RLS-first, offline-capable platform.

| Project | GitHub snapshot on 27 Nov 2026 | Stack/license and observed scope | Lesson |
|---|---:|---|---|
| openSIS Classic | 353 stars, 291 forks, 498 commits; pushed 26 Oct 2026 | PHP with Apache and MySQL/MariaDB; GPL; students/staff/schools, scheduling, attendance, grades, gradebook, reports, transcripts, communications, imports.[47] | Broad SIS feature map and higher-education ambition, but legacy PHP/MySQL conventions mean a security and tenant-isolation audit is essential. |
| RosarioSIS | 658 stars, 400 forks, 8,089 commits; pushed 25 Nov 2026 | PHP; PostgreSQL or MySQL/MariaDB; GPL-2.0; extensive school workflows, gradebook, scheduling, attendance, discipline, fees, reports, plugins.[48] | The strongest long-lived K-12 workflow reference; plugin/customization model is useful, but modern mobile/offline and cloud tenancy need new architecture. |
| Gibbon | 644 stars, 435 forks, 7,506 commits; pushed 26 Nov 2026 | PHP/Apache/MySQL with Docker dev setup; GPL-3.0; modules/themes, role-oriented school management, notifications, parent/teacher flows.[49] | Good modularity, translation and Docker practices; preserve the idea of extension modules but use API/event contracts and tests for tenant safety. |
| Frappe Education | 718 stars, 509 forks, 1,097 commits; pushed 23 Nov 2026 | Python/JavaScript on Frappe/ERPNext, MariaDB, Vue-based Frappe UI; education app includes student/teacher, admissions, fees, scheduling, exams and student portal; Frappe framework is MIT.[50] [56] | The best ERP extensibility and accounting/inventory integration story; evaluate Frappe if adopting a Python/MariaDB ERP rather than building a greenfield Postgres platform. |
| OpenEduCat Community | 915 stars, 794 forks, 1,715 commits; pushed 25 Nov 2026 | Odoo/Python module ecosystem; LGPL-3.0; admissions, student information, courses, exams, fees, attendance, library, transport, hostel, HR/payroll and reporting.[51] | Very broad module coverage and a permissive copyleft boundary, but verify community/enterprise feature splits before embedding in a commercial product. |
| Fedena | 547 stars, 560 forks, 1,472 commits; last code push May 2020 | Ruby on Rails; Apache-2.0; school/campus records.[52] | A historically influential open architecture, but low recent code activity makes it a reference and migration source, not a new core. |
| Moodle | 7,649 stars, 7,730 forks, 123,629 commits; pushed 24 Nov 2026 | PHP/JavaScript; GPL-3.0; learning platform, plugins, courses and assessment.[53] | Use as the LMS integration target, not as the SIS/ERP core. Its ecosystem and plugin discipline are major assets. |
| Open edX | 8,255 stars, 4,390 forks, 68,963 commits; pushed 26 Nov 2026 | Python/Django plus React micro-frontends; AGPL-3.0; LMS and Studio, modular monolith plus independently deployable apps.[54] | Powerful course delivery and authoring, but production deployment is complex and it is not a registrar/fees/attendance system. Integrate through LTI/REST/events. |
| Canvas LMS | 6,926 stars, 3,068 forks, 78,765 commits; pushed 10 Nov 2026 | Ruby with JavaScript, PostgreSQL/Redis ecosystem; AGPL-3.0.[55] | Strong LMS interoperability and course workflows; use as an external LMS or study its APIs rather than rebuilding its surface inside the SIS. |

Stars are popularity signals, not security or maintenance scores. Commit counts and recent push timestamps show active repositories, but they do not establish release quality, vulnerability response, data-protection posture, or commercial support. The older Fedena push history is the clearest warning against selecting solely by features.

## Reference architecture

```text
                 DNS/CDN/WAF/TLS (Cloudflare)
                              |
        PWA / Next.js or SvelteKit / mobile API clients
                              |
                    API gateway / Hono or NestJS
                              |
      +-----------------------+------------------------+
      |                        |                        |
  Modular SIS app        Auth / OIDC / WebAuthn    Read-only reporting API
  (domain + RLS)         Keycloak or ZITADEL         + Superset
      |                        |                        |
  PostgreSQL + RLS      sessions/claims/roles       warehouse/read replica
      |
  outbox + audit log ---- Queue/worker ---- search / notifications / media
      |                         |              |          |
  offline sync              object store     Meili/       R2/S3/Garage
 Electric/PowerSync/Zero    signed objects   Typesense
      |
  OpenTelemetry -> Collector -> Grafana/Loki/Tempo/Prometheus
```

A practical code layout is a monorepo with `apps/web`, `apps/api`, `apps/worker`, `apps/mobile`, `packages/domain`, `packages/db`, `packages/auth`, `packages/ui`, and `infra`. Put schema migrations, RLS policies, seed data, and policy tests in version control. Every feature should declare its tenant boundary, audit events, authorization rules, retention policy, offline behavior, and reporting exposure before implementation.

Use a primary Postgres database, a read replica or reporting database for dashboards, and an object store for files. Redis/Valkey is useful for ephemeral cache and rate limits, not as the record of attendance or payment. Search indexes are derived and rebuildable. Notifications and workflow state are derived from the durable outbox. This makes disaster recovery tractable.

## Zero-cost development and pilot path

1. Keep source, issues, CI, public container images, and static docs on GitHub Free. Use public-repository Actions or a self-hosted runner; do not store student data in Actions artifacts.[19] [20]
2. Host the PWA and documentation on Cloudflare Pages/Workers or GitHub Pages. Use Cloudflare WAF/DNS, but keep secrets and database credentials out of the edge bundle.[1]
3. Use Neon Free or Supabase Free for a disposable development database. Seed synthetic data only. Neon is better for many isolated demo projects; Supabase is faster for an integrated auth/storage prototype.[7] [8]
4. Use Cloudflare R2 for synthetic document/media tests, or local MinIO alternatives only if their current license and maintenance status are acceptable. R2’s free tier is sufficient for small demos.[3]
5. Run Keycloak, the API, worker, search, and observability locally with Docker Compose. Use Electric/PowerSync/Zero only for an offline proof of concept with synthetic data.[29] [30] [31]
6. Use free-tier Render, Railway, or Fly only for preview environments and demos. Render Free Postgres expires in 30 days and has no backups, so it must never be the source of truth.[13]

Expected cash cost is $0 if existing domains, cards, and developer hardware are excluded. The hidden cost is engineer time, and the free-tier limits must be treated as deliberate failure tests: paused databases, quota exhaustion, lost ephemeral files, and service restart.

## Low-cost production path

A credible small production deployment is one Hetzner shared cloud VM in the €5.49–€5.99/month class, or a similar 2–4 GB VPS, running Debian/Ubuntu, Docker, Coolify or Dokploy, Caddy/Traefik, the modular API, worker, Postgres, Valkey, Meilisearch Community, and an OpenTelemetry/Grafana-lite stack. Add an encrypted off-host backup destination and a second low-cost VM or managed database before onboarding institutions with consequential records. Hetzner lists free firewalls and private networking but bills public IPv4 separately; include VAT, IP, backups, and snapshots in the budget.[22] [23]

A realistic monthly envelope is:

| Stage | Expected monthly infrastructure cost | What it contains |
|---|---:|---|
| Pilot, one institution, low traffic | €6–€20 plus domain/email/SMS | One VPS, Coolify/Dokploy, Postgres, object storage on VPS or R2, daily off-host encrypted backups, Cloudflare DNS/WAF. |
| Small production, several institutions | €25–€75 | 4–8 GB application/database node or two smaller nodes, separate backup target, R2 or Garage, managed email/SMS usage, external uptime checks, stronger monitoring. |
| Production with managed database | $25–$80 plus compute and storage | Supabase Pro or a paid Postgres equivalent, one or two application VPSs, R2, backups, search, transactional email/SMS. Supabase Pro starts at $25 and its first Micro compute is covered by $10 credits, but additional projects/usage add cost.[7] |
| Higher assurance | $100–$300+ | HA/replication, separate reporting and search nodes, multi-region/object replication, managed backups, support, incident response, and paid messaging/video/AI. |

These are engineering estimates, not vendor quotes. They exclude staff, domain registration, taxes, transactional email/SMS/WhatsApp, app-store fees, TURN/video egress, payment processing, legal review, compliance audits, and GPU inference. For Indian deployments, Fly.io’s published India egress rate is materially higher than North America/Europe, so serve large media from R2 or a regional object store and keep the transactional database near the application.[14]

## Migration and delivery roadmap

**Phase 0: threat model and tenancy proof.** Model roles, institutions, data classifications, retention, consent, audit events, recovery objectives, and the tenant contract. Build a small Postgres schema with RLS policy tests and an authorization matrix before UI polish.

**Phase 1: registrar core.** Ship organizations, people, student lifecycle, programs, courses, sections, attendance, grading drafts, academic periods, files, notifications, and audit log. Add CSV import/export with staged validation and a human approval step.

**Phase 2: operational ERP.** Add admissions, fees, invoices, payments, concessions, HR, payroll, library, transport, hostel, and integrations. Keep finance ledgers immutable and integrate payment providers through idempotent webhooks.

**Phase 3: offline and ecosystem.** Add offline attendance/field forms, sync conflict policies, PWA installability, mobile push, LTI/OneRoster/SIS exports, Moodle/Open edX/Canvas integrations, search, BI, and video.

**Phase 4: scale and assurance.** Separate read models, add replicas, backup restore drills, external penetration testing, disaster-recovery exercises, rate-limit dashboards, data-subject export/deletion, key rotation, per-tenant quotas, and dedicated deployment tiers.

## Final choice matrix

| Decision | Recommended | Why |
|---|---|---|
|System of record|PostgreSQL + RLS|Transactions, constraints, extensions, mature operations, direct tenant enforcement.[27]|
|Backend shape|Modular monolith, TypeScript/NestJS or Python/Django|Lower operational and authorization complexity than early microservices.|
|Frontend|PWA-first Next.js/SvelteKit|One web surface, installable/offline-capable, good accessibility and responsive administration.|
|Auth|Keycloak for institution-grade federation; Better Auth for embedded TypeScript auth|OIDC/SAML/LDAP versus in-process developer velocity; WebAuthn/passkeys for staff.[41] [45] [46]|
|Sync|PowerSync or Electric first; Zero where its model fits|Postgres-aware partial replication, mobile/Flutter/React Native options, clear licenses.[29] [30] [31]|
|Search|Postgres first; Meilisearch CE or Typesense when needed|Derived, rebuildable indexes; license and scale boundaries are explicit.[33] [34]|
|Objects|R2 managed; Garage self-hosted|Low egress or open self-hosting; avoid new dependence on frozen MinIO OSS.[3] [35] [36]|
|Workflow|Outbox + worker first; Temporal for durable long processes|Avoid premature platform complexity; gain timers/retries/visibility when needed.[37]|
|BI|Custom tenant-filtered reporting API + Superset|Open dashboarding without exposing the primary write database.[39]|
|Observability|OpenTelemetry + Grafana/Loki/Tempo/Prometheus|Portable instrumentation and self-hosted control.[58]|
|Deployment|Coolify on Hetzner for low-cost production|Simple containers, TLS, backups and no PaaS license fee; migrate to Kubernetes only when operations justify it.[22] [24]|

The resulting product is not “free” in the sense of zero effort. It is free of per-seat and proprietary platform lock-in at the core, while keeping managed services interchangeable. That is the sustainable balance for a secure education platform: open standards and open-source business logic, a boring relational core, explicit tenant enforcement, derived services, tested backups, and a deployment path that can start at zero and move to a €10–€100/month operating envelope without rewriting the product.

## References

1. Cloudflare Workers plans and pricing - https://developers.cloudflare.com/workers/platform/pricing/
2. Cloudflare D1 pricing - https://developers.cloudflare.com/d1/platform/pricing/
3. Cloudflare R2 pricing - https://developers.cloudflare.com/r2/pricing/
4. Cloudflare Workers KV pricing - https://developers.cloudflare.com/kv/platform/pricing/
5. Cloudflare Queues pricing - https://developers.cloudflare.com/queues/platform/pricing/
6. Cloudflare Durable Objects pricing - https://developers.cloudflare.com/durable-objects/platform/pricing/
7. Supabase pricing - https://supabase.com/pricing
8. Neon pricing plans - https://neon.tech/pricing
9. Vercel pricing - https://vercel.com/pricing
10. Vercel Hobby plan limits - https://vercel.com/docs/accounts/plans/hobby-plan
11. Netlify pricing - https://www.netlify.com/pricing/
12. Render pricing - https://render.com/pricing
13. Render free services limitations - https://render.com/docs/free
14. Fly.io resource pricing - https://fly.io/docs/about/pricing/
15. Fly.io Free plan - https://docs.fly.io/about/free-plan/
16. Railway pricing - https://railway.com/pricing
17. Oracle Cloud Free Tier - https://www.oracle.com/cloud/free/
18. Google Cloud Free Tier - https://cloud.google.com/free
19. GitHub plans and included usage - https://docs.github.com/get-started/learning-about-github/githubs-products
20. GitHub Actions billing - https://docs.github.com/billing/managing-billing-for-github-actions/about-billing-for-github-actions
21. GitHub Codespaces billing - https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces
22. Hetzner Cloud hosting and pricing - https://www.hetzner.com/cloud/
23. Hetzner Cloud server overview and network pricing - https://docs.hetzner.com/cloud/servers/overview/
24. Coolify pricing and self-hosting - https://coolify.io/pricing
25. Dokploy open-source license update - https://dokploy.com/blog/we-are-updating-dokploys-open-source-license
26. CapRover self-hosted app hosting - https://caprover.com/
27. PostgreSQL row security policies - https://www.postgresql.org/docs/current/ddl-rowsecurity.html
28. SQLite serverless architecture - https://www.sqlite.org/serverless.html
29. Electric Sync documentation - https://electric.ax/docs/sync/
30. PowerSync open-source components and licenses - https://powersync.com/open-source
31. Zero open-source license - https://zero.rocicorp.dev/docs/open-source
32. Yjs collaborative CRDT documentation - https://docs.yjs.dev/
33. Meilisearch Community and Enterprise licensing - https://www.meilisearch.com/docs/resources/self_hosting/enterprise_edition
34. Typesense self-hosting and license comparison - https://typesense.org/typesense-vs-algolia/
35. MinIO AIStor and community-edition licensing status - https://www.min.io/pricing
36. Garage S3-compatible object storage - https://garagehq.deuxfleurs.fr/
37. Temporal self-hosted service guide - https://docs.temporal.io/self-hosted-guide
38. n8n Sustainable Use License - https://docs.n8n.io/n8n-community-license
39. Apache Superset official project - https://superset.apache.org/
40. BigBlueButton open-source license - https://bigbluebutton.org/open-source-project/open-source-license/
41. Keycloak open-source identity and access management - https://www.keycloak.org/
42. Authentik documentation and editions - https://docs.goauthentik.io/
43. ZITADEL identity infrastructure - https://zitadel.com/
44. Ory identity deployment options - https://www.ory.sh/
45. Better Auth framework - https://www.better-auth.com/
46. W3C Web Authentication Level 3 Recommendation - https://www.w3.org/TR/webauthn-3/
47. openSIS Classic repository - https://github.com/OS4ED/openSIS-Classic
48. RosarioSIS repository - https://github.com/francoisjacquet/rosariosis
49. Gibbon core repository - https://github.com/GibbonEdu/core
50. Frappe Education repository - https://github.com/frappe/education
51. OpenEduCat Community repository - https://github.com/openeducat/openeducat_erp
52. Fedena repository - https://github.com/projectfedena/fedena
53. Moodle repository - https://github.com/moodle/moodle
54. Open edX platform repository - https://github.com/openedx/edx-platform
55. Canvas LMS repository - https://github.com/instructure/canvas-lms
56. Frappe Framework repository - https://github.com/frappe/frappe
57. AI4Bharat IndicTrans2 - https://github.com/AI4Bharat/IndicTrans2
58. Grafana OpenTelemetry LGTM stack - https://grafana.com/docs/opentelemetry/docker-lgtm/
