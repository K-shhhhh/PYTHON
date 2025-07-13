# Q. IN AN GIVEN ARRAY, FIND IF THERE ARE ANY DUPLICATES(ONLY 1 PRESENT). IF IT PRESENT, RETURN TRUE AND THE NUMBER WHICH HAS A DUPLICATE

n = int(input("Enter size of nums: "))
nums = []
for idx in range(n):
    nums.append(int(input(f"Element {idx+1}: ")))
nums.sort()
print("\n", nums,"\n")
nums.sort()
found = False
for i in range(1,n):
    if nums[i] == nums[i - 1]:
        found = True
        print(found)
        print(f"Duplicated number : {nums[i]}\n")

if found == False:
    print(found)
    

