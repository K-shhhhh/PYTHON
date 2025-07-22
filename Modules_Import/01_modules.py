"""
MODULES:

- BASICALLY LIKE A CODE LIBRARY
- MODULE IS A FILE WRITTEN BY ANOTHER PROGRAMMER THAT GENERALLY HAS A FUNCTION(S)
  WE CAN USE
- IN SHORT TO BORROW A FILE, WE USE MODULES
- SYNTAX :-
    IMPORT FILE_NAME
    COMMAND

- SOME BASIC PYTHON BUILT IN FUNCTIONS ARE

| Module     | Purpose (in CS50 AI or real-world)                     |
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

