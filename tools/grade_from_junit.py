#!/usr/bin/env python3
"""Generate a simple grade summary from a pytest junit XML report.

Outputs a small JSON file with: total, passed, failed, skipped, percentage.
"""
import json
import sys
from xml.etree import ElementTree as ET


def parse_junit(path: str):
    tree = ET.parse(path)
    root = tree.getroot()
    # pytest produces a <testsuite> root with attributes
    total = int(root.attrib.get("tests", 0))
    failures = int(root.attrib.get("failures", 0))
    errors = int(root.attrib.get("errors", 0))
    skipped = int(root.attrib.get("skipped", 0))
    passed = total - failures - errors - skipped
    return {
        "total": total,
        "passed": passed,
        "failures": failures,
        "errors": errors,
        "skipped": skipped,
        "percentage": round((passed / total * 100) if total > 0 else 0, 2),
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: grade_from_junit.py <junit-xml>")
        sys.exit(2)
    report = parse_junit(sys.argv[1])
    out_path = "reports/grade_summary.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
    print("Wrote grading summary to", out_path)
