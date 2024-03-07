import sys


def check_odd_or_even(number):
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if len(sys.argv) <= 1:
    sys.exit(1)
if len(sys.argv) != 2:
    print("AssertionError: Wrong number of arguments")
    sys.exit(1)
try:
    number = int(sys.argv[1])
    check_odd_or_even(number)
except ValueError:
    print("AssertionError: argument is not an integer")
