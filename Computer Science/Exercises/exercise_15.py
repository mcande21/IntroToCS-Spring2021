# This program will create and test a couple different max functions.

# This function will return the larger out of the 2 numbers given
def max2(x, y):
    """
    This function will return the max of the given numbers
    :param x: is a number provided by the user
    :param y: is simply another number provided by the user
    :return: returning the largest number
    """
    if y < x:
        number = x
    else:
        number = y
    return number

print(max2(4, 49))

# this function will return the largest number out of the three given
def max3(x, y, z):
    """
    This program will determine and return the highest number out of three variables
    :param x: a number given by user
    :param y: another nuber given by user
    :param z: yet another number given by user
    :return: the largest number out of the 3
    """
    if x < y:
        if z < y:
            number = y
        else:
            number = z
    else:
        number = x
    return number

print(max3(47, 5, 7))

# This function will pick out the middle number and return that
def middle(x, y, z):
    """
    This function will return the middle value of three number
    :param x: a number given by user
    :param y: another number given by user
    :param z: yet another number given by user
    :return: the middle number out of the three
    """
    if x < y < z:
        number = y
    elif z < y < x:
        number = y
    elif x < z < y:
        number = z
    elif y < z < x:
        number = z
    elif z < x < y:
        number = x
    elif y < x < z:
        number = x
    return number


print(middle(45, 30, 32))
