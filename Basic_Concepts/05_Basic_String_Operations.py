"""1.CONCATENATION"""
str1 = "KRISH"
str2 = "LONGWANI"
print(str1 + " " + str2) # krishlongwani

"""2.LEN(STR)"""
print(len(str1)) # 5, as length of krish is 5

"""3.INDEXING = EACH CHAR IN STR HAS AN INDEX STARTING FROM 0 TO LAST CHAR
     HELPS IN ACCESSING CHAR, BUT WE CANT CHANGE IT USING INDEXING"""

print(str1[0]) # K, AS IT IS IN THE 0TH INDEX

"""4.SLICING = ACCESSING COLLECTIVE PARTS OF A STRING
    str[start_idx : ending_idx], but end index is not involved"""
print(str1[1 : 4])  # KRISH, 1ST INDEX IS K AND 4TH INDEX MEANS H

"""5.NEGATIVE SLICING = LAST CHAR HAS INDEX -1 AND THEN GOES ON"""
print(str1[-4 : -1])    # RIS, AS -4TH INDEX IS R AND -1TH INDEX IS E

# INCASE WE FORGET WRITING INDEX NUMBER, " " AT START_INX = 0TH INDEX AND " " AT END_INDEX = LEN(STR)
print(str1[ : 4])   # KRIS, " " MEANS 0TH INDEX
print(str1[-4 : ])  # RISH, " " MEANS LEN(STR)

"""6.ENDSWITH() = RETURNS TRUE IF STR END WITH ENTERED SUBSTR"""
print(str1.endswith("SH"))  # TRUE AS STR1 ENDS WITH SH

"""7.LOWER() = MAKES FIRST CHARACTER CAPITAL"""
print(str2.lower())    # MAKES LONGWANI TO longwani

"""8.CAPITALIZE() = MAKES FIRST CHARACTER CAPITAL"""
print(str2.capitalize())    # MAKES longwani TO Longwani

"""9.UPPER() = MAKES ALL CHARACTERS CAPITAL"""
print(str2.upper())    # MAKES Longwani TO LONGWANI

"""10.REPLACE() = REPLACES ALL OCCURENCES OF OLD TO KNEW"""
print(str2.replace("I","i"))    # MAKES LONGWANI to LONGWANi

"""11.FIND() = RETURNS INDEX OF 1ST OCCURENCE"""
print(str1.find("S"))   # RETURNS 3, AS INDEX OF S IS 3

"""12.COUNT() = COUNTS THE OCCURENCE OF SUBSTR IN STR"""
print(str1.count("SH")) # RETURNS 1, AS SH OCCURS ONCE IN KRISH

# Q1. INPUT FIRST NAME AND PRINT LENGTH
firstname = input("enter your name = ")     #kri$h
print(len(firstname))

# Q2. FIND OCCURENCE OF $ IN A STRING
print(firstname.find("$"))