# Codex instruction: Write the Macintosh PiForma Owner's Guide

You are producing the **full editable manuscript and Typst-based manual**, not just a four-page design test. The user will provide original Macintosh Plus and Macintosh SE Owner's Guide PDFs as design references, along with a current Typst project, photos and project repos where accessible.

Read **every file in this handoff packet** before drafting. Preserve detailed instructions, especially the exact bag layer order, keyboard orientation, battery wake problem, chime troubleshooting and the user's particular voice.

## Mission

Build a useful, period-authentic **Macintosh PiForma Owner's Guide** following the chapter organization of the Macintosh Plus manual, borrowing compatible SE visual conventions. It should sound like a semi-professional, friendly, modestly witty hobbyist who actually built the machine, without fluff or invented facts. Technical content needs to be specific and correct. Do not use original Apple manual passages verbatim; use them for structure and design reference.

## Important boundaries

- The current owner account of operations has highest priority, followed by verified live docs/configuration.
- PiForma is an experimental one-off built into an Apple IIc Monitor shell, not an officially manufactured Apple Macintosh.
- `Macintosh-PiForma-docs` is the intended canonical source; avoid introducing a competing factual documentation system. Inspect real source when available.
- Hardware details with unresolved status must remain marked for confirmation. If project documents contradict owner recollection, surface that fact and ask a focused question.
- Retain the humorous no-support section but do not falsely claim Apple approval, certification, service contracts or warranties.
- Bose speakers and stands require a real section even though model/connection/packing information is currently missing.
- No index initially. No disc/disk chapters or SCSI.

## Initial task sequence

1. Read handoff files, the Apple manuals, existing Typst source, and owner docs/repositories where available.
2. Produce `working-outline.md` with proposed final chapters, estimated content breadth and specific illustration slots.
3. Produce manuscript drafts of Welcome, About This Manual and Chapter 1 before changing the layout substantially.
4. Cross-check Chapter 1 actions against `content/02-chapter-1-getting-started.md` with a checklist. Don't lose layers, orientations, troubleshooting distinctions or packing/alignment caveats.
5. Draft Chapters 2 through 4, Appendix A and glossary using facts register. Insert explicit placeholders rather than invent anything.
6. Implement content as editable Typst, compile, inspect PDF/png renders, and compare actual geometry and illustrations against provided Apple manual PDFs. Iterate.
7. Produce a short `outstanding-questions.md` and `editorial-change-log.md`, plus final print-ready PDF only when material is verifiable enough.

## Definition of done for each chapter

Clear step-by-step instructions, authentic style, minimal fluff, illustration references where useful, every technical claim grounded in owner instruction or source, no conflicts hidden, successful PDF rendering and an open-issues list.

## Do now

Begin by summarizing the planned manual structure and any serious conflicts in source material. Then draft the first chapter. Do not silently finalize specifications you could not verify.
