# List = Used to store multiple items in a single variable
# It is denoted by square brackets
# It can store different types of data varying from integer, string, boolean, float etc.,

food = ['Apple','Pizza','Sphagetti']

# To access by index which starts from zero
print(food[0]) # return apple
print(food[1]) # returns pizza

# As lists are mutable we have the option to append or delete items as well
# To add an item at the end
food.append("Cake")
food.append("Pasta")
# To delete items at the end
food.pop()
food.pop()
# To insert an element at a given index
food.insert(0,"Ice-Cream")

# Sorting the list
food.sort()

# For loop iterating over the list
for items in food:
    print(items, end=' ')

