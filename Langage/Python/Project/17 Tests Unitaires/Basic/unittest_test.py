# python unittest_test.py -v
# coverage run -m unittest unittest_test.py
# coverage html

from unittest import TestCase, main

from main import add, divide

class TestCalculatruce(TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(5, 10), 15)

    def test_add_two_letters(self):
        self.assertEqual(add("a", "b"), "ab")

    def test_add_two_booleans(self):
        self.assertEqual(add(True, False), 1)
        self.assertEqual(add(True, True), 2)
        self.assertEqual(add(False, False), 0)

    def test_add_two_none(self):
        # Vérifie que none ne marche pas 
        with self.assertRaises(TypeError):
            add(None, None)

    def test_divide_two_numbers(self):
        self.assertEqual(divide(10, 2), 5)

if __name__ == '__main__':
    main()