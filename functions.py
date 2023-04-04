# Functions

# Allows you to follow DRY

# Do Not Repeat Yourself


# def print_something():
#     print("something has been printed")

# def print_something(print_string):
#     print(print_string)
#
# print_something(" Moham")
#
# # Java example
# # public void print_string(string_Text_)
#
#
# def greeting(name):
#     print("Hello, my name is " + name)
#
# greeting("Mohammad")

# Return Statement

# def addition(int1, int2):
#     return int1 + int2


# print(addition(2, 2))

# Default arguments

# def addition(int1=2, int2=2):
#     return int1 + int2
#
#
# print(addition(45, 45))


# Multiple Arguments

# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs:
#         print(arg)
#
#
# multi_args(1, 2, 2, 3, 3, 4, 5, 5)

# Type Hints

def greeting(name: str):
    print("Hello, my name is " + name)


greeting("24601")


def division(denum: int, num: int) -> float:
    return denum / num


print(division(12, 5))


def subtraction(int1: int = 5, int2: int = 2) -> int:
    return int1 - int2


print(subtraction())

# functions best practices

# 1. Name your methods using lowercase and underscores
# 2. All arguments should be clear in their need and where possible their type
# 3. remember the return statement or your function will return None in most cases
# 4. Keep your functions small as possible, and keep them readable
# 5. Use comments within your methods to help with instructions on how to use them
# 6. Consider using Type Hints to avoid errors earlier
