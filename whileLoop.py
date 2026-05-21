# While loop in Programming

# A while loop is a control structure that repeatedly executes a block of code as long as a specified condition remains true.

# The condition is checked before each iteration, and the loop stops once the condition becomes false.
# It is useful when the number of iterations is not known beforehand.

def print_numbers():

    # Function that prints numbers using while loop
    count = 0

    # while loop runs while the condition is true
    while count < 5:
        print(count)
        count += 1


# Calling the function
print_numbers()

