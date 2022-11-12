#!/usr/bin/env python3
# Created By: Nolan Shami
# Date: November 11th, 2022
# This program tells the user to enter a whole number,
# then uses a do while loop to calculate the factorial of that number.


def main():
    # define the variables
    loop_counter = 0
    factorial_answer = 1

    # get the user's positive integer
    user_integer_as_string = input("Enter a positive integer: ")
    print()

    #turns input into an integer
    try:
        user_integer_as_int = int(user_integer_as_string)

    #exception if user input is not a positive integer
    except Exception:
        print()
        print("I feel like that might be a decimal or a text...please enter a positive integer!")
        exit()

    #if statement to input if user input is 0
    if user_integer_as_int == 0:
        print("0 is not a positive integer...please enter a positive integer! ")
        exit()
    elif user_integer_as_int < 0:
        print("This is not even positive...please enter a positive integer!")
        exit()

    # calculate the factorial of user's positive integer using a loop format
    while True:
        loop_counter = loop_counter + 1
        factorial_answer = factorial_answer * loop_counter
        print("\nTracking {} times through the loop".format(loop_counter))
        if loop_counter >= user_integer_as_int:
            break

    print()
    print(
        "{} is the factor for {}!".format(
            factorial_answer, user_integer_as_int
        )
    )


if __name__ == "__main__":
    main()
