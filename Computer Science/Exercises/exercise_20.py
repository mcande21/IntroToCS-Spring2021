# this program will create a stair case function


def staircase(n):
    """
    This function will print a staircase fo "#" symbols
    :param n: This is an input by the user which describes the levels of stairs in the staircase
    :return: This will return a printed staircase of # symbols
    """
    x = 1
    for i in range(n):
        print(" " * (n - 1), "#" * x)
        n -= 1
        x += 1
    return None


staircase(int(input("n:")))