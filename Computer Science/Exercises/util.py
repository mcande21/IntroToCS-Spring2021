# file of helpful function
import pygame

def f2c(f):
    """
    Given temp in fahrenheit, calculate the temp in degrees celsius
    :param f: (float) temperature in fahrenheit
    :return: (float) temperature in celsius
    """
    c = 5 /9 * (f - 32)
    # return the answer
    return c

def circ_area(Radius):
    """
    This program will calculate the area of a circle
     givin the radius from the user
    :param Radius: (float) radius in inches
    :return: (float) area of circle
    """
    A = 3.14159 * (Radius ** 2)
    return A

def cone_volume(r, h):
    """
    This program will calculate the volume of a cone given the radius and height from the user
    :param r: (float) radius of circle
    :param h: (float) height of cone
    :return: (float) volume of the cone
    """
    V = 3.14159 * (r ** 2) * (h / 3)
    return V

def pop_est(y):
    """
    This program will estimate the populating in however many years the user wants
    :param y: (float) years
    :return: total population in (y) amount of years
    """
    # first calculation seconds from years
    D = y * 365
    H = D * 24
    M = H * 60
    S = M * 60
    # next calculating number of humans from seconds
    Pop = 328000000 + (S / 8) - (S / 12) + (S / 33)
    return Pop

def reverse(s):
    """
    Reverse the contents of a string
    :param s: the string to reverse
    :return: the characters from s in reverse order
    """
    # make an empty string to build up the reversed characters
    rev = ""
    # loop through all the characters
    for ch in s:
        # insert this character at the beginning of rev
        rev = ch + rev
    return rev