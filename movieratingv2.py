def get_age():
    customer_age = input("Welcome to the cinema. Please enter your age: ")
    return customer_age


def movie_age(customer_age):
    if customer_age.isdigit():
        customer_age = int(customer_age)
        if customer_age < 1 or customer_age > 117:
            print("Invalid Age! Please enter your correct age!")
        elif customer_age < 12:
            print("You can watch movies rated U, PG")
        elif customer_age < 15:
            print("You can watch movies rated U, PG, 12")
        elif customer_age < 18:
            print("You can watch movies rated U, PG, 12, 15")
        else:
            print("You can watch all the available movies!")
    else:
        print("Invalid Input! Please enter a valid age.")


age_grabber = get_age()
movie_age(age_grabber)
