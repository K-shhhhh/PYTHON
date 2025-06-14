"""
FUNCTIONS : 
- BLOCK OF STATEMENTS THAT PERFORM A SPECIFIC TASK
- UNLIKE LOOPS, FUNCTION CAN PERFORM SAME ACTIONS 1000'S OF TIMES
- WHEN THE CODE IS BEING REPEATED AGAIN AND AGAIN, WE CONVERT IT TO A FUNCTION
- IN STRING FUNCTIONS, WE DONT NEED TO RETURN VALUE AS NO PARAMETER IS USED, JUST CALL THE FUNCTION
- FUNCTION DEFINANTION : PROCESS OF DEFINING FUNCTIONS

- PARAMETERS : THE VARIABLES USED INSIDE A FUNCTION
- FUNCTION CALL : USING THE FUNCTION IN OUR PRIMARY CODE
- ARGUEMENTS : ACTUAL VALUES THAT USER INPUTS IN A FUNCTION

- SYNTAX:
    DEF FUNCTION_NAME(PARAMETER1,PARAMETER2,...):       # DEFINES FUNCTION
        STATMENTS AND WORK
        RETURN VAL                                      # THIS VALUE CAN BE ANYTHING

    FUNCTION_NAME(ARGUEMENT1,ARGUEMENT2,....)           # CALLS FUNCTIONS

- TYPES OF FUNCTIONS IN PY:
    1). BUILT IN FUNCTIONS = PRINT(), LEN(), TYPE(), RANGE(), INPUT()
    2). USER DEFINED FUNCTIONS = USER CREATES IT AS PER REQUIREMENT

DEFAULT PAPAMETERS: 
GIVING DEFAULT VALUE TO PARAMETER, WHICH IS USED WHEN NO ARGUEMENT IS PASSED

TO USE A VARIABLE IN LOOP IN FUNCTION, INITIALIZE IT INSIDE THE FUNCTION
"""

# Q1. WRITE A BASIC INT PROGRAM USING FUNCTIONS
a = int(input("enter number = "))
b = int(input("enter number = "))
def add(a,b):                                 # DEFINES FUNCTION
    sum = a + b                               # OPERATION
    return sum                                # RETURNS THE OPERATION TO FUNCTION

print("sum =",add(a,b),"\n")                  # PRINT ANSWER USING FUNCTION CALL

c = int(input("enter number = "))
d = int(input("enter number = "))

print("sum2 =",add(c,d),"\n")        # USING FUNCTION, WE AVOIDED REPEATING STATEMENTS


# Q2. WRITE A BASIC STR PROGRAM USING FUNCTIONS
def hello():                                  # DEFINE FUNCTION
    print("hello")                            # OPERATION

hello()                                       # FUNCTION CALL
print("\n")

# Q3. MAKE A FUNCTION THAT GIVES AVERAGE OF 3 NUMBERS
a = int(input("enter number = "))
b = int(input("enter number = "))
c = int(input("enter number = "))
def avg(a,b,c):                               # DEFINE FUNCTION
    x = (a+b+c)/3                             # OPERATION
    return x                                  # RETURNS OPERATION TO FUNCTION

print("average = ",avg(a,b,c),"\n")           # PRINT ANSWER USING FUNCTION CALL

# Q4. PRINT MULTIPLICATION OF 2 INT WITHOUT USING ARGUEMENTS IN FUNCTION CALL
sub1 = int(input("enter number = "))
sub2 = int(input("enter number = "))
def multi(a=sub1,b=sub2):                      # USING DEFAULT VALUES 
    pro = a * b                               
    return pro                                

print("product =",multi(),"\n")                # PRINT ANSWER WITHOUT ARGUEMENTS

# Q5. PRINT THE LENGTH OF A LIST 
list1 = ["krish","varnika","hiyu"]
def listlen(list1):                            # DEFINE FUNCTION                            
    length = len(list1)                        # OPERATION
    return length                              # RETURN OPERATION TO FUNCTION
print("length of list =",listlen(list1),"\n")

# Q6. PRINT ELEMENTS OF LIST1 IN SAME LINE 
def sameline(list1):                           # DEFINE FUNCTION 
    for element in list1:                      # OPERATION
        print(element, end = " ")              # NO NEED TO RETURN AS IT IS STRINGS

sameline(list1)
print("\n")

# Q7. FIND FACTORIAL OF N
n = int(input("enter number = "))
def calc_fact(n):                              # DEFINE FUNCTION
    fact  = 1                                  # INITIALIZE VARIABLE IN FUNCTION
    for i in range(1,n+1):                     # OPERATION      
        fact = fact * i
    return fact                                # RETURN OPERATION TO FUNCTION
print("factorial =",calc_fact(n),"\n") 

# Q8. CONVERT SGD TO INR
n = int(input("enter amount in SGD = "))
def convert(n):
    i = n * 66.49
    return i 
print(n,"SGD =",convert(n),"INR","\n")  

# Q9. PRINT EVEN OR ODD NUMBERS USING FUNCTIONS
n = int(input("enter number = "))
def oddeven(n):
    if (n%2==0):
        return "even"
    else:
        return "odd"
print("the number is =",oddeven(n))