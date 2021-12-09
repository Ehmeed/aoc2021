import unittest
from pathlib import Path

from day09 import smoke_basin, smoke_basin_sizes
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay09(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return smoke_basin(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(15, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(558, result)

    def test_part_two(self):
        def get_result(i): return smoke_basin_sizes(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(1134, test_result)

        result = get_result(filename)
        print(result)
        # self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
