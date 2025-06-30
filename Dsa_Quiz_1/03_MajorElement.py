# Q. IN A GIVEN ARRAY, FIND IF THERE IS AN MAJORITY ELEMENT

# MAJORITY ELEMENT : IF AN ELEMENT IS APPEARING FLOOR N/2 TIMES
# ASSUME THAT MAJORITY ELEMENT ALWAYS EXIST

n = int(input("Enter size of array : "))
arr = []
for element in range(n):
    element = int(input(f"enter element {element + 1} : "))
    arr.append(element)
print(arr)

# BRUTE FORCE APPROACH (O[n^2])    
for i in range(n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count = count + 1
    if count > n//2:
        print(f"MAJORITY ELEMENT = {arr[i]}")
        break
    
# SORTING APPROACH
arr.sort()
COUNT = 1
for i in range(1,n):
    if arr[i] == arr[i-1]:
        COUNT = COUNT + 1
    else: 
        COUNT = 1
    if COUNT > n//2:
        print(f"MAJORITY ELEMENT = {arr[i]}")
        break 