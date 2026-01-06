# Python Basics Tutorial

A comprehensive beginner-friendly Python project that demonstrates fundamental programming concepts through practical, well-documented examples.

---

## 📖 Overview

This repository contains educational Python modules designed to help beginners learn essential programming concepts step by step. Each module focuses on a specific topic with clear examples, type hints, interactive demonstrations, **and automated tests** to validate the solutions.

---

## 📁 Project Structure

```
python-basics/
│
├── exercises/
│   ├── variables.py      # Variables, data types, and type casting
│   ├── control_flow.py   # Conditional statements and logic
│   ├── functions.py      # Functions and parameters
│   ├── lists.py          # Lists and list operations
│   ├── loops/            # Loop exercises (for / while)
│   └── tuples/           # Tuple exercises
│
├── tests/                # Automated tests (pytest)
│
├── requirements.txt      # Project dependencies
├── run_test              # Script to run the test suite
├── .coveragerc           # Coverage configuration
└── README.md             # Project documentation
```

---

## 🎯 Modules

### 1. variables.py

Learn the fundamentals of Python variables:

* Variable declaration with type hints
* Basic data types (`str`, `int`, `float`, `bool`)
* User input handling
* Type casting and conversions
* Simple calculations

Topics covered:

* The `type()` function
* Input and output operations
* Converting between data types

---

### 2. control_flow.py

Master control flow structures in Python:

* `if` / `elif` / `else` statements
* Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
* Logical operators (`and`, `or`, `not`)
* Nested conditions
* Error handling with `try/except`

---

### 3. functions.py

Learn how to create reusable code using functions:

* Function definitions and calls
* Parameters and return values
* Default parameters
* `*args` and `**kwargs`
* Lambda functions
* Practical examples

---

### 4. lists.py

Explore Python lists and their operations:

* Creating and initializing lists
* Indexing and slicing
* Adding and removing elements
* List methods (`append`, `insert`, `remove`, `pop`)
* List comprehensions
* Nested lists

---

### 5. loops (folder)

Practice loop-based problem solving:

* `for` loops
* `while` loops
* Loop control statements (`break`, `continue`, `pass`)
* Iteration over ranges and collections
* Practical repetition exercises

---

### 6. tuples (folder)

Learn how to work with immutable data structures:

* Tuple creation and unpacking
* Indexing and slicing tuples
* Tuples vs lists
* Returning multiple values from functions
* Practical tuple-based exercises

---

## 🧪 Testing

This project includes an automated **test suite using pytest** to validate the exercises.

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run all tests

```bash
pytest
```

Or use the provided script:

```bash
./run_test
```

### Test coverage (optional)

```bash
pytest --cov
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.7 or higher
* Basic command-line knowledge

### Installation

```bash
git clone https://github.com/Dev-AlejandroMiranda/python-basics.git
cd python-basics
```

### Running the exercises

You can run any module directly:

```bash
python exercises/variables.py
python exercises/control_flow.py
python exercises/functions.py
python exercises/lists.py
```

Each module includes interactive examples that may prompt user input.

---

## 💡 Learning Path

Recommended order:

1. `variables.py`
2. `control_flow.py`
3. `functions.py`
4. `lists.py`
5. `loops/`
6. `tuples/`

---

## 🎓 Key Features

* Beginner-friendly and well-documented code
* Type hints for clarity
* Interactive examples
* Automated tests with pytest
* Progressive difficulty
* Real-world problem examples

---

## 🤝 Contributing

This is an educational project. Contributions are welcome:

* Suggest improvements
* Add exercises
* Improve documentation
* Add more tests

---

## 📝 License

Open source and intended for educational purposes.

---

## 👤 Author

Alejandro Miranda
GitHub: **@Dev-AlejandroMiranda**

---

## 🔮 Future Modules

Planned additions:

* dictionaries.py
* sets.py
* file_operations.py

---

⭐ If you find this project helpful, consider giving it a star on GitHub!

Happy Learning! 
