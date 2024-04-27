import sys


def filter_string(s, n):
    """Filters words from the input string `s` based on their length,
     keeping only words longer than `n`."""
    assert isinstance(s, str) and isinstance(n, int), "the arguments are bad"
    return [word for word in s.split() if len(word) > n]


def main():
    print("doc is: ", filter_string.__doc__)
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
