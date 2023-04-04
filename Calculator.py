# Calculator Using Functions

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def convert1(num1):
    return num1 / 100


def convert2(num1):
    return num1 * 3.281


print("Calculator")
print("\n1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")
print("5) Convert cm -> m")
print("6) Convert m -> feet")


def calculator():
    operator_choice = input("\nPlease select your chosen operation: ")

    num1 = int(input("\nSelect your first number: "))

    if operator_choice in ("1", "2", "3", "4"):
        num2 = int(input("\nSelect your second number: "))

        if operator_choice == "1":
            return f'\n{num1} + {num2} =  {num1 + num2}'

        elif operator_choice == "2":
            return f'\n{num1} - {num2} =  {num1 - num2}'

        elif operator_choice == "3":
            return f"\n{num1} * {num2} =  {num1 * num2}"

        elif operator_choice == "4":
            return f"\n{num1} / {num2} =  {num1 / num2}"

        elif operator_choice == "5":
            return f"\n{num1} / {100} =  {num1 / 100}"

        elif operator_choice == "6":
            return f"\n{num1} * {3.281} =  {num1 * 3.281}"

        else:
            return "\nInvalid input. Please enter a valid operation number."

    else:
        return "\nInvalid input. Please enter a valid operation number."


print(calculator())
