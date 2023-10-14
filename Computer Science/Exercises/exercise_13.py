# this prigram will have a function that can estimate
# the population in however many years the user wants

# creating the function called estimate_population

def estimate_population(r, p, y):
    """
    This program will estimate the population in y amount of years with a
    population rate of r and an initial population p.
    :param r: initial population rate
    :param p: this is the initial population
    :param y: this is the amount of years
    :return: number of population in y years
    """
    # establishing a counting number
    t = 0
    while t < y:
        # calculation and updating the population
        p = p + (r * p)
        # increment counter
        t = t + 1

    return int(p)

# testing out the function
pop = estimate_population(0.0111, 7.5e9, 3)
print(pop)
