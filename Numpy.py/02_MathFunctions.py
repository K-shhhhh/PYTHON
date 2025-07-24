# NUMPY HAS SOME BUILT IN MATH FUNCTIONS LIKE 

import numpy as np

arr = np.array([10, 20, 30, 40])

print(f"\n{arr}")

print("\nMinimum:", np.min(arr))                  
print("Maximum:", np.max(arr))                  
print("Sum:", np.sum(arr))                      
print("Mean:", np.mean(arr))                    
print("Standard Deviation:", np.std(arr),"\n")       

print("Sine:", np.sin(arr)) 
print("Cosine:", np.cos(arr),"\n")

print("Log base 10:", np.log10(arr))
print("Where >25:", np.where(arr > 25),"\n")   

print("Cumulative Sum:", np.cumsum(arr))
print("Cumulative Product:", np.cumprod(arr)) 