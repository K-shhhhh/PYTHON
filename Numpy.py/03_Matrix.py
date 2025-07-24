"""
MATRIX (2D Arrays)

- This is very NumPy is much more useful than lists
- We can create 2D Arrays quite easily in NumPy and perform operations on them with ease.
- Some of the useful opersations are:-
    
    1). Print shape as r0ws and columns
    2). Reshape 1D Np.Arrays to 2D Np.Arrays
    3). Flatten out  2D Np.Array to 1D Np.Array
    4). Transpose of Matrix (2D Arrays)
    5). Identity Matrix (2D Arrays)

"""
import numpy as np

# Q1. PRINT A 2D NP.ARRAY, ITS SIZE AND ITS DIMESIONS

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr_2d)
print("Shape:", arr_2d.shape)                   # 2,3 MEANS 2 ROWS AND 3 COULUMNS
print("Dimensions:", arr_2d.ndim,"D\n") 

# Q2. CONVERT A 1D NP.ARRAY TO A MATRIX

arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Actual Array : {arr}")
print("Dimension:",arr.ndim,"D\n")

reshaped = arr.reshape(2, 3)                    # 2,3 MEANS 2 ROWS AND 3 COLUMNS 
print("Reshaped Array:\n", reshaped)
print("New Dimension :",reshaped.ndim,"D\n")

# Q3. CONVERT A MARIX TO A 1D ARRAY FOR SIMPLIFICATION

print(arr_2d)
print("Dimensions:", arr_2d.ndim,"D\n")
flat = arr_2d.flatten()
print(f"Flattened 1D Array : {flat}")
print("New Dimension :",flat.ndim,"D\n")

# Q4. PRINT TRANSPOSE OF A MATRIX

print(f"Original : \n{arr_2d}")
print("Transpose : \n",arr_2d.T,"\n")

# Q5. PRINT AN IDENTITY MATRIX 

id_matrix = np.eye(2)                           # 2 = 2 * 2 matrix
print(id_matrix)




