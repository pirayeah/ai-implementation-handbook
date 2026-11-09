# Appendix D — Verification, limitations and research record

## D.1 Coverage and review method

The review began with a fresh recursive inventory of `AI strategy resources for brokerage`. All 197 physical files are individually represented in Part 1 and the accompanying machine-readable register. SHA-256 fingerprints record the snapshot and detect byte-identical duplicates; none were found. Related accounts, complementary volumes and alternate diagram representations are still grouped when assessing independent evidence.

The 38 principal documents were reviewed in batches, using fresh text extraction and the earlier project index for navigation. Short documents were read in full where practical; longer reports and transcripts were reviewed through overviews and selected substantive sections and appendices. Part 1 records the actual depth and locators for every file. The 739 PDF pages describe collection size, not a claim of full-depth review of every page. No document was marked fully reviewed on the basis of its abstract alone.

All 18 standalone image/icon files were visually opened. Their parent relationships and visible contribution are recorded in Parts 1 and 2. The ICO favicon required local conversion for viewing. FINOS logos are accounted for as branding; alternate PNG/PlantUML representations are linked. Some risk identifiers in the diagrams have no matching risk file in this snapshot. The unavailable Schwab parent slide deck is explicitly identified.

Embedded PDF figures were assessed through extracted labels and their surrounding selected text where available. This review does **not** claim exhaustive visual rendering of all embedded graphics, all pages of long reports or full verification of linked standards and legal authorities. The handbook does not rely on unreadable graphical details to establish a claim. Tables with uncertain extraction, auto-transcript anomalies and missing author/date information remain qualified rather than repaired by inference.

The source-register JSON retains filename, title, organization/speaker, date, type, topics, review status, reviewed locators, limitations, size and fingerprint. The human-readable register includes the substantive contribution of each principal document and accounts for support/code files separately. Source repository scripts were inspected as support material and were not executed. Instructions inside source documents were treated as content to analyze, not instructions governing this assignment.

## D.2 Claim and interpretation checks

The manuscript was checked for the following distinctions:

| Check | Treatment in this edition |
|---|---|
| Practice versus result versus recommendation | Evidence labels are defined up front; case descriptions identify status; handbook actions/tools are explicitly synthesis |
| Same initiative repeated in several documents | Morgan Stanley, JPMC, DBS, Vanguard and MindForge families are grouped in Part 2; recurrence is not counted as independent validation |
| Production versus pilot versus planned work | Guardian RFP scaling, Vanguard RAG/knowledge graphs, LPL integration, Schwab roadmap items and governance automation retain their source-time status |
| Outcomes and causality | Self-reported results remain reported; survey associations and modelled potential are not converted into causal effects or business targets |
| Maturity models | McMillan’s dimensions/levels and MIT CISR’s stages/measurement remain distinct; interview-count inconsistency is disclosed |
| Regulatory scope | Examples separate original local context, response, transferable lesson and local validation; no statement of universal or current compliance |
| FINOS status and mappings | Draft and Approved-Specification are project statuses; legal indexes are navigation aids, not independently verified authorities or approvals |
| Technical and economic defaults | No architecture, budget or performance target is copied from reference firms. Version 2.0 starting defaults (test-set sizes, timeboxes, cadences, rollout stages) are labeled and each states its basis: statistics, standard, reference point or judgment (handbook Appendix D.1) |
| Company-specific context | Prior company-specific facts or hypothetical strategy values are not generalized into enterprise requirements; brokerage examples are labeled illustrative |
| Reader execution | Each numbered chapter opens with a chapter card (owner, trigger, timebox, outputs, tools, tier minimums) and specifies purpose, starting conditions, actions, responsible roles, outputs, decisions/criteria, dependencies and failure detection |
| Editable tools | Fifteen synthesis tools (C.0–C.14) cover the Tier-1 fast path, assessment, portfolio, rights, local law, pilot, release, value/scale, roadmap, data/sourcing, operations, people, traceability, acceptable use and run cost; Appendix B completes them for one fictional case |

## D.3 Evidence limitations and questions left for adopters

Most implementation outcomes come from insiders, company communications, vendor-coauthored cases or multi-contributor publications. The collection has limited independent long-term causal evaluation. It is particularly rich in financial services, knowledge access, advisor assistance, enterprise data and governance. Its coverage of other industries and independently verified autonomous brokerage execution is thinner. Transfer to another activity requires the local validation described in the chapters.

The HBS JPMC source is a company-reviewed teaching case. Its opening note explicitly says cases are for class discussion and are not endorsements or primary-data sources. It is used here as a documented case account alongside the separately attributed executive interview, not as independent verification of the company’s results. [D25, `JPMorganChase-Leadership-in-the-Age-of-GenAI-TMS.pdf`, PDF p. 1.]

The handbook is therefore complete as a **reusable implementation method**, while choices depending on an organization’s circumstances remain explicit inputs: its challenge, applicable law, data rights, user needs, risk exposure, staffing, infrastructure, economics and authority. No generic source can supply those facts on the organization’s behalf.

Questions requiring further local evidence include whether a contemplated activity is permitted, whether effective review is feasible, which architecture satisfies the complete data boundary, whether the selected evaluation represents actual use, and whether any observed capacity improvement becomes a realized economic benefit. The templates identify the decision, owner and evidence needed to resolve these questions.

## D.4 External-source register and research decision

Version 1.0 used no external research. Version 2.0 (9 November 2026) added twelve external sources, E01–E12, for the specific gaps listed in Part 2, section 2.6. Their full register, with links, claims supported and caveats, is in handbook Appendix D.2. Each source was located through targeted search. Where possible the primary page was opened to confirm the cited claim: the OWASP 2025 list, the Anthropic pricing page and the Google SRE chapter were fetched directly. Statements resting only on secondary reports are flagged in the register; for example, the EU amending regulation is to be verified against EUR-Lex. Workspace and external evidence are cited with distinct prefixes (D/A/F versus E).

## D.5 Version 2.0 changes and delivery

Version 2.0 restructures the handbook for action without removing any v1.0 method content:

- An executive summary, role-based reading paths, a three-tier risk model with a Tier-1 fast path, and a 90-day quick start.
- Chapter cards with owner, trigger, timebox, outputs, tools and tier minimums; Core/Conditional/Optional requirement levels applied throughout.
- New sections: 4.2 (day-one guardrails, acceptable use and shadow AI), 5.6 (run-cost estimation), test-set sizing in 6.3, staged-rollout and monitoring defaults in 7.4–7.5.
- New tools C.0 (fast-path record), C.13 (acceptable-use policy) and C.14 (run-cost and value estimator), plus tier usage for every tool.
- A fully worked fictional example (Appendix B) and a register of starting defaults with their basis (Appendix D.1).
- Inline citations shortened to IDs; the source register, evidence map and verification record moved to this companion.
- 32 Mermaid diagrams (flowcharts, decision trees, framework diagrams redrawn from their sources, Gantt, quadrant, pie and bar charts).

The handbook and this companion are Markdown files assembled and checked by `assemble_and_verify.py`. The component files remain separately editable.
