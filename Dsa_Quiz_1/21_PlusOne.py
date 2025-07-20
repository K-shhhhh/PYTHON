# Q. GIVEN A LARGE INTEGER REPRESENTED AS AN INTEGER ARRAY DIGITS, WHERE EACH DIGITS[I] IS THE ITH DIGIT OF THE INTEGER. 
#    THE DIGITS ARE ORDERED FROM MOST SIGNIFICANT TO LEAST SIGNIFICANT IN LEFT-TO-RIGHT ORDER. 
#    INCREMENT THE LARGE INTEGER BY ONE AND RETURN THE RESULTING ARRAY OF DIGITS.

n = int(input("enter size of number = "))
digits = []
for element in range(n):
    element = int(input(f"enter digit {element + 1} : "))
    digits.append(element)
print("\n",digits)

# LOGIC : SIMILAR TO PALINDROME TYPE/ TAKE OUT LEADING DIGITS AND MULTIPLY BY 10 

result = 0
i = 0
while n > i:
    result = (result * 10) + digits[i]
    i = i + 1

result = result + 1                                     # ANSWER, BUT IN INTEGER (1234)
digits2 = []
for j in str(result):                                   # CONVERT INTEGER TO STRING ("1234")
    digits2.append(int(j))                              # CONVERT STRING TO ARRAY OF INTEGERS ([1,2,3,4])

print("\n",digits2)                                     # ANSWER IN FORM OF INTEGERS INSIDE AN ARRAY ([1,2,3,4])
