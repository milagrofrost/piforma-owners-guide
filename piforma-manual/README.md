# Current approved guide — October 17, 2026

Open the [74-page reviewed proof](output/macintosh-piforma-layout-reviewed.pdf). The approved study is applied throughout, with natural-width EB Garamond and direct specification language. Read [the change report](approved-redesign-report.md). Build instructions remain in the repository README. The active text baseline is `verification/manuscript-lock.json`.

# Active manual project

Start with the repository [README](../README.md) and [continuation handoff](../CONTINUING.md). Current reviewed proof: [63-page guide](output/macintosh-piforma-layout-reviewed.pdf).

Edit `manuscript/*.md` for prose, `styles/*.typ` for typography/layout and `assets/illustration-layout.json` for hardware-art size caps. Generated `chapters/*.typ` are included for direct Typst compilation but overwritten by the build. Screenshot crops are reproducible through `scripts/prepare-screenshots.py`; original numbered PNGs remain unchanged.

Run the build and the two verification commands documented in the root README. Current text baseline and saved checks are in `verification/`. The PDF is a working proof, not a final print release. The old four-page print-production prototype is intentionally excluded.

Keep owner corrections and verification questions in the fact register/editorial tracker, and capture needs in the photo checklist. See `../docs/history/working-session-readme.md` for the earlier session's chronological notes; it includes obsolete page counts and paths.
