"""
Unit tests for tuples.py module
================================
Tests tuple and set operations from the tuples module.
"""

import pytest


class TestTupleBasics:
    """Tests for basic tuple operations."""
    
    def test_tuple_creation(self):
        """Test creating tuples."""
        empty = ()
        single = (42,)
        multiple = (1, 2, 3)
        
        assert len(empty) == 0
        assert len(single) == 1
        assert len(multiple) == 3
    
    def test_tuple_immutability(self):
        """Test that tuples are immutable."""
        t = (1, 2, 3)
        with pytest.raises(TypeError):
            t[0] = 99  # Should raise TypeError
    
    def test_tuple_indexing(self):
        """Test accessing tuple elements."""
        fruits = ("apple", "banana", "cherry")
        assert fruits[0] == "apple"
        assert fruits[-1] == "cherry"
        assert fruits[1:3] == ("banana", "cherry")
    
    def test_tuple_concatenation(self):
        """Test tuple concatenation."""
        t1 = (1, 2)
        t2 = (3, 4)
        result = t1 + t2
        assert result == (1, 2, 3, 4)
    
    def test_tuple_repetition(self):
        """Test tuple repetition."""
        t = ("a",) * 3
        assert t == ("a", "a", "a")
    
    def test_tuple_methods(self):
        """Test tuple methods: count and index."""
        numbers = (1, 2, 3, 2, 4, 2, 5)
        assert numbers.count(2) == 3
        assert numbers.index(3) == 2


class TestTupleUnpacking:
    """Tests for tuple unpacking."""
    
    def test_basic_unpacking(self):
        """Test basic tuple unpacking."""
        coords = (10, 20)
        x, y = coords
        assert x == 10
        assert y == 20
    
    def test_multiple_unpacking(self):
        """Test unpacking multiple values."""
        person = ("Alice", 25, "Engineer")
        name, age, job = person
        assert name == "Alice"
        assert age == 25
        assert job == "Engineer"
    
    def test_swap_variables(self):
        """Test swapping variables with tuple unpacking."""
        a, b = 5, 10
        a, b = b, a
        assert a == 10
        assert b == 5
    
    def test_extended_unpacking(self):
        """Test extended unpacking with *."""
        numbers = (1, 2, 3, 4, 5)
        first, *middle, last = numbers
        assert first == 1
        assert middle == [2, 3, 4]
        assert last == 5


class TestSetBasics:
    """Tests for basic set operations."""
    
    def test_set_creation(self):
        """Test creating sets."""
        empty = set()
        numbers = {1, 2, 3, 4, 5}
        
        assert len(empty) == 0
        assert len(numbers) == 5
    
    def test_set_removes_duplicates(self):
        """Test that sets automatically remove duplicates."""
        s = {1, 2, 2, 3, 3, 3, 4}
        assert s == {1, 2, 3, 4}
        assert len(s) == 4
    
    def test_set_from_list(self):
        """Test creating set from list with duplicates."""
        lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        s = set(lst)
        assert s == {1, 2, 3, 4}
    
    def test_set_membership(self):
        """Test membership testing in sets."""
        s = {1, 2, 3, 4, 5}
        assert 3 in s
        assert 10 not in s
    
    def test_set_add_remove(self):
        """Test adding and removing elements."""
        s = {1, 2, 3}
        s.add(4)
        assert 4 in s
        
        s.remove(2)
        assert 2 not in s
        
        # discard doesn't raise error if element not found
        s.discard(99)  # Should not raise error
    
    def test_set_operations(self):
        """Test basic set operations."""
        s = {1, 2, 3}
        assert len(s) == 3
        
        s.clear()
        assert len(s) == 0


class TestSetMathOperations:
    """Tests for mathematical set operations."""
    
    def test_union(self):
        """Test set union."""
        a = {1, 2, 3}
        b = {3, 4, 5}
        result = a | b
        assert result == {1, 2, 3, 4, 5}
    
    def test_intersection(self):
        """Test set intersection."""
        a = {1, 2, 3, 4}
        b = {3, 4, 5, 6}
        result = a & b
        assert result == {3, 4}
    
    def test_difference(self):
        """Test set difference."""
        a = {1, 2, 3, 4}
        b = {3, 4, 5, 6}
        result = a - b
        assert result == {1, 2}
    
    def test_symmetric_difference(self):
        """Test symmetric difference."""
        a = {1, 2, 3, 4}
        b = {3, 4, 5, 6}
        result = a ^ b
        assert result == {1, 2, 5, 6}
    
    def test_subset_superset(self):
        """Test subset and superset operations."""
        a = {1, 2, 3}
        b = {1, 2, 3, 4, 5}
        
        assert a.issubset(b)
        assert b.issuperset(a)
        assert not b.issubset(a)
    
    def test_disjoint(self):
        """Test disjoint sets."""
        a = {1, 2, 3}
        b = {4, 5, 6}
        c = {3, 4, 5}
        
        assert a.isdisjoint(b)
        assert not a.isdisjoint(c)


class TestPracticalApplications:
    """Tests for practical applications."""
    
    def test_remove_duplicates(self):
        """Test removing duplicates from list."""
        items = ["apple", "banana", "apple", "cherry", "banana"]
        unique = list(set(items))
        assert len(unique) == 3
        assert set(unique) == {"apple", "banana", "cherry"}
    
    def test_find_common_elements(self):
        """Test finding common elements between lists."""
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        common = set(list1) & set(list2)
        assert common == {4, 5}
    
    def test_tuple_as_dictionary_key(self):
        """Test using tuples as dictionary keys."""
        locations = {
            (0, 0): "Origin",
            (1, 0): "East",
            (0, 1): "North"
        }
        assert locations[(0, 0)] == "Origin"
        assert locations[(1, 0)] == "East"
    
    def test_tuple_immutability_as_key(self):
        """Test that lists cannot be used as dict keys but tuples can."""
        d = {}
        
        # Tuple works as key
        d[(1, 2)] = "value"
        assert (1, 2) in d
        
        # List should raise TypeError
        with pytest.raises(TypeError):
            d[[1, 2]] = "value"


class TestEdgeCases:
    """Tests for edge cases and special scenarios."""
    
    def test_empty_tuple(self):
        """Test operations on empty tuple."""
        t = ()
        assert len(t) == 0
        assert t.count(1) == 0
    
    def test_empty_set(self):
        """Test operations on empty set."""
        s = set()
        assert len(s) == 0
        assert 1 not in s
    
    def test_single_element_tuple(self):
        """Test single element tuple (with comma)."""
        single = (42,)
        not_tuple = (42)
        
        assert isinstance(single, tuple)
        assert isinstance(not_tuple, int)
    
    def test_set_with_different_types(self):
        """Test set with different data types."""
        # Sets can contain different types
        mixed = {1, "hello", 3.14, True}
        assert len(mixed) >= 3  # True might equal 1 in set
    
    def test_frozen_set(self):
        """Test immutable frozenset."""
        fs = frozenset([1, 2, 3])
        
        # frozenset is immutable
        with pytest.raises(AttributeError):
            fs.add(4)
        
        # But can be used in operations
        fs2 = frozenset([3, 4, 5])
        result = fs | fs2
        assert result == frozenset([1, 2, 3, 4, 5])


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])