# Python is general purpose high level programming language which focusses on creating a user friendly syntax for programming purposes
# It works on the concept of indentation which is easy to understand and helps in readability
# It is an interpreted language which means each line is read one after the another instead of compiling the whole of the program at once.
# It was created back in the 1990s 
# Python is one of the most popular programming lanugage around the globe owing to facts such as it high level of versatality and libraries.
# Like always I will start the coding by writing the globally accepted paradigm which is printing the Hello World

print("Hello World")
# Python does not requires any terminator and print is used to print the data
# There are various data types in python as well which helps in carrying out various operations
# Number, String, Boolean, Float, 

name = "Anand" # String
# Another way is to assign the string with the data type while initializing the variable
name: str = "Anand"

age = 23 # Integer
age: int = 23

isPass = True #boolean
isPass : bool = False

percentage = 85.34 # float
percentage: float = 85.23

grade = 'A' # String as well as there is not any separate type of the Character type


# To check the type of a variable in Python type method is used
print(type(name))  #<class 'str'>
print(type(age))  # <class 'int'>
print(type(isPass)) # <class 'bool'>
print(type(percentage)) # <class 'float'>

# Printing the values together
print("My name is",name,"and my age is",age,". My grade is",grade,"and my pass status is",isPass,"with my percentage being",percentage)

# Now we will look into multiple assignment which allows us to assign variables at once instead assigning one by one

myName, myAge, myGrade = "Anand",23,'A'
# There is another method to assign multiple variabes with a single value
math, english, science = 45,34,34
print(myName, myAge, myGrade)
print(math,english,science)
