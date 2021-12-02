from util.util import read_mock_input
from day01 import count_increasing_sliding_windows

import unittest


class TestDay1(unittest.TestCase):

    def test_part_one(self):
        mock_input_data = """199
200
208
210
200
207
240
269
260
263
"""
        mock_input = read_mock_input(mock_input_data)
        n_increases = count_increasing_sliding_windows(mock_input, window_size=1)
        self.assertEqual(n_increases, 7)

    def test_part_two(self):
        mock_input_data = """199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    """
        mock_input = read_mock_input(mock_input_data)
        n_increases = count_increasing_sliding_windows(mock_input, window_size=3)
        self.assertEqual(n_increases, 5)


if __name__ == '__main__':
    unittest.main()