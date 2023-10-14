# this program will determine if a number is prime or not

def prime(n):
    """
    This function will determine if a number is prime or not
    :param n: number form the user, most likely an int
    :return: returning a side effect or a print value
    """
    for i in range(2, n):
        x = n % i
        if x == 0:
            print(i, "is a factor")
        elif i == n:
            print("you have a prime number baby")
    return print("There ya go pal")

numb = int(input("Alright what number do you want me to test? "))
answer = prime(numb)

print(answer)