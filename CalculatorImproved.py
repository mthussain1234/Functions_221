def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def convert_cm_to_m(num1):
    return num1 / 100


def convert_m_to_feet(num1):
    return num1 * 3.281


print("Calculator")
print("\n1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")
print("5) Convert cm -> m")
print("6) Convert m -> feet")

operator_choice = input("\nPlease select your chosen operation: ")

num1 = float(input("\nSelect your first number: "))

if operator_choice in ("1", "2", "3", "4"):
    num2 = float(input("\nSelect your second number: "))

if operator_choice == "1":
    print(f'\n{num1} + {num2} =  {add(num1, num2)}')

elif operator_choice == "2":
    print(f'\n{num1} - {num2} =  {subtract(num1, num2)}')

elif operator_choice == "3":
    print(f"\n{num1} * {num2} =  {multiply(num1, num2)}")

elif operator_choice == "4":
    print(f"\n{num1} / {num2} =  {divide(num1, num2)}")

elif operator_choice == "5":
    print(f"\n{num1} cm = {convert_cm_to_m(num1)} m")

elif operator_choice == "6":
    print(f"\n{num1} m = {convert_m_to_feet(num1)} feet")

else:
    print("\nInvalid input. Please enter a valid operation number.")
