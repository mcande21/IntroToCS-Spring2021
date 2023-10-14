# this program will create a function that
# counts the number of digits in a number

def checkdigit(number):
    """
    This function will add all the digits together. Another way of checking data
    :param number: (int) the number to convert into a digit counter thing
    :return: (int) the number of digits of a given number
    """
    # keep track of the sum of digits
    sum = 0
    while number != 0:
        # grab the ones digit
        digit = number % 10
        # add digit to the sum
        sum = sum + digit ** 0
        # remove the ones digit
        number = number // 10

    return sum

print(checkdigit(8))
