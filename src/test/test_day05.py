import unittest
from pathlib import Path

from day05 import hydrothermal_venture, hydrothermal_venture_all
from util.util import read_lines

filename = Path(__file__).stem


class TestDay5(unittest.TestCase):

    def test_part_one(self):
        in_data = read_lines(filename)
        result = hydrothermal_venture(in_data)
        self.assertEqual(5, result)

    def test_part_two(self):
        in_data = read_lines(filename)
        result = hydrothermal_venture_all(in_data)
        self.assertEqual(12, result)


if __name__ == '__main__':
    unittest.main()
