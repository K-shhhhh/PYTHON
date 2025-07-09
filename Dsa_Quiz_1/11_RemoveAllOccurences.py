# Q. FOR A GIVEN STRING S, REMOVE ALL OCCURENCES OF A SUBSTRING "PART" FROM IT

def remove_occurrences(s, part):                    # DEFINE FUNCTION                 
    while part in s:                                # LOOP RUNS UNTIL THERE IS NO "PART" LEFT IN S
        index = s.find(part)
        s = s[:index] + s[index + len(part):]       # MOST IMPORTANT LINE : S[:INDEX] = GETS TO INDEX BEFORE PART IS FOUND, S[INDEX+LEN(PART)] = GETS TO THE 
                                                    # REMAINING STRING AFTER REMOVING PART STRING AFTER REMOVING PART, "+" = COMBINE BOTH AFTER REMOVING PART FROM S
    return s

s = input("enter string : ")
part = input("enter part : ")
result = remove_occurrences(s, part)                # FUNCTION CALL
print(result)                                       # PRINT RESULT 
