# Keyword arguments: Arguments preceded by an identifier when we pass them to a function.
# The order of the arguments does not matter unlike positional argumnents
# Python knows the name of the arguments that out function receives

def hello(first, middle, last):
    print("Hello",first,middle,last)

hello(last="Bro", middle="it", first="Code")

hello("Bro","Code","Lit")