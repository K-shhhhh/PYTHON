# Q. FOR GIVEN INTERGERS X AND N, CALCULATE POW(X,N) WITH LEAST TIME COMPLEXITY

# RATHER THAN MULTIPLYING N NUMBER OF TIMES, WE USE A LOOP FOR BINARY FORM OF N

x = int(input("enter number : "))
n = int(input("enter power : "))

if  x == 0:
    print("answer = 0")
    exit()
if n == 0 or x == 0 or (x == -1 and n%2 == 0):
    print("answer = 1")
    exit()
    
if x == -1 and n % 2 != 0:
    print("answer = -1")
    exit()
    
binaryform = abs(n)
result = 1

if n < 0:
    x = 1/x

while (binaryform > 0):
    if (binaryform % 2 == 1):
        result = result * x
    x = x * x
    binaryform = binaryform // 2

print(f"answer = {result}")