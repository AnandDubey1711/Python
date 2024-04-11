# Type casting is the concept of changing the type of a variable to another in the programming
x = 1 #int
y = 2.0 # float
z = "1" # string

# To convert into an integer we can use type casting
# This converts the y variable into an integer
y = int(y)
print(type(y), y)
 
# Converting string to an integer
z = int(z)
print(type(z),z)

# Converting an integer to float
x = float(x)
print(type(x), x)
 
# Converting an integer and float to string
x = str(x)
print("The x is a", type(x))

y = str(y)
print("The y is a",type(y))

# What if the string is not an integer lets check
str2 = "anand"
# This would generate an error for the literal
# str2 = int(str2)
print(str2)
