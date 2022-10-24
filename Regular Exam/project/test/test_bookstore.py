from project.bookstore import Bookstore
import unittest

class TestBookstore(unittest.TestCase):
    BOOKS_LIMIT = 4
    AVAILABILITY = {"Tanya": 3, "Stoyan": 1}

    def setUp(self) -> None:
        self.bookstore = Bookstore(self.BOOKS_LIMIT)

    def test_init_expect_correct_values(self):
        self.assertEqual(self.BOOKS_LIMIT, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_books_limit_props(self):
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(error.exception))

    def test_len_expect_correct_value(self):
        self.bookstore.availability_in_store_by_book_titles = self.AVAILABILITY
        self.assertEqual(4, self.bookstore.__len__())

    def test_receive_book_if_not_enough_space_in_book_store_raise(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book("Mona", self.BOOKS_LIMIT + 1)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_receive_book_if_enough_space_in_book_store_add_book(self):
        book_name = "Tanya"
        self.bookstore.receive_book(book_name, 1)
        self.assertEqual({book_name: 1}, self.bookstore.availability_in_store_by_book_titles)
        self.bookstore.receive_book(book_name, 2)
        self.assertEqual({book_name: 3}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, self.bookstore.availability_in_store_by_book_titles["Tanya"])

    def test_receive_book_expect_to_return_correct_message(self):
        book_name ="Tanya"
        copies = 3
        expected_text = f"{copies} copies of {book_name} are available in the bookstore."
        actual_text = self.bookstore.receive_book(book_name, copies)
        self.assertEqual(expected_text, actual_text)

    def test_sell_book_if_book_not_available_raise(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("Mona", 2)
        self.assertEqual("Book Mona doesn't exist!", str(error.exception))

    def test_sell_book_if_not_enough_numbers(self):
        self.bookstore.availability_in_store_by_book_titles = {'Mona': 1}
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("Mona", 2)
        self.assertEqual("Mona has not enough copies to sell. Left: 1", str(error.exception))

    def test_sell_book_if_enough_numbers_return_correct_message(self):
        self.bookstore.availability_in_store_by_book_titles = {'Mona': 2}
        self.assertEqual("Sold 1 copies of Mona", self.bookstore.sell_book("Mona", 1))
        self.assertEqual({'Mona': 1}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(1, self.bookstore.total_sold_books)

    def test_str(self):
        self.bookstore.availability_in_store_by_book_titles = {'Mona': 2}
        self.bookstore.sell_book("Mona", 1)

        expected = """Total sold books: 1
Current availability: 1
 - Mona: 1 copies"""
        actual = self.bookstore.__str__()
        self.assertEqual(expected, actual)

