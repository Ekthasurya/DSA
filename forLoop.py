#For loop in Programming
#A for loop allows you to repeat a block of code a specific number of times.

#Widely used when the number of iterations is known in advance.

#Makes it easy to iterate over arrays, lists, or sequences, generate number series, and perform repetitive tasks efficiently.

for i in range(1, 6):
    print(i, end=" ")
print()

# A for loop has three main parts in most languages: initialization, condition, and update.

# Initialization sets the starting point of the loop.
# Condition is checked before each iteration; if true, the loop executes.
# Update changes the loop counter after each iteration.

#BASIC

for A in range(2, 11, 2):
    print(A, end=" ")
#range(start, stop, step)

# 2. For Each Loop

# The for-each loop is used to iterate directly over elements of a collection such as arrays or lists without using an index.

numbers = [1,2,3,4,5]
for num in numbers:
    print(num, end=" ",)

# 3. For Loop with Multiple Variables

# Some languages like C, C++, and Java allow multiple loop control variables in a for loop.


k, j = 0, 10
while k < 5 and j > 0:
    print("k=", k, ", j=", j)
    k += 1
    j -= 1


# 5. Nested For Loop

# A nested for loop is a loop inside another loop. It is used for multidimensional data or when multiple levels of iteration are needed.

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# 6. For Loop with Step/Stride

# Some programming languages allow you to specify a step or stride for the loop, letting you control the increment or decrement of the loop variable.

for i in range(0, 10, 3):
    print(i, end=" ")