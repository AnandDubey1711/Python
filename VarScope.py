# Scope = The region within which is a variable is recognized 
# A variable is only available from inside the region it is created.
# A global and locally scope versions of a variable can be created as well.

# Global variable
gl = 3

def sum():
    # Local variable
    a = 5
    return a*a

print(sum())