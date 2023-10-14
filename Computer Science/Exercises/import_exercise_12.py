# This program will test the num_password function
# I'm going to throw a couple different vsariations
# so i can see how they effect the passwords

import exercise_12

# testing out the function with different variations
a = exercise_12.num_passwords(94,2)
b = exercise_12.num_passwords(94,3)
c = exercise_12.num_passwords(94,10)
d = exercise_12.num_passwords(52,2)
e = exercise_12.num_passwords(52,3)
f = exercise_12.num_passwords(52,10)
print("(94,2) is", a)
print("(94,3) is", b)
print("(94,10) is", c)
print("(52, 10) is", d)
print("(52, 3) is", e)
print("(52,10) is", f)