# Q. IN AN ARRAY, FIND ALL UNIQUE SETS OF 3 ELEMENTS WHOSE SUM == 0

n = int(input("enter size of array : "))
nums = []
for element in range(n):
    element = int(input(f"enter element {element + 1} : "))
    nums.append(element)
print(f"\nArray = {nums}\n")

# 1. FORCE APPROACH (FIND ALL TRIPLETS AND THEN FIND SUM)
#    LOGIC : USE 3 LOOPS, I != J != K, USE SETS TO REMOVE REDUNDANCY, USE TUPLES AS THEY CAN BE ADDED INTO SETS BUT LISTS CANNOT

triplets = set()
for i in range(0,n):                                            # PICK 1ST NO.
    for j in range(i+1,n):                                      # PICK 2ND NO.
        for k in range(j+1,n):                                  # PICK 3RD NO.
            if (nums[i] + nums[j] + nums[k] == 0):
              total = tuple(sorted([nums[i], nums[j], nums[k]]))
              triplets.add(total)

for answer in triplets:
    print(list(answer))                                         # PRINT UNIQUE TRIPLETS IN LIST FORMAT

# 2. 2-POINTER APPROACH (OPTIMAL SOLUTION)
#    2-POINTER APPROACH IS ALWAYS USED ON A SORTED ARRAY
#    LOGIC : FIX VALUE OF I, WITH THE REMAINING SET OF VALUES, USE J AND K AS EXTREME VALUES AND USE 2 POINTER APPROACH TO FIND TRIPLET

nums.sort()
TRIPLETS = []

for i in range(n):
    
    if i > 0 and nums[i] == nums[i - 1]:                        # SKIP ITERATION IF DUPLICATE OF I
        continue

    j = i + 1
    k = n - 1

    while j < k:
        TOTAL = nums[i] + nums[j] + nums[k]

        if TOTAL > 0:
            k -= 1
        elif TOTAL < 0:
            j += 1
        else:
            TRIPLETS.append([nums[i], nums[j], nums[k]])

            while j < k and nums[j] == nums[j + 1]:             # SKIP DUPLICATES FOR J 
                j += 1
            while j < k and nums[k] == nums[k - 1]:             # SKIP DUPLICATES FOR K 
                k -= 1

            j += 1                                              # UPDATION FOR NEXT ITERATION
            k -= 1                                              # UPDATION FOR NEXT ITERATION

for answer in TRIPLETS:                                         # PRINT UNIQUE TRIPLETS
    print(answer)