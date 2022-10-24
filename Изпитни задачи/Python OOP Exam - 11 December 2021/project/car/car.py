from abc import ABC, abstractmethod


class Car(ABC):
    MIN_MODEL_LEN = 4
    DEFAULT_IS_TAKEN = False

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = self.DEFAULT_IS_TAKEN

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < self.MIN_MODEL_LEN:
            raise ValueError(f"Model {value} is less than {self.MIN_MODEL_LEN} symbols!")
        self.__model = value

    @abstractmethod
    def __check_if_speed_is_valid(self, value):
        pass

