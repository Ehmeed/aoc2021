from pathlib import Path

from util.util import read_lines
from day01 import sonar_sweep

import unittest

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay1(unittest.TestCase):

    def test_part_one(self):
        def get_result(i): return sonar_sweep(read_lines(i), window_size=1)
        test_result = get_result(test_filename)
        self.assertEqual(7, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(1711, result)

    def test_part_two(self):
        def get_result(i): return sonar_sweep(read_lines(i), window_size=3)
        test_result = get_result(test_filename)
        self.assertEqual(5, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(1743, result)


if __name__ == '__main__':
    unittest.main()
