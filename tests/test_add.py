import unittest

from day4.sumlist import recursive_list_sum


class sum(unittest.TestCase):
    def test_sum_is_succesful(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, 4]]), 10)


if __name__ == '__main__':
    unittest.main()
