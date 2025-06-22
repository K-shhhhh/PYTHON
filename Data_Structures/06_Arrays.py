"""
ARRAYS:-

In C/C++ or Java, arrays are fixed-size containers for storing values of the same type.
In Python, we use "lists" for the same purpose as it can perform all tasks by arrays and even more. 
So:
LISTS = ARRAYS in DSA using Python.
"""

# Q1. MAKE AN ARRAY (LIST) 
arr = [10, 20, 30, 40, 50]                              # create a list of 5 elements
print("My array is:", arr)
print("\n")

# Q2. ACCESS VALUES IN AN ARRAY
print("First value:", arr[0])                           # index 0 = first element
print("Last value:", arr[-1])                           # -1 = last element
print("\n")

# Q3. CHANGE A VALUE
arr[2] = 99                                             # change 3rd value to 99
print("Changed array:", arr)
print("\n")

# Q4. TAKE USER INPUT IN ARRAY
n = int(input("Size of array = "))                      # user defines size
arr = []                                                # empty array
for i in range(n):                                      # loop till n 
    val = int(input(f"Enter number {i+1}: "))             # take input
    arr.append(val)                                     # add element
print("Final array:", arr)
print("\n")

# Q5. PRINT ALL ELEMENTS SEPARATELY USING LOOP
print("Array values:")
for i in range(len(arr)):
    print(arr[i])
print("\n")

# Q6. FIND SMALLEST AND LARGEST ELEMENT
smallest = arr[0]                                       # Taking first element as smallest variable
largest = arr[0]                                        # Taking first element as smallest variable

for i in arr:
    if i < smallest:                                    # Compare 
        smallest = i
    if i > largest:                                     # Compare
        largest = i
print("Smallest:", smallest)
print("Largest:", largest)
print("\n")

# Q7. REVERSE THE ARRAY (2 POINTERS METHOD)
start = 0
end = len(arr) - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]         # Single line swap technique // a,b=b,a --> 1,5=5,1 = [5.....1] //
    start += 1
    end -= 1
print("Reversed array:", arr)
print("\n")

# Q8. LINEAR SEARCH (FIND POSITION OF A VALUE)
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
key = int(input("Enter number to search: "))
position = linear_search(arr, key)
if position != -1:
    print(f"Found at index:{position}")
else:
    print("Not found")
print("\n")

# Q9. COUNT HOW MANY TIMES A VALUE OCCURS
count = 0
target = int(input("Enter number to count: "))
for i in arr:
    if i == target:
        count += 1
print(f"{target} appears {count} times.")
print("\n")

# Q10. FIND SECOND LARGEST ELEMENT
arr_sorted = sorted(list(set(arr)))
print("Second largest:", arr_sorted[-2])
print("\n")

# Q11. FIND SECOND SMALLEST ELEMENT                    
print("Second largest:", arr_sorted[1])                
print("\n")

# Q12. PRINT ARRAY IN REVERSE (SLICING METHOD)
print("Reversed using slice:", arr[::-1])
print("\n")

"""
Summary :- 

| TASK                      | PYTHON EXAMPLE                    |
|---------------------------|-----------------------------------|
| Create array              | arr = [10, 20, 30]                |
| Access element            | arr[1]                            |
| Update value              | arr[2] = 99                       |
| Input from user           | arr.append(input())               |
| Loop through array        | for i in range(len(arr))          |
| Reverse array (2-pointer) | use while loop with arr[i], arr[j]|
| Search value              | for i in arr: if i == key         |
| Count occurrences         | if i == target: count += 1        |
| set(arr)                  | removes duplicates from arr       |
| list(set(arr))            | Converts the set back to a list   |
| sorted(...)               | Sorts the list in ascending order |
| Find second largest       | sorted(arr)[-2]                   |
| Find second smallest      | sorted(arr)[1]                    |
| Print reversed            | arr[::-1]                         |

"""