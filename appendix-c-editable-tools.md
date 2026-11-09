# Appendix C — Editable implementation tools

All tools in this appendix are **handbook synthesis**. Source references identify the practices and reasoning informing each tool; they do not imply that a source used this exact form. Copy the relevant tool into an organization’s working records, replace bracketed fields, assign names and attach/link evidence. An unanswered field remains open. A completed form does not substitute for testing, professional review or the decision of a competent authority.

Use a common use-case identifier to connect the forms. Keep the latest approved version, owner, change history and decision record. Existing systems can hold these records if the information and relationships remain accessible. Do not create a new platform merely to reproduce a worksheet.

**Which tools at which tier.**

| Tool | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| C.0 Fast-path record | Core | — | — |
| C.1 Readiness assessment | Organization-level | Organization-level | Organization-level |
| C.2 Intake and prioritization | — | Core | Core |
| C.3 Decision rights and control record | Optional | Core | Core |
| C.4 Legal and regulatory worksheet | — | Conditional | Core |
| C.5 Pilot charter and evaluation | — | Core | Core |
| C.6 Release checklist | — | Core | Core |
| C.7 Value review | Optional | Core | Core |
| C.8 Roadmap | Portfolio-level | Portfolio-level | Portfolio-level |
| C.9 Data, architecture and supplier record | Conditional | Core | Core |
| C.10 Operating, incident and change record | Feedback route only | Core | Core |
| C.11 People, capacity and adoption | Partial | Core | Core |
| C.12 Traceability | Program-level | Program-level | Program-level |
| C.13 Acceptable-use policy | Organization-level | Organization-level | Organization-level |
| C.14 Run-cost and value estimator | Optional | Core | Core |

Appendix B shows every tool completed for one fictional use case.

## C.0 Fast-path record for Tier-1 uses

**Supports:** approval of a low-risk use in an approved tool without the full intake. **Use at:** Tier 1 only. If any answer below is "no" or "unsure", use C.2 instead. **Owner:** business owner; line manager approves; Information Security confirms the tool. **Basis:** proportionate governance in D29 p. 14 and D30 pp. 53–55; tier triggers are handbook synthesis.

Use case / ID / owner / date: [ ]
Team and approximate number of users: [ ]
Task the AI supports, and the outcome it should improve: [ ]
Approved tool and version or configuration: [ ]
Data classes used (must be permitted for this tool under C.13): [ ]

| Tier-1 condition | Yes / No / Unsure | Note |
|---|---|---|
| Internal users only; no output reaches customers or the public without the user reviewing and owning it | [ ] | [ ] |
| The user reviews every output before using it | [ ] | [ ] |
| No automated action beyond the user’s own drafts | [ ] | [ ] |
| No decision about an individual’s finances, eligibility, suitability or employment | [ ] | [ ] |
| Errors are easy for the user to see and cheap to reverse | [ ] | [ ] |
| Only data classes the approved tool permits | [ ] | [ ] |

**Smoke test (starting default: at least 30 representative tasks, zero critical failures):** tasks tried [n]; critical failures [n]; typical problems seen [ ]; workaround or user guidance [ ].
Users trained on the acceptable-use policy and on this task’s limits: [date / evidence]
Feedback and incident route: [ ]
Success signal to check at the annual review: [ ]
Approval (line manager), security confirmation and inventory entry: [names / dates / link]

## C.1 Maturity and readiness assessment

**Supports:** mandate, investment scope and readiness-remediation decisions. **Owner:** Program Lead; each capability owner validates their evidence; sponsor accepts the resulting action plan. **Basis:** D19 pp. 2–6; D22 ll. 59–83 and 276–284; A02 companion maturity figure. **Use at:** Organization-level; Core once per mandate cycle.

Assessment scope: [entity/business units/use cases]  
Assessment date and reviewers: [ ]  
Strategic outcome under consideration: [ ]  
Existing deployment/experiment inventory reviewed: [link]  
Entry point in handbook and rationale: [ ]

| Dimension | Observed capability and operational example | Source artifacts / people consulted | Source-level label or unknown | Confidence and limitation | Next required capability, owner and decision date |
|---|---|---|---|---|---|
| Strategy and executive alignment | [ ] | [ ] | [ ] | [ ] | [ ] |
| Layered AI infrastructure | [ ] | [ ] | [ ] | [ ] | [ ] |
| Data and content readiness | [ ] | [ ] | [ ] | [ ] | [ ] |
| Governance and risk | [ ] | [ ] | [ ] | [ ] | [ ] |
| Adoption and organizational transformation | [ ] | [ ] | [ ] | [ ] | [ ] |
| Use prioritization and portfolio management | [ ] | [ ] | [ ] | [ ] | [ ] |

