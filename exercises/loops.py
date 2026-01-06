"""
Python Basics: Loops
====================
This module demonstrates loops in Python, including for loops, while loops,
loop control statements, and practical applications.

Topics covered:
- For loops with range()
- Iterating over sequences
- While loops
- Loop control (break, continue, pass)
- Nested loops
- Loop with else clause
- Practical examples
"""


def demonstrate_for_loops() -> None:
    """Demonstrate basic for loop concepts."""
    print("=" * 50)
    print("FOR LOOPS")
    print("=" * 50)
    
    # Basic for loop with range
    print("\n1. Basic for loop (0 to 4):")
    for i in range(5):
        print(f"  Iteration {i}")
    
    # For loop with start and end
    print("\n2. For loop with range(start, end):")
    for i in range(1, 6):
        print(f"  Number: {i}")
    
    # For loop with step
    print("\n3. For loop with step (counting by 2s):")
    for i in range(0, 10, 2):
        print(f"  Even number: {i}")
    
    # Counting backwards
    print("\n4. Counting backwards:")
    for i in range(5, 0, -1):
        print(f"  Countdown: {i}")
    print("  Blast off! 🚀")
    
    # Iterating over a string
    print("\n5. Iterating over a string:")
    word = "Python"
    for letter in word:
        print(f"  Letter: {letter}")
    
    # Iterating over a list
    print("\n6. Iterating over a list:")
    fruits = ["apple", "banana", "cherry", "date"]
    for fruit in fruits:
        print(f"  Fruit: {fruit}")
    
    # Using enumerate for index and value
    print("\n7. Using enumerate (index + value):")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    # Starting enumerate from 1
    print("\n8. Enumerate starting from 1:")
    for index, fruit in enumerate(fruits, start=1):
        print(f"  #{index}: {fruit}")


def demonstrate_while_loops() -> None:
    """Demonstrate while loop concepts."""
    print("\n" + "=" * 50)
    print("WHILE LOOPS")
    print("=" * 50)
    
    # Basic while loop
    print("\n1. Basic while loop:")
    count = 0
    while count < 5:
        print(f"  Count is: {count}")
        count += 1
    
    # While loop with condition
    print("\n2. While loop with user input simulation:")
    number = 1
    print("  Doubling numbers until we reach 100:")
    while number < 100:
        print(f"    {number}")
        number *= 2
    
    # Infinite loop with break (controlled)
    print("\n3. While True with break:")
    counter = 0
    while True:
        print(f"  Iteration {counter}")
        counter += 1
        if counter >= 3:
            print("  Breaking out of loop!")
            break


def demonstrate_loop_control() -> None:
    """Demonstrate break, continue, and pass statements."""
    print("\n" + "=" * 50)
    print("LOOP CONTROL STATEMENTS")
    print("=" * 50)
    
    # Break statement
    print("\n1. BREAK - Exit loop early:")
    print("  Finding first number divisible by 7:")
    for num in range(1, 20):
        if num % 7 == 0:
            print(f"  Found it! {num} is divisible by 7")
            break
        print(f"  Checking {num}...")
    
    # Continue statement
    print("\n2. CONTINUE - Skip to next iteration:")
    print("  Printing only odd numbers:")
    for num in range(10):
        if num % 2 == 0:  # If even
            continue  # Skip to next iteration
        print(f"  {num} is odd")
    
    # Pass statement
    print("\n3. PASS - Placeholder (does nothing):")
    for num in range(5):
        if num == 2:
            pass  # TODO: Add special handling for 2 later
        print(f"  Processing number: {num}")


def demonstrate_nested_loops() -> None:
    """Demonstrate nested loops."""
    print("\n" + "=" * 50)
    print("NESTED LOOPS")
    print("=" * 50)
    
    # Simple nested loop
    print("\n1. Multiplication table (3x3):")
    for i in range(1, 4):
        for j in range(1, 4):
            result = i * j
            print(f"  {i} x {j} = {result}")
        print()  # Empty line between rows
    
    # Pattern with nested loops
    print("2. Triangle pattern:")
    for i in range(1, 6):
        print("  " + "* " * i)
    
    # Nested loop with lists
    print("\n3. 2D grid coordinates:")
    for x in range(3):
        for y in range(3):
            print(f"  ({x}, {y})", end="  ")
        print()  # New line after each row


def demonstrate_loop_else() -> None:
    """Demonstrate loop with else clause."""
    print("\n" + "=" * 50)
    print("LOOP WITH ELSE CLAUSE")
    print("=" * 50)
    
    print("\n1. For-else (no break):")
    for num in range(3):
        print(f"  Number: {num}")
    else:
        print("  Loop completed normally!")
    
    print("\n2. For-else with break:")
    for num in range(10):
        print(f"  Checking {num}")
        if num == 3:
            print("  Found 3! Breaking...")
            break
    else:
        print("  This won't print because we broke out")
    
    print("\n3. While-else example:")
    count = 0
    while count < 3:
        print(f"  Count: {count}")
        count += 1
    else:
        print("  While loop finished!")


def sum_numbers(n: int) -> int:
    """Calculate sum of numbers from 1 to n using a loop."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(n: int) -> int:
    """Calculate factorial using a loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_prime_numbers(limit: int) -> list[int]:
    """Find all prime numbers up to a given limit."""
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def demonstrate_practical_examples() -> None:
    """Demonstrate practical loop applications."""
    print("\n" + "=" * 50)
    print("PRACTICAL EXAMPLES")
    print("=" * 50)
    
    # Sum of numbers
    print("\n1. Sum of numbers from 1 to 10:")
    result = sum_numbers(10)
    print(f"  Result: {result}")
    
    # Factorial
    print("\n2. Factorial of 5:")
    result = factorial(5)
    print(f"  5! = {result}")
    
    # Prime numbers
    print("\n3. Prime numbers up to 20:")
    primes = find_prime_numbers(20)
    print(f"  Primes: {primes}")
    
    # Finding maximum in a list
    print("\n4. Finding maximum in a list:")
    numbers = [23, 45, 12, 67, 34, 89, 11]
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print(f"  Numbers: {numbers}")
    print(f"  Maximum: {max_num}")
    
    # Counting occurrences
    print("\n5. Counting vowels in a string:")
    text = "Hello World"
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(f"  Text: '{text}'")
    print(f"  Vowel count: {count}")


def interactive_example() -> None:
    """Interactive loop example with user input."""
    print("\n" + "=" * 50)
    print("INTERACTIVE EXAMPLE: NUMBER GUESSING")
    print("=" * 50)
    
    print("\nLet's play a simple game!")
    print("I'm thinking of a number between 1 and 10.")
    
    secret_number = 7  # In a real game, use random.randint(1, 10)
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
                break
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid inputs
    else:
        print(f"\n😔 Game over! The number was {secret_number}.")


def main() -> None:
    """Run all loop demonstrations."""
    print("\n" + "🐍" * 25)
    print("WELCOME TO PYTHON LOOPS TUTORIAL")
    print("🐍" * 25)
    
    demonstrate_for_loops()
    demonstrate_while_loops()
    demonstrate_loop_control()
    demonstrate_nested_loops()
    demonstrate_loop_else()
    demonstrate_practical_examples()
    
    # Ask user if they want to play the interactive game
    print("\n" + "=" * 50)
    play_game = input("\nWould you like to play the number guessing game? (y/n): ")
    if play_game.lower() == 'y':
        interactive_example()
    
    print("\n" + "=" * 50)
    print("✅ Tutorial completed!")
    print("💡 Practice these concepts to master loops in Python!")
    print("=" * 50)


if __name__ == "__main__":
    main()