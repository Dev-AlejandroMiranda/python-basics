"""
functions.py

This module demonstrates Python functions:
- Function definition and calling
- Parameters and arguments
- Return values
- Default parameters
- Keyword arguments
- *args and **kwargs
- Lambda functions
- Docstrings
"""

print("=== Basic Function Definition ===")

# Simple function without parameters
def greet():
    """Print a greeting message."""
    print("Hello, World!")

greet()

# Function with parameters
def greet_person(name: str):
    """Greet a person by name."""
    print(f"Hello, {name}!")

greet_person("Alejandro")
greet_person("Maria")

print("\n=== Functions with Return Values ===")

# Function that returns a value
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Function with multiple operations
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    area = length * width
    return area

rectangle_area = calculate_area(5.0, 3.0)
print(f"Area of rectangle (5.0 x 3.0): {rectangle_area}")

print("\n=== Functions with Multiple Return Values ===")

def get_min_max(numbers: list[int]) -> tuple[int, int]:
    """Return the minimum and maximum values from a list."""
    return min(numbers), max(numbers)

nums = [3, 7, 1, 9, 4]
minimum, maximum = get_min_max(nums)
print(f"Numbers: {nums}")
print(f"Min: {minimum}, Max: {maximum}")

print("\n=== Default Parameters ===")

def power(base: int, exponent: int = 2) -> int:
    """
    Calculate base raised to exponent.
    Default exponent is 2 (square).
    """
    return base ** exponent

print(f"power(3): {power(3)}")           # Uses default exponent (2)
print(f"power(3, 3): {power(3, 3)}")     # Uses provided exponent (3)
print(f"power(2, 4): {power(2, 4)}")     # 2^4 = 16

def greet_with_time(name: str, time: str = "day") -> str:
    """Greet someone with time of day."""
    return f"Good {time}, {name}!"

print(greet_with_time("Alejandro"))
print(greet_with_time("Alejandro", "morning"))
print(greet_with_time("Alejandro", "evening"))

print("\n=== Keyword Arguments ===")

def create_profile(name: str, age: int, city: str, country: str) -> str:
    """Create a user profile string."""
    return f"{name}, {age} years old, from {city}, {country}"

# Positional arguments
profile1 = create_profile("Ana", 25, "Bogotá", "Colombia")
print(profile1)

# Keyword arguments (order doesn't matter)
profile2 = create_profile(country="Mexico", name="Carlos", age=30, city="CDMX")
print(profile2)

# Mix of positional and keyword
profile3 = create_profile("Luis", 28, city="Madrid", country="Spain")
print(profile3)

print("\n=== Variable Number of Arguments (*args) ===")

def sum_all(*numbers: int) -> int:
    """Sum any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40): {sum_all(10, 20, 30, 40)}")
print(f"sum_all(5): {sum_all(5)}")

def print_items(*items):
    """Print all items passed to the function."""
    print("Items:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")

print_items("apple", "banana", "cherry")

print("\n=== Variable Keyword Arguments (**kwargs) ===")

def print_info(**info):
    """Print key-value pairs of information."""
    print("Information:")
    for key, value in info.items():
        print(f"  {key}: {value}")

print_info(name="Alejandro", age=20, city="Medellín")
print()
print_info(language="Python", version="3.12", type="Programming")

print("\n=== Lambda Functions ===")

# Lambda function (anonymous function)
square = lambda x: x ** 2
print(f"square(5): {square(5)}")

# Lambda with multiple parameters
multiply = lambda x, y: x * y
print(f"multiply(4, 5): {multiply(4, 5)}")

# Lambda in sorted()
students = [
    {"name": "Ana", "grade": 85},
    {"name": "Carlos", "grade": 92},
    {"name": "Diana", "grade": 78}
]

sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
print("\nStudents sorted by grade:")
for student in sorted_students:
    print(f"  {student['name']}: {student['grade']}")

print("\n=== Practical Examples ===")

def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0

def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# Test practical functions
print(f"is_even(4): {is_even(4)}")
print(f"is_even(7): {is_even(7)}")
print(f"is_palindrome('radar'): {is_palindrome('radar')}")
print(f"is_palindrome('hello'): {is_palindrome('hello')}")
print(f"factorial(5): {factorial(5)}")
print(f"25°C to Fahrenheit: {celsius_to_fahrenheit(25)}°F")

print("\n=== Nested Functions ===")

def outer_function(text: str):
    """Demonstrate nested functions."""
    
    def inner_function():
        """Inner function that uses outer scope variable."""
        print(f"Inner function says: {text}")
    
    print(f"Outer function says: {text}")
    inner_function()

outer_function("Hello from nested functions!")

print("\n=== Interactive Calculator ===")

def calculator():
    """Simple interactive calculator."""
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                return
        else:
            print("Error: Invalid operation!")
            return
        
        print(f"Result: {num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

calculator()

print("\n=== Program Complete ===")