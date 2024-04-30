# Exception = Events detected during execution that interrupt the flow of a program 
# It helps in handling any kind of anomaly which could occur in program based on irrelevant input from the user's side as well
try:
    numerator = int(input("Enter a number to divide:"))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print("{:.2f}".format(result))