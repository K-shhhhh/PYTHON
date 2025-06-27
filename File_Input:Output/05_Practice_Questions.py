# Q1. CREATE A NEW FILE "Practice.txt" USING PYTHON. ADD SOME DATA IN IT.
with open("Practice.txt","w+") as f:
    f.write("Hi everyone\nwe are learning file I/O\nusing Java\nI like programming in Java")
    

# Q2. WAP TO REPLACE ALL OCCURENCE OF "JAVA" WITH "PYTHON" 
with open("Practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("Practice.txt","w") as f:
    f.write(new_data)

# Q3. SEARCH IF THE WORD "LEARNING" EXISTS IN THE FILE OR NOT
def check_for_word():
    word = "learning"
    with open("Practice.txt","r") as f: 
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("Not Found")

check_for_word()

# Q4. FIND THE EXACT LINE NUMBER AT WHICH THE WORD "FILE" OCCCURS, PRINT -1 IF WORD NOT FOUND
def check_for_line():
    WORD = "file"
    DATA = True
    line_no = 1
    with open("Practice.txt","r") as f:
        while DATA:
            DATA = f.readline()
            if(WORD in DATA):
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()

# Q5. IN A FILE "NUMBERS.PY" CONTAINING NUMBERS SEPARATED BY COMMA, PRINT THE COUNT OF EVEN NUMBERS    
def check_even():
    Count = 0
    with open("Numbers.txt", "r") as f:
        DATA1 = f.read()
        print("File data:", DATA1)
        nums = DATA1.split(",")
        for i in nums:
            try:
                if int(i) % 2 == 0:
                    Count += 1
            except ValueError:
                continue  # skip any non-integer text
    return Count

print("Total even numbers:", check_even())




