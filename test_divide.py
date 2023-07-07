import unittest
from divide import divide


class MainTestCase(unittest.TestCase):
    def test_divide_valid_8_4(self):
        self.assertEqual(2, divide(8, 4))


if __name__ == '__main__':
    unittest.main()
