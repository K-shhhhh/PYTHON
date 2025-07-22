# Q. GIVEN TWO STRINGS STR1 AND STR2, PRINT TRUE IF STR1 IS AN ANAGRAM OF STR2, AND FALSE OTHERWISE.

str1 = input("enter 1st string : ")
str2 = input("enter 2nd string : ")
print(str1," ",str2)

if sorted(str1) == sorted(str2):
    print(True)
else:
    print(False)