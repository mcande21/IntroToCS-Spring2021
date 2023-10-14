# This program will create a function that can
# calculate the number of passwords using characters

def num_passwords(chars, n):
    """
    This function will calculate the number of passwords a user can create
    :param chars: number of characters to choose from to create the password
    :param n: number of characters allowed in the password the user can create
    :return: the total number of passwords that can be created
    """
    # keep track of the sums of passwords
    sum = 0

    # keep track of the length of the passwords
    i = 1

    # loop to count from 1 up to 10
    while i <= n:
        # add your code here
        sum = sum + chars ** i
        # increment i
        i = i + 1

    return sum



