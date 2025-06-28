# Q. TAKE AN ARRAY AND FIND MAXIMUM SUBARRAY SUM 

"""
- Subarray : continuous part of the array, [1],[1,2],[1,2,3] .... for arr = [1,2,3,4]
- Total no. of subarrays = (n*(n+1))/2 where n is no. of elements in array
- Brute Force Approach : loop through every start and end index, calculate the sum, and track the max.
- Kadane's Algorithm : tracks the current subarray sum and resets if sum goes negative.
"""
# HOW TO PRINT SUBARRAYS OF A GIVEN ARRAY (OPTIONAL)
n = int(input("enter size of array : "))
arr = []
for i in range(n):
    num = int(input(f"enter element {i+1} : "))
    arr.append(num)
print(f"Your array = {arr}\nAll Subarrays : ")
for start in range(n):
    for end in range(start,n):
        for i in range(start, end + 1): 
            print(arr[i], end=" ")
        print()
    print()
        
# BRUTE FORCE APPROACH [O(n^2) TIME COMPLEXITY] 
maxsum = 0
for start in range(n):
    currsum = 0
    for end in range(start,n):
        currsum += arr[end]
        maxsum = max(currsum,maxsum)
print(f"maximum subarray sum using Brute Force Approach : {maxsum}")

# KADANE'S ALGORITHM [0(n)] 
curr_sum = 0
max_sum = float('-inf')
for i in range(n):
    curr_sum += arr[i]
    max_sum = max(curr_sum,max_sum)
    if curr_sum < 0:
        curr_sum = 0
print(f"maximum subarray sum using Kadane's Algorithm : {max_sum}")



