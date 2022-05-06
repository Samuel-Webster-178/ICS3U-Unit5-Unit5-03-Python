#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates middle grade percentage


def calculate_percentage(grade):
    # I calculate grade percentage

    # process
    if grade == "4+":
        percentage = 97
    elif grade == "4":
        percentage = 90
    elif grade == "4-":
        percentage = 83
    elif grade == "3+":
        percentage = 78
    elif grade == "3":
        percentage = 75
    elif grade == "3-":
        percentage = 71
    elif grade == "2+":
        percentage = 68
    elif grade == "2":
        percentage = 64
    elif grade == "2-":
        percentage = 61
    elif grade == "1+":
        percentage = 58
    elif grade == "1":
        percentage = 54
    elif grade == "1-":
        percentage = 51
    elif grade == "R":
        percentage = 30
    elif grade == "NE":
        percentage = 0
    else:
        percentage = -1

    # output
    return percentage


def main():
    # I am main, I receive input and call functions

    # input
    grade = input("Enter grade: ")
    mid_percentage = calculate_percentage(grade)
    print("Level {0} has a middle percentage of {1}%.".format(grade, mid_percentage))
    print("\nDone.")


if __name__ == "__main__":
    main()
