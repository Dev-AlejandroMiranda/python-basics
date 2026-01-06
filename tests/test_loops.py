"""
Unit tests for loops.py module
================================
Tests the functions and concepts from the loops module.
"""

import pytest
import sys
from pathlib import Path

# Add exercises folder to path
exercises_path = Path(__file__).parent.parent / "exercises"
sys.path.insert(0, str(exercises_path))

from loops import sum_numbers, factorial, find_prime_numbers


class TestSumNumbers:
    """Tests for sum_numbers function."""
    
    def test_sum_positive_numbers(self):
        """Test sum of positive numbers."""
        assert sum_numbers(5) == 15  # 1+2+3+4+5 = 15
        assert sum_numbers(10) == 55  # 1+2+...+10 = 55
    
    def test_sum_one(self):
        """Test sum of just 1."""
        assert sum_numbers(1) == 1
    
    def test_sum_zero(self):
        """Test sum with 0."""
        assert sum_numbers(0) == 0
    
    def test_sum_large_number(self):
        """Test sum with larger number."""
        assert sum_numbers(100) == 5050


class TestFactorial:
    """Tests for factorial function."""
    
    def test_factorial_basic(self):
        """Test basic factorial calculations."""
        assert factorial(5) == 120  # 5! = 5*4*3*2*1 = 120
        assert factorial(3) == 6    # 3! = 3*2*1 = 6
        assert factorial(4) == 24   # 4! = 4*3*2*1 = 24
    
    def test_factorial_zero(self):
        """Test factorial of 0 (should be 1)."""
        assert factorial(0) == 1
    
    def test_factorial_one(self):
        """Test factorial of 1."""
        assert factorial(1) == 1
    
    def test_factorial_large(self):
        """Test factorial of larger number."""
        assert factorial(10) == 3628800


class TestFindPrimeNumbers:
    """Tests for find_prime_numbers function."""
    
    def test_primes_up_to_10(self):
        """Test finding primes up to 10."""
        expected = [2, 3, 5, 7]
        assert find_prime_numbers(10) == expected
    
    def test_primes_up_to_20(self):
        """Test finding primes up to 20."""
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        assert find_prime_numbers(20) == expected
    
    def test_primes_up_to_2(self):
        """Test with limit 2 (only prime is 2)."""
        assert find_prime_numbers(2) == [2]
    
    def test_primes_up_to_1(self):
        """Test with limit 1 (no primes)."""
        assert find_prime_numbers(1) == []
    
    def test_no_primes(self):
        """Test with limit 0 (no primes)."""
        assert find_prime_numbers(0) == []
    
    def test_primes_count(self):
        """Test that correct number of primes are found."""
        primes = find_prime_numbers(100)
        assert len(primes) == 25  # There are 25 primes up to 100


class TestLoopConcepts:
    """Tests for loop concepts (integration tests)."""
    
    def test_sum_with_loop_vs_formula(self):
        """Verify loop sum matches mathematical formula."""
        n = 50
        loop_result = sum_numbers(n)
        formula_result = n * (n + 1) // 2
        assert loop_result == formula_result
    
    def test_factorial_recursive_vs_iterative(self):
        """Compare iterative factorial with expected results."""
        test_cases = [
            (0, 1),
            (1, 1),
            (5, 120),
            (7, 5040)
        ]
        for n, expected in test_cases:
            assert factorial(n) == expected
    
    def test_prime_properties(self):
        """Test that all returned numbers are actually prime."""
        primes = find_prime_numbers(30)
        
        for prime in primes:
            # A prime number has no divisors except 1 and itself
            divisors = [i for i in range(2, prime) if prime % i == 0]
            assert len(divisors) == 0, f"{prime} is not prime!"


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])