# Conversation, Not Delegation

<!-- BADGES:START -->
[![ai](https://img.shields.io/badge/-ai-ff6f00?style=flat-square)](https://github.com/topics/ai) [![human-ai-interaction](https://img.shields.io/badge/-human--ai--interaction-blue?style=flat-square)](https://github.com/topics/human-ai-interaction) [![critical-thinking](https://img.shields.io/badge/-critical--thinking-blue?style=flat-square)](https://github.com/topics/critical-thinking) [![prompting](https://img.shields.io/badge/-prompting-blue?style=flat-square)](https://github.com/topics/prompting) [![quarto](https://img.shields.io/badge/-quarto-blue?style=flat-square)](https://github.com/topics/quarto) [![book](https://img.shields.io/badge/-book-795548?style=flat-square)](https://github.com/topics/book) [![ai-partnership](https://img.shields.io/badge/-ai--partnership-blue?style=flat-square)](https://github.com/topics/ai-partnership)
<!-- BADGES:END -->

How to Think With AI, Not Just Use It

## About this Book

Most people use AI to get outputs. They delegate tasks, collect answers, and move on. That approach gets you something, but it costs you something too — it costs you the thinking that would have made you better at your work.

This book teaches a different way. Instead of delegating to AI, you can **converse** with it — brainstorming, challenging assumptions, stress-testing reasoning, and exploring angles you would not have considered alone. When you do this, the AI does not replace your thinking. It amplifies it.

You do not need a technical background. You do not need to write code. You need curiosity, a willingness to think critically, and a problem worth solving.

## Book Structure

The book is organized into the following sections:

### Part 1: Understanding the Landscape
- The Delegation Trap
- What Is AI?
- What Are Large Language Models?
- Does AI Make Us Dumber?

### Part 2: Principles
- AI Last
- The Conversation Loop
- Staying Critical
- VET Your AI: The Push-Back Framework

### Part 3: The Methodology
- Is Prompting Dead?
- Prompt Chaining: Building on What You Started
- Eight Techniques for Deeper Thinking
- Using AI to Help You Use AI

### Part 4: Putting It Together
- Conversations Across Disciplines: a complete community-workshop case
- When the Loop Runs Itself (advanced and optional)
- Becoming More Capable

### Appendices
- Prompt Structuring Frameworks (RTCF, CRAFT, CO-STAR, RISEN, APE)
- Quick Reference Cards
- Further Reading
- About the Author

## Related Books

This book is a standalone guide to thinking with AI. It has a companion book that applies the same methodology to Python programming, but neither requires the other.

- **[Converse Python, Partner AI](https://michael-borck.github.io/converse-python-partner-ai)**: The same conversation-based methodology, through the lens of Python development

Other books by the same author cover specific technical tracks:

- **[Think Python, Direct AI](https://michael-borck.github.io/think-python-direct-ai)**: Computational Thinking for Beginners
- **[Code Python, Consult AI](https://michael-borck.github.io/code-python-consult-ai)**: Python Fundamentals for the AI Era
- **[Ship Python, Orchestrate AI](https://michael-borck.github.io/ship-it-python-in-production)**: Professional Python in the AI Era
- **[Build Web, Guide AI](https://michael-borck.github.io/build-web-guide-ai)**: Business Web Development with AI

## Development

This book is being developed as a [Quarto](https://quarto.org/) project, with content written in Markdown format.

To build the book locally:

```bash
quarto render
```

The rendered output will be in the `_book/` directory. To build the web edition and preprocessed 6 × 9 inch PDF/EPUB locally from the parent workspace:

```sh
python book-publisher/publish.py --book cnd --llm --preprocess --render
python conversation-not-delegation/scripts/check_manuscript.py
```

The core practice includes paper/comparative routes and a fully worked example with printed inputs. No AI account is required. See [EDITORIAL-REVISION.md](EDITORIAL-REVISION.md) for the revision and validation record. This command does not publish the website or upload to KDP.

## License

This work is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

## Contact

Michael Borck — [GitHub](https://github.com/michael-borck)

## Repository Structure

This book is part of the [books.borck.education](https://books.borck.education) series. Publishing (PDF, EPUB, llm.txt, chatbot, cover generation) is handled by the [book-publisher](https://github.com/michael-borck/book-publisher) repo.

| Path | Purpose |
|---|---|
| `index.qmd` | Preface (landing page) |
| `_quarto.yml` | Reading order and Quarto formats |
| `cover.png` | Cover image |
| `copyright-page.tex` | Copyright page for PDF |
| `pdf-header.tex` | LaTeX header for PDF |
| `epub-styles.css` | EPUB styles |
| `scripts/` | Offline manuscript regression checks |
| `notes/` | Working notes, outlines, planning docs (not published) |
| `rag-documents/` | Generated RAG chunks for chatbot |
| `_book/` | Rendered output (gitignored) |
| `_print_source/` | Generated print source (gitignored) |
