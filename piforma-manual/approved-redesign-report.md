# Approved art direction applied — October 17, 2026

The full guide now follows the approved six-page study. The current proof is **69 PDF pages**, at 6 × 7.25 inches. [Reviewed guide](output/macintosh-piforma-layout-reviewed.pdf). Run `scripts/review-approved-redesign.py --iteration NAME` after a build to export the facing-page proof.

## Typography and compositions

EB Garamond replaces horizontally compressed Times New Roman. Body text is 10.5 pt at natural width in the existing 242 pt reading column, with 6 pt Typst leading and 7 pt paragraph spacing. Headings are natural-width 15/12 pt; marginal copy is 8.5 pt and captions 8 pt. Long headings have their own leading so their lines do not collide. No 85% scaling remains in the active book style.

The book uses all six approved composition families: dedicated chapter openings, text-led procedures with a genuine annotation rail, a full-page bag plate, grouped opposite-side controls, illustrated software stations, and open full-width technical tables. The stand drawing now sits between the stand and peripheral setup steps. The battery explanation and interior photograph form a deliberate facing-page pair. Short care and troubleshooting topics stay together; the service-department joke and frozen-application procedure are no longer split across a page turn.

The existing silent-startup paragraph appears alongside the startup instructions. The AtEase and Show Desktop stations use the existing paragraphs and screen pixels. An enlarged AtEase detail is explicitly identified as a detail of Figure 1-7. Original figure identifiers, all 28 original manuscript captions, illustration proportions, and supplied source PNGs are retained.

## More confident copy

At the owner's direction, specifications now state the details directly. “Recorded 4 GB RAM” becomes “4 GB RAM”; “Recorded power architecture” becomes “Power architecture.” The prose identifies the actual ports, charger, bag construction and replacement mouse wheel without repeatedly attributing them to project records. The technical appendix introduces the hardware and software directly.

This is an editorial confidence change using the existing facts, not a claim that new device testing took place. Archive-versus-installed-script distinctions, approximate startup timing, the unusual battery-wake behavior, hidden in-bag charging display, and other operationally meaningful qualifications remain. The owner's six-second active-application close, 84% photographed battery reading, exact packing/setup/shutdown procedures and humor are preserved. Provenance and unresolved editorial questions remain outside the publication copy.

## Review and validation

Two complete rendered iterations were inspected. The first exposed spacing problems around the new font's initials, cover lines and long headings; these were corrected before acceptance. The second build reports no compiler warnings, text-bound violations or text-overlap issues. Every page was inspected in rendered contact sheets; the principal instructional, hardware, battery, software and appendix spreads were also reviewed as facing pages.

All **22 editorial preservation checks** pass. All **372 manuscript text units** appear in the PDF, and all **28 source figure captions** occur once. Original software screenshot and interior-photo hashes match their provenance records. The publication contains no occurrence of “recorded.” Fonts are embedded. Physical print testing remains to be done.

The pre-redesign PDF and editable sources are saved locally in `output/redesign-2026-10-17/before-manual.pdf` and `before/`. The approved study remains an historical design reference; its original source lock describes the pre-redesign manuscript. The active baseline for further work is `verification/manuscript-lock.json`.
