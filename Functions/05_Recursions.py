"""
RECURSION:-

- IN FUNCTIONS, WE HAVE A CALLING STATEMENT AFTER DEFINING THE FUNCTION 
- IN RECURSIONS, THE CALLING STATEMENT IS INSIDE THE FUNCTION I.E. IT CALLS ITSELF

- DEFINATION : WHEN A FUNCTION CALLS ITSELF REPEATEDLY IS CALLED RECURSION (SIMILAR TO LOOPS)

- ALL WORK DONE BY LOOPS CAN BE DONE BY RECURSION AND VICE VERSA
- IN MAX CASES WE PREFER LOOPS BUT IN SOME SPECIFIC CASES WE USE RECURSIONS

- IF WE RETURN NO VALUE, IT MEANS THAT WE ARE RETURNING CONTROL OF THE FUNCTION
- JUST LIKE WE HAVE END CONDITON IN LOOPS, WE HAVE BASE CASE IN RECURSION

- CALL STACK : DATA STRUCTURE THAT KEEPS TRACK OF SEQUENCE OF FUNCTION CALLS
- PROGRAM FLOW WITH RECURSIONS : 
        1). CALL FUNCTION AND STACK BUILD-UP UNTIL REACHES BASE CASE
        2). FUNCTION CALLS BEGIN TO RETURN THEIR COMMANDS IN REVERSE, FROM BASE CASE TO FIRST CASE
        3). AS EACH FUNCTION CALL COMPLETES AND RETURNS, IT IS REMOVED (STACK UNWINDING) 
        4). PROGRAM ENDS WHEN INTIAL FUNCTION CALL FINISHES ITS EXECUTION
"""
print("\n")

# Q1. WAP TO PRINT NUMBERS FROM N TO 1 USING RECURSIONS

n = int(input("enter n = "))                            # USER INPUT
def show(n):                                            # DEFINE FUNCTION
    if(n==0):                                           # BASE CASE
        return  0                                       # NO NEED TO RETURN ANYTHING
    print(n)                                            # COMMAND
    show(n-1)                                           # "RUN FUNCTION AGAIN" WITH UPDATED VALUE OF N

show(n)                                                 # CALL THE WHOLE FUNCTION 
print("\n")

# Q2. WAP TO PRINT FACTORIAL OF N

def fact(n):                                            # DEFINE FUNCTION
    if (n == 1 or n == 0):                              # BASE CASE
        return 1                                        # 1 AS 1! = 1
    return fact(n-1) * n                                # RETURN FINAL VALUE OF N! TO FUNCTION AFTER RECURSION

print(f"Factorial of {n} :",fact(n))                    # FUNCTION CALL AND PRINT
print("\n")

# Q3. WAP TO CALCULATE SUM OF FIRST N NUMBERS

def sum(n):                                             # DEFINE FUNCTION
    if (n == 0):                                        # BASE CASE
        return 0                                        # NO NEED TO RETURN ANYTHING
    return sum(n-1) + n                                 # RETURN FINAL VALUE OF N! TO FUNCTION AFTER RECURSION

print(f"Sum of all number till {n} :",sum(n))           # FUNCTION CALL AND PRINT
print("\n")

# Q4. WAP TO PRINT ALL ELEMENTS IN A LIST USING RECURSION

list1 = ["krish","hiyu","vero","suhaan","kashish"]      # CREATE LIST
def printall(list1,index=0):                            # DEFINE FUNCTION WITH LIST1 AND INDEX AS PARAMETER
    if (index == len(list1)):                           # BASE CASE
        return                                          # NO NEED TO RETURN ANYTHING
    print(list1[index])                                 # PRINT ELEMENT FROM 0 TO LEN(LIST1)
    printall(list1,index + 1)                           # "RUN FUNCTION AGAIN" WITH UPDATED VALUE OF INDEX

printall(list1)