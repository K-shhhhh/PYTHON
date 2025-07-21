# Q. GIVEN AN ARRAY OF INTEGERS ARR, PRINT TRUE IF THE NUMBER OF OCCURRENCES OF EACH VALUE IN THE ARRAY IS UNIQUE OR FALSE OTHERWISE 
# LOGIC : SORT ARR, COUNT HOW MANY TIMES EACH UNIQUE NUMBER IS STORED, STORE THAT VALUE IN A LIST, 
#         COMPARE IF LENGTH OF THAT LIST AND LENGTH OF LIST WHEN CONVERTED INTO A SET IS SAME OR NOT 
#         AS A SET REMOVES ALL THE DUPLICATES.

n = int(input("enter size of number = "))
arr = []
for element in range(n):
    element = int(input(f"enter digit {element + 1} : "))
    arr.append(element)
arr.sort()
print("\n",arr)
frequency_list = []                                         # LIST THAT COUNTS HOW MANY TIMES AN UNIQUE NUMBER IS STORED 
i = 0
        
while i < n:
    count = 1                                               # A NUMBER IS ATLEAST STORED ONCE
    j = i + 1                                               # INDEX TO NEXT ELEMENT IN ARR
    while j < n and arr[i] == arr[j]:                       # CHECK IF ELEMENT IS NOT THE LAST ONE AND NEXT ELEMENT IS THE SAME OR NOT
        count += 1                                          # INCREMENT
        j += 1                                              # INCREMENT
    frequency_list.append(count)                            # REGISTER HOW MANY TIMES THE ELEMENT WAS COUNTED 
    i = j                                                   # SHIFT TO NEXT UNIQUE ELEMENT
        
if len(frequency_list) == len(set(frequency_list)):         # CONVERT LIST INTO SET AS SET REMOVES ALL THE DUPLICATES AND CHECK LENGTH
    print(True)
else:
    print(False)