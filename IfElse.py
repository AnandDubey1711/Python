# If statement = a block of code that will execute when a condition is true or not
# First we will take an input which would be checked by if to print output based on the condition which is met
# If else based looping is used to provide user with a condition which is executed when the first condition is not met
# Whereas the if-else ladder is used to check for various conditions within the loop 

age = int(input("What is your age? "))

# Now we will create an if-else ladder based condition to check based upon one's age that whether he is allowed to drive or not
# We already take the age as input from the user above
if age<18:
    print("You are not eligible for a driving license")
elif age>=18 and age<60:
    print("You are eligible for a driving license")
elif age>=60:
    print("You should drive but under supervision due to health related issues")
else:
    print("Invalid Input")

# This code above checks whether one is eligible for the license or not and generates the output based on it as well.


# Logical Operators with if else in python
# There are three main logical operators which are and, or & not operator which are used to compare and provide output based on the conditions given

# Lets take an example
temp = float(input("What is the temperature right now? "))
if temp>=0 and temp<=30:
    print("Weather is sunny today")
    print("Go outside")
elif temp<0 or temp >30:
    print("Weather is bay today")
    print("Stay inside")
else:
    print("Invalid input")


