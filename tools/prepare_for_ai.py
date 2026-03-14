#!/usr/bin/env python3
"""
Prepare 'Conversation, Not Delegation' for ingestion into an LLM.

Reads all chapter and appendix .qmd files in book order, strips YAML
frontmatter and image references, and writes a single clean text file
ready to paste into ChatGPT, Claude, NotebookLM, or any other AI tool.

Usage:
    python prepare_for_ai.py              # writes to conversation-not-delegation.txt
    python prepare_for_ai.py output.txt   # writes to output.txt
"""

import re
import sys
from pathlib import Path

# Book structure in reading order
CHAPTERS = [
    "index.qmd",
    "chapters/what-is-ai.qmd",
    "chapters/what-are-llms.qmd",
    "chapters/the-delegation-trap.qmd",
    "chapters/does-ai-make-us-dumber.qmd",
    "chapters/the-conversation-loop.qmd",
    "chapters/ai-last.qmd",
    "chapters/staying-critical.qmd",
    "chapters/rtcf.qmd",
    "chapters/prompt-chaining.qmd",
    "chapters/seven-techniques.qmd",
    "chapters/using-ai-to-help-you-use-ai.qmd",
    "chapters/vet-your-ai.qmd",
    "chapters/conversations-across-disciplines.qmd",
    "chapters/becoming-more-capable.qmd",
    "appendices/a-craft-framework.qmd",
    "appendices/b-quick-reference.qmd",
    "appendices/c-further-reading.qmd",
]


def strip_frontmatter(text):
    """Remove YAML frontmatter between --- markers."""
    return re.sub(r"\A---\n.*?\n---\n*", "", text, count=1, flags=re.DOTALL)


def strip_images(text):
    """Remove image references (![...](...))."""
    return re.sub(r"!\[.*?\]\(.*?\)\{?.*?\}?", "", text)


def strip_mermaid(text):
    """Remove mermaid code blocks."""
    return re.sub(r"```\{mermaid\}.*?```", "", text, flags=re.DOTALL)


def strip_quarto_directives(text):
    """Remove Quarto-specific directives like ::: callouts and {#sec-...}."""
    text = re.sub(r"\{#sec-[\w-]+(?:\s+\.[\w-]+)?\}", "", text)
    text = re.sub(r"^:::\s*\{.*?\}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^:::\s*$", "", text, flags=re.MULTILINE)
    return text


def clean(text):
    """Apply all cleaning steps."""
    text = strip_frontmatter(text)
    text = strip_images(text)
    text = strip_mermaid(text)
    text = strip_quarto_directives(text)
    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    project_root = Path(__file__).resolve().parent.parent
    output_file = sys.argv[1] if len(sys.argv) > 1 else "conversation-not-delegation.txt"
    output_path = project_root / output_file

    sections = []
    sections.append("CONVERSATION, NOT DELEGATION")
    sections.append("How to Think With AI, Not Just Use It")
    sections.append("By Michael Borck")
    sections.append("=" * 60)

    for chapter_path in CHAPTERS:
        full_path = project_root / chapter_path
        if not full_path.exists():
            print(f"  Skipping (not found): {chapter_path}")
            continue
        text = full_path.read_text(encoding="utf-8")
        cleaned = clean(text)
        if cleaned:
            sections.append(f"\n{'=' * 60}")
            sections.append(f"SOURCE: {chapter_path}")
            sections.append(f"{'=' * 60}\n")
            sections.append(cleaned)

    output_path.write_text("\n".join(sections) + "\n", encoding="utf-8")

    word_count = sum(len(s.split()) for s in sections)
    print(f"Written to: {output_path}")
    print(f"Word count: ~{word_count:,}")
    print(f"Chapters:   {len(CHAPTERS)}")
    print(f"\nPaste this file into ChatGPT, Claude, NotebookLM, or any AI tool.")
    print(f"Then have a conversation with it — push back, question, iterate.")


if __name__ == "__main__":
    main()
