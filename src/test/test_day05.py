import unittest
from pathlib import Path

from day05 import hydrothermal_venture, hydrothermal_venture
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay5(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return hydrothermal_venture(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(5, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(5442, result)

    def test_part_two(self):
        def get_result(i): return hydrothermal_venture(read_lines(i), include_diagonals=True)
        test_result = get_result(test_filename)
        self.assertEqual(12, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(19571, result)


if __name__ == '__main__':
    unittest.main()
