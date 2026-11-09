# Enterprise AI handbook — version 2.0

Open **[the handbook](enterprise-ai-strategy-and-implementation-handbook.md)**. It contains:

- an executive summary, role-based reading paths, a three-tier risk model with a Tier-1 fast path, and a 90-day quick start
- ten chapters, each opening with a chapter card (owner, trigger, timebox, outputs, tools, tier minimums)
- Appendix A, a source key; Appendix B, a fully worked fictional example; Appendix C, fifteen editable tools (C.0–C.14); Appendix D, starting defaults with their basis, plus the external-source register

The audit trail is in **[the evidence companion](handbook-evidence-companion.md)**: the complete 197-file source register, the evidence map and cross-case pattern matrix, and the verification record.

The workspace collection is the source collection folder, `AI strategy resources for brokerage`. Version 2.0 also cites twelve external sources (E01–E12) for gaps the collection did not cover. Each is registered with its link, the claim it supports and its caveats in Appendix D.2.

Diagrams are written in Mermaid. They render on GitHub and GitLab, and in VS Code with a Mermaid preview extension.

## Editing and rebuilding

Edit the component files, then run `python assemble_and_verify.py`. That rebuilds both outputs, regenerates the source key from `source-register.json`, and writes `verification-report.json`. The script checks source fingerprints, citation locator bounds, FINOS and external IDs, chapter cards, tool numbering, table shape and code fences.

| Component | Becomes |
|---|---|
| [handbook-chapters.md](handbook-chapters.md) | Front matter and Chapters 1–10 |
| `appendix-a-source-key.md` (generated) | Appendix A |
| [appendix-b-worked-example.md](appendix-b-worked-example.md) | Appendix B |
| [appendix-c-editable-tools.md](appendix-c-editable-tools.md) | Appendix C |
| [appendix-d-defaults-and-sources.md](appendix-d-defaults-and-sources.md) | Appendix D |
| [appendix-a-source-register.md](appendix-a-source-register.md), [evidence-map-and-patterns.md](evidence-map-and-patterns.md), [appendix-d-verification.md](appendix-d-verification.md) | Evidence companion, Parts 1–3 |

No source-repository scripts were executed. A copy of the version 1.0 files was kept outside the project during the revision.

## License

The handbook text, tools and diagrams are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). You may share and adapt them, including commercially, with attribution.

The license covers this repository’s own content only. Cited sources, such as reports, articles, case studies and the FINOS repository, belong to their respective owners and are referenced, not redistributed. Organization names appear only as references to published sources and do not imply endorsement. The worked example in Appendix B is fictional.
