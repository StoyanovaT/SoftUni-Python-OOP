from project.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):
    NAME = "Richi"
    TYPE = "Dog"
    SOUND = "Bau Bau"
    KINGDOM = 'animals'

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test_mammal__init_should_create_proper_obj(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual(self.KINGDOM, self.mammal._Mammal__kingdom)

    def test_make_sound__expect_correct_sound(self):
        actual_result = self.mammal.make_sound()
        expected_result = f"{self.NAME} makes {self.SOUND}"

        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom_expect_correct_kingdom(self):
        actual_result = self.mammal.get_kingdom()

        self.assertEqual(self.KINGDOM, actual_result)

    def test_info__expect_correct_info(self):
        actual_result = self.mammal.info()
        expected_result = f"{self.NAME} is of type {self.TYPE}"
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
