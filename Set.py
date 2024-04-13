# Set : A set is a collection which is unordered, unindexed. No duplicate values

utensils = {"Fork","Plates","Knife"}
dishes = {"Bowl","Plate","Cup"}
print(utensils)
print(dishes)
# To add an item to set
utensils.add("Napkin")

# To remove an item from the set
utensils.remove("Fork")

# To empty the set
# utensils.clear()

# Update to any particular element of the set
utensils.update(dishes)
# Another method
dinner_table = utensils.union(dishes)

print(dinner_table)

# To get the differences between two sets
print(utensils.difference(dishes))

# To get the common between two sets
print(utensils.intersection(dishes))

# Printing each item of the sets
for item in utensils:
    print(item)



