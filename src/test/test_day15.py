import unittest
from pathlib import Path

from day15 import chiton
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay15(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return chiton(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(40, test_result)

        result = get_result(filename)
        print(f"Part one result: {result}")
        self.assertEqual(487, result)

    def test_part_two(self):
        def get_result(i): return chiton(read_lines(i), tiles=5)
        test_result = get_result(test_filename)
        self.assertEqual(315, test_result)

        result = get_result(filename)
        print(f"Part two result: {result}")
        # self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
