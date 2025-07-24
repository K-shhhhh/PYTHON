"""
SORTING (Axis)

- This file shows how to analyze data row-wise and column-wise
- In 2D Arrays,

    Axis = 0 ----> Column
    Axis = 1 ----> Row

- We use this same logic for sorting as well

"""
import numpy as np
import random

# Q1. PRINT THE SUM OF ROW ELEMENTS AND SUM OF COLUMN ELEMENTS IN A RANDOM 2D MATRIX

matrix = np.random.randint(0, 20, size = (3,3))
print("\nOriginal :\n",matrix)
print("\nSum of all elements :",np.sum(matrix),"\n")
print("Sum of all column elements :",np.sum(matrix, axis=0),"\n")
print("Sum of all row elements :",np.sum(matrix, axis=1),"\n")

# Q2. SORT A 1D NP.ARRAY

arr = np.random.randint(0,100,size = 10)
print(arr)
print(np.sort(arr),"\n")

# Q3. SORT A 2D MATRIX BY ROWS AND COLUMNS

print(matrix,"\n")
print(np.sort(matrix, axis=0),"\n") 
print(np.sort(matrix, axis=1),"\n")  

# Q4. A TABLE OF 3 STUDENTS HAS ROWS AS STUDENT SCORES AND COLUMNS AS SUBJECT, FIND:-
#     1). TOTAL SCORE OF EACH STUDENT OUT OF 300 
#     2). MAX MARKS OF EACH SUBJECT

scores = np.array([[85, 87, 95], 
                   [88, 88, 80], 
                   [70, 95, 75]])

print(scores,"\n")
print("Total Score of Each Student out of 300 :",np.sum(scores, axis=1))  
print("Highest marks in each subject :",np.max(scores, axis=0))   
