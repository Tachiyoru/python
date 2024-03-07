__doc__ = "filter(function or None, iterable) --> filter object\
\
Return an iterator yielding those items of iterable for which function(item)\
is true. If function is None, return the items that are true."
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
