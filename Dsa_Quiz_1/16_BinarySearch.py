# Q. GIVEN AN ARRAY AND A TARGET, USE BINARY SEARCH TO FIND OUT AT WHAT INDEX IS THE TARGET PRESENT IN THE ARRAY. IF TARGET NOT FOUND, PRINT NOT FOUND

# BINARY SEARCH / 2-POINTER APPROACH
n = int(input("Enter size of nums: "))
nums = []
for idx in range(n):
    nums.append(int(input(f"Element {idx+1}: ")))
nums.sort()
print("\n", nums,"\n")

target = int(input("Enter target: "))

start = 0
end = n - 1
found = False       

while start <= end:
    mid = (start + end) // 2   
    if nums[mid] == target:
        print(f"Target found at index {mid}")
        found = True
        break
    elif nums[mid] < target:
        start = mid + 1        
    else:
        end = mid - 1          

if found == False:
    print("Not Found")