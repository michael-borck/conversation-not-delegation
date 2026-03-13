# Conversation, Not Delegation — Book Scaffold & Claude Code Brief

## Context for Claude Code

This document is a complete brief for building the generic (non-Python) edition of
*Conversation, Not Delegation*. A separate Python-centric edition (*Converse Python,
Partner AI*) covers the programming audience. This book targets anyone who uses AI
as a thinking tool — students, professionals, researchers, educators — across any
discipline.

The book is authored by Michael Borck, published under MIT licence, and will be
released as both a free Quarto website (GitHub Pages) and a KDP paperback. All
content must be discipline-agnostic. Python-specific examples belong in the sibling
book, not here.

The following existing `.qmd` source files are available in the repo and should be
drawn on, adapted, and reorganised according to this scaffold. They must not be
copied verbatim — each needs light editing to remove any Python-specific framing
and to fit the voice and argument of this book.

---

## Source Files Available

| File | Use in book |
|---|---|
| `what-is-ai.qmd` | Part 1, Chapter 1 |
| `what-are-llms.qmd` | Part 1, Chapter 2 |
| `cognitive-offload.qmd` | Part 1, Chapter 4 |
| `ai-last-resort-philosophy.md` | Part 2, Chapter 6 (needs reframe — see notes) |
| `rtcf-prompt-framework.md` | Part 3, Chapter 8 |
| `prompt-chaining.qmd` | Part 3, Chapter 9 |
| `seven-techniques.qmd` | Part 3, Chapter 10 |
| `ai-to-help-you-use-ai.qmd` | Part 3, Chapter 11 |
| `strategic-prompting-guide.qmd` | Part 3, Chapter 10 (merge or companion) |
| `ethics-integrity.qmd` | Woven through — not a standalone chapter |
| `how-to-tell-whats-real-online.qmd` | Part 3, Chapter 12 (VET companion) |
| `craft-prompting-framework.qmd` | Reference only — RTCF is preferred, CRAFT is appendix |
| `cognitive-prompting.qmd` | Background context only — do not include directly |

---

## Book Structure

### Front Matter

- Title page
- About this book (one page: what it is, who it is for, how to use it)
- A note on the sibling book (*Converse Python, Partner AI*)

---

### Part 1 — Understanding the Landscape

The scene-setting section. Gives readers enough foundation to understand why the
CND mindset matters without being an AI literacy textbook.

---

**Chapter 1 — What Is AI?**

*Source: `what-is-ai.qmd`*

Light edit only. Remove any business-school-specific framing. Keep the "no magic,
just software" tone. Ensure the closing section connects forward to LLMs specifically.

Key points to preserve:
- AI is pattern recognition, not thinking
- Three convergent forces that made now different (data, compute, algorithms)
- The practical framing: AI as a capable but literal collaborator

---

**Chapter 2 — What Are Large Language Models?**

*Source: `what-are-llms.qmd`*

Light edit. Remove "Prerequisites: Read What is AI?" (it now precedes this chapter
naturally). Keep the "predicts the next word" core explanation — it is excellent.

Key points to preserve:
- LLMs learned from prediction but generalised to reasoning
- They have read everything and experienced nothing (this phrase must survive —
  it is a throughline for the whole book)
- Why this matters for how you work with them

---

**Chapter 3 — The Delegation Trap**

*Source: New chapter — no existing file. Write from scratch.*

This is the philosophical heart of the book and should be treated as such.
Draw on the framework description Michael provided:

Core argument:
- Delegation gets you output. Conversation gets you understanding.
- The delegation mindset asks: "How do I get AI to do this for me?"
- The conversation mindset asks: "How do I use AI to think better with me?"
- Judgement cannot be delegated to something that has read everything but
  experienced nothing.

Include:
- The Delegation vs Conversation mindset table (two-column: what you ask, what
  you get, what you lose)
- The "process over product" argument: those who obsess over process will always
  outperform those who collect outputs
- The bottom line: the goal is not to get AI to do your work. It is to become
  more capable yourself, with AI as your thinking partner.

Tone: Direct. This chapter should feel like a manifesto, not a lecture.

---

**Chapter 4 — Does AI Make Us Dumber?**

*Source: `cognitive-offload.qmd`*

Minimal editing required — this chapter is already excellent and largely
discipline-agnostic. The "metacognitive laziness" framing is exactly right.

Key points to preserve:
- Cognitive offload is not new and not inherently bad
- The real risk is outsourcing judgement, not effort
- Active use (conversation) preserves and builds capability; passive use
  (delegation) erodes it