**Evidence anchors — synthesis for using McMillan’s labels:**

- **Ad Hoc:** show individual experiments and dependencies on particular people; record what is absent or unknown.
- **Emerging:** show intent, assigned initiatives or partial tools, and which capabilities remain unproven.
- **Managed:** inspect written ownership and repeatable procedures, then examine a delivery/review/incident example showing that they work reliably within the assessed scope.
- **Scaled:** examine use across relevant units, continuing measurement, shared ownership and improvements over time; do not award this label from tool access alone.

These are qualitative evidence prompts, not a validated numerical scoring system. Do not derive a weighted average or MIT CISR stage from them. Discuss MIT’s transition separately: [experiment/prepare; pilots/capabilities; scaled ways of working; future-ready innovation], supported by [evidence] and qualified by [unknowns].

Readiness decision for the candidate scope: [ready for discovery / bounded experiment / pilot / production remediation / expansion assessment]  
Blocking capabilities: [ ]  
Work permitted while resolving them: [ ]  
Sponsor decision, conditions, owner and review trigger: [ ]

## C.2 Use-case intake and prioritization worksheet

**Supports:** discovery, alternative selection and portfolio investment. **Owner:** business owner; Program Lead maintains comparison; finance, technical/data and control reviewers challenge their domains. **Basis:** D34 pp. 21–23; D27 ll. 297–321; D24 p. 4; D38 ll. 18–49 and 95–100, treated as a proposed framework. **Use at:** Tier 2–3 Core (Tier 1 uses C.0).

Use case / version / status: [ ]  
Business domain and accountable owner: [ ]  
User and affected non-users: [ ]  
Problem, frequency, consequence and evidence: [ ]  
Current workflow and exception path: [link]  
Baseline period, population, sample and limitations: [ ]  
Desired outcome and quality/impact constraints: [ ]  
AI contribution being hypothesized: [ ]  
Permitted scope: [users, tasks, data, locations, actions]  
Out of scope and unresolved: [ ]

| Alternative | How it would address the problem | Task/outcome evidence | Full cost and capacity | Constraints/risks | Disposition and rationale |
|---|---|---|---|---|---|
| Current process / no change | [ ] | [ ] | [ ] | [ ] | [ ] |
| Procedure, search or deterministic automation | [ ] | [ ] | [ ] | [ ] | [ ] |
| Relevant conventional ML / analytics option | [ ] | [ ] | [ ] | [ ] | [ ] |
| Relevant generative / agent option | [ ] | [ ] | [ ] | [ ] | [ ] |

Delete alternatives that are inapplicable, recording why; add other credible options.

**Eligibility:** problem supported [ ]; accountable owner accepts [ ]; plausible permitted data/action path [ ]; evaluation feasible [ ]; named capacity path [ ]. Unresolved condition and evidence needed: [ ]. Eligibility decision: [eligible / hold / redesign / stop].

| Comparison dimension | Evidence / uncertainty | Assessment on locally agreed scale | Importance/weight if used | What would change the assessment? |
|---|---|---|---|---|
| Strategic/business importance | [ ] | [ ] | [ ] | [ ] |
| Outcome improvement and confidence | [ ] | [ ] | [ ] | [ ] |
| Data and technical feasibility | [ ] | [ ] | [ ] | [ ] |
| Workflow/adoption feasibility | [ ] | [ ] | [ ] | [ ] |
| Full cost / economics | [ ] | [ ] | [ ] | [ ] |
| Time to useful evidence | [ ] | [ ] | [ ] | [ ] |
| Dependencies / scarce capacity | [ ] | [ ] | [ ] | [ ] |
| Residual risk and control burden | [ ] | [ ] | [ ] | [ ] |

Compare candidates using the same definitions. Agree any weights before ranking; show whether reasonable changes in priorities change the order. Keep mandatory constraints outside compensating scores.

Portfolio disposition: [discovery / data prerequisite / comparative experiment / pilot / production work / retain/refine / defer / stop]  
Funded scope, cost limit and released capacity: [ ]  
Prerequisites and owners: [ ]  
Decision-maker, date, conditions and next evidence review: [ ]

## C.3 Governance, ownership and decision-rights matrix

**Supports:** explicit authority at each stage. **Owner:** sponsor and Program Lead, validated by each function. **Basis:** D16 pp. 6–7; D29 pp. 7–8, 17–18; D30 pp. 60–63, 75–78, 99–103. **Use at:** Matrix: Core once per organization. Control record: Tier 2–3 Core.

