# This program will p[lay the game oh no.

for i in range(101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("oh no")
    elif i % 5 == 0:
        print("no")
    elif (i % 3 == 0):
        print("oh")
    else:
        print(i)