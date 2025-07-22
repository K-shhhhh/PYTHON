# Calculator With Error Handling

a = int(input("\nenter no. 1 : "))
b = int(input("enter no. 2 : "))

try:
    a = float(a)
    a = float(a)
except ValueError:
    print("INVALID INPUT, PLEASE ENTER NUMBERS")
    exit()

print("\npress 1 for +")
print("press 2 for -")
print("press 3 for *")
print("press 4 for /")
choice = int(input("enter your choice of opreation : "))

if choice == 1:
    print(a+b)
if choice == 2:
    print(a-b)
if choice == 3:
    print(a*b)
if choice == 4:
    try:
        c = a/b
        print(c)
    except ZeroDivisionError:
        print("\nCant divide by zero!")
    else:
        print("\nperformed division on valid input!")
    finally:
        print("\nCode Executed.")
