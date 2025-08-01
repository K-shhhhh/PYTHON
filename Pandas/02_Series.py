"""
SERIES (1D Labeled Array)

- A Series is like a list or NumPy array but with labels (index)
- We can create a series with a list
    
    Syntax:-
        variable_abc = pd.Series([Value_1, Value_2, Value_3,....])
        print(variable_abc)
        
- Index is automatically generated (0, 1, 2,...)
- We can also create Series with custom index

    Syntax:-
        variable_abc = pd.Series([Value_1, Value_2, Value_3,....],index = ['Index_1', 'index_2', 'index_3'])
        print(variable_abc)

- A series Behaves like a mix of list + dictionary and perform its operations like :-

    1). Indexing 
    2). Slicing
    3). Logical Operations

    Syntax for all : Same as we use in Lists


- We Can Create Series from a dictionary.

    Syntax:-
        dict = {'key_1' : value_1, 'key_2' : value_2, 'key_3' : value_3, ....}
        variable_abc = pd.Series(dict)
        print(variable_abc)
    
    Note : Here, Keys become indices and values become data. 

- We can access values and index separately like:-

    print(variable_abc.values)
    print(variable_abc.index)

"""

import numpy as np
import pandas as pd
import random

# Q1. PRINT A RANDOM 1D ARRAY LIKE A COLUMN IN EXCEL

column = pd.Series(np.random.randint(0,20,size = 5))
print(f"\n{column}\n")

# Q2. PRINT MARKS OF 3 STUDENTS OUT OF 100

marks = pd.Series([77,88,99], index = ['Hiyu','Vero','Krish'])
print(marks,"\n")

# Q3. PRINT MARKS OF KRISH 

print(f"Marks of Krish : {marks['Krish']}\n")

# Q4. PRINT GRADES OF 3 STUDENTS I

d = {'a': 1, 'b': [2,3], 'c': [4,5,6,7]}
s = pd.Series(d)
print(s,"\n")

# Q5. PRINT VALUES AND INDICES DIFFERENTLY FROM THE ABOVE 2 PANDA SERIES

print(marks.index)
print(s.values)



