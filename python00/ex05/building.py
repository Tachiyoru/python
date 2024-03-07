__doc__ = "count all type of character in an arg given or in an input"
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


# your tests and your error handling
if __name__ == "__main__":
    main()
