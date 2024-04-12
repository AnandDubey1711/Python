# Loop Control : This is used to handle loops execution where there is a tweaking required from the normal sequence
# Break : Used to terminate the loop entirely
# Continue : Skips to the next iteration of the loop
# Pass: does nothing acts as a placeholder

# Lets take an example for the break control statement
phone = "344-2353-6788"

for i in phone:
    if i=='-':
        break
    print(i, end='')

print()
# Using continue which skips the iteration instead of breaking out of the loop like the break statement
for i in phone:
    if i=='-':
        continue
    
    print(i, end='')

print()

# Pass which acts as a placeholder and really does nothing
for i in phone:
    if i=='-':
        pass
    else:
        print(i, end='')