Replace role labels with names and delegated authority. Assign one accountable decision-maker for each decision; separately identify required specialist concurrence. Some decisions have different competent authorities and must not be collapsed into a single signature.

| Decision / responsibility | Accountable authority | Prepares / executes | Required review or concurrence | Decision evidence | Escalation / stop authority |
|---|---|---|---|---|---|
| Mandate and funding | [sponsor/governing authority] | [business leaders / Program Lead] | [finance, relevant leaders] | [mandate, readiness, capacity] | [ ] |
| Business outcome and workflow | [business owner] | [product/domain team] | [affected operations/users] | [baseline, scope, acceptance] | [ ] |
| Portfolio investment | [portfolio authority] | [Program Lead / owner] | [finance, tech/data, control input] | [C.2] | [ ] |
| Permitted data use and business meaning | [data owner / competent authority] | [steward / domain expert] | [local legal/privacy, security as needed] | [C.4/C.9] | [ ] |
| Architecture and sourcing | [technical authority] | [technical lead / procurement] | [security, operations, data, local reviewers] | [decision record, flows, cost] | [ ] |
| Pilot exposure | [delegated pilot authority] | [business/technical leads] | [required control/operational reviews] | [C.5, containment evidence] | [ ] |
| Evaluation acceptance | [business owner for fitness] | [evaluation/domain specialists] | [proportionate independent challenge] | [rubric, results, failures] | [ ] |
| Security acceptance | [Information Security authority] | [security specialists / delivery team] | [relevant risk and technical owners] | [threat/control test evidence] | [ ] |
| Local legal/regulatory determination | [authorized legal/compliance reviewer] | [qualified reviewer] | [other competent local expertise] | [C.4] | [ ] |
| Residual-risk acceptance | [delegated risk acceptance authority] | [owner and risk specialists] | [required control owners] | [tested controls, remaining exposure] | [ ] |
| Production release | [release authority] | [technical and operational owners] | [required business/control decisions] | [C.6] | [ ] |
| Run, monitor and respond | [operational owner] | [service team, data/content owners] | [security/business as relevant] | [runbook, alerts, incidents] | [ ] |
| Material change / expansion | [scope/funding/release authorities] | [owner / Program Lead / technical lead] | [affected local/control/operational owners] | [C.7 and changed evidence] | [ ] |
| Retirement | [business owner] | [operations / data / procurement] | [records/privacy/security and dependents] | [closure checklist] | [ ] |
| Independent assurance | [locally designated assurance authority] | [independent reviewers / audit] | [per applicable charter] | [review scope and findings] | [ ] |

Conflict-of-interest safeguards: [ ]  
Small-organization role combinations and workload: [ ]  
Who maintains the use-case record and review calendar: [ ]  
Maximum delegated scope and escalation path for unresolved decisions: [ ]

**Use-case control record:**

| Failure / harm and affected party | Inherent assessment | Control and lifecycle point | Control owner | Test evidence / limitation | Residual assessment and competent decision |
|---|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

Policy exception, if any: [rule, authority, rationale, compensating controls, expiration, monitoring and closure]. A policy exception cannot override an applicable legal restriction.

## C.4 Local legal and regulatory review worksheet

**Supports:** permitted design, pilot, release, operation and expansion in each relevant jurisdiction. **Owner:** locally authorized legal/compliance reviewer; the business owner supplies the complete use context. **Basis:** D01 pp. 5, 25–28; D29 pp. 11, 14–18, 22; D30 pp. 75–78. **This worksheet is jurisdiction-neutral.** **Use at:** Tier 3 Core; Tier 2 Conditional (personal data, customer communication, regulated activity or new jurisdiction).

Entity / service / use-case version: [ ]  
Sector and regulated activity, if any: [ ]  
Operating jurisdictions, customer/affected-person locations and relevant provider/data routes: [ ]  
Purpose, users, output, advice/decision/action boundary and human role: [ ]  
Reviewer, competence/authority and date: [ ]

| Jurisdiction / sector / entity | Requirement or open question | Primary source, exact locator, issuing body and version/date | Status and applicability reasoning | Responsible reviewer | Required evidence | Affected decision / control / lifecycle stage | Determination, conditions and review date |
|---|---|---|---|---|---|---|---|
| [ ] | [ ] | [ ] | [law / regulation / guidance / judicial interpretation / contract / company policy / unresolved] | [ ] | [ ] | [ ] | [ ] |