- Connect closing to Chapter 3's argument: conversation is the protective practice

---

### Part 2 — Principles

Four principles that govern how a good AI conversation works. These are mindset
layers, not techniques. Techniques come in Part 3.

---

**Chapter 5 — The Conversation Loop**

*Source: New chapter — written from scratch, anchored to the diagram.*

The Conversation Loop (Brainstorm / Ideate / Iterate / Amplify / Repeat) is the
organising metaphor for the entire methodology. This chapter introduces it and
explains what is happening at each stage.

Structure:
- Open with the diagram description: four stages in a loop, with a feedback arc
  from Amplify back to Brainstorm
- Explain each stage in one to two paragraphs:
  - Brainstorm: you arrive with a question, a problem, or a half-formed idea —
    not a task to outsource
  - Ideate: you and AI explore possibilities together; this is generative and
    divergent
  - Iterate: you push back, refine, redirect; this is where conversation happens
    and delegation is most tempting
  - Amplify: you take the best of what emerged and make it yours; you own the
    output
  - Repeat: most good work loops more than once; knowing when to re-enter is a skill
- Close with: "Your expertise + AI's breadth = amplified thinking. The bottleneck
  is your thinking, not the model."

This chapter should be short and visual-friendly. The diagram does most of the work.

---

**Chapter 6 — AI Last**

*Source: `ai-last-resort-philosophy.md`*

Significant reframe required. The existing file is written for developers (tokens,
API costs, rate limits). Rewrite for a general audience using the same core logic
but framed around cognitive effort and skill preservation rather than cost.

Core argument stays identical:
- Solve as much as you can before reaching for AI
- Smaller, focused prompts produce better results
- You stay sharp by doing the groundwork yourself
- AI earns its keep on the genuinely hard parts

Replace developer-specific examples with discipline-agnostic equivalents:
- Instead of "linters and formatters", use "your notes, your prior knowledge,
  your search results"
- Instead of "token costs compound at scale", use "effort compounds: the less
  thinking you do, the less capable you become"
- The five-step workflow can stay structurally but needs example rewrite

Remove the Further Reading section (developer-specific references).

---

**Chapter 7 — Staying Critical**

*Source: New chapter — draws on `ethics-integrity.qmd` and
`how-to-tell-whats-real-online.qmd` for material but is not a reproduction.*

This is the ethics answer — embedded as a practical principle, not a governance
lecture. The chapter's job is to answer: "How do I make sure I'm the one thinking?"

Structure:
- Short opening: AI is confident even when wrong. Your critical eye is not
  optional.
- Academic integrity as a specific case (2-3 paragraphs max — real stakes,
  practical habits, not moralising)
- The Flag System from `how-to-tell-whats-real-online.qmd` condensed to a
  practical reference (Yellow flag / Red flag table can be preserved but tightened)
- Close: connect forward to VET Your AI in Part 3 as the operational version of
  this principle

---

### Part 3 — The Methodology

This is the practical section. Each chapter gives readers something they can use
immediately. Sequence mirrors the Conversation Loop.

---

**Chapter 8 — RTCF: Starting Conversations Well**

*Source: `rtcf-prompt-framework.md`*

RTCF (Role, Task, Context, Format) is the entry-level prompting framework for this
book. CRAFT is in the appendix for reference but RTCF is the primary tool.

Edits required:
- Remove ISYS6014 module framing and "Week 1" references
- Remove CloudCore-specific examples; replace with discipline-agnostic equivalents
  across three domains: writing/research, data/analysis, professional/workplace
- Keep the Quick Reference Card — it is excellent
- Add a short section: "RTCF is a scaffold, not a script" — once you internalise
  the four elements, you stop filling out a template and start thinking in terms
  of what the AI needs to know
- Keep the "Connection to Assessments" section only if rewritten generically;
  otherwise remove

---

**Chapter 9 — Prompt Chaining: Building on What You Started**

*Source: `prompt-chaining.qmd`*

Light edit. Already mostly discipline-agnostic. Remove any Python-specific examples
if present. Ensure the three approaches (Guided Workflow, Sequential, Parallel) are
illustrated with generic examples — research, writing, analysis, planning.

Key point to emphasise: prompt chaining is the Iterate stage of the Conversation
Loop made explicit. Each link in the chain is a moment where you review and steer.

---

**Chapter 10 — Seven Techniques for Deeper Thinking**

*Source: `seven-techniques.qmd` and `strategic-prompting-guide.qmd`*

The seven techniques are good and mostly discipline-agnostic. Edit as follows:
- Remove educator-specific framing ("for your students") — reframe all seven as
  techniques the reader uses themselves
