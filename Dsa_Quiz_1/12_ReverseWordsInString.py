# Q. REVERSE WORDS IN A STRING INLUDING SPACES ETC

s = input("Enter string: ")
n = len(s) - 1
word = ""
sentence = ""
while n >= 0:
    if s[n] != " ":                     # WHEN CHARACTER IS NOT SPACE
        word = s[n] + word
    else:
        if word != "":                  # CHECKING IF WORD ENDED
            sentence += word + " "      # ADD WORD TO NEW SENTENCE
            word = ""                   # RESET WORD TO NULL
    n -= 1

if word != "":                          # ENTERING THE FIRST WORD FROM ORIGINAL STRING MANUALLY AS IT IS STILL STORED IN VARIABLE "WORD"
    sentence += word

print(sentence.strip())                 # REMOVE TRIALING OR LEADING SPACES