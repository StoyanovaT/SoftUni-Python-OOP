from project04need_for_speed.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)