from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon class docstring
    """

    # Pas de super().__init__(first_name, is_alive)
    # = pas de passage dans character
    def __init__(self, first_name, is_alive=True):
        """ Baratheon initiator """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

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
    # Pas de super().__init__(first_name, is_alive)
    # = pas de passage dans character
    def __init__(self, first_name, is_alive=True):
        """ Lannister initiator """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        self.is_alive = False

    def __str__(self):
        """Lannister's method __str__: returns string
        with name, color of eyes and hairs but it goes through repr"""

    def __repr__(self):
        """Lannister's method __repr__: returns string
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
