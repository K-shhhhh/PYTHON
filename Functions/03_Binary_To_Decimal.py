# BINARY TO DECIMAL CONVERSION

"""
GENERAL NUMBER SYSTEM
-------------------------
- Decimal (Base 10): Uses digits 0 to 9
  ↳ Example: 2004

- Binary (Base 2): Used by computers (only 0s and 1s)
  ↳ Example: 010010

METHOD: BINARY ➡️ DECIMAL
----------------------------
1. Start from the **rightmost digit** (LSB).
2. Multiply each digit by 2 raised to the power of its position.
3. Add all the results.

🧮 Notation:
(Binary)₂ = (Decimal)₁₀
"""

# EXAMPLE 1: Convert 101010 to Decimal
# --------------------------------------
# 0 * 2^0 = 0
# 1 * 2^1 = 2
# 0 * 2^2 = 0
# 1 * 2^3 = 8
# 0 * 2^4 = 0
# 1 * 2^5 = 32
# ----------------
# Decimal = 42
# Result: (101010)₂ = (42)₁₀

# EXAMPLE 2: Convert 110010 to Decimal
# --------------------------------------
# 0 * 2^0 = 0
# 1 * 2^1 = 2
# 0 * 2^2 = 0
# 0 * 2^3 = 0
# 1 * 2^4 = 16
# 1 * 2^5 = 32
# ----------------
# Decimal = 50
# Result: (110010)₂ = (50)₁₀

"""
BINARY TO DECIMAL CHEATSHEET
-------------------------------
1     = 1
10    = 2
11    = 3
100   = 4
101   = 5
110   = 6
111   = 7
1000  = 8
1001  = 9
1010  = 10
"""

"""
NEGATIVE BINARY TO DECIMAL (Two's Complement)
-------------------------------------------------
To convert a negative binary number to decimal:
1. Flip all bits (1's complement)
2. Add 1 (binary addition) → this gives 2's complement
3. Convert the result to decimal
4. Add a minus sign
"""

# Q1. WRITE A CODE TO CONVERT BINARY TO DECIMAL

n = int(input("Enter binary number = "))  # Accept input as integer

def binarytodecimal(n):
    result = 0
    power = 0
    while n > 0:
        remainder = n % 10
        result += remainder * (2 ** power)
        power += 1
        n = n // 10
    return result

print(f"Decimal number = {binarytodecimal(n)}")  # Output result