Use the following prompts to identify issues, without assuming that every prompt corresponds to a legal duty:

- Does the actual activity require authorization, restrictions on advice/decisioning, professional responsibility or specific review?
- What permits collection, processing, disclosure and secondary use of each data class? What changes when using a provider or derived data store?
- Do records, explanations, disclosure, accessibility, human review, complaint handling, contestability or remediation requirements apply? Which local legal/judicial processes and remedies are relevant?
- What contractual, intellectual-property, licensing, workforce or consumer obligations affect sources, models, outputs and deployment?
- Are notice, consultation, testing, external approval or incident reporting required? By whom, for which entity, at what point and with what evidence?
- Do requirements differ across jurisdictions or conflict? Can scope, data routes, operating model or separate deployments resolve the conflict?

For each answer, distinguish confirmed applicability from an interpretation awaiting review. A reference to a law’s name or a FINOS mapping is not sufficient. Preserve the underlying authority, effective status and local reasoning. Obtain qualified local advice where needed.

**Disposition:** [permitted within stated scope / permitted with conditions / further review needed / redesign / do not proceed].  
Conditions blocking pilot or release: [ ]  
External approval/notification dependency, only if established: [authority, evidence, owner, timing]  
Cross-jurisdiction resolution or separate-scope decision: [ ]  
Change triggers requiring re-review: [new location, user, data route, action, provider, applicable requirement or interpretation]  
Decision sign-off and evidence link: [ ]

## C.5 Pilot charter and evaluation plan

**Supports:** controlled experimentation and continue/redesign/stop decisions. **Owner:** business owner; evaluation lead maintains the plan; relevant control/operations reviewers accept exposure. **Basis:** D04 ll. 367–463; D25 pp. 12–13; D26 ll. 216–246; D29 pp. 16–19; FINOS mi-5, Implementation Guidance. **Use at:** Tier 2–3 Core (Tier 1 uses the smoke test in C.0).

Pilot / use-case version / owner: [ ]  
Decision to be informed and hypothesis: [ ]  
Business baseline, comparison and limitations: [ ]  
Alternative approaches: [ ]  
Allowed users, task types, languages, data and actions: [ ]  
Environment and permitted exposure: [offline / shadow / supervised / limited live, with details]  
User recruitment, capacity, duration and evidence-based rationale: [ ]  
Fallback, stop mechanism and incident route: [ ]  
Required permissions/reviews before starting: [links]

| Measure / requirement | Definition and denominator | Baseline and evidence | Acceptance threshold and rationale, set before results | Sample/coverage and evaluator | Result / uncertainty / decision |
|---|---|---|---|---|---|
| Primary business outcome | [ ] | [ ] | [ ] | [ ] | [ ] |
| Correctness and completeness | [ ] | [ ] | [ ] | [ ] | [ ] |
| Critical error / adverse impact | [ ] | [ ] | [ ] | [ ] | [ ] |
| Relevant group/language/task differences | [ ] | [ ] | [ ] | [ ] | [ ] |
| Citation/source or prediction evidence | [ ] | [ ] | [ ] | [ ] | [ ] |
| Permission/egress/action controls | [ ] | [ ] | [ ] | [ ] | [ ] |
| Review/correction and total task effort | [ ] | [ ] | [ ] | [ ] | [ ] |
| Latency, failure and continuity | [ ] | [ ] | [ ] | [ ] | [ ] |
| Full cost per successful outcome | [ ] | [ ] | [ ] | [ ] | [ ] |

**Test-set sizing (6.3):** critical-error rate to rule out [ ]% → clean cases needed ≈ 3 ÷ rate = [n]; slices sized separately [list]; pass-rate interval method [Wilson].  
**Evaluation evidence record:** development examples [ ]; held-out evaluation [ ]; regression cases [ ]; provenance/permissions [ ]; expert rubric [ ]; disagreement resolution [ ]; repeated tests for variability [ ]; critical cases [ ]; independent challenge [ ]. If using a model judge: version/rubric [ ], expert calibration [ ], disagreement/escalation [ ], cost [ ]. For agents: allowed tools/actions, trajectory tests, state/credential boundaries, authorization, retries and recovery [ ].

| Decision | Explicit criterion to complete before pilot starts | Follow-through |
|---|---|---|
| **Continue** | [task benefit supported; mandatory controls pass; limitations fit scope; feasible next-stage cost/ownership] | [funded production-readiness actions and authority] |
| **Redesign** | [valuable problem; named remediable failure; acceptable bounded next experiment] | [change, owner, cost limit, retest and deadline] |
| **Stop** | [unsupported value; infeasible/impermissible scope; unacceptable harm/cost; better alternative] | [containment/closure, artifacts, learning and reassignment] |
| **Suspend immediately** | [defined consequential failure or loss of required control] | [who disables, whom to notify, safe fallback and restoration evidence] |

