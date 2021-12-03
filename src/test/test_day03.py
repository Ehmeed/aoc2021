import unittest
from pathlib import Path

from util.util import read_lines
from day03 import binary_diagnostic, binary_diagnostic_oxygen

filename = Path(__file__).stem


class TestDay3(unittest.TestCase):

    def test_part_one(self):
        in_data = read_lines(filename)
        final_position = binary_diagnostic(in_data)
        self.assertEqual(final_position, 198)

    def test_part_two(self):
        in_data = read_lines(filename)
        final_position = binary_diagnostic_oxygen(in_data)
        self.assertEqual(final_position, 230)


if __name__ == '__main__':
    unittest.main()
