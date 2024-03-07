__doc__ = """This module provides a function to
    count occurrences of an item in a list.

Functions:
- count_in_list(lst: list, item: Any) -> int:
    Counts the occurrences of a specified item in the given list.
    Returns the count of occurrences.

Example:
    count_in_list([1, 2, 2, 3, 4, 2], 2)  # Returns 3
    count_in_list(['a', 'b', 'c', 'c', 'c'], 'c')  # Returns 3

Usage:
    from ft_package import count_in_list
        print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
        print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
"""


def count_in_list(lst, item):
    return lst.count(item)
