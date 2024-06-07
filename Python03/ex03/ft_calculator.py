class calculator:
    """ A class that is able to do calculations
    (addition, multiplication, subtraction, division)
    of vector with a scalar. """
    def __init__(self, vector):
        """calculator's constructor, takes list of numbers"""
        self.vector = vector

    def __add__(self, scalar) -> None:
        """add the value to the whole vector"""
        if isinstance(scalar, int):
            result = [x + scalar for x in self.vector]
            self.vector = result
            print(result)
        else:
            raise ValueError("The scalar must be an integer")

    def __mul__(self, scalar) -> None:
        """multiply the value to the whole vector"""
        if isinstance(scalar, int):
            result = [x * scalar for x in self.vector]
            self.vector = result
            print(result)
        else:
            raise ValueError("The scalar must be an integer")

    def __sub__(self, scalar) -> None:
        """subtract the value to the whole vector"""
        if isinstance(scalar, int):
            result = [x - scalar for x in self.vector]
            self.vector = result
            print(result)
        else:
            raise ValueError("The scalar must be an integer")

    def __truediv__(self, scalar) -> None:
        """divide the value to the whole vector"""
        if isinstance(scalar, int):
            if scalar == 0:
                raise ValueError("The scalar must not be zero")
            result = [x / scalar for x in self.vector]
            self.vector = result
            print(result)
        else:
            raise ValueError("The scalar must be an integer")


def main():
    try:
        v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        print("---")
        v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        print("---")
        v3 = calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 5
    except Exception as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
