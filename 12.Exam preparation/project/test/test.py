from project.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    NAME = "Game of thrones"
    YEAR = 2010
    RATING = 8
    ACTORS = ['Kit Harrington', 'Emilia Clark', 'Peter Duncklige']

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test__init_expect_correct_props(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter__raise_if_empty_str(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_year_setter__raise_if_less_than_1887(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = 1800
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor__if_name_not_in_actors_adding_it(self):
        name = "Emilia"
        name2 = "Kit"
        self.movie.add_actor(name)
        self.movie.add_actor(name2)
        self.assertEqual([name, name2], self.movie.actors)

    def test_add_actor__if_name_in_actors_return_message(self):
        name = "Emilia"
        self.movie.add_actor(name)
        self.assertEqual(f"{name} is already added in the list of actors!", self.movie.add_actor(name))
        self.assertEqual([name], self.movie.actors)

    def test_gt_returns_correct_message_if_first_movie_has_greater_rating(self):
        another_movie_name = "Star Wars"
        another_movie = Movie(another_movie_name, 1959, self.RATING - 1)

        self.assertEqual(f'"{self.movie.name}" is better than "{another_movie.name}"', self.movie.__gt__(another_movie))

    def test_gt_returns_correct_message_if_second_movie_has_greater_rating(self):
        another_movie_name = "Star Wars"
        another_movie = Movie(another_movie_name, 1959, self.RATING + 1)

        self.assertEqual(f'"{another_movie.name}" is better than "{self.movie.name}"', self.movie.__gt__(another_movie))

    def test_repr_returns_correct_message(self):
        self.movie.actors = ['Kit Harrington', 'Emilia Clark', 'Peter Duncklige']

        expected = f"Name: {self.NAME}\n" \
               f"Year of Release: {self.YEAR}\n" \
               f"Rating: {self.RATING:.2f}\n" \
               f"Cast: {', '.join(self.ACTORS)}"

        actual = repr(self.movie)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()