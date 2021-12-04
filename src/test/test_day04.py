import unittest
from pathlib import Path

from util.util import read_lines
from day04 import giant_squid

filename = Path(__file__).stem


class TestDay4(unittest.TestCase):

    def test_part_one(self):
        in_data = read_lines(filename)
        result = giant_squid(in_data)
        self.assertEqual(result, 4512)

    def test_part_two(self):
        in_data = read_lines(filename)
        result = giant_squid(in_data, last_wins=True)
        self.assertEqual(result, 1924)

if __name__ == '__main__':
    unittest.main()
