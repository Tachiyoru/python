__doc__ = "filter(function or None, iterable) --> filter object\
\
Return an iterator yielding those items of iterable for which function(item)\
is true. If function is None, return the items that are true."
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
