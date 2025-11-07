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
import re
import shutil
from pathlib import Path
from typing import List, Optional


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


def _split_into_topics(text: str) -> List[dict]:
    """Split lesson text into smaller topics using headings and simple heuristics.

    Returns a list of dicts: {"title": str, "summary": str}
    """
    topics: List[dict] = []
    lines = text.splitlines()
    cur_title: Optional[str] = None
    cur_lines: List[str] = []

    def flush():
        if cur_title or cur_lines:
            title = cur_title or (cur_lines[0] if cur_lines else "Topic")
            summary = "\n".join(cur_lines).strip()
            topics.append({"title": title.strip(), "summary": summary})

    for ln in lines:
        stripped = ln.strip()
        if not stripped:
            if cur_lines:
                cur_lines.append(ln)
            continue
        if re.match(r"^#{1,6}\s+", stripped):
            if cur_title or cur_lines:
                flush()
            cur_title = re.sub(r"^#{1,6}\s+", "", stripped)
            cur_lines = []
            continue
        if re.match(r"^(-|\*|\d+\.)\s+", stripped) and not cur_title:
            if cur_lines:
                flush()
            cur_title = None
            cur_lines = [stripped]
            continue
        cur_lines.append(ln)

    flush()
    if not topics:
        topics.append({"title": "Lesson", "summary": text})

    for t in topics:
        t["title"] = t.get("title") or "Topic"
        t["summary"] = (t.get("summary") or "").strip()
    return topics


def _generate_example_code(topic: dict) -> str:
    """Create a tiny example function illustrating the topic using simple heuristics."""
    title = (topic.get("title") or "topic").lower()
    func_name = re.sub(r"[^0-9a-zA-Z_]+", "_", title).strip("_")[:30] or "example"
    # function name must not start with a digit
    if func_name and func_name[0].isdigit():
        func_name = f"f_{func_name}"
    if "sum" in title or "total" in title or "add" in title:
        code = f"def {func_name}(numbers):\n    \"\"\"Return the sum of a list of numbers.\"\"\"\n    return sum(numbers)\n"
    elif "reverse" in title or "reversed" in title:
        code = f"def {func_name}(s):\n    \"\"\"Return the reversed string.\"\"\"\n    return s[::-1]\n"
    elif "validate" in title or "is_" in title or "check" in title:
        code = f"def {func_name}(value):\n    \"\"\"A simple truthy checker.\"\"\"\n    return bool(value)\n"
    else:
        code = f"def {func_name}(x):\n    \"\"\"Return the input unchanged (example).\"\"\"\n    return x\n"
    return code


def _generate_student_skeleton(example_code: str) -> str:
    """Create an incomplete version of example_code with TODO markers for student to implement."""
    lines = example_code.splitlines()
    out_lines: List[str] = []
    in_def = False
    for ln in lines:
        if ln.startswith("def "):
            out_lines.append(ln)
            in_def = True
            continue
        if in_def:
            out_lines.append("    # TODO: implement this function")
            out_lines.append("    raise NotImplementedError()")
            in_def = False
            continue
        out_lines.append(ln)
    if not out_lines:
        return "# TODO: implement\n"
    return "\n".join(out_lines) + "\n"


def _generate_test_for_example(topic: dict, example_module: str, func_name: str, example_file_path: Optional[str] = None) -> str:
    """Generate a pytest file that tests the example function with a couple of cases."""
    tests = [
        "import pytest",
        f"from {example_module} import {func_name}",
    ]
    # Try to infer behavior by reading the source of the example module file if available
    src = ''
    try:
        if example_file_path:
            p = Path(example_file_path)
            if p.exists():
                src = p.read_text(encoding='utf8')
        else:
            mod_path = Path(example_module.replace('.', '/') + '.py')
            if mod_path.exists():
                src = mod_path.read_text(encoding='utf8')
    except Exception:
        src = ''

    if 'return sum' in src or 'sum(' in src:
        tests.append(f"def test_{func_name}_sum_basic():")
        tests.append(f"    assert {func_name}([1,2,3]) == 6")
        tests.append(f"    assert {func_name}([]) == 0")
    elif "return s[::-1]" in src or "[::-1]" in src:
        tests.append(f"def test_{func_name}_reverse_basic():")
        tests.append(f"    assert {func_name}('abc') == 'cba'")
        tests.append(f"    assert {func_name}('') == ''")
    elif 'return bool' in src or 'bool(' in src:
        tests.append(f"def test_{func_name}_truthy_basic():")
        tests.append(f"    assert {func_name}(1) is True")
        tests.append(f"    assert {func_name}(0) is False")
    else:
        # fallback: echo behavior
        tests.append(f"def test_{func_name}_echo_basic():")
        tests.append(f"    assert {func_name}(42) == 42")
        tests.append(f"    assert {func_name}('x') == 'x'")

    return "\n".join(tests) + "\n"


