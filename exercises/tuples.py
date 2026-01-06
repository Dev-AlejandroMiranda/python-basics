"""
Python Basics: Tuples and Sets
===============================
This module demonstrates tuples and sets in Python, their characteristics,
operations, and practical applications.

Topics covered:
- Creating and using tuples
- Tuple immutability
- Tuple operations and methods
- Tuple unpacking
- Creating and using sets
- Set operations (union, intersection, difference)
- Set methods
- Practical applications
"""


def demonstrate_tuple_basics() -> None:
    """Demonstrate basic tuple concepts."""
    print("=" * 50)
    print("TUPLES - BASICS")
    print("=" * 50)
    
    # Creating tuples
    print("\n1. Creating tuples:")
    empty_tuple = ()
    single_tuple = (42,)  # Note the comma!
    numbers_tuple = (1, 2, 3, 4, 5)
    mixed_tuple = (1, "hello", 3.14, True)
    
    print(f"  Empty tuple: {empty_tuple}")
    print(f"  Single element: {single_tuple}")
    print(f"  Numbers: {numbers_tuple}")
    print(f"  Mixed types: {mixed_tuple}")
    
    # Tuple without parentheses (tuple packing)
    print("\n2. Tuple packing (no parentheses):")
    coordinates = 10, 20, 30
    print(f"  Coordinates: {coordinates}")
    print(f"  Type: {type(coordinates)}")
    
    # Accessing elements
    print("\n3. Accessing tuple elements:")
    fruits = ("apple", "banana", "cherry", "date")
    print(f"  Fruits tuple: {fruits}")
    print(f"  First fruit: {fruits[0]}")
    print(f"  Last fruit: {fruits[-1]}")
    print(f"  Middle fruits: {fruits[1:3]}")
    
    # Tuples are immutable
    print("\n4. Tuples are IMMUTABLE:")
    print("  ❌ Cannot modify: fruits[0] = 'apricot'")
    print("  ❌ Cannot append: fruits.append('elderberry')")
    print("  ✅ Can create new tuple: fruits + ('elderberry',)")
    new_fruits = fruits + ("elderberry",)
    print(f"  New tuple: {new_fruits}")


def demonstrate_tuple_operations() -> None:
    """Demonstrate tuple operations and methods."""
    print("\n" + "=" * 50)
    print("TUPLE OPERATIONS")
    print("=" * 50)
    
    numbers = (1, 2, 3, 2, 4, 2, 5)
    
    # Length
    print("\n1. Tuple length:")
    print(f"  Tuple: {numbers}")
    print(f"  Length: {len(numbers)}")
    
    # Count method
    print("\n2. Count occurrences:")
    count_2 = numbers.count(2)
    print(f"  How many 2's: {count_2}")
    
    # Index method
    print("\n3. Find index of element:")
    index_3 = numbers.index(3)
    print(f"  Index of 3: {index_3}")
    
    # Membership testing
    print("\n4. Membership testing:")
    print(f"  Is 4 in tuple? {4 in numbers}")
    print(f"  Is 10 in tuple? {10 in numbers}")
    
    # Concatenation
    print("\n5. Tuple concatenation:")
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    combined = tuple1 + tuple2
    print(f"  {tuple1} + {tuple2} = {combined}")
    
    # Repetition
    print("\n6. Tuple repetition:")
    pattern = ("*",) * 5
    print(f"  ('*',) * 5 = {pattern}")
    
    # Min, Max, Sum
    print("\n7. Tuple functions:")
    nums = (15, 42, 8, 23, 4)
    print(f"  Tuple: {nums}")
    print(f"  Min: {min(nums)}")
    print(f"  Max: {max(nums)}")
    print(f"  Sum: {sum(nums)}")
    
    # Sorting (returns list)
    print("\n8. Sorting tuple (returns list):")
    sorted_nums = sorted(nums)
    print(f"  Sorted: {sorted_nums} (type: {type(sorted_nums).__name__})")


def demonstrate_tuple_unpacking() -> None:
    """Demonstrate tuple unpacking."""
    print("\n" + "=" * 50)
    print("TUPLE UNPACKING")
    print("=" * 50)
    
    # Basic unpacking
    print("\n1. Basic unpacking:")
    coordinates = (10, 20)
    x, y = coordinates
    print(f"  Tuple: {coordinates}")
    print(f"  x = {x}, y = {y}")
    
    # Multiple values
    print("\n2. Unpacking multiple values:")
    person = ("Alice", 25, "Engineer")
    name, age, job = person
    print(f"  Tuple: {person}")
    print(f"  Name: {name}, Age: {age}, Job: {job}")
    
    # Swapping variables
    print("\n3. Swapping variables:")
    a = 5
    b = 10
    print(f"  Before: a = {a}, b = {b}")
    a, b = b, a  # Elegant swap using tuple unpacking
    print(f"  After:  a = {a}, b = {b}")
    
    # Extended unpacking with *
    print("\n4. Extended unpacking with * (Python 3+):")
    numbers = (1, 2, 3, 4, 5)
    first, *middle, last = numbers
    print(f"  Tuple: {numbers}")
    print(f"  First: {first}")
    print(f"  Middle: {middle}")
    print(f"  Last: {last}")
    
    # Unpacking in loops
    print("\n5. Unpacking in loops:")
    points = [(1, 2), (3, 4), (5, 6)]
    print("  Points:")
    for x, y in points:
        print(f"    Point: x={x}, y={y}")
    
    # Returning multiple values from function
    print("\n6. Function returning multiple values:")
    def get_stats(numbers: tuple) -> tuple:
        return min(numbers), max(numbers), sum(numbers)
    
    data = (5, 10, 15, 20)
    minimum, maximum, total = get_stats(data)
    print(f"  Data: {data}")
    print(f"  Min: {minimum}, Max: {maximum}, Sum: {total}")


