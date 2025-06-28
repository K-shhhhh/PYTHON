# Q. INPUT A SOTED ARRAY AND RETURN PAIR WITH TARGET SUM 

n = int(input("enter size of array = "))
arr = []
for element in range(n):
    element = int(input(f"enter element number {element + 1} : "))
    arr.append(element)
print(arr)

# BRUTE FORCE [O[n^2] Time Complexity]
target = int(input("enter target value = "))
for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] == target:
            print(f"Indices of the Pair : [{i}, {j}]")
            print(f"Pair values: {arr[i]}, {arr[j]}")
            exit()
print("No pair found with the given target.")

# 2 pointer approach [0[n] Time Complexity]
i = 0
j = n - 1 
while (i<j):
    pairsum = arr[i] + arr[j]
    if (pairsum > target):
        j = j - 1
    elif (pairsum < target):
        i = i + 1
    if (pairsum == target):
        print(f"Indices of the Pair : [{i}, {j}]")
        print(f"Pair values: {arr[i]}, {arr[j]}")
        exit()
print("No pair found with the given target")