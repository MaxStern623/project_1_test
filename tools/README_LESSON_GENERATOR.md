Lesson Generator
================

This small utility can generate short lessons from a template and instructor notes. It will attempt to use LangChain/OpenAI when an `OPENAI_API_KEY` is present and the packages are installed. If those are not available, it will fall back to a deterministic local generator.

Usage (fallback/local):

```bash
# Create two small files: template.md and notes.md
python -m tools.lesson_generator --template template.md --notes notes.md
```

Usage (LLM):

```bash
export OPENAI_API_KEY=sk-...
pip install langchain openai
python -m tools.lesson_generator --template template.md --notes notes.md --model gpt-4o-mini
```

The fallback generator produces a simple markdown structure: title (first non-empty line of the template), learning objectives (3 bullets derived from notes), an overview, suggested activities and a short assessment.

The tool is intentionally small and safe for CI environments where external API access is not available.
