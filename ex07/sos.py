import sys


__doc__ = "print a string in Morse Code from a char string"


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


# def find_morse_letter():
#     return


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
