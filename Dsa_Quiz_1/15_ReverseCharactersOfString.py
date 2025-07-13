# Q. REVERSE CHARACTERS IN A STRING 
# LOGIC : SWAP EXTREME INDICES AND USE 2 POINTER APPROACH UNTIL BOTH INDICES MATCH

# 2-POINTER APPROACH
STR = input("enter string : ")
s = list(STR)                                               # CONVERT STRING TO LIST TO PERFORM OPERATIONS
left_idx = 0
right_idx = len(s) - 1
while left_idx < right_idx: 
    s[left_idx], s[right_idx] = s[right_idx], s[left_idx]   # SWAP
    left_idx = left_idx + 1                                 # MOVE LEFT INDEX TOWARDS RIGHT INDEX
    right_idx = right_idx - 1                               # MOVE RIGHT INDEX TOWARDS LEFT INDEX 

STR = str(s)                                                # CONVERT LIST TO STRING AGAIN        
print(STR)
