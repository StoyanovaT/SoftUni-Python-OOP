from abc import ABC, abstractmethod


class Horse(ABC):
    MIN_NAME_LENGTH = 4
    DEFAULT_IS_TAKEN_STATE = False

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = self.DEFAULT_IS_TAKEN_STATE

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < self.MIN_NAME_LENGTH:
            raise ValueError(f"Horse name {value} is less than {self.MIN_NAME_LENGTH} symbols!")
        self.__name = value

    @property
    @abstractmethod
    def speed(self):
        pass

    @speed.setter
    @abstractmethod
    def speed(self, value):
        pass

    @abstractmethod
    def train(self):
        pass