Changing criteria after observing results: [original criterion, change, reason, approving authority and effect on conclusion].  
Final decision, evidence links, dissent, remaining limitations and next review: [ ]

**Illustrative example, without benchmark targets:** a staff policy-search assistant might compare current search, improved conventional search and a grounded assistant using representative inquiries. Experts assess required facts, omissions and supporting citations; operations tests stale-source and permission-change behavior; users measure complete task time including verification. A faster answer that increases incorrect advice or correction effort fails the intended hypothesis. The organization sets actual thresholds from its baseline and consequences.

## C.6 Production readiness and release checklist

**Supports:** authorization of a defined production scope. **Owner:** operational owner and technical lead prepare; business owner accepts fitness; competent release authority decides. **Basis:** D30 pp. 99–103, 109–113; D29 pp. 8, 17–19; FINOS mi-10, Implementation Guidance. **Use at:** Tier 2–3 Core. Tier 2 may mark a row "not applicable" only with a written reason; Tier 3 completes every row.

Release / version / scope / planned exposure: [ ]  
Named business owner, operational owner and release authority: [ ]

| Readiness item | Named evidence owner | Evidence / result / unresolved limit | Pass, conditional or fail | Approver / condition |
|---|---|---|---|---|
| Scope, intended users, locations, data and actions match approval | [ ] | [ ] | [ ] | [ ] |
| Business task and critical-error acceptance | [ ] | [ ] | [ ] | [ ] |
| Relevant independent challenge complete | [ ] | [ ] | [ ] | [ ] |
| Local legal/regulatory/contract decisions complete | [ ] | [ ] | [ ] | [ ] |
| Information Security tests and required acceptance | [ ] | [ ] | [ ] | [ ] |
| Source semantics, quality, permissions and refresh | [ ] | [ ] | [ ] | [ ] |
| Model/prompt/index/tool/code versions traceable | [ ] | [ ] | [ ] | [ ] |
| End-to-end integration and authorized action handling | [ ] | [ ] | [ ] | [ ] |
| Human review workload, competence and authority | [ ] | [ ] | [ ] | [ ] |
| Load, latency, dependency failures and capacity tested | [ ] | [ ] | [ ] | [ ] |
| Operating budget, cost attribution and limits | [ ] | [ ] | [ ] | [ ] |
| Alerts have thresholds, responders and response authority | [ ] | [ ] | [ ] | [ ] |
| Content/data/model change and regression process | [ ] | [ ] | [ ] | [ ] |
| Support, incident handling and affected-user route | [ ] | [ ] | [ ] | [ ] |
| Tested disablement/recovery and continuity workflow | [ ] | [ ] | [ ] | [ ] |
| Supplier support, changes, incidents and exit commitments | [ ] | [ ] | [ ] | [ ] |
| Data/log/artifact access, retention and deletion approved | [ ] | [ ] | [ ] | [ ] |
| Training, user guidance and relevant communications ready | [ ] | [ ] | [ ] | [ ] |
| Inventory, runbook, decisions and review date current | [ ] | [ ] | [ ] | [ ] |

Any conditional item must specify an authorized limit, owner, due date and closure evidence. A legally required condition or essential untested control cannot be waived by marking it conditional.

Release decision: [approve defined scope / restrict / return for redesign / stop]  
Residual-risk acceptance and required concurrences: [ ]  
Rollout stages, limits, widening conditions and abort triggers: [ ]  
Post-release review date, owner and minimum evidence: [ ]  
Signed decision/version and supporting record: [ ]

## C.7 Value review and scale/refine/retire guide

**Supports:** continued operation and capital allocation. **Owner:** business owner and finance, with operational and control evidence. **Basis:** D19 p. 6; D34 p. 22; D24 p. 4; D38 ll. 381–429, 550–577. **Use at:** Tier 2–3 Core at the tier review cadence; Tier 1 Optional.

Review period / scope / versions / eligible work volume: [ ]  
Comparison design, task mix and other material changes: [ ]

