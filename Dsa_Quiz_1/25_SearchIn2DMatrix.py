# Q. SEARCH FOR A TARGET IN A 2D MATRIX, RETURN TRUE IF TARGET FOUND AND FALSE OTHERWISE

"""
- THERE IS A 2D MATRIX WITH M ROWS AND N COLUMNS.
- EACH ROW IS SORTED IN NON-DECREASING ORDER
- FIRST INTEGER IN EACH ROW > LAST INTEGER IN PREVIOUS ROW

- EXAMPLE : M = 3, N = 4, TARGET = 34
    | 1  | 3  | 5  | 7  |
    | 10 | 11 | 16 | 20 |
    | 23 | 30 | 34 | 60 |

"""

# 1. BRUTE FORCE APPROACH : CHECK EVERY CELL ([TIME COMPLEXITY = O(M*N)])
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(matrix)
target = int(input("enter target value = "))

total_rows = len(matrix)                            # Number of rows
total_cols = len(matrix[0])                         # Number of columns

result = False                                      # Assume target is not found by default

for i in range(total_rows):                         # Outer Loop on rows
    for j in range(total_cols):                     # inner loop on columns
        if target == matrix[i][j]:                  # check if each cell == Target
            result = True

print(result)                                       # print answer


# 2. OPTIMAL APPROACH
"""
- LOGIC : IMAGINE THIS 2D MATRIX AS A FLATTENED OUT 1D SORTED ARRAY AND WE WILL PERFORM 1D BINARY SEARCH ON IT. 
          FIND THE MID_VALUE IN THE 1D SORTED ARRAY AND THEN MOVE ACCORDINGLY TO FIND TARGET.

- TO ACCESS ELEMENTS IN A 2D MATRIX USING A FLATTENED (1D) INDEX WE USE A FORMULA :
    
    IFF, 1). index // total_columns → gives the row_num

         2). index % total_columns → gives the col_number
    
    THEN, 3). element = matrix[row_num][col_num]
        
        where,
        index = current index in 1D flattened version
        total_columns = number of columns in each row of the matrix (i.e. len(matrix[0]))
"""

total_rows = len(matrix)                                # Number of rows
total_cols = len(matrix[0])                             # Number of columns

start_index = 0                                         # Start of the 1D search range
end_index = total_rows * total_cols - 1                 # End of the 1D search range

result = False                                          # Assume target is not found by default

while start_index <= end_index:                         # Binary Search Loop
    mid_index = (start_index + end_index) // 2          # Find the middle index

    row_num = mid_index // total_cols                   # Convert flat index to row number 
    col_num = mid_index % total_cols                    # Convert flat index to column number
    mid_value = matrix[row_num][col_num]                # Calculate Middle Value of the 1D array

    if mid_value == target:                             # If match found
        result = True
        break
    elif mid_value < target:                            # If target is bigger
        start_index = mid_index + 1                     # Search in the 2nd half
    else:
        end_index = mid_index - 1                       # Search in the 1st half

print(result)                                           # print answer
