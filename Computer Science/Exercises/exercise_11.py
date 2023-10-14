# this program will define a function that draws triangles of stars
# This will be done using a while function

def draw_triangle(N):
    """
    This function will draw  vertical triangle with astrix's in a print setting
    :param N: This is the input value from the user describing the amount of max stars
    :return: this function will return a set of astrix's looking like a star
    """
    # this integer will let us keep count
    n = 1

    # Now to set up the function in a while function
    while n < N:
        print('*' * n)
        # now we have to increase the n value by 1
        n = n + 1
    # Now we have to set up another while function for to descend
    while n >= 0:
        # this will print it all out
        print('*' * n)
        # and now we continue to descend
        n = n - 1
    return None

draw_triangle(6)