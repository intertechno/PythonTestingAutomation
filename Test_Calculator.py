import unittest
from Calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        calc = SimpleCalculator(10, 5)
        self.assertEqual(calc.add(), 15)

    def test_subtract(self):
        calc = SimpleCalculator(10, 5)
        self.assertEqual(calc.subtract(), 5)

    def test_multiply(self):
        calc = SimpleCalculator(10, 5)
        self.assertEqual(calc.multiply(), 50)

    def test_divide(self):
        calc = SimpleCalculator(10, 5)
        self.assertEqual(calc.divide(), 2)

    def test_divide_by_zero(self):
        calc = SimpleCalculator(10, 0)
        with self.assertRaises(ValueError):
            calc.divide()

if __name__ == '__main__':
    unittest.main()
