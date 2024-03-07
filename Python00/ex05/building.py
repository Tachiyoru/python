__doc__ = """This script counts the number of uppercase letters, lowercase
    letters, punctuation marks, spaces, and digits in a given text.

Functions:
- count(text: str) -> None:
    Counts the occurrences of uppercase letters, lowercase letters,
        punctuation marks, spaces, and digits in the provided text.
    Prints the counts for each category.

Usage:
- If run as a script with a command-line argument, it will count
    the characters in that argument.
- If run without any command-line arguments, it will prompt the user
    to input text to be counted.
- The counts will be printed to the console.
-  "Python 3.0, released in 2008, was a major revision that is not
    completely backwardcompatible with earlier versions. Python 2
    was discontinued with version 2.7.18 in 2020."
"""
import sys


def count(text):
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in '.,!?;:':
            punctuation_count += 1

    total_characters = len(text)
    print("The text contains", total_characters, "characters:")
    print(upper_count, "upper letters")
    print(lower_count, "lower letters")
    print(punctuation_count, "punctuation marks")
    print(space_count, "spaces")
    print(digit_count, "digits")


def main():
    if len(sys.argv) > 2:
        raise AssertionError("Too many arguments")
    if len(sys.argv) < 2:
        print("What is the text to count? ")
        str = input()
        count(str)
    else:
        count(sys.argv[1])
    return


if __name__ == "__main__":
    main()
