import sys


def filter_string(s, n, condition):
    """Filters words from the input string `s` based on their length,
     keeping only words longer than `n`."""
    assert isinstance(s, str) and isinstance(n, int), "The arguments are wrong"
    return [word for word in s.split() if condition(word)]


def main():
    print("doc is: ", filter_string.__doc__)
    try:
        if len(sys.argv) != 3:
            raise AssertionError("The number of arguments is not 3")
        s = str(sys.argv[1])
        n_str = sys.argv[2]
        if not n_str.isdigit():
            raise AssertionError("The third argument is not digit")
        n = int(n_str)
        print(filter_string(s, n, lambda x: len(x) > n))
    except Exception as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
