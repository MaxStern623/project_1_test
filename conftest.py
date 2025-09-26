"""
Pytest configuration for the defensive programming calculator project.

This file ensures that the answers and practice packages can be imported
in the test environment by adding the project root to the Python path.
"""
import sys
from pathlib import Path

# Add the project root to Python path so imports work
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))