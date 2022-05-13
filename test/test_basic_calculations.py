import unittest
from basic_calculator.TestCalculator import TestCalculator


class TestBasicCalculations(unittest.TestCase):
    def test_add(self):
        print(" testing test_add in TestBasicCalculations ")
        self.assertEqual(TestCalculator.add(1, 2), 3)

    def test_addval(self):
        print(" testing test_addval in TestBasicCalculations ")
        calculator = TestCalculator(1, 2)
        self.assertEqual(calculator.addval(), 3)

    def test_addval2(self):
        print(" testing test_addval2 in TestBasicCalculations ")
        self.assertEqual(TestCalculator.addval2(3, 5), 8)


if __name__ == "__main__":
    unittest.main()
