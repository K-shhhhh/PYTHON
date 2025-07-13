# Q. CALCULATE THE NTH TERM IN FIBONACCI SERIES

n = int(input("Enter the nth number you want in the fibonacci series : "))
if n == 0:
    print(f"{n}th term = {n}")
a = 0
b = 1
for i in range (2,n+1):
    a , b = b , a + b               # MAIN LINE : NEW A BECOMES OLD B, NEW B BECOMES A + B
if n > 0:
    print(f"{n}th term = {b}")
else:
    print(f"{n}th term = {a}")