def demonstrate_set_basics() -> None:
    """Demonstrate basic set concepts."""
    print("\n" + "=" * 50)
    print("SETS - BASICS")
    print("=" * 50)
    
    # Creating sets
    print("\n1. Creating sets:")
    empty_set = set()  # Note: {} creates an empty dict, not set!
    numbers_set = {1, 2, 3, 4, 5}
    fruits_set = {"apple", "banana", "cherry"}
    
    print(f"  Empty set: {empty_set}")
    print(f"  Numbers: {numbers_set}")
    print(f"  Fruits: {fruits_set}")
    
    # Sets remove duplicates
    print("\n2. Sets automatically remove duplicates:")
    with_duplicates = {1, 2, 2, 3, 3, 3, 4}
    print(f"  Input: {1, 2, 2, 3, 3, 3, 4}")
    print(f"  Result: {with_duplicates}")
    
    # Creating set from list
    print("\n3. Creating set from list:")
    numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique_numbers = set(numbers_list)
    print(f"  List: {numbers_list}")
    print(f"  Set: {unique_numbers}")
    
    # Sets are unordered
    print("\n4. Sets are UNORDERED:")
    set1 = {3, 1, 4, 1, 5, 9, 2, 6}
    print(f"  Created: {3, 1, 4, 1, 5, 9, 2, 6}")
    print(f"  Result: {set1}")
    print("  Note: Order may vary each time!")
    
    # Membership testing (very fast!)
    print("\n5. Membership testing (fast!):")
    large_set = set(range(1000000))
    print(f"  Is 500000 in set? {500000 in large_set}")
    print(f"  Is 2000000 in set? {2000000 in large_set}")


def demonstrate_set_operations() -> None:
    """Demonstrate set operations and methods."""
    print("\n" + "=" * 50)
    print("SET OPERATIONS")
    print("=" * 50)
    
    fruits = {"apple", "banana", "cherry"}
    
    # Adding elements
    print("\n1. Adding elements:")
    print(f"  Original: {fruits}")
    fruits.add("date")
    print(f"  After add('date'): {fruits}")
    
    # Removing elements
    print("\n2. Removing elements:")
    fruits.remove("banana")  # Raises error if not found
    print(f"  After remove('banana'): {fruits}")
    
    fruits.discard("grape")  # Does NOT raise error if not found
    print(f"  After discard('grape'): {fruits} (no error)")
    
    # Pop (removes arbitrary element)
    print("\n3. Pop (removes arbitrary element):")
    numbers = {1, 2, 3, 4, 5}
    print(f"  Original: {numbers}")
    popped = numbers.pop()
    print(f"  Popped: {popped}")
    print(f"  After pop: {numbers}")
    
    # Clear
    print("\n4. Clear all elements:")
    temp_set = {1, 2, 3}
    print(f"  Before: {temp_set}")
    temp_set.clear()
    print(f"  After clear(): {temp_set}")
    
    # Length
    print("\n5. Set length:")
    colors = {"red", "green", "blue"}
    print(f"  Colors: {colors}")
    print(f"  Length: {len(colors)}")


def demonstrate_set_math() -> None:
    """Demonstrate mathematical set operations."""
    print("\n" + "=" * 50)
    print("SET MATHEMATICAL OPERATIONS")
    print("=" * 50)
    
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"\nSet A: {set_a}")
    print(f"Set B: {set_b}")
    
    # Union (all elements from both sets)
    print("\n1. UNION (A | B or A.union(B)):")
    union = set_a | set_b
    print(f"  A | B = {union}")
    print("  Contains all elements from both sets")
    
    # Intersection (common elements)
    print("\n2. INTERSECTION (A & B or A.intersection(B)):")
    intersection = set_a & set_b
    print(f"  A & B = {intersection}")
    print("  Contains only common elements")
    
    # Difference (in A but not in B)
    print("\n3. DIFFERENCE (A - B or A.difference(B)):")
    difference = set_a - set_b
    print(f"  A - B = {difference}")
    print("  Elements in A but not in B")
    
    # Symmetric Difference (in either but not both)
    print("\n4. SYMMETRIC DIFFERENCE (A ^ B):")
    sym_diff = set_a ^ set_b
    print(f"  A ^ B = {sym_diff}")
    print("  Elements in either set but not in both")
    
    # Subset and Superset
    print("\n5. SUBSET and SUPERSET:")
    set_c = {1, 2, 3}
    set_d = {1, 2, 3, 4, 5}
    print(f"  C = {set_c}")
    print(f"  D = {set_d}")
    print(f"  Is C subset of D? {set_c.issubset(set_d)}")
    print(f"  Is D superset of C? {set_d.issuperset(set_c)}")
    
    # Disjoint sets (no common elements)
    print("\n6. DISJOINT (no common elements):")
    set_e = {1, 2, 3}
    set_f = {4, 5, 6}
    print(f"  E = {set_e}")
    print(f"  F = {set_f}")
    print(f"  Are E and F disjoint? {set_e.isdisjoint(set_f)}")


