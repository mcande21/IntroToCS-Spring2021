# This function will ask the user for some names and print them out on different lines in alphabetical order

number_names = int(input("How many names do you want to work with? "))
names = []
for i in range(number_names):
    name = input("What name you want to add? ")
    names.append(name)

# Now im going to print out the names in alphabetical order
names.sort()
for i in range(len(names)):
    print(names[i])
