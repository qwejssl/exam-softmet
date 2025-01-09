"""
Unit tests for the split_fractional_part function in modf_logic.py.
Uses standard Python unittest framework.
"""

import unittest
from modf_example.modf_logic import split_fractional_part


class TestModfLogic(unittest.TestCase):
    """
    Test class for validating the split_fractional_part function
    from the modf_logic module.
    """

    def test_zero(self):
        """
        Test that passing 0 returns fractional=0.0, integer=0.0.
        """
        frac, integer = split_fractional_part(0)
        self.assertEqual(frac, 0.0)
        self.assertEqual(integer, 0.0)

    def test_positive_number(self):
        """
        Test a positive decimal number (3.75) returns
        fractional=0.75, integer=3.0.
        """
        frac, integer = split_fractional_part(3.75)
        self.assertAlmostEqual(frac, 0.75, places=7)
        self.assertEqual(integer, 3.0)

    def test_negative_number(self):
        """
        Test a negative decimal number (-2.5) returns
        fractional=-0.5, integer=-2.0.
        """
        frac, integer = split_fractional_part(-2.5)
        self.assertAlmostEqual(frac, -0.5, places=7)
        self.assertEqual(integer, -2.0)

    def test_whole_number(self):
        """
        Test a whole number (5) returns fractional=0.0,
        integer=5.0.
        """
        frac, integer = split_fractional_part(5)
        self.assertEqual(frac, 0.0)
        self.assertEqual(integer, 5.0)

    def test_large_number(self):
        """
        Test a large decimal number with many fractional digits,
        ensuring we account for floating-point precision.
        """
        value = 123456789.987654321
        frac, integer = split_fractional_part(value)
        self.assertAlmostEqual(frac, 0.987654321, delta=1e-8)
        self.assertEqual(integer, 123456789.0)


if __name__ == '__main__':
    unittest.main()
