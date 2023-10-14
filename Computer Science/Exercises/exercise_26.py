# This function will calculate the minimum and maximum of a list of numbers

def miniMaxSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i])
    arr.sort()
    new_max = sum - int(arr[0])
    new_min = sum - int(arr[len(arr) - 1])
    return (new_min, new_max)


# M a i n   P r o g r a m


if miniMaxSum([7, 9, 3, 1, 5]) == (16, 24):

    print("Sample Test 0 Passed")

else:

    print("Sample Test 0 Failed")

# Try your own list of numbers

print("enter all numbers on one line separated by spaces")

v = [int(x) for x in input("numbers: ").split()]

print(' '.join([str(x) for x in miniMaxSum(v)]))