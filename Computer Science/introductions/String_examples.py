import util

# examples of manipulating string data.
s = "somethingreallycoolandinteresting"

# we might wnt to know how many characters are in the string
# Our len() also works with string
print("There are", len(s), "characters in", s)

# We can also access characters from the same square bracket
# notation from lists and tuples
print(s[0], s[len(s)- 1])

# be careful of "off by one" errors
# we need our -1 because a string starts counting from 0
print(s[len(s)-1])

# self check
print(s[5], s[15])

# loop over al characters in a string using a for loop
# EX: count the number of i's in a string

i_count = 0
for ch in s:
    # check if the character is an i
    if ch == "i":
        i_count += 1
print("There are", i_count, "i's in this string", s)

# we can also loop over the indices of each character
d_count = 0
for i in range(len(s)):
    # we now need to access the character at index i
    if s[i] == "d":
        d_count += 1
print("There are", d_count, "d's in the string", s)

# combining twi strings
str1 = "CS"
str2 = "140"
str3 = str1 + str2
print(str3)

print(util.reverse(s))
print(util.reverse("racecar"))
print(util.reverse("michaelcooperanderson"))

# find A STRING INSIDE antoher sting
print(s.find("th"))
# python will return -1 if the string is not found
print(s.find("shitty"))
# find also lets us specify the starting idex for the search
print(s.find("co", 10))


# substring/slice operation
print(s[9:15])

# EX) ask the user for two numbers seperaTED BY A COMMA
# TAKE THE AVERAGE OF THESE TWO NUMBERS
data = input("enter two numbers separated by a comma: ")
comma = data.find(",")
num1 = float(data[:comma])
num2 = float(data[comma + 1:])
print((num1 + num2) /2)
