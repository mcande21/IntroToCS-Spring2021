# This program will compute the sum of cubes from 1 to 10^3

# setting the counter (i) and the sum of all numbers (sum)
i = 1
sum = 0
# starting the while loop
while i <= 10:
    # assigning and cubing the i value
    x = i ** 3
    # adding that value to the sum
    sum = sum + x
    # adding to the counter
    i = i + 1

# just printing out the value
print("The sum of values 1-10 cubed is:", sum)