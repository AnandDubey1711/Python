# In python we can take input from the user using the input function
# This allows one to take input from the user and use the date for further operations

# Takes string as an input
name = str(input("Enter your name: "))
# Takes integer as an input
age = int(input("Enter your age: "))
# Takes string as an input from the user
gender = str(input("Enter your gender M/F: "))
# Takes a float as an input
height = float(input("Enter your height: "))

# We can also concatenate these strings as well by converting the other variables into string 
print(name.capitalize(), age, gender, height)
