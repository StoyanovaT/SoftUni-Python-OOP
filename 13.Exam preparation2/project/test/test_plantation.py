from project.plantation import Plantation
import unittest


class TestPlantation(unittest.TestCase):
    VALID_SIZE = 3
    INVALID_SIZE = -2

    def setUp(self) -> None:
        self.plantation = Plantation(self.VALID_SIZE)

    def test_init_valid_expect_valid_props(self):
        self.assertEqual(self.VALID_SIZE, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_if_invalid_expect_raise(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.size = self.INVALID_SIZE

        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker__if_worker_already_added_raise(self):
        worker = "Tanya"
        self.plantation.workers.append(worker)
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker(worker)
        self.assertEqual("Worker already hired!", str(error.exception))
        self.assertEqual([worker], self.plantation.workers)

    def test_hire_worker__adds_worker_return_correct_str(self):
        worker = "Tanya"
        self.assertEqual(f"{worker} successfully hired.", self.plantation.hire_worker(worker))
        self.assertEqual([worker], self.plantation.workers)

    def test_len_return_correct_count_of_plants(self):
        plants = {'Tanya': ["rose", 'tulip'], 'Stoyan': ['rose']}
        self.plantation.plants = plants
        self.assertEqual(3, self.plantation.__len__())

    def test_planting_if_worker_not_hired_rise(self):
        worker = 'Stoyan'
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, "rose")
        self.assertEqual(f"Worker with name {worker} is not hired!", str(error.exception))

    def test_planting_if_plantation_full_rise(self):
        worker = "Tanya"
        plant = 'rose'
        self.plantation.workers = [worker]
        self.plantation.plants = {'Tanya': ["rose", 'tulip'], 'Stoyan': ['rose']}
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, plant)
        self.assertEqual("The plantation is full!", str(error.exception))

    def test_if_worker_has_planted_plants_add_new_plant_and_return_correct_str(self):
        worker = 'Tanya'
        plant = 'rose'
        self.plantation.workers = [worker]
        self.plantation.plants = {'Tanya': ['tulip'], 'Stoyan': ['rose']}
        self.assertEqual(f"{worker} planted {plant}.", self.plantation.planting(worker, plant))
        self.assertEqual({'Tanya': ['tulip', "rose"], 'Stoyan': ['rose']}, self.plantation.plants)

    def test_if_worker_have_none_planted_plants__add_worker_and_plant_and_return_correct_str(self):
        worker = 'Tanya'
        plant = 'rose'
        self.plantation.workers = [worker]
        self.assertEqual(f"{worker} planted it's first {plant}.", self.plantation.planting(worker, plant))
        self.assertEqual({'Tanya': ["rose"]}, self.plantation.plants)

    def test_str__return_correct_text(self):
        self.plantation.workers = ['Tanya', 'Stoyan']
        self.plantation.plants = {'Tanya': ['tulip', "rose"], 'Stoyan': ['rose']}
        expected = """Plantation size: 3
Tanya, Stoyan
Tanya planted: tulip, rose
Stoyan planted: rose"""
        actual = self.plantation.__str__()

        self.assertEqual(expected, actual)

    def test_repr_return_correct_text(self):
        self.plantation.workers = ['Tanya', 'Stoyan']
        self.plantation.plants = {'Tanya': ['tulip', "rose"], 'Stoyan': ['rose']}
        expected = """Size: 3
Workers: Tanya, Stoyan"""
        actual = self.plantation.__repr__()

        self.assertEqual(expected, actual)

