#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This program tells you if a year is a leap year


def main():
    # This program tells you if a year is a leap year
    # Input
    user_year = input("Please enter a year : ")

    try:
        # Process and Output
        user_year = int(user_year)
        if user_year % 4 == 0:
            if user_year % 100 == 0:
                if user_year % 400 == 0:
                    print("{0} is a leap year".format(user_year))
                else:
                    print("{0} is not a leap year".format(user_year))
            else:
                print("{0} is a leap year".format(user_year))
        else:
            print("{0} is not a leap year".format(user_year))
    except Exception:
        print("Invalid input")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
