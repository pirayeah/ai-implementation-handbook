# Appendix D — Starting defaults, external sources and limitations

## D.1 Register of starting defaults

A starting default lets a team begin without a long debate. Replace it when local evidence, consequences or law justify a different value, and record the reason in tool C.12. The **basis** column says honestly where each value comes from:

- **Statistics** — follows mathematically from the stated assumptions.
- **Standard** — taken from a published external practice source.
- **Reference point** — informed by durations or practices reported in the collection, which are not norms.
- **Judgment** — the handbook’s editorial judgment, offered so that teams have a concrete place to start.

| Default | Value | Where used | Basis |
|---|---|---|---|
| Tier assignment rule | Highest triggered tier; unknown moves the use case up a tier | Tiers section | Judgment, applying proportionality in D29 p. 14 and D30 pp. 53–55 |
| Tier 1 smoke test | ≥30 representative tasks, zero critical failures (≈ ≤10% at 95%) | C.0, 6.3 | Statistics [E07]; the threshold choice is judgment |
| Tier 2 evaluation | ≥150 critical-relevant held-out cases, zero critical failures (≈ ≤2%) | 6.3, C.5 | Statistics [E07]; the threshold choice is judgment |
| Tier 3 evaluation | ≥300 held-out cases, zero critical failures (≈ ≤1%), more if consequences require | 6.3, C.5 | Statistics [E07]; the threshold choice is judgment |
| Pass-rate interval | Wilson score interval | 6.3, C.5 | Statistics [E08] |
| Held-out share | At least one third of cases, never used for tuning | 6.3 | Judgment, building on development/evaluation separation in 6.3 |
| Test-set composition | 60% common; 20% exceptions and stale/conflicting sources; 10% out of scope; 10% adversarial and permission | 6.3 | Judgment |
| LLM-judge calibration | ≥100 expert-labeled, stratified items, including known critical patterns | 6.5 | Judgment, applying FINOS mi-15 calibration guidance; at n = 100, a 90% agreement estimate has a 95% interval of about ±6 points [E08] |
| Pilot timebox | Tier 1: 2–4 weeks; Tier 2: 8–12 weeks; Tier 3: 3–6 months or more | Tiers, Ch. 6 | Judgment; reference points: about 4 months of UAT at Prudential and a 9-month initial pilot at Morgan Stanley [D29 pp. 16–19; D04 ll. 367–463] |
| Mandate size | Two pages; no more than three outcomes in year one | 1.2 | Judgment |
| Readiness assessment timebox | 3–5 weeks | Ch. 1 card | Judgment |
| Scoring anchors and weights | Anchored 1–5 scales; equal weights unless agreed before scoring; double-the-top-priority sensitivity test | 2.4 | Judgment |
| Concurrent pilots | No more than named domain experts with released time; typically 1–3 in year one | 2.4 | Judgment |
| Problem statements in the first round | 15–30 | Quick start | Judgment |
| Interim acceptable-use policy | Within 3 weeks; inventory within 6 weeks | Quick start, 4.2 | Judgment; the need for clear policy and education is from D08 ll. 519–530 |
| Rollout stages | Stage 1 one team or about 5% of eligible users; Stage 2 about 25–50%; each stage at least one full business cycle including peak load; one change at a time | 7.4 | Standard [E12] for canary principles and its 5% example; the percentages and stage structure are judgment |
| Monitoring samples | Tier 2 monthly ≥50 interactions; Tier 3 weekly ≥50 in the first cycle | 7.5 | Judgment; the detection limit (≈6% for 50 clean cases) is statistics [E07] |
| Periodic review cadence | Tier 1 annual; Tier 2 every 6 months; Tier 3 quarterly; always after material change | Tiers, Ch. 9 | Judgment, applying risk-based review frequency in D30 p. 108 |
| First value review | 90 days after full release | Ch. 9 card | Judgment |
| Adoption checkpoints | 30, 60 and 90 days after release | Ch. 8 card | Judgment |
| Quick-start plan | 90 days, three workstreams | Quick start | Judgment, sequencing Chapters 1–6 |

## D.2 External sources

The workspace collection did not cover these gaps: general control catalogues beyond FINOS, management-system standards, shadow-AI prevalence, statistical sample sizing, token and pricing mechanics, staged-rollout practice, and current AI-literacy law. For each gap, targeted research was done on 9 November 2026, and only primary or authoritative sources were used where available. They support the specific statements cited in the text and nothing more. Check each one for later editions before relying on it.

