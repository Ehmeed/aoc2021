import unittest
from pathlib import Path

from util.util import read_lines
from day02 import final_position_multiplied, final_position_multiplied_with_aim

filename = Path(__file__).stem


class TestDay2(unittest.TestCase):

    def test_part_one(self):
        in_data = read_lines(filename)
        final_position = final_position_multiplied(in_data)
        self.assertEqual(final_position, 150)

    def test_part_two(self):
        in_data = read_lines(filename)
        final_position = final_position_multiplied_with_aim(in_data)
        self.assertEqual(final_position, 900)


if __name__ == '__main__':
    unittest.main()
