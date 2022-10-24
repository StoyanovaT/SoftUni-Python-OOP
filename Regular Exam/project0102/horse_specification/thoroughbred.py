from project0102.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TRAIN_INCREASE = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        self.speed = min(self.speed + self.TRAIN_INCREASE, self.MAX_SPEED)



