import unittest
from divide import divide, IncorrectInput, MissingArgument


class DivideTestCase(unittest.TestCase):
    # Testing the happy paths
    def test_divide_valid_8_4(self):
        self.assertEqual(2, divide(8, 4))

    def test_divide_valid_negative_denominator(self):
        self.assertEqual(-2, divide(8, -4))

    def test_divide_valid_negative_numerator(self):
        self.assertEqual(-2, divide(-8, 4))

    def test_divide_valid_negative_arguments(self):
        self.assertEqual(2, divide(-8, -4))

    # Testing what happens if the arguments are string
    def test_divide_invalid_strings(self):
        with self.assertRaises(IncorrectInput):
            divide("3", "7")

    # Test division by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(3, 0)

    # Testing behaviour if the two arguments are missing
    def test_divide_missing_both_arguments(self):
        with self.assertRaises(MissingArgument):
            divide()

    # Testing behaviour if numerator is missing
    def test_divide_missing_numerator(self):
        with self.assertRaises(MissingArgument):
            divide(None, 2)

    # Testing behaviour if denominator is missing
    def test_divide_missing_denominator(self):
        with self.assertRaises(MissingArgument):
            divide(2, None)


if __name__ == '__main__':
    unittest.main()
