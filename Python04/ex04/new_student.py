import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """ Generate a random id of 15characters"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """ Student class"""
    name: str
    surname: str
    active: bool = True
    login: str = field(default=None)
    id: str = field(default=None)

    def __post_init__(self):
        """ Post initialization"""
        if self.login is None:
            self.login = self.name[0] + self.surname.lower()
        else:
            raise ValueError("login is not initializable")
        if self.id is None:
            self.id = generate_id()
        else:
            raise ValueError("id is not initializable")


def main():
    student = Student(name="Edward", surname="agle")
    print(student)
    print("---ERROR CASE ---")
    student2 = Student(name="Edward", surname="agle", id="toto")
    print(student2)


if __name__ == "__main__":
    main()
