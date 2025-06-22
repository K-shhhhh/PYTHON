# Decimal to Binary Conversion in Python

# Number Systems Overview
# --------------------------
# Decimal (Base 10): Human-readable numbers
# Example: 2004
# 
# Binary (Base 2): Machine-readable (0s and 1s)
# Example: 010010

# 📘 Method: Repeated Division by 2
# ---------------------------------
# To convert a decimal number to binary:
# → Divide the number by 2 repeatedly and record the remainders.
# → Sort the remainders from bottom to top to get the binary number.
#
# Notation:
# (Decimal)₁₀ = (Binary)₂

# Example 1: Convert 42 to Binary
# ---------------------------------
# 42 / 2 = 21  → R = 0
# 21 / 2 = 10  → R = 1
# 10 / 2 = 5   → R = 0
# 5 / 2  = 2   → R = 1
# 2 / 2  = 1   → R = 0
# 1 / 2  = 0   → R = 1
#
# Binary: 101010
# Result: (42)₁₀ = (101010)₂

# Example 2: Convert 50 to Binary
# ---------------------------------
# 50 / 2 = 25  → R = 0
# 25 / 2 = 12  → R = 1
# 12 / 2 = 6   → R = 0
# 6 / 2  = 3   → R = 0
# 3 / 2  = 1   → R = 1
# 1 / 2  = 0   → R = 1
#
# Binary: 110010
# Result: (50)₁₀ = (110010)₂

# Decimal to Binary Cheatsheet (2 to 10)
# ------------------------------
# 2  → 10
# 3  → 11
# 4  → 100
# 5  → 101
# 6  → 110
# 7  → 111
# 8  → 1000
# 9  → 1001
# 10 → 1010

# Two's Complement: Representing Negative Numbers
# --------------------------------------------------
# Most common method to represent negative numbers in binary.
#
# MSB (Most Significant Bit):
# → 0 → Positive number
# → 1 → Negative number
#
# Steps to Convert Negative Decimal to Binary:
# 1. Convert absolute value to binary
# 2. Prefix with a 0
# 3. Flip the bits → 1's Complement
# 4. Add 1 → 2's Complement
# 5. Final result is stored in memory
# 6. Check MSB for the sign

# Q1. WRITE A CODE TO CONVERT DECIMAL TO BINARY

n = int(input("Enter decimal number = "))  # User input

def decimaltobinary(n):
    result = 0
    power = 1
    while n > 0:
        remainder = n % 2
        result = result + (remainder * power)
        power = power * 10
        n = n // 2
    return result

print(f"Binary representation = {decimaltobinary(n)}")

# Note: This function returns binary as an integer (e.g., 1010), not a string.
# For more accurate binary formatting, use `bin(n)[2:]`x


 