| Outcome or cost | Baseline / counterfactual | Observed result and evidence quality | Attribution limit / uncertainty | Business/finance validation |
|---|---|---|---|---|
| Successful completed outcomes | [ ] | [ ] | [ ] | [ ] |
| Quality, critical errors and adverse effects | [ ] | [ ] | [ ] | [ ] |
| Total workflow effort, checking and rework | [ ] | [ ] | [ ] | [ ] |
| Capacity released and actual management use | [ ] | [ ] | [ ] | [ ] |
| Incremental revenue/contribution or cash cost change | [ ] | [ ] | [ ] | [ ] |
| Build/integration and transition costs | [ ] | [ ] | [ ] | [ ] |
| Data/content, evaluation and human review | [ ] | [ ] | [ ] | [ ] |
| Model/infrastructure/licenses and shared allocation | [ ] | [ ] | [ ] | [ ] |
| Support, controls, learning and supplier management | [ ] | [ ] | [ ] | [ ] |
| Cost per successful outcome | [ ] | [ ] | [ ] | [ ] |

New scope considered: [users/tasks/locations/data/actions/volume]  
Changes requiring re-evaluation: [ ]  
Reusable assets and their owners/contracts: [ ]  
New integration, adoption, local review and operating costs: [ ]  
Shared-service capacity and failure concentration: [ ]  
Demand/cost scenarios and assumptions: [ ]

**Decision guide:** expand only with supported benefit, working controls, operating capacity and validation of changed context. Refine when useful outcomes remain but a specific quality, cost or workflow condition needs improvement. Retain when value is adequate and expansion is unjustified. Restrict/suspend when required controls or operating quality fail. Retire when the case no longer meets the business need or an alternative is better. Insufficient evidence requires a bounded evidence plan or a stop decision.

Decision / authority / rationale / alternatives / follow-up: [ ]  
If retiring: continuity [ ]; access/credentials/jobs disabled [ ]; dependency owners informed [ ]; sources/indexes/logs/caches/backups/artifacts handled under approved requirements [ ]; supplier exit [ ]; inventory/finance updated [ ]; closure verified [ ].

## C.8 Dependency-based roadmap template

**Supports:** funded execution and executive review. **Owner:** Program Lead; every owner validates their commitment. **Basis:** D32 pp. 3–4, 9; D19 pp. 2–6; D34 pp. 21–23. Durations, budget and staffing are deliberately left for local estimation. **Use at:** Core for any portfolio beyond a single Tier-1 use.

Mandate / outcomes / approved horizon: [ ]  
Portfolio capacity and investment envelope: [ ]  
Planning assumptions and unresolved executive choices: [ ]

| Initiative / work package | Business outcome | Accountable person | Deliverable and acceptance evidence | Prerequisites and their owners | People/cost commitment | Milestone and decision authority | Measure / baseline / target | Review trigger / alternative |
|---|---|---|---|---|---|---|---|---|
| [readiness or discovery] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [data/control prerequisite] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [pilot/evaluation] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [integration/production] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [adoption/operation] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [expansion/retirement] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

Use rows for work that produces a reviewable deliverable. Connect dependencies explicitly. Mark work that can run together and the actual scarce person/service limiting parallel delivery. Dates require owner-accepted estimates and capacity; confidence and unresolved dependencies remain visible.

Executive decision summary: [challenge; selected approach; coherent actions; alternatives; funding/capacity; required decisions; unresolved issues; evidence that will trigger change].

## C.9 Data readiness, architecture and supplier decision record

**Supports:** build/buy/configure/host decisions and data preparation. **Owner:** technical lead, business data owner and engineering steward. **Basis:** D14 ll. 132–258 and A01 blueprint; D26 ll. 90–120; D30 pp. 152–153; FINOS mi-16, Implementation Guidance. **Use at:** Tier 2–3 Core; Tier 1 Conditional when new data is connected.

| Source / derived asset | Authoritative meaning, coverage and limits | Business / technical owners | Permitted purpose, users and rights | Quality/freshness/reconciliation evidence | Flow, storage, retention/deletion and support |
|---|---|---|---|---|---|
| [source] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [index/embeddings/cache/logs/output] | [ ] | [ ] | [ ] | [ ] | [ ] |

Unresolved semantic/quality issues, remediation owner and release impact: [ ]  
Representative questions/cases and verified results: [ ]  
Data-flow diagram covering model, evaluation, monitoring, support and backups: [link]

| Architecture / sourcing option | Task evidence | Permitted data/control fit | Integration and operational capacity | Full cost, continuity and exit | Choice / reason |
|---|---|---|---|---|---|
| [current/rules/search] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [hosted/managed option] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [internally operated option] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [hybrid if relevant] | [ ] | [ ] | [ ] | [ ] | [ ] |

