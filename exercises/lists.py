"""
lists.py

This module demonstrates Python lists:
- Creating lists
- Accessing elements (indexing)
- List slicing
- List methods (append, insert, remove, etc.)
- List operations
- List comprehensions
- Nested lists
"""

print("=== Creating Lists ===")

# Empty list
empty_list: list = []
print(f"Empty list: {empty_list}")

# List with initial values
fruits: list[str] = ["apple", "banana", "cherry", "date"]
numbers: list[int] = [1, 2, 3, 4, 5]
mixed: list = ["text", 42, 3.14, True]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")

# List length
print(f"\nLength of fruits: {len(fruits)}")

print("\n=== Accessing Elements (Indexing) ===")

# Positive indexing (starts at 0)
print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")
print(f"Last fruit: {fruits[3]}")

# Negative indexing (starts from end)
print(f"Last fruit (negative): {fruits[-1]}")
print(f"Second to last: {fruits[-2]}")

print("\n=== List Slicing ===")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Slicing syntax: list[start:end:step]
print(f"numbers[2:5]: {numbers[2:5]}")        # Elements from index 2 to 4
print(f"numbers[:4]: {numbers[:4]}")          # First 4 elements
print(f"numbers[5:]: {numbers[5:]}")          # From index 5 to end
print(f"numbers[::2]: {numbers[::2]}")        # Every second element
print(f"numbers[::-1]: {numbers[::-1]}")      # Reverse the list
print(f"numbers[1:8:2]: {numbers[1:8:2]}")    # From 1 to 7, step 2

print("\n=== Modifying Lists ===")

fruits = ["apple", "banana", "cherry"]
print(f"Original: {fruits}")

# Change an element
fruits[1] = "blueberry"
print(f"After changing index 1: {fruits}")

# Append (add to end)
fruits.append("date")
print(f"After append: {fruits}")

# Insert at specific position
fruits.insert(1, "avocado")
print(f"After insert at index 1: {fruits}")

print("\n=== Removing Elements ===")

fruits = ["apple", "banana", "cherry", "date", "banana"]
print(f"Original: {fruits}")

# Remove by value (removes first occurrence)
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# Pop (remove by index and return value)
popped = fruits.pop(2)
print(f"Popped element: {popped}")
print(f"After pop(2): {fruits}")

# Pop last element
last = fruits.pop()
print(f"Popped last: {last}")
print(f"After pop(): {fruits}")

# Clear all elements
fruits_copy = fruits.copy()
fruits_copy.clear()
print(f"After clear(): {fruits_copy}")

print("\n=== List Methods ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

# Sort (modifies original list)
numbers.sort()
print(f"After sort(): {numbers}")

# Reverse
numbers.reverse()
print(f"After reverse(): {numbers}")

# Count occurrences
fruits = ["apple", "banana", "apple", "cherry", "apple"]
apple_count = fruits.count("apple")
print(f"\nFruits: {fruits}")
print(f"Count of 'apple': {apple_count}")

# Find index
banana_index = fruits.index("banana")
print(f"Index of 'banana': {banana_index}")

print("\n=== List Operations ===")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"list1 + list2: {combined}")

# Repetition
repeated = list1 * 3
print(f"list1 * 3: {repeated}")

# Membership
print(f"2 in list1: {2 in list1}")
print(f"10 in list1: {10 in list1}")

print("\n=== List Comprehensions ===")

# Basic list comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Transform strings
fruits = ["apple", "banana", "cherry"]
uppercase = [fruit.upper() for fruit in fruits]
print(f"Uppercase fruits: {uppercase}")

print("\n=== Nested Lists ===")

# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Accessing nested elements
print(f"\nElement at [0][0]: {matrix[0][0]}")
print(f"Element at [1][2]: {matrix[1][2]}")
print(f"Element at [2][1]: {matrix[2][1]}")

print("\n=== Copying Lists ===")

original = [1, 2, 3]

# Shallow copy methods
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

original.append(4)

print(f"Original (modified): {original}")
print(f"Copy 1: {copy1}")
print(f"Copy 2: {copy2}")
print(f"Copy 3: {copy3}")

print("\n=== Common List Functions ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(f"Numbers: {numbers}")
print(f"min(): {min(numbers)}")
print(f"max(): {max(numbers)}")
print(f"sum(): {sum(numbers)}")
print(f"sorted() [doesn't modify]: {sorted(numbers)}")
print(f"Original still: {numbers}")

print("\n=== Interactive Example ===")

# Build a shopping list
shopping_list: list[str] = []

print("Create your shopping list (type 'done' to finish):")
while True:
    item = input("Add item: ").strip()
    if item.lower() == "done":
        break
    if item:
        shopping_list.append(item)
        print(f"Added '{item}' to list")

print(f"\nYour shopping list ({len(shopping_list)} items):")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")

print("\n=== Program Complete ===")