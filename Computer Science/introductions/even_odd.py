# This program will just tell me if a number is even or odd
import random

y = int(input("aight give me a number: "))
if y % 2 == 0:
    print("yo nummba is even")
else:
    print("yo numba is odd")

# now I am picking 30 random numbers and listing if they are even or odd
for i in range(31):
    number = random.randrange(31)
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
