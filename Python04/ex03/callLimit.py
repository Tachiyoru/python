def callLimit(limit: int):
    """ Decorator set the limits the number
        of times a function can be called."""
    count = 0

    def callLimiter(function):
        """ Real decorator that limits the number of times"""

        def limit_function(*args: any, **kwargs: any):
            """ Inner function """
            nonlocal count
            count += 1
            if count > limit:
                return print(f"Error: function {function.__name__}\
                 at " f"{hex(id(function))} call too many times")
            return function(*args, **kwargs)
        return limit_function
    return callLimiter


def main():

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
