"""
MODULES:

- BASICALLY LIKE A CODE LIBRARY
- MODULE IS A FILE WRITTEN BY ANOTHER PROGRAMMER THAT GENERALLY HAS A FUNCTION(S)
  WE CAN USE
- IN SHORT TO BORROW A FILE, WE USE MODULES
- THERE ARE MANY WAYS THROUGH WHICH WE CAN IMPORT A MODULE

| Syntax                             | Meaning                         | Example                                  | When to Use                             |
| ---------------------------------- | ------------------------------- | ---------------------------------------- | --------------------------------------- |
| `import module`                    | Imports entire module           | `import math` → `math.sqrt(4)`           | Standard, safest, avoids conflicts      |
| `import module as alias`           | Imports module with a nickname  | `import numpy as np` → `np.array([...])` | Long module names (like numpy, pandas)  |
| `from module import name`          | Imports specific function/class | `from math import sqrt` → `sqrt(4)`      | You only need one or two things         |
| `from module import name as alias` | Specific item with nickname     | `from math import sqrt as s` → `s(4)`    | Rarely used, but useful in name clashes |
| `from module import *`             | Imports everything directly     | `from art import *` → `tprint("Hi")`     | Only for small, safe modules            |

- SYNTAX :-
    IMPORT FILE_NAME
    COMMAND

- SOME BASIC PYTHON BUILT IN FUNCTIONS ARE

| Module     | Purpose (in CS50 Courses or real-world)                     |
| ---------- | ------------------------------------------------------ |
| `math`     | Square roots, powers, constants like π                 |
| `random`   | Random moves in Tic-Tac-Toe or AI simulations          |
| `datetime` | Timestamps, durations (used in logging or time checks) |
| `sys`      | Command-line arguments (e.g., `sys.argv`)              |
| `os`       | File handling, directory paths                         |
| `calendar` | Date-based logic                                       |


"""

# Q1. IMPORT AND REMOVE SAMPLE.TXT
import os
os.remove("Sample.txt")

# Q2. IMPORT MATH MOUDLE AND USE 3 FUNCTIONS OF IT 
import math

print(math.sqrt(16))        # 4.0
print(math.pow(2, 3))       # 8.0 (same as 2 ** 3)
print(math.floor(3.7))      # 3
print(math.pi)              # 3.1415....
print("\n")

# Q3. PRINT A RANDOM NUMBER FROM 1 TO 10 AND CHOOSE A RANDOM SYMBOL FROM X AND O

import random 

print(random.randint(1, 10))         # Random number from 1 to 10
print(random.choice(['X', 'O']))     # Randomly choose from list        
print("\n")

# Q4. PRINT CURRENT DATE AND TIME

import datetime

now = datetime.datetime.now()
print(now)

