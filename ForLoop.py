# For loop : A statement which will execute its code of block a limited amount of time unlike while loop which can also run infinite times

# For loop which iterates over range of value starting from 0-10
import time

for i in range(10):
    print(i, end=" ")

# For loop which iterates over a string
for i in "String":
    print(i, end=" ")

# For loop here takes a range with a step value meaning every second value would be skipped
for i in range(50, 100,2):
    print(i)

# Creating a countdown using thread sleep method with the for loop
# Here the time.sleep ensures that there is a delay of 1 sec for each count in for loop whereas the step value makes sure that the count is in reverse
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year")

