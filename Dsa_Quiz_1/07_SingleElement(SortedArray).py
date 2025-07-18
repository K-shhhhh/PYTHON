# Q. GIVEN AN SORTED ARRAY, EACH NUMBER IS PRESENT TWICE IN THE ARRAY BUT 1 NUMBER IS PRESENTED TWICE. FIND AND RETURN THAT NUMBER.

# LOGIC : SINGLE ELEMENT WOULD BE THE ELEMENT THAT IS NOT EQUAL TO THE NEXT OR PREVIOUS ELEMENT IN THE SORTED ARRAY

n = int(input("enter size of array : "))
numbers = []
for element in range(n):
    element = int(input(f"enter element {element + 1} : "))
    numbers.append(element)
numbers.sort()
print(numbers)

if numbers[0] != numbers[1]:
    print(f"single element = {numbers[0]}")
    exit()
if numbers[n-1] != numbers[n-2]:
    print(f"single element = {numbers[n-1]}")
    exit()

for i in range(1,n-1):
    if numbers[i] == numbers[i+1] and numbers[i] == numbers[i-1]:
        print(f"single element = {numbers[i]}")
        exit()