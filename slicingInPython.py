# slicing: It is the concept of creating a substring elements from another string indexing[] or slice() is used
# It has three indexes which are start, stop and step to skip 

name = "Iron Man"

# The name variable sliced into another string named firstName where the index from 0 to 4 is sliced to provide firstName a value
firstName = name[0:4]
# Another way to write this is by just providing the ending index
firstName = name[:4] # Does the same work 
lastName = name[4:len(name)]

print(firstName, lastName)

# Step : It is optional field in which we can skip over a given number of index based on the user's requirements
funkyName = name[0:len(name):2]
print(funkyName)

# To reverse a string we can just provide the step index as -1
reverseName = name[::-1]
print(reverseName)

#Slice function
# Lets take a website for this 
