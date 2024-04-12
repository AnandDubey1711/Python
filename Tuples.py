# Tuples: Collection which is ordered and unchangeable used to group together related data
# Tuples are immutable and cannot be tampered with once they are created by the user

student = (21,"Bro","Male")
print(student)
# Prints the output as class tuples
print(type(student))

# Printing all the elements of tuples using a for loop
for items in student:
    print(items)

# Using conditionals with tuples
if "Bro" in student:
    print("Bro Code does exists")