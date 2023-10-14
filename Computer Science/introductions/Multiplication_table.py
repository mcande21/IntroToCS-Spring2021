# use two nested loops to generate a multiplication table for numbers 1-10

# outer loop will iterate through the rows of our table
for i in range(1, 11):
    # inner loop will iterate through the columns of a single row
    for j in range (1, 11):
        # print allows us to specify a "named parameter" called "end"
        # that gets printed after all data has been output. By defult
        # end is set to /n
        print(i*j, end="\t")
    # we are done outputing data for a single row
    # print a new line
    print()