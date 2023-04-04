def fizz(num):
    return num % 3 == 0
def buzz(num):
    return num % 5 == 0
def fizzbuzz(num):
    return num % 3 == 0 and num % 5 == 0

num = 1


while num <= 100:
    if fizzbuzz(num):
        print("FizzBuzz")
    elif fizz(num):
        print("Fizz")
    elif buzz(num):
        print("Buzz")
    else:
        print(num)
    num = num + 1



