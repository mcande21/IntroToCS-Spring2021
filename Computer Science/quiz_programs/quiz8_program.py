# This program will generate a truth and false table for x and y values


print("X \t\t Y \t\t not X \t\t not Y \t\t X and Y \t X or Y \t not X and not Y \t not (X or Y)")
print("--------------------------------------------------------------------------------------------------")
for x in (True, False):
    for y in (True, False):
        print(x, "\t", y, "\t", not x, "\t\t", not y, "\t\t", (x and y), "\t\t", (x or y), "\t\t\t", (not x) and (not y), "\t\t\t", (not x) or (not y))