import unittest
from divide import divide, IncorrectInput


class DivideTestCase(unittest.TestCase):
    def test_divide_valid_default(self):
        self.assertEqual(0.5, divide())

    def test_divide_valid_8_4(self):
        self.assertEqual(2, divide(8, 4))

    def test_divide_invalid_strings(self):
        with self.assertRaises(IncorrectInput):
            divide("3", "7")

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(3, 0)


if __name__ == '__main__':
    unittest.main()
