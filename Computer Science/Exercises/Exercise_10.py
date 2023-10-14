# This program is testing the functions I have created in util.py

# importing my util.py file
import util

# testing area of a circle
# Asking the user for a radius
Radius = float(input("Whats the radius of the circle you trying to figure out?(in.): "))

# Calling on the circ_area function
Area = util.circ_area(Radius)

# Printing out the data
print("With a radius of", Radius, "the area of your circle is:", round(Area, 2))

# testing volume of cone
# Asking the user for radius of circle and height of cone
r = float(input("What is the radius of the circle at the base of the cone? "))
v = float(input("What is the height of the cone you are working with? "))

# Calling on the cone_volume function
Volume = util.cone_volume(r,v)

# printing out the data
print("With a radius of", r, "and a height of", v,)
print("The volume of the cone will be:", round(Volume, 2))

# testng the population estimate
# Asking the user for years to estimate
y = float(input("How many years are we estimating here? "))

# calling on the pop_est function
pop = util.pop_est(y)

# printing the data
print("In about", y, "years, the population will be:", int(pop), "people")

