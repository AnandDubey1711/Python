# Nested Funcitons = Function calls inside other function calls 
# Innermost function calls are resolved first
# Returned value is used as argument for the next outer function 

# One such example where variou methods are nested within one another wherein the input is taken and output is returned within the single line
import math
print(round(abs(float(input("Enter a whole positive number: ")))))

print(round(abs(int(input("Enter a decimal number: ")))))