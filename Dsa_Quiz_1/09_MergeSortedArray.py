# Q. MERGE 2 SORTED ARRAYS, GIVEN THAT 1ST ARRAY WILL HAVE AS MANY EXTRA 0s as NUMBER OF ELEMENTS IN 2ND ARRAY

# 3 POINTER METHOD
# LOGIC : GO BACKWARDS IN A AND THEN COMPARE GREATEST ELEMENTS OF A AND B AND KEEP SHIFTING THE INDEX IN A

a = [1,2,3,0,0,0]
b = [2,5,6]
m = 3
n = len(b)
i = m - 1
j = n - 1
index = m + n -1

while (i >= 0 and j >= 0):
    if a[i] >= b[j]:
        a[index] = a[i]
        index = index - 1
        i = i - 1
    else:
        a[index] = b[j] 
        index = index - 1
        j = j - 1
while j >= 0:               # If any elements are left in b
    a[index] = b[j]
    index -= 1
    j -= 1
        
print(a)

    