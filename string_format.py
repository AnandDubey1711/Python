# str.format() = optimal method that gives users more control when displaying output
animal = 'cow'
item = 'moon'

print("The {} jumped over the {}".format(animal, item))
# Another way is by using the f sign
print(f'The {animal} jumped over the {item}')

# To handle the order of assigment the braces can also be provided with the index accordingly
print("The {1} jumped over the {0}".format(animal, item))


# leaving the space for the input using the format method
text = "The {} jumped over the {}"
print(text.format(animal, item))

statement = "Youtube is a {} platform"
print(statement.format('streaming'))
print(statement.format('social media'))
