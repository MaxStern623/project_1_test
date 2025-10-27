Lesson Generator
================

This document merges usage notes and the lesson generator description. The tool generates short lessons from a template and instructor notes, and can also use the project's `docs/RECREATE_PROJECT.md` as an example reference.

CLI options added:

- `--template PATH` (required unless `--reference` is used)
- `--notes PATH` (required unless `--reference` is used)
- `--reference PATH` (optional) — instead of template+notes, pass a single reference document (for example `docs/RECREATE_PROJECT.md`) and the generator will produce a lesson inspired by it.
- `--output PATH` (optional) — write output to a file instead of printing to stdout.
- `--model MODEL` (optional) — prefer a remote LLM when `OPENAI_API_KEY` is present.

Examples

```bash
# Generate from separate template + notes
python -m tools.lesson_generator --template template.md --notes notes.md --output lesson.md

# Generate from the project's recreate doc
python -m tools.lesson_generator --reference docs/RECREATE_PROJECT.md --output lesson_from_recreate.md
```

The generator will attempt to use LangChain/OpenAI if `OPENAI_API_KEY` is set and the packages are installed. Otherwise it falls back to a deterministic local generator that produces a structured markdown lesson.
