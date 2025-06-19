# HERE IS THE CODE OF A SIMPLE CALCULATOR

class Calculator:

    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def multi(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b == 0:
            return "Cannot divide by Zero!"
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    
def main():
    cal = Calculator()
    print("\nWELCOME TO THE OOPS CALCULATOR!\nTYPE 'EXIT' TO QUIT")

    while True:
        n1 = input("ENTER FIRST NUMBER : ")
        if n1.lower() == 'exit':
            print("EXITING OOPS CALCULATOR, THANK YOU!")
            break
        n2 = input("ENTER SECOND NUMBER : ")
        if n2.lower() == 'exit':
            print("EXITING OOPS CALCULATOR, THANK YOU!")
            break
        
        try:
            n1 = float(n1)
            n2 = float(n2)
        except ValueError:
            print("INVALID INPUT, PLEASE ENTER NUMBERS")

        print("\nCHOOSE OPERATION : ")
        print("1. + ADDITION")
        print("2. - SUBTRACTION")
        print("3. * MULTIPLICATION")
        print("4. / DIVISION")
        print("5. ** POWER")

        choose = input("ENTER CHOICE (1/2/3/4/5) : ")

        if choose == '1':
            print("\nRESULT :", cal.add(n1,n2))
            print("THANK YOU.")
            break
        elif choose == '2':
            print("\nRESULT :", cal.sub(n1,n2))
            print("THANK YOU.")
            break
        elif choose == '3':
            print("\nRESULT :", cal.multi(n1,n2))
            print("THANK YOU.")
            break
        elif choose == '4':
            print("\nRESULT :", cal.div(n1,n2))
            print("THANK YOU.")
            break
        elif choose == '5':
            print("\nRESULT :", cal.power(n1,n2))
            print("THANK YOU.")
            break
        else:
            print("\nINVALID CHOICE.")
            print("THANK YOU.")

        
main()

        
    