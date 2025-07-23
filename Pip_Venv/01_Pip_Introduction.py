"""
PIP ( Python's package installer )

- It helps install libraries made by others like:-
    1). Numpy 
    2). Pandas etc
- These libraries help do complex things easily like:-
    1). Math
    2). File handling
    3). Web development
    4). AI etc

- Syntax to Pip to install user-library:-
    
    Pip3 install library_name (Type this in terminal only)

- After installing, just import File_name in your code and use its functions

- To see the list of packages intalled :-
    
    Pip3 list (Type this in terminal only)
"""

# Q1. USING PIP, PRINT 3 EMOJIES

"""
In terminal - Pip3 install emoji
"""

import emoji

print(emoji.emojize("I Love Python:snake:"))                    # EMOJIZE() IS THE FUNCTION WE USE FROM EMOJI LIBRARY
print(emoji.emojize("I Love my House:house:"))
print(emoji.emojize("I Love Babies:baby:\n"))

# Q2, USING PIP, PRINT A PROGRAMMING JOKE

"""
In terminal - Pip3 install pyjokes
"""

import pyjokes                                                  

joke = pyjokes.get_joke()                                       # GET_JOKE() IS THE FUNCTION WE USE FROM PYJOKES LIBRARY                                    
print("Joke :",joke)

# Q3, USING PIP, PRINT A KANYE WEST QUOTE FROM AN HTTPS SITE

"""
In terminal - Pip3 install requests
"""

import requests

response = requests.get("https://api.kanye.rest")               # GET() IS THE FUNCTION WE USE FROM REQUESTS LIBRARY
quote = response.json()

print("\nKanye says:", quote['quote'])
