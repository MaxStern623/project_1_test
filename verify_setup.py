#!/usr/bin/env python3
"""
Verification script for the updated defensive programming calculator project.
This script checks that all configurations are properly updated and working.
"""

import os
import sys
import subprocess
from pathlib import Path


def check_file_exists(filepath: str, description: str) -> bool:
    """Check if a file exists and report status."""
    if Path(filepath).exists():
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT FOUND")
        return False


def check_directory_structure():
    """Verify the project directory structure is correct."""
    print("🔍 Checking Project Structure...")

    required_paths = [
        ("answers/src/__init__.py", "Answers source package"),
        ("answers/src/main.py", "Answers CLI module"),
        ("answers/src/exceptions.py", "Answers exceptions module"),
        ("answers/src/operations/__init__.py", "Answers operations module"),
        ("answers/tests/test_operations.py", "Answers operations tests"),
        ("answers/tests/test_cli.py", "Answers CLI tests"),
        ("answers/tests/test_exceptions.py", "Answers exceptions tests"),
        ("practice/src/__init__.py", "Practice source package"),
        ("practice/src/main.py", "Practice CLI module"),
        ("practice/src/exceptions.py", "Practice exceptions module"),
        ("practice/src/operations/__init__.py", "Practice operations module"),
        ("practice/tests/test_operations.py", "Practice operations tests"),
        ("practice/tests/test_cli.py", "Practice CLI tests"),
        ("practice/tests/test_exceptions.py", "Practice exceptions tests"),
        ("demo_differences.py", "Demo script"),
        ("DEFENSIVE_PROGRAMMING_README.md", "Detailed guide"),
        ("A1_IMPLEMENTATION_SUMMARY.md", "Project summary"),
    ]

    all_good = True
    for filepath, description in required_paths:
        if not check_file_exists(filepath, description):
            all_good = False

    return all_good


def check_old_directories_removed():
    """Check that old src/ and tests/ directories are removed."""
    print("\n🔍 Checking Old Directories Removed...")

    old_paths = ["src/", "tests/"]
    all_good = True

    for old_path in old_paths:
        if Path(old_path).exists():
            print(f"❌ Old directory still exists: {old_path}")
            all_good = False
        else:
            print(f"✅ Old directory properly removed: {old_path}")

    return all_good


def test_functionality():
    """Test that both implementations work."""
    print("\n🧪 Testing Functionality...")

    tests = [
        (["python3", "-m", "answers.src.main", "add", "2", "3"], "Answers version basic operation"),
        (["python3", "-m", "practice.src.main", "add", "2", "3"], "Practice version basic operation"),
    ]

    all_good = True
    for cmd, description in tests:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✅ {description}: SUCCESS")
            else:
                print(f"❌ {description}: FAILED (exit code {result.returncode})")
                if result.stderr:
                    print(f"   Error: {result.stderr.strip()}")
                all_good = False
        except Exception as e:
            print(f"❌ {description}: ERROR - {e}")
            all_good = False

    return all_good


def check_configurations():
    """Check that configuration files are updated."""
    print("\n⚙️ Checking Configuration Files...")

    # Check pytest.ini
    pytest_config = Path("pytest.ini").read_text()
    if "answers/tests practice/tests" in pytest_config:
        print("✅ pytest.ini: Updated test paths")
    else:
        print("❌ pytest.ini: Test paths not updated")
        return False

    # Check pyproject.toml
    pyproject_config = Path("pyproject.toml").read_text()
    if "defensive-programming-calculator" in pyproject_config:
        print("✅ pyproject.toml: Updated project name")
    else:
        print("❌ pyproject.toml: Project name not updated")
        return False

    # Check .gitignore
    gitignore_config = Path(".gitignore").read_text()
    if "/src/" in gitignore_config and "/tests/" in gitignore_config:
        print("✅ .gitignore: Updated with old directory ignores")
    else:
        print("❌ .gitignore: Not updated with old directory ignores")
        return False

    return True


def main():
    """Run all verification checks."""
    print("🛡️ Defensive Programming Calculator - Configuration Verification")
    print("=" * 70)

    checks = [
        ("Project Structure", check_directory_structure),
        ("Old Directories Cleanup", check_old_directories_removed),
        ("Configuration Files", check_configurations),
        ("Functionality", test_functionality),
    ]

    all_passed = True
    for check_name, check_func in checks:
        try:
            if not check_func():
                all_passed = False
        except Exception as e:
            print(f"❌ {check_name}: ERROR - {e}")
            all_passed = False

    print("\n" + "=" * 70)
    if all_passed:
        print("🎉 All checks PASSED! Project is properly configured.")
        print("\n📚 Next steps:")
        print("   1. Read DEFENSIVE_PROGRAMMING_README.md for detailed guide")
        print("   2. Try: python3 demo_differences.py")
        print("   3. Start learning with practice/ implementation")
        return 0
    else:
        print("⚠️  Some checks FAILED. Please review the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
