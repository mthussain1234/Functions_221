# Calculator Using Functions
## How to Use
* Run the program in a Pycharm
* Select the  operation by entering the corresponding number.
* Enter the numbers needed for the operation.
* Output will show the result
* Operations


**The following operations are available:**

* Add
* Subtract
* Multiply
* Divide
* Convert cm to m
* Convert m to feet

**The following functions are used in the program:**

`add(num1, num2)`: adds `num1` and `num2` and returns the result

`subtract(num1, num2)`: subtracts `num2` from `num1` and returns the result

`multiply(num1, num2)`: multiplies `num1` and `num2` and returns the result

`divide(num1, num2)`: divides `num1` by `num2` and returns the result

`convert1(num1)`: converts `num1` from cm to m and returns the result

`convert2(num1)`: converts `num1` from m to feet and returns the result

### Full code and example run
```commandline
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
```

**Output:**

```commandline
Calculator

1) Add
2) Subtract
3) Multiply
4) Divide
5) Convert cm -> m
6) Convert m -> feet

Please select your chosen operation: 4

Select your first number: 3

Select your second number: 2

3 / 2 =  1.5

Process finished with exit code 0

```
