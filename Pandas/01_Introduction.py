"""
PANDAS

- It is a Python library used for data analysis and manipulation
- Built on top of NumPy
- Provides flexible, user- friendly data structures that feel more like Excel tables or SQL data
- These structures are:-

    1). Series : 1D Labelled Array (Like Excel Column)
    
    2). DataFrame : 2D table of rows and columns (Like Excel Sheet or SQL Table)


"""
import pandas as pd

# Q1. PRINT A SERIES

data = [10, 20, 30]
s = pd.Series(data)
print(f"\n{s}\n")

# Q2. PRINT A DATAFRAME 

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'LA', 'Chicago']
}

df = pd.DataFrame(data)
print(df,"\n")


