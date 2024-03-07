__doc__ = """This script filters words from a given string
 based on their length.

Functions:
- filter_string(s: str, n: int) -> list[str]:
    Filters words from the input string `s` based on their length,
     keeping only words longer than `n`.
    Returns a list of filtered words.

Usage:
- Run this script with two command-line arguments:
    1. The input string `s` to be filtered.
    2. The minimum length `n` of words to keep.
- Example:
    python script_name.py "This is a sample sentence" 3
    This will filter out words with length less than 3 characters
        from the given string.
"""
import sys


def filter_string(s, n):
    assert isinstance(s, str) and isinstance(n, int), "the arguments are bad"
    return [word for word in s.split() if len(word) > n]


def main():
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    s = str(sys.argv[1])
    n_str = sys.argv[2]
    if not n_str.isdigit():
        raise AssertionError("the arguments are bad")
    n = int(n_str)
    print(filter_string(s, n))


if __name__ == "__main__":
    main()
