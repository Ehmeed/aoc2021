import unittest
from pathlib import Path

from day06 import lanternfish
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay06(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return lanternfish(read_lines(i), days=80)
        test_result = get_result(test_filename)
        self.assertEqual(5934, test_result)

        result = get_result(filename)
        print(result)
        # self.assertEqual(None, result)

    def test_part_two(self):
        def get_result(i): return lanternfish(read_lines(i), days=256)
        test_result = get_result(test_filename)
        self.assertEqual(26984457539, test_result)

        result = get_result(filename)
        print(result)
        # self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
