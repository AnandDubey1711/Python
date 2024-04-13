# Function: A block of code which is executed only when it is called and helps in removing the repetition in code
# The function is created by using the def keyword to declare the function

def hello():
    print("Hello World")

# Calling the function
hello()

# Function can also be provided with params which can be used to carry out various operations
# Summation of two values using a function

def summation(a,b):
    sum = a+b
    print(sum)


summation(23,23)

# In functions return statement are also used to return values/objects back to the caller
# These values/objects are known as function's return value

def multiply(num1, num2):
    result = num1*num2
    return result

print(multiply(34,23))