- Merge the three strategic techniques from `strategic-prompting-guide.qmd`
  (Risk Deep-Dive, Reverse Prompting, AI Debate) as an eighth, ninth, and tenth
  technique or as a "strategic layer" subsection
- Use the same example domain variety across all techniques: one workplace example,
  one research/study example, one personal/professional development example

---

**Chapter 11 — Using AI to Help You Use AI**

*Source: `ai-to-help-you-use-ai.qmd`*

Light edit. Already excellent and discipline-agnostic. The meta-prompting concept
is one of the most practically useful ideas in the book.

Add a short bridge at the end connecting to VET: "Once AI has helped you figure
out what to ask, VET helps you make sure you can stand behind the answer."

---

**Chapter 12 — VET Your AI: The Push-Back Framework**

*Source: New chapter — written from scratch, anchored to the framework.*

VET (Verify, Explain, Test) is the critical evaluation layer that runs through
the Iterate stage of the Conversation Loop. It operationalises "staying critical"
from Chapter 7 into a three-step habit.

Structure:
- Open: the most dangerous AI output is the one that sounds right
- Introduce the three steps with their questions:
  - Verify: Can I find this independently? (Check sources, cross-reference claims,
    look up citations)
  - Explain: Can I explain this in my own words? (If not, you don't understand it.
    Rewrite in your language. Teach it to someone.)
  - Test: Does this hold up under scrutiny? (Devil's advocate it. Check edge cases.
    Ask "what if?")
- One worked example showing VET applied to an AI output in a realistic scenario
- Close: VET is not about distrusting AI. It is about owning the output.

---

### Part 4 — Putting It Together

Two short chapters that move from individual skills to integrated practice.

---

**Chapter 13 — A Conversation Across Disciplines**

*Source: New chapter — written from scratch with worked examples.*

Four complete worked examples showing the full Conversation Loop in practice
across four different domains. Each example should show a realistic starting
point, a realistic AI conversation (summarised, not transcribed), and the human
steering decisions that made it a conversation rather than a delegation.

Domains:
1. Writing and research (essay planning, literature review, argument development)
2. Data and analysis (interpreting results, identifying patterns, stress-testing
   conclusions)
3. Planning and decision-making (project scoping, risk identification, option
   comparison)
4. Professional communication (drafting, revising, adapting tone for audience)

Each example should explicitly call out which stage of the Conversation Loop is
active and which framework (RTCF / prompt chaining / VET) is in use.

---

**Chapter 14 — Becoming More Capable**

*Source: New chapter — closing argument, written from scratch.*

This is the book's conclusion. It should feel earned, not added.

Core argument:
- The goal was never to get AI to do more. It was to become more capable yourself.
- The practices in this book compound: better questions produce better conversations;
  better conversations produce deeper understanding; deeper understanding produces
  better questions.
- "Judgement can't be delegated to something that has read everything but experienced
  nothing." — return to this phrase as the closing note.

Short chapter. Do not pad.

---

### Back Matter

**Appendix A — CRAFT Prompting Framework**

*Source: `craft-prompting-framework.qmd`*

Included as a reference appendix for readers who encounter CRAFT in other contexts
or prefer a five-element structure. Note its relationship to RTCF: same family,
slightly more detailed, equally valid.

---

**Appendix B — Quick Reference Cards**

Collect the key one-page references in one place:
- RTCF quick reference card
- VET Your AI three-step card
- Conversation Loop stage summary
- Seven Techniques at a glance

---

**Appendix C — For Educators**

A short note (not a chapter) directing educators to the companion book
*Partner, Don't Police* for assessment design, rubric frameworks, and the
"Conversation Not Delegation" approach applied to student work. Include the
GitHub link.

---

## Voice and Tone Notes for Claude Code

- Direct, not academic. This is a practitioner book.
- Short paragraphs. White space is not wasted.
- No em dashes. Use commas, colons, or a new sentence instead.
- The phrase "has read everything but experienced nothing" is a throughline — it
  appears in Chapter 2, Chapter 3, and Chapter 14. Do not cut it.
- Examples should span disciplines. Never three examples from the same domain in
  the same chapter.
- Do not moralize. When ethics comes up, it comes up as practical stakes, not
  lecture.
- The book's argument is coherent: Chapters 1-2 establish what AI is, Chapter 3
  establishes what goes wrong, Chapters 4-7 establish the principles that fix it,
  Chapters 8-12 give the tools, Chapters 13-14 show it working and close the loop.
  Every chapter should feel like it advances this argument, not just adds content.

