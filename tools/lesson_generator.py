"""Lesson generator: uses LangChain/OpenAI when available, otherwise falls back to a safe local generator.

API:
  generate_lesson(template: str, notes: str, model: Optional[str]=None) -> str

CLI:
  python -m tools.lesson_generator --template TEMPLATE_FILE --notes NOTES_FILE

Behavior:
  - If langchain + openai packages are available and OPENAI_API_KEY present, it will attempt to call the LLM.
  - Otherwise it will use a deterministic, local template-based generator that produces a structured lesson.
"""
from __future__ import annotations

import argparse
import json
import os
from typing import Optional


def _local_generate(template: str, notes: str) -> str:
    """Produce a deterministic lesson from a template and notes without calling external services.

    The output is a short structured lesson in markdown.
    """
    # Minimal text normalization
    template = template.strip()
    notes = notes.strip()

    # Make small heuristics to pull a title and goals from the template/notes
    title = None
    for line in template.splitlines():
        if line.strip():
            title = line.strip()
            break
    if not title:
        title = "Lesson"

    # Extract 3 bullet points from notes if present
    bullets = []
    for line in notes.splitlines():
        line = line.strip()
        if not line:
            continue
        # treat lines starting with '-' or '*' as bullets
        if line.startswith("-") or line.startswith("*"):
            bullets.append(line.lstrip("-* "))
        else:
            # split longer lines into simple bullets heuristically
            if len(bullets) < 3 and len(line) > 40:
                # cut at 40 chars
                bullets.append(line[:60].rstrip() + "...")
            elif len(bullets) < 3:
                bullets.append(line)
        if len(bullets) >= 3:
            break

    if not bullets:
        bullets = ["Introduce the topic.", "Show an example.", "Add exercises."]

    # Build a simple lesson structure
    parts = []
    parts.append(f"# {title}\n")
    parts.append("## Learning Objectives")
    for b in bullets:
        parts.append(f"- {b}")
    parts.append("\n## Overview")
    parts.append(template)
    parts.append("\n## Suggested Activities")
    parts.append("1. Quick demo/example\n2. Guided exercise\n3. Reflection questions")
    parts.append("\n## Short Assessment")
    parts.append("- 3 short questions to check comprehension")

    return "\n\n".join(parts)


def generate_lesson(template: str, notes: str, model: Optional[str] = None) -> str:
    """Generate a lesson using an LLM if available, otherwise use a local fallback.

    The function keeps behaviour deterministic when falling back.
    """
    # Try to use LangChain/OpenAI if available and API key is present
    if os.environ.get("OPENAI_API_KEY"):
        try:
            # Lazy import to avoid hard dependency
            from langchain import LLMChain, PromptTemplate
            from langchain.llms import OpenAI

            prompt_text = (
                "You are an instructional designer. Given a template and notes, "
                "produce a short lesson in markdown with: title, learning objectives, overview, activities, and a short assessment.\n\n"
                "Template:\n{template}\n\nNotes:\n{notes}\n\nLesson:\n"
            )
            prompt = PromptTemplate(template=prompt_text, input_variables=["template", "notes"])
            llm = OpenAI(model_name=model or "gpt-4o-mini", temperature=0.0)
            chain = LLMChain(llm=llm, prompt=prompt)
            out = chain.run({"template": template, "notes": notes})
            return out
        except Exception:
            # If any error occurs (missing packages, network issues), fall back
            pass
    # Fallback deterministic generator
    return _local_generate(template, notes)


def _read_file(path: str) -> str:
    with open(path, "r", encoding="utf8") as fh:
        return fh.read()


def _cli() -> int:
    parser = argparse.ArgumentParser(description="Generate a lesson from template and notes or a reference doc")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--template", help="Path to template file")
    group.add_argument("--reference", help="Path to a reference document (single file) to inspire the lesson")
    parser.add_argument("--notes", help="Path to notes file (used with --template)")
    parser.add_argument("--model", required=False, help="Optional model name for remote LLM")
    parser.add_argument("--json", action="store_true", help="Output JSON with fields {title, lesson}")
    parser.add_argument("--output", help="Write lesson to a file instead of stdout")
    args = parser.parse_args()

    if args.reference:
        # Use the reference file as both template and notes to let the generator summarize it
        template = _read_file(args.reference)
        notes = template
    else:
        if not args.template or not args.notes:
            parser.error("--template and --notes are required when --reference is not used")
        template = _read_file(args.template)
        notes = _read_file(args.notes)

    lesson = generate_lesson(template, notes, model=args.model)

    if args.json:
        # Try to extract title as first header
        title = None
        for line in template.splitlines():
            if line.strip():
                title = line.strip()
                break
        out_data = json.dumps({"title": title or "Lesson", "lesson": lesson}, ensure_ascii=False, indent=2)
        if args.output:
            with open(args.output, "w", encoding="utf8") as fh:
                fh.write(out_data)
        else:
            print(out_data)
    else:
        if args.output:
            with open(args.output, "w", encoding="utf8") as fh:
                fh.write(lesson)
        else:
            print(lesson)
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
