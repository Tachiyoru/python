from abc import ABC, abstractmethod


class Character(ABC):
    """
    Your docstring for Class.
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Your docstring for Constructor.
        """
        print("///////////passe par character ///////////////")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Your docstring for Method."""
        pass


class Stark(Character):
    """Your docstring for Class."""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for Method."""
        self.is_alive = False


def main():
    Ned = Stark("Ned")
    print("1:", Ned.__dict__)
    print("Ned is alive is : ", Ned.is_alive)
    Ned.die()
    print("Ned is alive is : ", Ned.is_alive)
    print("---")
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    # hodor = Character("hodor")


if __name__ == "__main__":
    main()
