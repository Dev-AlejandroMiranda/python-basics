# Tests for Python Basics

This directory contains unit tests for all modules in the `exercises/` folder. The tests are written using pytest and cover the main functions and concepts from each module.

## 📁 Test Structure

```
tests/
├── test_loops.py       # Tests for loops module
├── test_tuples.py      # Tests for tuples and sets module
├── test_functions.py   # Tests for functions module (to be added)
├── test_lists.py       # Tests for lists module (to be added)
└── README.md          # This file
```

## 🚀 Getting Started

### 1. Install Dependencies

First, install pytest and related testing tools:

```bash
# From the python-basics root directory
pip install -r requirements.txt
```

Or install pytest directly:

```bash
pip install pytest pytest-cov
```

### 2. Running Tests

#### Run all tests
```bash
# From the python-basics root directory
pytest

# Or with more verbose output
pytest -v
```

#### Run tests for a specific module
```bash
# Test only loops module
pytest tests/test_loops.py

# Test only tuples module
pytest tests/test_tuples.py
```

#### Run a specific test class
```bash
pytest tests/test_loops.py::TestFactorial
```

#### Run a specific test function
```bash
pytest tests/test_loops.py::TestFactorial::test_factorial_basic
```

### 3. Test Coverage

Check how much of your code is covered by tests:

```bash
# Generate coverage report
pytest --cov=exercises --cov-report=html

# View the report
# Open htmlcov/index.html in your browser
```

Simple coverage report in terminal:
```bash
pytest --cov=exercises --cov-report=term-missing
```

## 📊 Understanding Test Output

### Successful Test Run
```
tests/test_loops.py::TestSumNumbers::test_sum_positive_numbers PASSED  [ 10%]
tests/test_loops.py::TestSumNumbers::test_sum_one PASSED               [ 20%]
```

### Failed Test
```
tests/test_loops.py::TestFactorial::test_factorial_basic FAILED        [ 30%]

================================ FAILURES =================================
___________________ TestFactorial.test_factorial_basic ____________________

    def test_factorial_basic(self):
        assert factorial(5) == 120  # Expected 120 but got different value
E       AssertionError: assert 119 == 120
```

## 🧪 Test Organization

Each test file is organized into classes by functionality:

### test_loops.py
- `TestSumNumbers` - Tests for sum_numbers function
- `TestFactorial` - Tests for factorial function
- `TestFindPrimeNumbers` - Tests for prime number finding
- `TestLoopConcepts` - Integration tests for loop concepts

### test_tuples.py
- `TestTupleBasics` - Basic tuple operations
- `TestTupleUnpacking` - Tuple unpacking tests
- `TestSetBasics` - Basic set operations
- `TestSetMathOperations` - Set mathematical operations
- `TestPracticalApplications` - Real-world use cases
- `TestEdgeCases` - Edge cases and special scenarios

## 💡 Writing Your Own Tests

Here's a simple template for adding new tests:

```python
import pytest
from exercises.your_module import your_function

class TestYourFunction:
    """Tests for your_function."""
    
    def test_basic_case(self):
        """Test basic functionality."""
        result = your_function(5)
        assert result == expected_value
    
    def test_edge_case(self):
        """Test edge case."""
        result = your_function(0)
        assert result == expected_value
    
    def test_error_handling(self):
        """Test that errors are raised properly."""
        with pytest.raises(ValueError):
            your_function(-1)
```

## 🎯 Test Best Practices

1. **One assertion per test** (when possible)
   - Makes it clear what failed
   - Easier to debug

2. **Descriptive test names**
   ```python
   # Good
   def test_factorial_of_zero_returns_one(self):
   
   # Less clear
   def test_factorial(self):
   ```

3. **Test both positive and negative cases**
   ```python
   def test_valid_input(self):
       assert function(5) == expected
   
   def test_invalid_input(self):
       with pytest.raises(ValueError):
           function(-1)
   ```

4. **Use fixtures for repeated setup**
   ```python
   @pytest.fixture
   def sample_data():
       return [1, 2, 3, 4, 5]
   
   def test_with_fixture(sample_data):
       assert sum(sample_data) == 15
   ```

## 🐛 Common Testing Scenarios

### Testing for Exceptions
```python
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0
```

### Testing with Multiple Cases (Parametrize)
```python
@pytest.mark.parametrize("input,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (10, 3628800)
])
def test_factorial_multiple_cases(input, expected):
    assert factorial(input) == expected
```

### Testing Approximate Values (Float Comparison)
```python
def test_float_comparison():
    result = 0.1 + 0.2
    assert result == pytest.approx(0.3)
```

## 📈 CI/CD Integration

These tests can be integrated into CI/CD pipelines:

### GitHub Actions Example
```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt
      - run: pytest --cov=exercises
```

## 🎓 Learning Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Real Python - Testing Guide](https://realpython.com/pytest-python-testing/)
- [Python Testing with pytest (Book)](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)

## 🤝 Contributing Tests

When adding new modules to `exercises/`, please also add corresponding tests:

1. Create `test_<module_name>.py` in the `tests/` directory
2. Write comprehensive tests covering main functionality
3. Include edge cases and error handling tests
4. Run `pytest` to ensure all tests pass
5. Check coverage with `pytest --cov`

## ✅ Checklist for Good Tests

- [ ] Tests are independent (can run in any order)
- [ ] Tests are repeatable (same result every time)
- [ ] Tests are fast (run quickly)
- [ ] Tests have clear, descriptive names
- [ ] Tests cover happy path and edge cases
- [ ] Tests check error handling
- [ ] Code coverage is above 80%

---

**Happy Testing! 🧪**
