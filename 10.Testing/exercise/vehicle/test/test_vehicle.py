from project.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    FUEL = 100
    HORSE_POWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_vehicle__init(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_vehicle__drive__expect_if_less_fuel_raise(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_vehicle_drive__expect_if_enough_fuel_decrease_fuel(self):
        distance = 50
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance
        self.vehicle.drive(distance)
        expected_result = self.FUEL - fuel_needed
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_vehicle_drive__expect_reduces_fuel_with_max_possible_distance(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION
        self.vehicle.drive(distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test_vehicle_refuel__expect_if_not_enough_capacity_raise(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(error.exception))

    def test_vehicle_refuel__expect_increase_fuel(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount

        self.vehicle.refuel(fuel_amount)
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_vehicle__str__expect_correct_str(self):
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        actual_result = str(self.vehicle)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
