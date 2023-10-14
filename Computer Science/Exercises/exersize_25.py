def sumPairs(a, b):
    """
    This function will calculate and return of two sums entered by a user
    :param a: list a is a tuple from the user
    :param b: list b is another tuple from the user
    :return: is a sume of the two lists
    """
    y = []
    for i in range(len(a)):
        n = a[i] + b[i]
        y.append(n)
    return y


# M a i n   P r o g r a m


# Don't worry about how the main program works


# Test Sample Input 0

if sumPairs([5, 6, 7], [3, 6, 10]) == [8, 12, 17]:
    print("Sample Input 0 Passed")

else:
    print("Sample Input 0 Failed")

# Test Sample Input 1

if sumPairs((17, 28, 30, 5), (99, 16, 8, 88)) == [116, 44, 38, 93]:
    print("Sample Input 1 Passed")

else:
    print("Sample Input 1 Failed")

# Try your own inputs

print("Enter your own numbers on one line (separated by spaces)")

a = [int(x) for x in input("A:").split()]

b = [int(x) for x in input("B:").split()]

print(sumPairs(a, b))