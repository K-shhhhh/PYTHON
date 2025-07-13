# Q. GIVEN AN ALPHANUMERIC STRING, PRINT SECOND LARGEST NUMBER, IF NO NUMBERS PRESENT, PRINT -1
# LOGIC : TAKE FIRST NUMBER AS LARGEST, COMPARE WITH NEXT NUMBER AND KEEP UPDATING UNTIL ALL NUMBERS ARE CHECKED


str1 = input("enter alphanumeric string : ")
largest = -1 
second_largest = -1
for character in str1:
    if character.isdigit():                         # IGNORES ALL NON-NUMERIC VALUES
        num_ele = int(character)                    # CONVERT NUMERIC VALUE INSIDE THE STRING TO AN INTEGER
        if num_ele > largest:
            second_largest = largest
            largest = num_ele
        elif largest > num_ele > second_largest:
            second_largest = num_ele
    
print(second_largest)