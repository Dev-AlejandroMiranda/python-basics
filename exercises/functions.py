"""
variables.py

This module demonstrates basic Python concepts:
- Variables
- Data types
- Type hints
- User input
- Type casting
"""

# Basic variables with type hints
name: str = "Alejandro"
age: int = 20
height: float = 1.75
is_student: bool = True

print("=== Basic Variables ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Student: {is_student}")

print("\n=== Variable Types ===")
print(f"type(name): {type(name)}")
print(f"type(age): {type(age)}")
print(f"type(height): {type(height)}")
print(f"type(is_student): {type(is_student)}")

# User input (input always returns a string)
print("\n=== User Input ===")
user_name: str = input("Enter your name: ")

user_age_str: str = input("Enter your age: ")
user_age: int = int(user_age_str)  # type casting

print(f"Hello {user_name}, next year you will be {user_age + 1} years old.")

# Simple calculation
print("\n=== Simple Calculation ===")
birth_year: int = 2025 - user_age
print(f"You were born in approximately {birth_year}.")
