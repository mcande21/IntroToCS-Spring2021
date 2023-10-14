# This program is going to ask the user for a range of numbers and add them all up
import random

print("1.")
start = float(input("what you wanna use as a start number?"))
stop = float(input("what you wann ause as a stop number?"))
i = start
sum = 0
while i < stop:
    sum += start
    start += 1
    i += 1
print(sum)

# This while loop will print out a countdown like a lift off
print("-----------------------------")

print("2.")
i = 0
while i <= 11:
    if i == 0:
       print("T-minus")
    elif i <= 10:
        print(i)
    else:
        print("Lift off!!")
    i += 1

print("----------------------")

# This while loop will add up all even numbers between 0 and 500
print("3.")
i = 0
while i <= 250:
    sum = i * (i + 1)
    i += 1
print("All the even numbers between 0 and 500 added together equal", sum)

print("----------------------")

# This while loop will allow the user to guess a randomly generated number
print("4.")
i = 0
count = 0
while i < 1:
    number = random.randrange(101)
    guess = float(input("Alright whats your guess?"))
    if guess == number:
        i += 1
    else:
        count += 1
print("It took the user", count, "times to guess the generated number.")

print("------------------------------------")

# This while loop will have a 74% chance printing hello and a 25% chance finishing
print("5.")
i = 0
count = 0
prob = .75
while i < 1:
    p = random.random()
    if p < prob:
        print("hello")
        count += 1
    else:
        i += 1
print("The computer said hello", count, "times.")