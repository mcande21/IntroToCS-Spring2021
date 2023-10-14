# This program will determine if a number by the user is prime or not.

def prime(n):
    """
    This function will create a for loop that determines if a number is prime or not
    :param n: This is the int number in discussion
    :return: Will return either a boolean True or False value. True if prime False if not prime
    """
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True
# MAIN PROGRAM
n = int(input("Alright what number you want me to test? "))

if prime(n):
    print("Hey! your number", n, " is prime!")
if not prime(n):
    print("Sorry pal your number", n, "ain't Prime")

