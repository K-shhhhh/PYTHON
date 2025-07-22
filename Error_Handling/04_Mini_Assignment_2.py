# Quiz Game with Error Handling

print("\nYou will be asked 3 questions. Choose the correct option number (1, 2, or 3).")

result = 0

print("\nQ1: What is the capital of France?\n1. Berlin   2. Paris   3. Rome")
try:
    ans1 = int(input("Enter Answer-1: "))
    if ans1 not in [1, 2, 3]:
        print("Invalid option selected!")
        exit()
    if ans1 == 2:
        result = result + 1
except ValueError:
    print("Please enter a number between 1 and 3 only.")
    exit()

# Question 2
print("\nQ2: Who was First President of the US?\n1. Abrahim Lincoln   2. George Washington  3. John F. Kennedy")
try:
    ans2 = int(input("Enter Answer-2: "))
    if ans2 not in [1, 2, 3]:
        print("Invalid option selected!")
        exit()
    if ans2 == 2:
        result = result + 1
except ValueError:
    print("Please enter a number between 1 and 3.")
    exit()

print("\nQ3: Who wrote 'Harry Potter'?\n1. Tolkien   2. Rowling   3. Shakespeare")
try:
    ans3 = int(input("Enter Answer-3: "))
    if ans3 not in [1, 2, 3]:
        print("Invalid option selected!")
        exit()
    if ans3 == 2:
        result = result + 1
except ValueError:
    print("Please enter a number between 1 and 3.")
    exit()

print(f"\nYour score = {result}/3")
if result == 3:
    print("Well done!")
elif result == 2:
    print("Almost there!")
elif result == 1:
    print("Keep going!")
else:
    print("Better luck next time")
