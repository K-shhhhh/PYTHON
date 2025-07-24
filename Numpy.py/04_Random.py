"""
NUMPY + RANDOM

- These 2 libraries can be used together to perform various tasks.
- Numpy Specializes in math operations and with Random we can fill random values.
- Some of these are :- 

    1). Random integers in a matrix
    2). Random floats in a matrix       (Default values : 0.0 to 1.0)
    3). Rndom Normal distribution
    4). Shuffling of an np.array and etc

"""
import numpy as np
import random

# Q2. PRINT A MATRIX OF 6 RANDOM INTEGER VALUES FROM 1 TO 50

print("\n",np.random.randint(1, 50 ,size = (2,3)),"\n")

# Q2. PRINT A MATRIX OF 6 RANDOM FLOAT VALUES FROM 0 TO 100

random_float = np.random.rand(2,3) * 100                                    # * 100 WILL GIVE FLOAT FROM 0 TO 100
print("\n",random_float,"\n")                                               # 2x3 matrix

# Q3. PRINT Random Normal Distribution With Mean =  0 and Std = 1
    
print(np.random.randn(2, 3),"\n")  

# Q4. SHUFFLE AN NP.ARRAY

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(f"Original : {arr}")
np.random.shuffle(arr)
print("Shuffled :",arr,"\n")

# Q5. CREATE A RANDOM MATRIX, PRINT ITS TRANSPOSE AND THEN CONVERT IT INTO A 1D ARRAY

rand_matrix = np.random.randint(1, 100, size=(3, 4))
print("Random 3x4 Matrix:\n", rand_matrix,"\n")

print("Transpose:\n", rand_matrix.T,"\n")

flat = rand_matrix.flatten()
print("Flattened to 1D:\n", flat)




