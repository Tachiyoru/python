__doc__ = """Module initializer for ft_package.

This module initializes the ft_package package,
making the count_in_list function available for import.

Functions and Variables:
- count_in_list: Function for counting occurrences of an item in a list.

Usage:
    You can import count_in_list from ft_package like this:
    from ft_package import count_in_list
    Then, you can use count_in_list to count occurrences of an item in a list.
"""
from .count_in_list import count_in_list

__all__ = ['count_in_list']
