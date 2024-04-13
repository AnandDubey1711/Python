# Index Operator: Gives access to a sequences elements (str, list, tuple)
name = 'Bro Code'

# To check if the variable is number or not
# print(name.isalnum())
print(name.lower())
count = 0

for i in range(0,len(name)):
    if name[i]=='o':
        count+=1
print(count)

# To capitalize the first letter of the name
if (name[0].islower()):
    name = name.capitalize()
# name = 'Bro Code'
print(name)

# If the name's first digit is alpha numeric than the name string is set to upper case
if (name[0].isalpha()):
    name = name.upper()
print(name)

# If the name's first digit is upper case then the output should be returned as true
if (name[0].isupper()):
    print(True)

# Indexing the string using the square brackets
first_name = name[0:3]
print(first_name)

