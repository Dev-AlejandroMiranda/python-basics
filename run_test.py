"""
Test Runner Script
==================
A convenient script to run all tests with various options.
"""

import sys
import subprocess
from pathlib import Path


def print_header(text: str) -> None:
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def run_command(command: list) -> int:
    """Run a command and return the exit code."""
    try:
        result = subprocess.run(command, check=False)
        return result.returncode
    except FileNotFoundError:
        print("  Error: pytest not found. Please install it:")
        print("   pip install pytest pytest-cov")
        return 1


def check_pytest_installed() -> bool:
    """Check if pytest is installed."""
    try:
        subprocess.run(["pytest", "--version"], 
                      capture_output=True, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


def main():
    """Main test runner function."""
    print_header(" Python Basics - Test Runner")
    
    # Check if pytest is installed
    if not check_pytest_installed():
        print("  pytest is not installed!")
        print("\nTo install pytest, run:")
        print("   pip install pytest pytest-cov")
        print("\nOr install all requirements:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    print(" pytest is installed\n")
    
    # Show menu
    print("Choose an option:")
    print("  1. Run all tests")
    print("  2. Run all tests with coverage")
    print("  3. Run tests for loops module")
    print("  4. Run tests for tuples module")
    print("  5. Run all tests (verbose)")
    print("  6. Generate HTML coverage report")
    print("  0. Exit")
    
    choice = input("\nEnter your choice (0-6): ").strip()
    
    commands = {
        "1": ["pytest"],
        "2": ["pytest", "--cov=exercises", "--cov-report=term-missing"],
        "3": ["pytest", "tests/test_loops.py", "-v"],
        "4": ["pytest", "tests/test_tuples.py", "-v"],
        "5": ["pytest", "-v"],
        "6": ["pytest", "--cov=exercises", "--cov-report=html"],
    }
    
    if choice == "0":
        print("\n Goodbye!")
        sys.exit(0)
    
    if choice not in commands:
        print("\n Invalid choice!")
        sys.exit(1)
    
    print_header(f"Running Option {choice}")
    exit_code = run_command(commands[choice])
    
    if choice == "6" and exit_code == 0:
        print("\n" + "=" * 60)
        print(" HTML coverage report generated!")
        print(" Open htmlcov/index.html in your browser to view it")
        print("=" * 60)
    
    if exit_code == 0:
        print("\n" + "=" * 60)
        print(" All tests passed!")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("  Some tests failed. Check the output above.")
        print("=" * 60)
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()