---

## Slide Content Reference (Exact Text)

These are the exact phrases and structures from the source presentation slides.
Use this wording precisely -- these are the canonical formulations of each
framework and should appear verbatim in the relevant chapters.

---

### Title Slide

**Conversation, Not Delegation**
*Your expertise + AI's breadth = amplified thinking*

Use the subtitle as a recurring touchstone. It appears on the title page and
should be echoed in Chapter 5 (The Conversation Loop) and Chapter 14 (Becoming
More Capable).

---

### The Power of Conversational Analysis

> A single prompt gives you a single answer.
> A **conversation** gives you **understanding**.

Use this as the opening lines of Chapter 3 (The Delegation Trap). It is the
clearest possible statement of the book's core argument and should land early.

---

### The Conversation Loop

**Diagram:** Brainstorm → Ideate → Iterate → Amplify (with feedback arc back to Brainstorm)

**Taglines (both must appear):**
- *Your expertise + AI's breadth = amplified thinking*
- *The bottleneck is your thinking, not the model.*

The diagram should be recreated as a Mermaid flowchart in Chapter 5. The two
taglines appear together immediately below the diagram.

---

### The RTCF Framework

*A simple structure for your AI conversations:*

| Component | Question | Example |
|---|---|---|
| **Role** | Who should AI be? | "You are an experienced food scientist..." |
| **Task** | What should it do? | "Analyse this fermentation data..." |
| **Context** | What background? | "Oat milk study, 4 treatments, 48 hours..." |
| **Format** | How should output look? | "Table with statistical summary..." |

---

### VET Your AI

*A simple 3-step push-back framework:*

**Verify** -- Can I find this independently?
- Check sources
- Cross-reference claims
- Look up citations

**Explain** -- Can I explain this in my own words?
- If not, you don't understand it
- Rewrite in your language
- Teach it to someone

**Test** -- Does this hold up under scrutiny?
- Devil's advocate it
- Check edge cases
- Ask "what if?"

---

### VET in Practice

This table is the worked example for Chapter 12. Use it as the primary
illustration of VET applied to real AI output. The scientific domain (fermentation,
pH, temperature) makes it discipline-agnostic in the sense that it is clearly
not the reader's field -- which is the point. VET works even when you are not
the domain expert.

| AI says... | V: Verify | E: Explain | T: Test |
|---|---|---|---|
| "Studies show pH drops faster in co-culture" | Find the actual studies | Can I explain the mechanism? | What about different substrates? |
| "Optimal temperature is 37C" | Check the literature | Why 37C specifically? | What happens at 35C or 40C? |
| "This method has 95% recovery rate" | Where's that number from? | What does 95% mean here? | Under what conditions? |

---

## Images for the Repo (Assets)

The following images should be saved into the book's `images/` or `assets/`
directory for reference during development. They are the source slides that
the written content is drawn from. Claude Code does not need to embed them
directly -- the text content is captured above -- but having them in the repo
is useful for visual consistency checks and for any future slide/presentation
derivatives.

Files to include:
- `conversation-not-delegation-title.png` -- title slide
- `conversation-loop-diagram.png` -- the Brainstorm/Ideate/Iterate/Amplify diagram
- `vet-your-ai.png` -- the three-column VET framework
- `vet-in-practice.png` -- the worked example table
- `rtcf-framework.png` -- the four-column RTCF framework
- `power-of-conversational-analysis.png` -- the "single prompt / conversation" slide

The Conversation Loop diagram should be recreated natively in Mermaid for the
HTML output and as a clean SVG for the PDF/KDP output. The screenshot version
is a reference only.

---

## Quarto Config Notes

- Output targets: HTML (GitHub Pages) and PDF (KDP paperback)
- Numbering: chapters numbered, appendices lettered
- The Conversation Loop diagram from the slides should be recreated in Mermaid
  or as an SVG asset — do not rely on screenshot images in the final book
- Cross-references between chapters should use Quarto's `@sec-` syntax

---

## KDP Differentiation Notes

The Python sibling book (*Converse Python, Partner AI*) will share the same core
methodology. To satisfy KDP duplicate content requirements:
- This book's examples must be entirely non-Python
- Chapter 3 (The Delegation Trap) and Chapter 14 (Becoming More Capable) are the
  philosophical anchors and will have the most shared conceptual content — these
  must be written fresh in each book, not copied
- The methodology chapters (8-12) will share structure but differ entirely in
  examples
- Both books should be independently coherent — a reader of one should not need
  the other
