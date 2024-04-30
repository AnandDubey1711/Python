# Functionalities of random module
import random as rd

# To generate a random int value between 1 to 10
x = rd.randint(1,10)
print(x)

# To generate a random float value
y = rd.random()
print('{:.2f}'.format(y))


cards = [1,2,3,4,5,6,7,8,9,'Q','K','J','A']

rd.shuffle(cards)
print(cards)
