"""
control_flow.py

This module demonstrates control flow structures in Python:
- if/elif/else statements
- Comparison operators
- Logical operators
- Nested conditions
- Conditional expressions (ternary operator)
"""

print("=== IF/ELIF/ELSE Statements ===")

# Basic if statement
age: int = 20

if age >= 18:
    print(f"Age {age}: You are an adult.")
else:
    print(f"Age {age}: You are a minor.")

# if/elif/else chain
print("\n=== Grade Classification ===")
score: int = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")

# Comparison operators
print("\n=== Comparison Operators ===")
x: int = 10
y: int = 20

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # Equal
print(f"x != y: {x != y}")  # Not equal
print(f"x > y: {x > y}")    # Greater than
print(f"x < y: {x < y}")    # Less than
print(f"x >= y: {x >= y}")  # Greater or equal
print(f"x <= y: {x <= y}")  # Less or equal

# Logical operators
print("\n=== Logical Operators ===")
is_student: bool = True
has_id: bool = True
age: int = 22

print(f"is_student: {is_student}, has_id: {has_id}, age: {age}")
print(f"is_student AND has_id: {is_student and has_id}")
print(f"is_student OR has_id: {is_student or has_id}")
print(f"NOT is_student: {not is_student}")
print(f"is_student AND age >= 18: {is_student and age >= 18}")

# Nested conditions
print("\n=== Nested Conditions ===")
temperature: int = 25
is_raining: bool = False

if temperature > 30:
    print("It's hot outside!")
    if is_raining:
        print("But it's raining, take an umbrella.")
    else:
        print("Great day for the beach!")
elif temperature > 20:
    print("The weather is pleasant.")
    if is_raining:
        print("Light rain, take a jacket.")
else:
    print("It's cold outside!")

# Conditional expression (ternary operator)
print("\n=== Conditional Expression ===")
age: int = 17
status: str = "adult" if age >= 18 else "minor"
print(f"Age {age}: You are a {status}")

# Interactive example
print("\n=== Interactive: Number Checker ===")
try:
    number: int = int(input("Enter a number: "))
    
    # Check multiple conditions
    if number > 0:
        print(f"{number} is positive")
    elif number < 0:
        print(f"{number} is negative")
    else:
        print(f"{number} is zero")
    
    # Check even or odd
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    
    # Check range
    if 1 <= number <= 10:
        print(f"{number} is between 1 and 10")
    elif 11 <= number <= 100:
        print(f"{number} is between 11 and 100")
    else:
        print(f"{number} is outside the range 1-100")
        
except ValueError:
    print("Error: Please enter a valid integer.")

print("\n=== Program Complete ===")