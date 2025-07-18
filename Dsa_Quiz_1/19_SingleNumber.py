# Q. GIVEN AN INTEGER ARRAY, EACH NUMBER APPEARS TWICE EXCEPT 1. FIND THAT NUMBER APPEARING SINGLE TIME.
# LOGIC : USE XOR AS IT RETURNS 1 ONLY WHEN BITS ARE DIFFERENT, THEREFORE IT WILL CUT THE DUPLICATES AND ONLY THE NUMBER APPEARING ONCE WILL BE LEFT 

n = int(input("enter size of array : "))
nums = []
for element in range(n):
    element = int(input(f"enter element {element + 1} : "))
    nums.append(element)
print("\n",nums,"\n")
result = 0                  
for i in nums:
    result = result ^ i 
print(f"number appearing single time : {result}")