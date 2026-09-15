# Developmental revision record

Revision completed: 2026-09-15. **Editorial revision closed; reader and release sign-off remain separate.**

This completes the approved follow-up to the structural/resource pass in
`95fd37a` and README correction in `3912a09`. It does not claim that a new
reader has tested the book or that a revised edition has been published.

## Disposition of the audit

| Area | Completed revision |
|---|---|
| Structure | Delegation Trap first; AI Last before the loop; VET immediately after Staying Critical; autonomous loops advanced/optional near the end. Stable chapter filenames and anchors retained. |
| Chapter ownership | Cognitive offload now separates assisted performance from learning; AI Last owns the workflow; the loop owns correction and handover; the conclusion asks for demonstrated transfer rather than repeating a manifesto. |
| Evidence | Qualified categorical claims about memory, retrieval, novelty, sycophancy, prompting, skill loss, and permanent employment advantages. Replaced misleading bibliography descriptions with direct primary sources and explicit limits. |
| Worked case | Complete fictional community workshop: initial attempt, source cards, failed proposal, weak/adequate/strong steering, corrected capacity/time/cost, VET, final owned note, and an unresolved approval. |
| Learning design | Observable outcomes for every part; cumulative learning record; independent changed-workshop task with answer checks; paper/comparative activities and accessibility options. |
| Cadence | Full repeated AI-practice ending retained in only 3/15 chapters. Removed duplicate conclusions and second epigraphs; reduced the eight-technique chapter from ten callouts to two. Short reference-style prompt examples remain intentional. |
| Decision map | One quick-reference map covering checkable delegation, conversation, bounded automation, and avoiding AI/seeking expertise. |
| Resources | Removed-tool promises remain retired. Corrected README order, licence wording to match the existing CC BY-SA licence, chapter download paths, and failing author-site destinations. Added an open-author-copy alternative for the PNAS paper. |
| Production | Replaced a Mermaid series diagram that generated malformed EPUB XHTML with a portable reading-path table. Rebuilt HTML, PDF, EPUB, and llm.txt. |

The original comics remain a deliberate series feature, not newly generated
illustrations or redesigned covers. Their rhetorical shorthand is not empirical
evidence; the LLM chapter explicitly qualifies its “read everything” comic.

## Length and style review

Approximate configured prose: **28,538 words**, versus 46,824 in the initial
audit (about 39% shorter, including the earlier removal of the tools appendix).
There are 20 configured QMD files and 15 core chapters.

Core chapters now range from roughly 939 to 2,179 words. The short introduction
to the trap, AI orientation, learning-evidence chapter, AI Last, optional loop
extension, and conclusion have distinct, bounded jobs and usable practice.
They were reviewed as deliberate short chapters, not expanded to hit a quota.
The worked case has printed inputs and a transfer task despite being compact.

The scan reports 21 callouts across configured files and 15 in core chapters.
No cross-file repeated sentences met the scanner's threshold. This is not a
claim that all rhetorical repetition disappeared. Framework names, concise
reference tables, and the series comics intentionally recur.

## Verification

- `python scripts/check_manuscript.py`: **4 tests passed**: configured order,
  local source references/assets, worked-case arithmetic, and practice variation.
- The same tests passed in an isolated source copy without `_book`,
  `_print_source`, `llm.txt`, or generated chatbot documents.
- Shared publisher `--book cnd --llm --preprocess --render`: successful HTML,
  PDF, EPUB, and canonical downloads.
- Rendered validator: **20 HTML pages; 1,401 local targets/anchors; zero errors**.
  EPUB ZIP integrity, XHTML well-formedness, internal links, and the configured
  chapter sequence in its 22-entry spine checked.
- PDF: **148 pages, 6 × 9 inches**. Chapter boundaries reviewed in reading order
  from extracted PDF text. Final physical pages 11–12 and 116–119 inspected
  visually: reading-path table, source cards, steering comparison, timetable,
  VET, and independent task. This is not a visual proofread of every page.
- Joint public-reference scan: 53/54 distinct URLs reachable. The PNAS DOI
  returned HTTP 403 to automated requests; the added author manuscript is
  accessible. Reachability does not validate a source's claims.
- Publisher metadata audit: zero errors; two existing KDP warnings remain:
  dashboard status unverified and KDP source commit unrecorded.
- `git diff --check`: checked at handoff.

## Reader and release gates—not completed by this revision

1. A reader unfamiliar with the book attempts the changed-workshop task without
   the answer key, then produces a capstone record. Record where instructions
   were unclear, whether all constraints were noticed, and what help was needed.
2. Complete a human page-by-page proofread and inspect the EPUB in a target
   reader. Automated XHTML checks do not test every reader's layout or
   accessibility. The PDF is not tagged.
3. Approve any cover change separately; inspect the print proof/KDP preview,
   verify publishing metadata, and choose the release version.

No source commit/push, GitHub Pages deployment, hosted chatbot refresh, or KDP
upload was performed in this closing revision. The local free-edition downloads
are rebuilt; hosted editions are unchanged.
