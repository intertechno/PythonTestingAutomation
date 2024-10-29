import pytest
from calculator import SimpleCalculator

def test_add():
    calc = SimpleCalculator(10, 5)
    assert calc.add() == 15

def test_subtract():
    calc = SimpleCalculator(10, 5)
    assert calc.subtract() == 5

def test_multiply():
    calc = SimpleCalculator(10, 5)
    assert calc.multiply() == 50

def test_divide():
    calc = SimpleCalculator(10, 5)
    assert calc.divide() == 2

def test_divide_by_zero():
    calc = SimpleCalculator(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide()

# ----------------------------------------
# import unittest
# from calculator import SimpleCalculator

# class TestSimpleCalculator(unittest.TestCase):

#     def test_add(self):
#         calc = SimpleCalculator(10, 5)
#         self.assertEqual(calc.add(), 15)

#     def test_subtract(self):
#         calc = SimpleCalculator(10, 5)
#         self.assertEqual(calc.subtract(), 5)

#     def test_multiply(self):
#         calc = SimpleCalculator(10, 5)
#         self.assertEqual(calc.multiply(), 50)

#     def test_divide(self):
#         calc = SimpleCalculator(10, 5)
#         self.assertEqual(calc.divide(), 2)

#     def test_divide_by_zero(self):
#         calc = SimpleCalculator(10, 0)
#         with self.assertRaises(ValueError):
#             calc.divide()

# if __name__ == '__main__':
#     unittest.main()