def create_lesson_package(lesson_markdown: str, out_dir: str, lesson_name: Optional[str] = None) -> Path:
    """Create a package folder with examples, student skeletons, tests, and a README.md lesson."""
    out = Path(out_dir).expanduser().resolve()
    lesson_name = lesson_name or re.sub(r"[^0-9a-zA-Z_-]", "_", (lesson_markdown.splitlines()[0] if lesson_markdown else "lesson")).strip('# ').strip()[:40]
    base = out / lesson_name
    # remove any existing generated lesson to avoid stale files
    if base.exists():
        shutil.rmtree(base)
    examples_dir = base / "examples"
    student_dir = base / "students"
    tests_dir = base / "tests"
    solutions_dir = base / "solutions"
    examples_dir.mkdir(parents=True, exist_ok=True)
    student_dir.mkdir(parents=True, exist_ok=True)
    tests_dir.mkdir(parents=True, exist_ok=True)
    solutions_dir.mkdir(parents=True, exist_ok=True)

    # write README.md (lesson)
    (base / "README.md").write_text(lesson_markdown, encoding="utf8")

    topics = _split_into_topics(lesson_markdown)
    created = []
    for i, topic in enumerate(topics, start=1):
        # normalize to valid python identifier fragment
        safe_title = re.sub(r"[^0-9a-zA-Z_]+", "_", (topic.get("title") or f"topic_{i}"))
        safe_title = re.sub(r"_+", "_", safe_title).strip("_").lower()[:40]
        if not safe_title:
            safe_title = f"topic_{i}"
        if safe_title[0].isdigit():
            safe_title = f"t_{safe_title}"
        example_name = f"example_{safe_title}.py"
        student_name = f"student_{safe_title}.py"
        test_name = f"test_{safe_title}.py"

        example_code = _generate_example_code(topic)
        student_code = _generate_student_skeleton(example_code)

        m = re.match(r"def\s+([0-9a-zA-Z_]+)", example_code)
        func_name = m.group(1) if m else "example"
        # ensure function name is a valid identifier and does not start with digit
        func_name = re.sub(r"[^0-9a-zA-Z_]+", "_", func_name)
        if func_name and func_name[0].isdigit():
            func_name = f"f_{func_name}"

        # write example and student files
        (examples_dir / example_name).write_text(example_code, encoding="utf8")
        (student_dir / student_name).write_text(student_code, encoding="utf8")
        # write a solved student solution (copy of the example) into solutions/
        (solutions_dir / student_name).write_text(example_code, encoding="utf8")

        module_path = f"examples.{Path(example_name).stem}"
        example_file = str((examples_dir / example_name).resolve())
        test_code = _generate_test_for_example(topic, module_path, func_name, example_file_path=example_file)
        (tests_dir / test_name).write_text(test_code, encoding="utf8")

        created.append({
            "topic": topic["title"],
            "example": str(examples_dir / example_name),
            "student": str(student_dir / student_name),
            "solution": str(solutions_dir / student_name),
            "test": str(tests_dir / test_name),
        })

    # ensure packages
    for p in (examples_dir, student_dir, tests_dir, solutions_dir, base):
        init = p / "__init__.py"
        if not init.exists():
            init.write_text("# package init\n", encoding="utf8")

    manifest = {"lesson": lesson_name, "created": created}
    (base / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf8")
    return base


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

            # Richer structured prompt: ask for JSON + a markdown lesson so the output
            # can be machine-parsed (JSON) and human-readable (Markdown). Keep temperature low
            # for deterministic output when possible.
            prompt_text = (
                "You are an expert instructional designer and experienced Python instructor."
                " Given a project template and instructor notes, produce TWO outputs separated by a line"
                " containing only '---OUTPUT-JSON-END---':\n\n"
                "(1) A strict JSON object with the following top-level keys:"
                " title (string), audience (string), estimated_duration (string), difficulty ("
                "\"beginner\"|\"intermediate\"|\"advanced\"), prerequisites (list of strings),"
                " learning_objectives (list of short strings), overview (string), activities (list of objects),"
                " assessment (list of question strings), example_solution (string, optional), references (list of strings)."
                " The activities list items should be objects with keys: title, steps (list of strings), duration."
                " Ensure the JSON is parseable and contains no explanatory text outside the JSON object.\n\n"
                "Then output (2) a human-friendly Markdown lesson with sections: Title, Learning Objectives, Overview, Suggested Activities, Short Assessment, Example Solution, References."
                " Use the provided Template and Notes to fill these fields. Keep JSON concise and markdown clear.\n\n"
                "Template:\n{template}\n\nNotes:\n{notes}\n\nJSON then Markdown:\n"
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
