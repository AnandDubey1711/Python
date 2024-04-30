# *args = parameter that will pack all arguments in a tuple useful so that a func can accept a varying amount of arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum+=i
    print(stuff)
    return sum

# We can provide as many input/ arguments based on our own requirements
# We can name the param based on requirements
print(add(1,2,45,23,23))

def sub(*val):
    sum = 0
    for i in val:
        sum-=i
    return sum

print(sub(12,1,234,23,2))