| ID | Source (issuer, title, date) | Link | Claim supported | Scope and caveats |
|---|---|---|---|---|
| E01 | NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023 | <https://www.nist.gov/itl/ai-risk-management-framework> | Voluntary framework with Govern, Map, Measure and Manage functions | Voluntary US guidance; not a legal requirement |
| E02 | NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST AI 600-1, July 2024 | <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf> | Profile of the AI RMF covering 12 generative-AI risks, with more than 200 suggested actions | Voluntary; its originating executive order has since been revoked, but the document remains published |
| E03 | ISO/IEC, *ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system*, December 2023 | <https://webstore.iec.ch/publication/90574> | Certifiable AI management-system standard for organizations that provide or use AI; audits the management system, not a model | Paid standard; certification is optional |
| E04 | OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*, released November 2024 | <https://genai.owasp.org/llm-top-10/> | Risk list including prompt injection, system-prompt leakage, vector and embedding weaknesses, excessive agency and unbounded consumption | Community list; a later edition may supersede it |
| E05 | OWASP GenAI Security Project, *OWASP Top 10 for Agentic Applications 2026*, released December 2025 | <https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/> | Agent-specific risks such as goal hijack, tool misuse and identity and privilege abuse | Community list |
| E06 | Microsoft and LinkedIn, *2024 Work Trend Index Annual Report*, 8 May 2024 | <https://news.microsoft.com/source/2024/05/08/microsoft-and-linkedin-release-the-2024-work-trend-index-on-the-state-of-ai-at-work/> | 75% of knowledge workers used AI at work; 78% of AI users brought their own AI tools; 39% of users had received AI training from their company | Vendor survey; global sample; 2024 snapshot |
| E07 | Hanley, J. A. and Lippman-Hand, A., "If nothing goes wrong, is everything all right? Interpreting zero numerators", *JAMA* 249(13):1743–1745, 1983 | <https://jamanetwork.com/journals/jama/article-abstract/389714> | Rule of three: zero events in *n* trials gives a 95% upper bound of about 3/*n* | Assumes independent, representative trials |
| E08 | Brown, L. D., Cai, T. T. and DasGupta, A., "Interval Estimation for a Binomial Proportion", *Statistical Science* 16(2), 2001 | <https://doi.org/10.1214/ss/1009213286> | The simple Wald interval performs poorly; the Wilson interval is recommended, especially for small *n* | Statistical method; the handbook computed its interval values itself |
| E09 | Regulation (EU) 2024/1689 (AI Act), Article 4, as amended by Regulation (EU) 2026/1744 (published in the Official Journal on 24 July 2026) | <https://eur-lex.europa.eu/eli/reg/2024/1689/oj> | The AI literacy duty for providers and deployers has applied since 2 February 2025; the amendment rewrote Article 4 without changing that date | EU law only; the amendment details were taken from secondary reports and must be verified against the consolidated EUR-Lex text and local advice |
| E10 | OpenAI Help Center, "What are tokens and how to count them?" | <https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them> | Rule of thumb: a token is about 4 characters, or about ¾ of a word, in English; other languages differ | Approximation; tokenizers differ by model and provider |
| E11 | Anthropic, "Pricing", Claude API documentation | <https://platform.claude.com/docs/en/about-claude/pricing> | Example of per-million-token pricing with separate input and output rates; prompt-caching prices; a 50% Batch API discount on input and output tokens (checked 9 November 2026) | Prices change; use contracted rates. Provider cited as an example only, not a recommendation |
| E12 | Google, *The Site Reliability Workbook*, Chapter 16 "Canarying Releases" | <https://sre.google/workbook/canarying-releases/> | A canary is a partial, time-limited deployment compared with a control; it should be representative; run one canary at a time; the example uses 5% of traffic | Written for software services; applied by analogy to AI workflow rollouts |

**Use rule.** Before adding any further external source, record the exact gap, the decision it affects and why the workspace evidence is insufficient. Then read the primary source and record its scope and date. Keep workspace and external evidence separate.

## D.3 Limitations adopters must keep in view

- **Evidence base.** Most implementation outcomes in the collection come from insiders, company communications, vendor-coauthored cases or multi-contributor publications. Independent, long-term causal evaluation is scarce. The collection is strongest on financial services, knowledge access, advisor assistance, enterprise data and governance. It is thin on other industries and on independently verified autonomous execution.
- **Defaults are not benchmarks.** Every starting default above is a place to begin, not evidence that a value is sufficient for a particular use case. Tier 3 and any legally designated activity may need far stricter evidence.
- **No legal determination.** Nothing in this handbook decides whether an activity is permitted in a jurisdiction. Tool C.4 and qualified local advice do that.
- **The worked example is fictional.** Appendix B shows how the mechanics work; its numbers must not be quoted as results.
- **Currency.** External sources were checked on 9 November 2026. Standards, threat lists, prices and law change; check for later editions.

The companion file [handbook-evidence-companion.md](handbook-evidence-companion.md) holds the full source register, review depth, evidence map, cross-case pattern matrix and verification record.
