"""
BITWISE OPERATORS ( & , | , ^ , ~ , << , >> )
Operate on the binary representation of integers, They're used to perform operations bit by bit
"""

# 1). BITWISE AND `&` (Exclusive AND)
# Returns 1 only if both bits are 1.
a = 5    # binary = 101
b = 3    # binary = 011
print(a & b)  # Output: 1 [binary = 001]

# 2). BITWISE XOR ^ (Exclusive OR)
# Returns 1 only if bits are different.
a = 5    # binary = 101
b = 3    # binary = 011
print(a ^ b)  # Output: 6 (binary = 110)

"""
Properties of XOR
A). a ^ a = 0	[A number XORed with itself is 0]
B). a ^ 0 = a	[A number XORed with 0 is itself]
C). a ^ b = b ^ a [Commutative]
D). (a ^ b) ^ c = a ^ (b ^ c) [Associative]
"""

# 3. BITWISE OR |
# Returns 1 if at least one bit is 1.
a = 5    # binary = 101
b = 3    # binary = 011
print(a | b)  # Output: 7 [binary = 111]

# 4. BITWISE NOT ~
# Inverts each bit. Works with signed integers using 2's complement.
a = 5    # binary = 101
print(~a)  # Output: -6 ------> (~5 → -(5 + 1) = -6)

# 5. LEFT SHIFT <<
# Shifts bits to the left (multiplies by powers of 2).
a = 3  # binary = 011
print(a << 1)  # Output: 6 [binary = 110] -----> (0011 << 1 = 0110)


# 6. RIGHT SHIFT >>
# Shifts bits to the right (integer divide by powers of 2).
a = 8  # binary = 1000
print(a >> 2)  # Output: 2 [binary = 10] -------> (1000 >> 2 = 0010)

"""
Summary of Bitwise Operators : 

| Operator    | Name             | Symbol | Meaning                                 |
|-------------|------------------|--------|-----------------------------------------|
| AND         | Bitwise AND      | `&`    | 1 only if both bits are 1               |
| OR          | Bitwise OR       | `|`    | 1 if at least one of the bits is 1      |
| XOR         | Bitwise XOR      | `^`    | 1 if the bits are different             |
| NOT         | Bitwise NOT      | `~`    | Inverts all the bits                    |
| Left Shift  | Shift left bits  | `<<`   | Moves bits left (multiplies by 2)       |
| Right Shift | Shift right bits | `>>`   | Moves bits right (divides by 2)         |
"""