Technique choice and need for RAG/fine-tuning/agents, if any: [reason and evidence, not assumed prerequisites]  
Supplier AI disclosure: [intended use/limits, components, training/evaluation disclosure, source rights, provider access/processing/retention/training, subproviders, versions/changes, security, evaluation, incidents, support, portability and deletion]  
Undisclosed items, compensating controls and acceptance/rejection: [ ]  
Decision, owners, versions, local conditions and revisit trigger: [ ]

## C.10 Operating, incident and change record

**Supports:** dependable operation and restoration/change decisions. **Owner:** operational owner, working with business, data, security and supplier owners. **Basis:** D30 pp. 100, 109–113; D29 pp. 8, 17–19; FINOS mi-4 and mi-10, Implementation Guidance. **Use at:** Tier 2–3 Core; Tier 1 needs only the feedback and incident route.

| Signal / failure | Definition, data and approved retention | Threshold / cadence | Named responder and authority | Containment / fallback | Restoration evidence |
|---|---|---|---|---|---|
| [quality/critical error] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [source/access/security] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [availability/cost] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [complaint/misuse] | [ ] | [ ] | [ ] | [ ] | [ ] |

Incident: [time, affected scope, observed behavior, impact/unknowns, versions, action/control evidence, lead, containment, affected-user support, required local notification determination, root cause, corrective action and restoration decision]. Record observed events and testable facts; a model-generated explanation is not itself proof of the cause or a faithful trace of internal reasoning.

Change: [proposed model/prompt/source/tool/code/user/action/provider change, reason, impact assessment, relevant tests, local/control re-review, approval, deployment/fallback, monitoring and closure].

Review cadence and material-change triggers: [ ]  
Exercise results for disablement, provider loss, content error and permission change: [ ]

## C.11 People, capacity and adoption plan

**Supports:** team formation, make/hire/partner choices and workflow readiness. **Owner:** Program Lead, business owner, functional managers and people/learning lead. **Basis:** D34 pp. 9–11, 21–23; D36 ll. 118–151; D12 pp. 2–4. **Use at:** Core for each funded use case; Tier 1 completes the workflow-change and training rows only.

| Capability needed | Named person / relevant delivery evidence | Actual available capacity and existing obligations | Gap and assignment/reskill/hire/partner choice | Manager commitment / backup | Deliverable demonstrating readiness |
|---|---|---|---|---|---|
| [Program Lead] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [business/domain/content] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [product/data/engineering] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [evaluation/control/operations] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [learning/change/finance/procurement] | [ ] | [ ] | [ ] | [ ] | [ ] |

Role/workflow change: [what is removed, retained, added, verified or escalated]  
Capacity benefit and management action needed to realize it: [ ]  
Learning by role and practical competence evidence: [ ]  
User feedback and triage owner: [ ]  
Adoption measures, task completion, quality and burden: [ ]  
Workforce implications decided / unresolved and leadership communication: [ ]  
Supplier knowledge-transfer and ownership/exit plan: [ ]

## C.12 Question-to-decision and evidence traceability

**Supports:** adapting the strategy when leadership answers or evidence change. **Owner:** Program Lead; responsible decision-makers validate entries. **Basis:** handbook synthesis drawing on D19 p. 6; D30 pp. 67–74, 112–113; FINOS heuristic assessment, section H. This is a reusable blank tool and contains no private company Q&A from prior work. **Use at:** Core for the Program Lead; Optional for single use cases.

| Question and why it matters | Answer / evidence, source, date and provider | Status: confirmed, reported, hypothesis or unknown | Decision and accountable authority | Alternatives if answer changes | Required validation / owner | Review trigger and affected roadmap/artifact |
|---|---|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

Keep consequential disagreements visible. An executive preference is a decision input, not proof of technical performance or legal applicability. When updating a decision, retain the earlier rationale and identify which evidence changed.

## C.13 Acceptable-use policy for AI tools (template)

**Supports:** day-one guardrails, shadow-AI reduction and literacy evidence (Chapter 4.2). **Use at:** organization-wide; review at least annually and when tools or law change. **Owner:** Program Lead drafts; Information Security, Legal/Compliance, Privacy and HR approve; line managers brief teams. **Basis:** D30 pp. 30, 48; D08 ll. 519–530; FINOS ri-23 (acceptable-use policy and training as an IP and data-leakage mitigation); E06; E09. Replace bracketed text; keep it to two pages.

