import unittest
from pathlib import Path

from util.util import read_lines
from day04 import day4

filename = Path(__file__).stem


class TestDay4(unittest.TestCase):

    def test_part_one(self):
        in_data = read_lines(filename)
        final_position = day4(in_data)
        self.assertEqual(final_position, -1)

if __name__ == '__main__':
    unittest.main()
