# Functions in programming

# A function is a block of code that performs a specific task and can be reused whenever needed.

# Avoids writing the same code again and again.
# Makes programs simple and easy to understand by breaking into smaller parts.
# Accepts input (parameters) and gives output.
# Finding and fixing errors become easier.

# Built-in functions

# These predefined functions provided by programming languages or libraries to perform common tasks such as mathematical calculations, input/output, or string operations.
# For example, the sqrt() function from the C++ <cmath> library calculates the square root of a number.

import math

# built-in function
result = math.sqrt(25)

print("Square Root:", result)



# User-defined
# These functions are functions written by programmers to perform specific tasks required in a program.
# They help organize code and allow reuse of logic whenever needed.

def greet():
    print("Hello, World!")

greet()   # calling user-defined function