class calculator:
    """ A class that is able to do calculations """

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """calculator's class method prints product of scalar
        multiplications of V1 and V2"""
        print("Dot product is:", sum([x * y for x, y in zip(V1, V2)]))

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """calculator's class method prints sum vector of V1 and V2"""
        print("Add Vector is:", [float(x + y) for x, y in zip(V1, V2)])

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        print("Sous Vector is:", [float(x - y) for x, y in zip(V1, V2)])


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
