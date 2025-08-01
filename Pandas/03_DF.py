"""
DATAFRAME (2D Table)

- like an Excel sheet or SQL table
- A DataFrame is a collection of Series that share the same index.
- Rows: Each row is an record
- Columns: Each column is a variable 

- We can Create a DataFrame from a dictionary:

   Syntax:-
        dict = {'key_1' : value_1, 'key_2' : value_2, 'key_3' : value_3, ....}
        variable_abc = pd.DataFrame(dict)
        print(variable_abc) 

- Index is automatically generated (0, 1, 2,...)
- We can also create Series with custom index
    
    Syntax:-
        variable_abc = pd.DataFrame( dict_name,index = ['Index_1', 'index_2', 'index_3'])
        print(variable_abc)

- We can also access columns, rows or each cell just like we do in SQL:-

    1). Accessing Columns
    - Returns a pd.Series of that consists of values of that column
    - Syntax :-
        print(varaible_abc["column_name"])
    
    - We can add columns as well
    - Syntax:-
        variable_abc["New_column_name"] = [Value!, value_2, value_3, ....]
        print(variable_abc)

    2). Acessing rows
    - 2 ways we can do that:-

        A). By index label i.e. using name of the row like ["Student_1",.....]
        - syntax:-
            print(variable_abc.loc[row_name])
        
        B). By numeric position i.e. using numeric position of row like [0,1,2....]
        - syntax:-
            print(variable_abc.iloc[row_numeric_position])

    3). Acessing particular cell
    - Returns the exact value of the cell you want
    - syntax:-
        print(variable_abc["column_name"].loc["row_name"])

- There are many dataframe attributes like:-
    
    1). variable_abc.shape        # (rows, columns)
    2). variable_abc.columns      # Index of column names
    3). variable_abc.index        # Index of row labels
    4). variable_abc.dtypes       # Data type of each column
    5). variable_abc.head(2)       # First 2 rows
    6). variable_abc.tail(2)      # Last 2 rows

- Summary Table:- 
| Task / Description         | Command                                       |
| -------------------------- | --------------------------------------------  |
| Create DataFrame from dict | `pd.DataFrame({...})`                         |
| Access column              | `variable_abc['Age']`                         |
| Access row (row_name)      | `variable_abc.loc[abc]`                       |
| Access row (row_number)    | `variable_abc.iloc[1]`                        |
| Access Cell (Name_Based)   | `variable_abc.loc["column_name"],["row_name"]`|
| Access Cell (Number_Based) | `variable_abc.iloc[column_no],[row_no]`       |
| Add new column             | `variable_abc['Score'] = [...]`               |
| Get shape                  | `variable_abc.shape`                          |
| Get column names           | `variable_abc.columns`                        |
| Get data types             | `variable_abc.dtypes`                         |
| View top rows              | `variable_abc.head(n)`                        |
| View bottom rows           | `variable_abc.tail(n)`                        |

    
"""
import numpy as np
import random 
import pandas as pd

# Q1. CREATE A TABLE OF NAME, AGE AND CITY OF 3 STUDENTS

dict = {
    'Name': ["Hiyu", "Vero", "Krish"],
    'Age': np.random.randint(15,30, size = 3),
    'City': ["New York", "LA", "Chicago"]
}

dataframe = pd.DataFrame(dict,index=["Student_1", "Student_2", "Student_3"])
print(f"\n{dataframe}\n")

# Q2. ADD A ROW OF MARKS IN THE TABLE
dataframe["Marks"] = [85, 90, 95]
print(dataframe,"\n")

# Q3. PRINT NAMES OF ALL STUDENTS

print(dataframe['Name'],"\n")

# Q4. PRINT DETAILS OF HIYU

print(dataframe.loc["Student_1"],"\n")                               # Access row by index label

# Q5. PRINT DETAILS OF KRISH

print(dataframe.iloc[2],"\n")                                        # Access row by numeric position

# Q6. PRINT AGE OF VERO

print(f"Age of Vero : {dataframe.loc["Student_2","Age"]}\n")        # Access using names

print(f"Marks of Krish : {dataframe.iloc[2,3]}\n")                  # Access using numbers

# Q7. PRINT THE DATAFRAME ATTRIBUTES LISTED ABOVE

print(f"Size of table :{dataframe.shape}\n")       
print(f"Column names : {dataframe.columns}\n")      
print(f"Row names : {dataframe.index}\n")        
print(f"Data Type of each column : \n{dataframe.dtypes}\n")       
print(f"First 2 rows : \n{dataframe.head(2)}\n")       
print(f"Last 2 rows : \n{dataframe.tail(2)}\n")      