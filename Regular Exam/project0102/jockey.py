class Jockey:
    MIN_AGE = 18
    DEFAULT_HORSE = None

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = self.DEFAULT_HORSE

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value.isspace():
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_AGE:
            raise ValueError(f"Jockeys must be at least {self.MIN_AGE} to participate in the race!")
        self.__age = value

