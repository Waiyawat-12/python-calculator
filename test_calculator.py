import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)


    # Add the following test methods to the TestCalculator class:
        self.assertEqual(self.calc.add(-2, -2), -4)
        self.assertEqual(self.calc.add(-2, 2), 0)
        self.assertEqual(self.calc.add(2, -3), -1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), -2)
        self.assertEqual(self.calc.subtract(-3, -3), 0)
        self.assertEqual(self.calc.subtract(-5, 2), -7)
        self.assertEqual(self.calc.subtract(2, -5), 7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 9) 27)
        self.assertEqual(self.calc.multiply(3, -9) -27)
        self.assertEqual(self.calc.multiply(-6, 6) -36)
        self.assertEqual(self.calc.multiply(-3, -3) 9)

    def test_divide(self):
        self.assertEqual(self.calc.divide(9, 3) 3)
        self.assertEqual(self.calc.divide(9, -3) -3)
        self.assertEqual(self.calc.divide(-81, 9) -9)
        self.assertEqual(self.calc.divide(-9, -9) 1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 4), 2)
        self.assertEqual(self.calc.modulo(5, -5) 0)
        self.assertEqual(self.calc.modulo(-4, 3) 2)
        self.assertEqual(self.calc.modulo(-5, 4) -1)

if __name__ == '__main__':
    unittest.main()