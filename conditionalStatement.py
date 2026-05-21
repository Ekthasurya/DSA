#onditional statements help a program make decisions. They check whether a condition is true or false and execute different blocks of code based on the result. This allows programs to behave differently in different situations.

#If Conditional Statement:- The if statement checks a condition and executes a block of code only when the condition is true.

x = 7

if x > 0:
    print("x is positive")

#If-Else Conditional Statement:-The if-else statement checks a condition and runs one block of code if the condition is true, and another block of code if the condition is false.

a = -5

if a > 0:
    print("a is positive")
else:
    print("a is not positive")
    

# if-Else if Conditional Statement :- The if-else if statement is used to check multiple conditions. The program evaluates each condition one by one and executes the block of code for the first condition that is true.

b = 0

if b > 0:
    print("b is positive")
elif b < 0:
    print("b is negative")
else:
    print("b is zero")

#Switch Conditional Statement :- The switch statement checks a variable against multiple possible values. Each option is written as a case, and the program executes the matching case. A break statement is usually used to stop execution after a case runs


day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day!")


#Key Considerations for Switch Case Statements:------>
#1. Constant Expression: A switch expression must evaluate to 
# a constant value. This can include constants or arithmetic operations.

r = 10
s = 5

match r + s:
    case 15:
        print("Result is 15.")
    case 20:
        print("Result is 20.")
    case _:
        print("No match found.")  


# 2. Limited to Certain Types: Switch statements are mainly designed for int, char, or string values depending on the language.

grade = 'B'

match grade:
    case 'A':
        print("Excellent!")
    case 'B':
        print("Good!")
    case _:
        print("Not specified.")

# Ternary Expression Conditional Statement:-->The ternary operator is a short way to write an if-else statement. It evaluates a condition and returns one value if the condition is true, and another value if the condition is false.

# It is called a ternary operator because each ternary expression uses three parts.
# Multiple ternary expressions can also be nested to check more conditions.

n =10

print("n is positive" if n > 0 else "n is not positive")  