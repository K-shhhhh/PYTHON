"""
TRY AND EXCEPT 

- Try and except statements are used for exception handling, which allows a program to gracefully manage errors that occur during execution instead of crashing.
- Necessary to use in real life projects and assignments to make sure unvalid user input/programmer mistake stops the program to run
- Generally works on runtime error types
- Basic Syntax : 
    try:
        # risky code
    except ErrorType:
        # what to do if error comes
    except ErrorType2:
        # what to do if error2 comes

- Additional Block in TRY_EXCEPT:

    1). Else : executed only if no exception occurs within the try block and it should run when the try block completes successfully.
    
    2). Finally : always executed (doesnt matter if code goes to TRY block or an EXCPET or ELSE block)

- Summary :-

| Term      | What It Does                       |
| --------- | ---------------------------------- |
| `try`     | Runs risky code                    |
| `except`  | Handles error if it occurs         |
| `else`    | Runs only if no error              |
| `finally` | Runs always, even if there's error |

"""

# Q1. USE TRY AND EXCEPT TO NULLYFY VALUE ERROR

try:
    num = int("hello")
except ValueError:
    print("That's not a number")

# Q2. USE TRY AND EXCEPT TO NULLYFY ZERRODIVISIONERROR

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero.")

# Q3. USE TRY AND EXCEPT TO NULLYFY MULTIPLE ERRORS

try:
    x = int(6)
    y = 10 / 0
except ValueError:                      # This is skipped as there is no value error, but if it were, only this block would have run                      
    print("Invalid number format.")        
except ZeroDivisionError:
    print("Division by zero.")

# Q4. USE ELSE BLOCK WITH TRY EXCEPT STATEMENT

try:
    x = 10 / 2
except ZeroDivisionError:               # Skipped as no error
    print("Division error.")
else:                                   # Executed
    print("Success! Result is:", x)

# Q5. USE FINALLY BLOCK WITH TRY EXCEPT STATEMENT

try:
    x = "krish"
except ValueError:                      # Skipped as no error
    print("Division error.")
else:                                   # Executed
    print("Success!")
finally:                                # Executed no matter what block runs before it 
    print("Execution completed.")
    




