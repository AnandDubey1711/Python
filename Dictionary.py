# Dictionary : A dictionary is a changeable, unordered collection of unique key:value pairs 
# It is fast because they use hashing which allows one to access the value in quick manner 

capitals = {
    'USA':'Washington DC',
    'India':'New Delhi',
    'China':'Beijing',
    'Russia':'Moscow'
}

print(capitals)
# To get the key in the dictionary
print(capitals.keys())
# TO get the value from the dictionary
print(capitals.values())

# Accessing the values using the key
print(capitals['China'])
print(capitals.get('Russia'))

# Printing all elements of dictionary in the form of a key-value pair
print(capitals.items())


# Printing the entire dictionaries
for key,value in capitals.items():
    print(key,value)

# As dictionary are mutable they can updated to add new key value pair or to add new values
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"})
print(capitals.items())

# To remove a key-value pair from the dictionary
capitals.pop('China')
print(capitals.items())

# To clear the dictionary elements
capitals.clear()