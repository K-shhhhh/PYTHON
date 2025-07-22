"""
ERRORS IN PYTHON:

- Errors in Python are problems that prevent a program from running correctly or producing the expected output

| Type          | Meaning                                       | Example Code                                          | Example Error                 |
| --------------| --------------------------------------------- | ----------------------------------------------------- | ----------------------------- |
| Syntax Error  | Broken grammar of Python                      | `if x = 5`                                            | `SyntaxError: invalid syntax` |
| Runtime Error | Happens during execution; crashes the program | `5 / 0`                                               | `ZeroDivisionError`           |
| Logical Error | Code runs, no crash, but result is wrong      | Area of circle: `3 * r * r` instead of `3.14 * r * r` | No error, just wrong result   |

- Logical Errors are often the most challenging to detect as the code runs without errors, but the output is not what was intended

- There are Common types of runtime errors include:- 

| Error Name          | What It Means                                           | Example                        |
| ------------------- | ------------------------------------------------------- | ------------------------------ |
| `ZeroDivisionError` | You tried to divide by zero                             | `10 / 0`                       |
| `ValueError`        | Wrong type of value used                                | `int("hello")`                 |
| `TypeError`         | Wrong type of data used with an operation               | `"hi" + 5`                     |
| `NameError`         | You used a variable that doesn't exist                  | `print(x)` before defining `x` |
| `IndexError`        | You accessed an invalid list index                      | `a = [1,2]; print(a[5])`       |
| `KeyError`          | Dictionary key not found                                | `d = {"a":1}; print(d["z"])`   |
| `FileNotFoundError` | Tried to open a file that doesn't exist                 | `open("abc.txt")`              |
| `ImportError`       | Tried to import a module or function that doesn't exist | `from math import squareroot`  |
| `AttributeError`    | Tried using a method that doesn't belong to the object  | `"hello".push()`               |

"""

# Q1. SHOW A SYNTAX ERROR

"""if x = 5"""                    # SHOWS SYNTAX ERROR WHEN WE RUN IT 

# Q2. SHOW A RUNTIME ERROR

a = 5/0
print(a)                    # SHOWS ZERODIVISIONERROR WHEN WE RUN IT

# Q3. SHOW A LOGICAL ERROR

r = 2
area = 3.14 * r             # SHOWS NO ERROR BUT OUR LOGIC IS WRONG
print(area)