def demonstrate_practical_examples() -> None:
    """Demonstrate practical applications of tuples and sets."""
    print("\n" + "=" * 50)
    print("PRACTICAL EXAMPLES")
    print("=" * 50)
    
    # 1. Using tuples for coordinates
    print("\n1. Tuples for coordinates (immutable points):")
    point1 = (10, 20)
    point2 = (30, 40)
    
    def distance(p1: tuple, p2: tuple) -> float:
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
    
    dist = distance(point1, point2)
    print(f"  Point 1: {point1}")
    print(f"  Point 2: {point2}")
    print(f"  Distance: {dist:.2f}")
    
    # 2. Tuple as dictionary key (immutable)
    print("\n2. Tuples as dictionary keys:")
    locations = {
        (0, 0): "Origin",
        (1, 0): "East",
        (0, 1): "North"
    }
    print(f"  Location at (0, 0): {locations[(0, 0)]}")
    print(f"  Location at (1, 0): {locations[(1, 0)]}")
    
    # 3. Removing duplicates with sets
    print("\n3. Removing duplicates from list:")
    items = ["apple", "banana", "apple", "cherry", "banana", "date"]
    unique_items = list(set(items))
    print(f"  Original: {items}")
    print(f"  Unique: {unique_items}")
    
    # 4. Finding common elements
    print("\n4. Finding common interests:")
    alice_hobbies = {"reading", "gaming", "cooking", "hiking"}
    bob_hobbies = {"gaming", "hiking", "music", "art"}
    common = alice_hobbies & bob_hobbies
    print(f"  Alice's hobbies: {alice_hobbies}")
    print(f"  Bob's hobbies: {bob_hobbies}")
    print(f"  Common hobbies: {common}")
    
    # 5. Email validation (unique emails)
    print("\n5. Processing unique emails:")
    email_list = [
        "user1@email.com",
        "user2@email.com",
        "user1@email.com",  # Duplicate
        "user3@email.com",
        "user2@email.com"   # Duplicate
    ]
    unique_emails = set(email_list)
    print(f"  Total emails: {len(email_list)}")
    print(f"  Unique emails: {len(unique_emails)}")
    print(f"  Duplicates removed: {len(email_list) - len(unique_emails)}")
    
    # 6. RGB color as tuple
    print("\n6. RGB colors as tuples:")
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    print(f"  Red: {RED}")
    print(f"  Green: {GREEN}")
    print(f"  Blue: {BLUE}")


def interactive_example() -> None:
    """Interactive example for tuples and sets."""
    print("\n" + "=" * 50)
    print("INTERACTIVE EXAMPLE: UNIQUE WORD COUNTER")
    print("=" * 50)
    
    print("\nEnter a sentence and I'll analyze it:")
    sentence = input("Your sentence: ")
    
    # Convert to lowercase and split into words
    words = sentence.lower().split()
    
    # Get unique words using set
    unique_words = set(words)
    
    print(f"\n📊 Analysis:")
    print(f"  Total words: {len(words)}")
    print(f"  Unique words: {len(unique_words)}")
    print(f"  Duplicate words: {len(words) - len(unique_words)}")
    print(f"\n📝 All unique words: {sorted(unique_words)}")
    
    # Count frequency of each word
    print(f"\n🔢 Word frequency:")
    for word in unique_words:
        count = words.count(word)
        print(f"  '{word}': {count} time(s)")


def main() -> None:
    """Run all tuple and set demonstrations."""
    print("\n" + "🐍" * 25)
    print("WELCOME TO PYTHON TUPLES & SETS TUTORIAL")
    print("🐍" * 25)
    
    # Tuples
    demonstrate_tuple_basics()
    demonstrate_tuple_operations()
    demonstrate_tuple_unpacking()
    
    # Sets
    demonstrate_set_basics()
    demonstrate_set_operations()
    demonstrate_set_math()
    
    # Practical examples
    demonstrate_practical_examples()
    
    # Ask user if they want to try the interactive example
    print("\n" + "=" * 50)
    try_interactive = input("\nWould you like to try the word counter? (y/n): ")
    if try_interactive.lower() == 'y':
        interactive_example()
    
    print("\n" + "=" * 50)
    print("✅ Tutorial completed!")
    print("💡 Key takeaways:")
    print("   • Tuples are immutable, ordered collections")
    print("   • Sets are mutable, unordered, unique collections")
    print("   • Use tuples for fixed data, sets for uniqueness")
    print("=" * 50)


if __name__ == "__main__":
    main()