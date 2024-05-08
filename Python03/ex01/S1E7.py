from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon class docstring
    """
    # Override __new__ method
    def __new__(cls, first_name, is_alive=True):
        """ Baratheon constructor """
        instance = super().__new__(cls)
        instance.first_name = first_name
        instance.is_alive = is_alive
        instance.family_name = 'Baratheon'
        instance.eyes = 'brown'
        instance.hairs = 'dark'
        return instance

    def __init__(self, first_name, is_alive=True):
        """ Baratheon initiator """

    def die(self):
        self.is_alive = False

    def __str__(self):
        """Baratheon's method __str__: returns string
        with name, color of eyes and hairs but it goes through repr"""

    def __repr__(self):
        """Baratheon's method __repr__: returns string
        with name, color of eyes and hairs"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"


class Lannister(Character):
    """
    Lannister class docstring
    """
    # Override __new__ method
    def __new__(cls, first_name, is_alive=True):
        """ Lannister constructor """
        instance = super().__new__(cls)
        instance.first_name = first_name
        instance.is_alive = is_alive
        instance.family_name = 'Lannister'
        instance.eyes = 'blue'
        instance.hairs = 'light'
        return instance

    def __init__(self, first_name, is_alive=True):
        """ Lannister initiator """

    def die(self):
        self.is_alive = False

    def __str__(self):
        """Baratheon's method __str__: returns string
        with name, color of eyes and hairs but it goes through repr"""

    def __repr__(self):
        """Baratheon's method __repr__: returns string
        with name, color of eyes and hairs"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}\
, Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
