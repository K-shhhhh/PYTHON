# Q. IMAGINE CLIMBING A STAIRCASE OF N STAIRS. WE CAN TAKE ONLY 1 OR 2 STEPS AT A TIME.VHOW MANY WAYS CAN WE REACH THE TOP I.E. N STEPS.
# LOGIC : IF WE LOOK AT ANSWERS FOR EACH VALUE OF N = [1,2,3,45] WE SEE THE ANSWERS AS [1,2,3,5,8]. 
#         CLEARLY WE CAN SEE IN [1,2,3,5,8] THAT THIS IS A FIB SERIES. THEREFORE WE WILL USE FIB LOGIC OF A(ORIGINAL) = FIRST ELEMENT[1], 
#         B(ORIGINAL) = SECOND ELEMENT[2] AND  A(NEW) = B(OLD), B(NEW) = A + B 

n = int(input("ENTER NUMBER OF STEPS : "))
if n == 1:                                          # FIRST ELEMENT = 1
    print("NUMBER OF STEPS : 1") 
    exit()
if n == 2 :                                         # SECOND ELEMENT = 2
    print("NUMBER OF STEPS : 2")
    exit()
a = 1
b = 2
for i in range(3,n+1):                              # USE N+1 AS IT WILL INCLUDE N
    a,b=b,a+b                                       # FIB LOGIC
print(f"NUMBER OF WAYS TO REACH N STEPS : {b}")