from pathlib import Path

from util.util import read_lines
from day01 import count_increasing_sliding_windows

import unittest

filename = Path(__file__).stem


class TestDay1(unittest.TestCase):

    def test_part_one(self):
        in_data = read_lines(filename)
        n_increases = count_increasing_sliding_windows(in_data, window_size=1)
        self.assertEqual(n_increases, 7)

    def test_part_two(self):
        in_data = read_lines(filename)
        n_increases = count_increasing_sliding_windows(in_data, window_size=3)
        self.assertEqual(n_increases, 5)


if __name__ == '__main__':
    unittest.main()
