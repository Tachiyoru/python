__doc__ = """This script demonstrates a custom filter function and its usage.

Functions:
- ft_filter(func, iterable) -> list:
 Filters elements from the input iterable based on the given function `func`.
 Returns a list containing elements for which `func(element)` returns `True`.

Example Usage:
- Run this script without any command-line arguments.
- The script defines a function `is_even(n)` which
    returns `True` if `n` is even.
- It then demonstrates the usage of the custom filter function `ft_filter`
     to filter even numbers from a list of numbers.
- The filtered numbers are printed to the console.

Note:
- The function `ft_filter` behaves similarly to Python's
    built-in `filter` function.
"""
import sys


def ft_filter(func, iterable):
    return [x for x in iterable if func(x)]


def is_even(n):
    return n % 2 == 0


def main():
    if len(sys.argv) != 1:
        raise AssertionError("Too many arguments")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = ft_filter(is_even, numbers)
    print(filtered_numbers)


if __name__ == "__main__":
    print("filter doc =")
    print(filter.__doc__)
    main()
