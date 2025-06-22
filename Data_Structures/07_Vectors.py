"""
VECTORS:-

In C++, vectors are dynamic arrays that grow or shrink automatically.
Python's lists behave the same way — dynamic size, flexible types, built-in methods.

So:
LISTS = VECTORS in Python for all DSA purposes.

"""

# Q1. CREATE VECTOR (LIST) AND ADD VALUES
vec = []               # empty list = vector
vec.append(10)         # add elements using append
vec.append(20)
vec.append(30)
print("My vector is:", vec)

# Q2. REMOVE VALUES FROM VECTOR
vec.pop()              # removes last element (30 removed)
vec.remove(10)         # removes value 10 (by value, not index)
print("After removing:", vec)

# Q3. INSERT AND MODIFY ELEMENTS
vec.insert(0, 99)      # insert 99 at index 0
vec[1] = 42            # change value at index 1
print("Modified vector:", vec)

# Q4. LOOP THROUGH VECTOR
for val in vec:
    print("Value:", val)

# Q5. PRACTICE: FIND SINGLE NUMBER (XOR method)
nums = [2, 2, 3, 4, 4]
result = 0
for num in nums:
    result ^= num      # XOR cancels duplicates
print("Single number is:", result)

"""
SUMMARY :-

| TASK                      | PYTHON METHOD                    |
|---------------------------|----------------------------------|
| Create vector             | vec = []                         |
| Add values                | vec.append(val)                  |
| Remove values             | vec.pop(), vec.remove(val)       |
| Insert/Update             | vec.insert(i, val), vec[i] = val |
| Loop                      | for val in vec:                  |
| Dynamic memory            | Grows/shrinks without manual size|

In Python, mastering lists means you automatically understand both arrays and vectors from C++.
No need for separate classes or imports.
"""