1. **Purpose and scope.** This policy covers every use of AI tools for [organization] work, on any device, including AI features inside other software. It applies to [employees, contractors, others acting on our behalf].
2. **Approved tools.** Only tools on the approved list [link] may be used for work. To request a new tool or a new use case, use [route]; requests are answered within [n] working days.
3. **Data you may use.**

| Data class | Approved general assistant | Approved specialist tool (per its record) | Public consumer AI tools |
|---|---|---|---|
| Public | Allowed | Allowed | [Allowed / Not allowed] |
| Internal | [Allowed] | Allowed | Not allowed |
| Confidential (including client data) | [Allowed only if listed] | Only if listed in the tool’s record | Not allowed |
| Restricted (for example credentials, special-category personal data, inside information) | Not allowed | Only if explicitly approved | Not allowed |

4. **Your responsibilities.** Check every output before you rely on it or send it. You remain responsible for work you produce with AI. Do not present AI output as verified fact without checking the source. Follow disclosure rules for [client communications, regulatory filings, other].
5. **Prohibited uses.** [Making or communicating decisions about clients, employees or applicants without the approved process; generating advice or recommendations outside an approved tool; entering credentials or restricted data; attempting to bypass controls; uses prohibited by law.]
6. **Building with AI.** Staff-built workflows, agents, plug-ins or automations must be registered at [inventory link] before they are shared or connected to company data or systems. A registration window runs until [date] for existing uses, without penalty.
7. **Vendor and embedded AI.** Tell [procurement / Program Lead] when a product you use adds AI features or changes its data terms.
8. **Training.** Complete [course] before first use and [refresher] each year. Role-specific training is required for [roles / tools].
9. **Reporting.** Report wrong, harmful or leaked outputs, and suspected misuse, to [route] immediately. Reports made in good faith are welcome.
10. **Consequences and review.** Breaches are handled under [policy]. This policy is reviewed by [owner] on [date] and after material changes in tools or law.

Approved by / date / version: [ ]
Staff acknowledgement method and evidence location: [ ]

## C.14 Run-cost and value estimator

**Supports:** investment comparison, pilot budget, release economics and value review (Chapters 2.4, 5.6, 9.2). **Use at:** Tier 2–3 Core; Tier 1 Optional. **Owner:** technical lead estimates usage; finance validates rates and treatment; business owner validates volumes and benefit. **Basis:** D38 ll. 381–429; D10 pp. 11–12; E10; E11. Use contracted prices, measured tokens and stated assumptions.

Scenario: [low / expected / high]
Period: [month]
Eligible work volume and expected use rate: [ ]

| Line | Formula / driver | Assumption and source | Low | Expected | High |
|---|---|---|---|---|---|
| Requests per period | eligible tasks × use rate × requests per task | [ ] | [ ] | [ ] | [ ] |
| Input tokens per request | prompt + retrieved context + history (measured) | [ ] | [ ] | [ ] | [ ] |
| Output tokens per request | measured | [ ] | [ ] | [ ] | [ ] |
| Model usage cost | requests × (in × in-price + out × out-price) ÷ 1,000,000 × (1 + retry rate) | [contracted rates] | [ ] | [ ] | [ ] |
| Embedding, indexing, storage | documents × refresh rate × unit cost | [ ] | [ ] | [ ] | [ ] |
| Hosting, platform and licences | allocated per period | [ ] | [ ] | [ ] | [ ] |
| Evaluation runs | cases × repetitions × cost per run + expert hours × rate | [ ] | [ ] | [ ] | [ ] |
| Production quality sampling | sampled items × minutes × loaded rate | [ ] | [ ] | [ ] | [ ] |
| Human checking in the workflow | requests × extra minutes × loaded rate | [ ] | [ ] | [ ] | [ ] |
| Support, operations, security, governance | allocated hours × rate | [ ] | [ ] | [ ] | [ ] |
| Training, change, supplier management | allocated per period | [ ] | [ ] | [ ] | [ ] |
| **Total attributable cost** | sum | | [ ] | [ ] | [ ] |
| Successful outcomes | completed tasks meeting the agreed quality standard | [ ] | [ ] | [ ] | [ ] |
| **Cost per successful outcome** | total ÷ successful outcomes (report "none demonstrated" if zero) | | [ ] | [ ] | [ ] |
| Baseline cost per outcome | current process, same quality standard | [ ] | [ ] | [ ] | [ ] |
| Supported incremental benefit | finance-validated; capacity is not cash until acted on | [ ] | [ ] | [ ] | [ ] |

One-time costs (build, integration, data remediation, transition): [ ]
Largest cost driver and lever: [ ]
Finance validation and date: [ ]
