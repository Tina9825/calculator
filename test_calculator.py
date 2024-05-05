import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

  def test_add(self):
    self.assertEqual(add(5, 3), 8)
    self.assertEqual(add(-2, 10), 8)

  def test_subtract(self):
    self.assertEqual(subtract(10, 4), 6)
    self.assertEqual(subtract(2, -5), 7)

  def test_multiply(self):
    self.assertEqual(multiply(3, 4), 12)
    self.assertEqual(multiply(-2, 5), -10)

  def test_divide(self):
    self.assertEqual(divide(10, 2), 5)
    self.assertEqual(divide(6, -2), -3)
    self.assertEqual(divide(1, 0), "Error: Cannot divide by zero")

if __name__ == "__main__":
  unittest.main()
