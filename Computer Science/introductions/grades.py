# This program will give us an analisys of collection of grades
def compute_average(grades):
    """
    Compute and return the average of a collection of grades
    :param grades: tuple of multiple grades
    :return: the average of these grades
    """
    # add up all numbers
    sum = 0
    for g in grades:
        sum += g
    # devide by the number of times
    avg = sum / len(grades)

    return avg

def compute_median(grades):
    """
    Compute/find the middle element of a list of a grade
    if there is an # of element, take the average of the middle two items
    :param grades: list of grades
    :return: median
    """
    # sort the list of data
    grades.sort()

    # if the length is odd then return the middle element
    # otherwise return the average of the two middle elements
    if len(grades) % 2 == 1:
        # odd
        return grades[len(grades) // 2]
    else:
        # even
        mid1 = grades[len(grades) // 2]
        mid2 = grades[len(grades) // 2 - 1]
        # return avg
        return(mid1 + mid2) / 2


# MAIN PROGRAM
grades_tuple = (98, 89, 77, 91, 83, 94)
print("We will analyze", len(grades_tuple), "grades")
print("The third grade is", grades_tuple[2])
print("The average of these numbers is", round(compute_average(grades_tuple), 2))


grades_list = [98, 89, 77, 91, 83, 94]
print("We will no alanlyze a list with", len(grades_list), "grades")
print("The third grade is", grades_tuple[2])
print("The average of these numbers is", round(compute_average(grades_tuple), 2))

grades_list[2] = 87
print("The third grade is now", grades_list[2])
print("The average of this list is now", round(compute_average(grades_list), 2))
print("The median of this list is", compute_median(grades_list))

new_grade = int(input("Enter new grade: "))
# append to the end of our list (add this value to the last location)
grades_list.append(new_grade)
print("We will now analyze a list with", len(grades_list), "grades")
print("The average of this list is now", round(compute_average(grades_list), 2))
print("The median of this list is", compute_median(grades_list))