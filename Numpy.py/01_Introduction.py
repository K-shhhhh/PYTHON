"""
NUMPY (Numerical Python)

- Powerful library in Python used for:
    1). Fast numerical calculations
    2). Matrix operations
    3). Backend for libraries like Pandas etc
    4). Efficient storage and processing of numerical data

- It is an alternative to Python lists, especially when performing operations with lists and numbers.

- Example:- (Multiply values in a list)
    
    1). my_list = [1, 2, 3, 4, 5]
        print(my_list * 2)  
        Output: [1,2,3,4,5,1,2,3,4,5]           # This is not multiplication

    2). import numpy as np
        my_array = np.array([1, 2, 3, 4, 5])
        print(my_array * 2)  
        Output: [2 4 6 8 10]                    # Proper Multiplication

- Just like in lists, we can perform operations on np.array as well:-

    1). Mathematical Operations
        a = np.array([1, 2, 3, 4])

        print(a + 5)--------> Output : [6 7 8 9]
        print(a * 2)--------> Output : [2 4 6 8]
        print(a ** 2)-------> Output : [1 4 9 16] 
        print(a / 2)--------> Output : [0.5 1.  1.5 2. ]
   
    2). Loops
    - Syntax :
            arr = np.array([10, 20, 30])
            for val in arr:
                print(val)

    3). Attributes
    - Np.array can use similar attributes like:-
        
        A). Shape = Size of Array
        
        B). Dimension = Dimension of that array (1D,2D,3D) ETC

    4). Broadcasting (Cant be done in lists) 
    - Perform operations between arrays of different shapes

        A). 1D Array Broadcasting
            a = np.array([1, 2, 3])
            b = 10
            print(a + b)   
            Output : [11 12 13]             # b is “broadcasted” across `a`

        B). 2D Array Broadcasting
            m = np.array([[1, 2], [3, 4]])
            v = np.array([10, 20])
            print(m + v)  
            Output : [[11 22], [13 24]]     # v is “broadcasted” across `m`

    5). Indexing (1D and 2D Array)
    - Check Q5

    6). Slicing (1D and 2D Array)
    - Check Q6

    7). Logical Operations
    - Check Q9 and Q10
    



- Summary:
| Feature               | Python List  | NumPy Array        |
| --------------------- | ------------ | ------------------ |
| Speed                 | Slower       | Much faster        |
| Memory usage          | More         | More efficient     |
| Math operations       | Manual/loops | Direct & optimized |
| Data type flexibility | Mixed types  | Must be same type  |
| Built-in tools        | Limited      | Tons of tools      |

"""

# Q1. CREATE AN ARRAY USING NUMPY AND USE SOME BASIC ATTRIBUTES

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("\nMy array:", arr)

shape = list(arr.shape)                                     # CONVERT TUPLE INTO LIST FOR CONVINIENCE
print("Type:", type(arr))                                   # NUMPY ARRAY WILL BE PRINTED                   
print("shape:",shape)                          
print("Dimensions:", arr.ndim,"D\n")           

# Q2. MULTIPLY AND ADD 2 NUMPY ARRAYS

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a)
print(b)
print("Addition:",a+b)
print("Multiplication:",a*b,"\n")

# Q3. USING NUMPY, MAKE ARRAYS WITH SHORTCUTS

print(np.zeros(10))                                         # ALL ELEMENTS AS ZERO 
print(np.ones(10))                                          # ALL ELEMENTS AS ONE
print(np.arange(0,20,2))                                    # LIKE RANGE FUNCTION WITH (START,END,STEP) WITH END NOT INCLUDED
print("\n")

# Q4. GENERATE 5 RANDOM NUMBERS BETWEEN 1 TO 100

import random

random_array = np.random.randint(1,101,size=5)              # USING BOTH NUMPY AND RANDOM LIBRARY FUNCTIONS IN ONE LINE OF CODE    
print("Random 5 no. between 1 to 100 :",random_array,"\n")

# Q5. PRINT LAST AND FIRST ITEM OF A 1D AND 2D NP.ARRAY

arr1 = np.array([10, 20, 30, 40, 50, 60])
print(arr1[0])   
print(arr1[-1],"\n") 

matrix = np.array([[1, 2, 3],[4, 5, 6]])

print(matrix[0,0])                                         # 1ST ROW, 1ST ELEMENT    
print(matrix[1, 2],"\n")                                   # 2ND ROW, 3RD ELEMENT

# Q6. PRINT FIRST HALF OF A 1D AND 1ST COLUMN 2D NP.ARRAY

print(arr1[0:2])
print(matrix[:,1],"\n")                                    # [ALL ROWS :, COLUMN 1]

# Q7. PRINT TRUE IF ELEMENTS OF THE NP.ARRAY ARE GREATER THAT 35 AND PRINT THEM

print(arr1 > 35)         

values = arr1[arr1 > 35]
print(values,"\n")     

# Q8. PRINT ALL EVEN NUMBERS TILL 40

nums = np.arange(0, 41)                                    # SHORTCUT TO CREATE ARRAY FROM 0 TO 40                                          
even = nums[nums % 2 == 0]
print(even) 



