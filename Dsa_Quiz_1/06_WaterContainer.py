# Q. FOR A GIVEN ARRAY [HIEGHT], ASSUME EACH ELEMENT AS Y-AXIS AND X-AXIS AS THE REFERENCE FOR EACH INDEX WITH THE DIFFERENCE AS 1. FIND THE MAX AMOUNT OF WATER THE CONTAINER CAN STORE. (area = min.hieght * width)

n = int(input("Enter size of array = "))
hieght = []
for element in range(n):
    element = int(input(f"enter hieght number {element + 1} : "))
    hieght.append(element)
print(hieght)

# BRUTE FORCE APPROACH
maxwater = 0
for i in range(n):                      # i = left boundary
    for j in range(i+1,n):              # j = right boundary
        width = j-i
        cont_water = width * min(hieght[i],hieght[j])
        maxwater = max(maxwater,cont_water)
print(f"maximum amount of water in a container : {maxwater} units")
        
# OPTIMAL APPROACH (2 POINTER)
i = 0
j = n -1
while(i < j):
    width = j-i
    cont_water = width * min(hieght[i],hieght[j])
    maxwater = max(maxwater,cont_water)
    if (hieght[i]<hieght[j]):
        i = i + 1
    elif(hieght[j]<hieght[i]):
        j = j - 1
    else:
        i = i + 1

print(f"maximum amount of water in a container : {maxwater} units") 