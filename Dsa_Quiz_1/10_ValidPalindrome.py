# Q. FOR A GIVEN STRING, IF IT IS A VALID PALINDROME THEN RETURN TRUE, IF NOT THEN RETURN FALSE

# 2 POINTER APPROACH

str1 = input("enter string : ")
print(str1)
str1 = "".join(c.lower() for c in str1 if c.isalnum()) # CONVERTS ALL LETTERS TO LOWERCASE, REMOVES ALL SPACES, PUNCUATION ETC AND JOINS THE RESULT BACK INTO A CLEANED STRING
n = len(str1)
j = n - 1
i = 0
a = True
while (i<=j):
    if str1[i] != str1[j]:
        a = False
        break
    i = i + 1
    j = j -1
     
print(a)