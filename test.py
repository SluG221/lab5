import unittest

from main import SimpleCalc


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalc()

    def test_plus(self):
        self.assertEqual(self.calculator.plus(3, 6), 9)

    def test_mult(self):
        self.assertEqual(self.calculator.mult(2, 7), 14)

    def test_sub(self):
        self.assertEqual(self.calculator.sub(12, 6), 6)

    def test_div(self):
        self.assertEqual(self.calculator.div(99, 11), 9)


if __name__ == "__main__":
    unittest.main()
