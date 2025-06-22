"""
LISTS:
 
BUILT IN DATA TYPE THAT STORES A SET OF VALUES
CAN STORE VALUES OF DIFFERENT DATA TYPE I.E. INT, FLOAT, STR 
EXAMPLE : marks = [54,56,78]        
          student = ["krish","87","Surat"]
          student[0] = "Arjun"
INDEXING AND SLICING IS ALLOWED IN LISTS WITH END INDEX NOT INCLUDED
LISTS ARE MUTABLE / CHANGEABLE IN PYTHON BUT STRINGS ARE NOT
LISTS ALSO HAVE FUNCTIONS CALLED LIST METHODS
EXAMPLES : APPEND(), SORT(), SORT(REVERSE=TRUE), REVERSE(), INSERT(INDEX, ELEMENT)
           REMOVE(), POP()
IN LISTS, USE METHOD FIRST THEN PRINT BUT IN STRINGS WE CAN USE FUNCTION AND PRINT TOGETHER
"""

# Q1. MAKE A LIST OF NAME, MARKS, CITY; PRINT IT; ACCESS ITS 3rd INDEX; PRINT ITS LENGTH
marks = ["krish", 96, "surat", "hiyu", 89, "surat"] 
print(marks)
print(marks[3])
print(len(marks))
print("\n")

# Q2. CHANGE THE NAME HIYU TO HEADACHE IN THE LIST
marks[3] = "HEADACHE"
print(marks)
print("\n")

# Q3. USE APPEND, SORT, REVERSE SORT, REVERSE, INSERT, REMOVE, POP METHODS IN A LIST
list = [10, 40, 20, 50, 30]
list.append(60)                     # Add 60 at the end
print(list,"\n")

list.reverse()                      # Reverse the order of list
print(list,"\n")

list.sort()                         # Sort list in ascending order
print(list,"\n")

list.sort(reverse=True)             # Sort list in descending order
print(list,"\n")         

list.insert(3, 70)                  # Insert 70 at index 3
print(list,"\n")

list.remove(70)                     # Remove element 70
print(list,"\n")

list.pop(5)                         # Remove element at index 5
print(list)
print("\n")

# Q4. TAKE 4 MOVIES FROM USER, MAKE A LIST AND PRINT IT
movie1 = input("ENTER MOVIE : ")
movie2 = input("ENTER MOVIE : ")
movie3 = input("ENTER MOVIE : ")
movie4 = input("ENTER MOVIE : ")
movies = []
movies.insert(0, movie1)
movies.insert(1, movie2)
movies.insert(2, movie3)
movies.insert(3, movie4)
print(movies,"\n")

# Q5. PRINT A LIST WITH USER INPUTS 
n = int(input("ENTER LENGTH OF LIST = "))
list1 = []
for ele in range(1, n+1):
    i = int(input("ENTER NUMBER = "))
    list1.append(i)
print(list1, "\n")

# Q6. CHECK IF A FIXED LIST CONTAINS PALINDROME OF ELEMENTS
list1 = ["krish", 5, 5, "KRish"]
if (list1[0] == list1[3]):
    if(list1[1] == list1[2]):
        print("PALINDROME","\n")
    else:
        print("NON PALINDROME","\n")
else:
    print("NON PALINDROME","\n")

