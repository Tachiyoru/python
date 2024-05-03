import sys


def ft_filter(func, iterable):
    """Filters elements from the input iterable based on
            the given function `func`.
 Returns a list containing elements for which `func(element)`
     returns `True`."""
    return [x for x in iterable if func(x)]


def is_even(n):
    """Returns `True` if `n` is even."""
    return n % 2 == 0


def main():
    if len(sys.argv) != 1:
        raise AssertionError("Too many arguments")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = ft_filter(is_even, numbers)
    print(filtered_numbers)


if __name__ == "__main__":
    print(" filter doc is: ", filter.__doc__)
    main()
