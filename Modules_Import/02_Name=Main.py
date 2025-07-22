"""
__NAME__ == "__MAIN__":

- Every Python file has a special built-in variable called __name__.
- If file running directly, then __name__ == "__main__"
- If the file is being imported into another file, then __name__ becomes the name of that file

- __name__ == "__main__" block says:-

- “Only run this code when this file is executed directly — NOT when imported elsewhere.”

"""

# Q. USE DATETIME, MATH, RANDOM MODULES AS FUNCTION AND CALL THEM USING __NAME__ == "__MAIN__" BLOCK

import datetime
import random
import math

# 1. Print today’s date
def today():
    current_date = datetime.date.today()
    print("Today is:", current_date)

# 2. Roll a dice (1–6)
def roll_dice():
    result = random.randint(1, 6)
    print("Dice rolled:", result)

# 3. Calculate circle area
def circle_area(r):
    area = math.pi * r * r
    print(f"Area of circle with radius {r} is: {area:.2f}")

if __name__ == "__main__":
    today()
    print()
    roll_dice()
    print()
    circle_area(15)

