# Q. SORT AN ARRAY CONTAIING 0s,1s AND 2s (0s = RED,1s =  WHITE,2s = BLUE)
n = int(input("enter size of array : "))
arr = []
for element in range(n):
    element = int(input(f"enter element {element + 1} : "))
    arr.append(element)
print(arr,"\n")

# BRUTE FORCE APPROACH [0(nLogn) TIME COMPLEXITY]
arr.sort()
print(arr,"\n")

# DUTCH NATIONAL FLAG ALGORITHM (0[n] TIME COMPLEXITY)
"""
3-POINTERS USED (LOW,MID,HIGH)
LOGIC : STORE ALL Os IN 0 TO (LOW-1), 1s IN LOW TO (MID-1), 2s IN (HIGH+1) TO (N-1)
FROM MID TO HIGH, WE STORE OUR UNSORTED ELEMENTS, THEN WE SORT EACH ELEMENT AND DO HIGH++ AND MID-- UNTIL MID = HIGH
"""
mid = 0
high = n-1
low = 0
while(mid<=high):
    if arr[mid] == 0:
        arr[low],arr[mid] = arr[mid],arr[low]
        mid = mid + 1
        low = low + 1
    elif arr[mid] == 1:
        mid = mid + 1
    else: 
        arr[high],arr[mid] = arr[mid],arr[high]
        high = high - 1
print(arr)