from tools.lesson_generator import generate_lesson


def test_local_generate_simple():
    template = "Introduction to X\n\nThis is a short template."
    notes = "- Define X\n- Show example\n- Add exercise"
    out = generate_lesson(template, notes)
    assert "# Introduction to X" in out
    assert "Learning Objectives" in out
    assert "Suggested Activities" in out
    assert "Short Assessment" in out
