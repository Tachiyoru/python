__doc__ = """This script translates alphanumeric strings to Morse code.

Constants:
- NESTED_MORSE: A dictionary containing mappings of alphanumeric characters
 to Morse code representations.

Functions:
- translate(s: str) -> str:
    Translates the input string `s` to Morse code using the mappings defined
     in the NESTED_MORSE dictionary.
    Raises an AssertionError if the input string contains characters
     not present in the dictionary.

- is_alphanumeric_with_spaces(s: str) -> bool:
    Checks if the input string `s` contains
      only alphanumeric characters and spaces.
    Returns True if the string is alphanumeric with spaces, False otherwise.

Usage:
- Run this script with one command-line argument: the string to be translated
    to Morse code.
- The input string must contain only alphanumeric characters and spaces.
- The translated Morse code will be printed to the console.

Example:
    python script_name.py "Hello World"
    This will translate the string "Hello World" to Morse code
        and print the result.
"""
import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "$": "...-..- ",
    "@": ".--.-. ",
    "À": ".--.- ",
    "Ä": ".-.- ",
    "Å": ".--.- ",
    "È": ".-..- ",
    "É": "..-.. ",
    "Ö": "---. ",
    "Ü": "..-- ",
    "ß": "...--.. ",
}


def translate(s):
    morse_code = ""
    for char in s.upper():
        if char in NESTED_MORSE:
            morse_code += NESTED_MORSE[char]
        else:
            raise AssertionError("Invalid character in input string")
    return morse_code


def is_alphanumeric_with_spaces(s):
    return s.replace(' ', '').isalnum()


def main():
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    s = sys.argv[1]
    if not is_alphanumeric_with_spaces(s):
        raise AssertionError("the arguments are bad")
    print(translate(s))

    return


if __name__ == "__main__":
    main()
