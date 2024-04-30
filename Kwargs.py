# *kwargs: It is an argument which is used to pack to arguments into a dictionary
# Useful so that a function can accpet a varying amount of keyword argument

def hello(**kwargs):
    # Accessing the value with a dictionary by providing the value 
    print("Hello "+kwargs['first']+" "+kwargs['middle']+" " + kwargs['last'])
    # Another way is by using the key, value combination nature of kwargs
    for key,value in kwargs.items():
        print(value) # Prints the values [bro, dude, code]
        print(key) # print the key [first, second, last]

hello(first='Bro', middle='Dude' ,last='code')