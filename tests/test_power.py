import unittest

from day4.power import power


class TestPower(unittest.TestCase):
    def test_power_is_successful(self):
        self.assertEqual(power(3, 4), 81)
        self.assertEqual(power(3, 3), 27)

    # def test_pow_positive_base_neg_exponent(self):
    #     self.assertEqual(power(3, -4), 81)
    #     self.assertEqual(power(3, -3), -27)


if __name__ == '__main__':
    unittest.main()
