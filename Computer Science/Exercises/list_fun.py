# # this program will create a list that the user can ad to until they put in a negetive number
#
# # make an empty list first
# list = []
#
# # lopp until we see a negative number
# done = False
# while not done:
#     # read a number
#     n = int(input("Enter a number (negative to quit): "))
#     # check if the number is non-negative
#     if n < 0:
#         done = True
#     else:
#         list.append(n)
#
# # done with the loop
# # sort the data
# list.sort()
# print(list)

n = int(input("Yo give me a number: "))
list = []
while n > 0:
    list.append(n)
    n = int(input("Yo give me a number: "))

list.sort()
print(list)
