# This for loop will ask the user for a start and stop
# number and add up all the value in between.
start = int(input("What do you want as a start number? "))
stop = int(input("What do you want as a stop number? "))
total = 0
for i in range(start, stop):
    total = total + i
print("The sum of your numbers is", total)

print("---------------------------------")

# this for loop will print out a ocuntdown from t-minus 10 - 1 Liftoff
for i in range(0,12):
    if i == 0:
        print("T-minus")
    elif i == 11:
        print("Lift off!!")
    else:
        print(i)

print("-------------------------------")

# This for loop will add all numbers between 0 and 500 that are even

for i in range(501):
    if i == 250:
        sum = i * (i + 1)
    else:
        None
print("The sum of all even numbers between 0 and 500 is", sum)

print("----------------------------")

# This for loop will add up the rolls from ten dice roll
import random
dice = 0
for i in range(11):
    n = random.randrange(7)
    dice += n
print("The total from 10 dice rolls is", dice)