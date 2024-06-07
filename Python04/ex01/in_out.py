def square(x: int | float) -> int | float:
    """ Return the square of x """
    return x * x


def pow(x: int | float) -> int | float:
    """ Return x to the power of x """
    return x ** x


def outer(x: int | float, function) -> object:
    """ Return a function that takes no arguments and returns
    the result of calling function with x as an argument. """
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        res = x
        for i in range(count):
            res = function(res)
        return res
    return inner


def main():
    try:
        my_counter = outer(3, square)
        print(my_counter())
        print(my_counter())
        print(my_counter())
        print("---")
        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())
    except Exception as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
