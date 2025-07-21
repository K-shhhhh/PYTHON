# Q. GIVEN AN INTEGER N, RETURN THE NUMBER OF PRIME NUMBERS THAT ARE STRICTLY LESS THAN N.
# LOGIC : ANY NON-PRIME NUMBER WILL HAVE AT LEAST ONE FACTOR LESS THAN OR EQUAL TO √N
# EXAMPLE : FOR N = 30, ONLY CHECK UP TO I = 5 (5 * 5 = 25 < 30, BUT 6 * 6 = 36 > 30).

n = int(input("ENTER VALUE OF N : "))
if n < 2:
    print(0)                                    # 0 AND 1 ARE NON - PRIMES
prime = [True] * n                              # MAKE A LIST OF SIZE N, WHERE "TRUE" = NUMBERS ARE PRIME
prime[0] = prime[1] = False                     # AS WE ALREADY KNOW, 0 AND 1 ARE NON - PRIMES, MAKE 0TH AND 1ST ELEMENT "FALSE" = NUMBERS ARE NON-PRIME              
i = 2
while i * i < n:                                # USING LOGIC OF ONLY CHECKING UNTIL FOR I UNTIL I*I<N
    if prime[i]:                                # IF I IS "TRUE" = PRIME NUMBER, SO WE WILL MARK ALL MULTIPLES OF I AS "FALSE" = NON-PRIME
        for j in range(i * i, n, i):            # ALL MULTIPLES OF I, LIKE IF I = 2, CHECKING FOR 4,6,8... 
            prime[j] = False                    # MARKING J AS "FALSE" = NON-PRIME AS IT IS DIVISIBLE BY I OR AS WE ASSUMED 4,6,8,10...
    i += 1                                      # INCREMENT I

result = sum(prime)                             # AS WE KNOW, "TRUE" = PRIME AND "FALSE" = NON-PRIME, SO WE COUNT ALL "TRUE" AND STORE IT 
print(result)                                   # PRINT NO. OF 