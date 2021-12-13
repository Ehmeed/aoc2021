import sys
import unittest
from pathlib import Path

from day13 import transparent_origami
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay13(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return transparent_origami(read_lines(i), return_dot_count=True)
        test_result = get_result(test_filename)
        self.assertEqual(17, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(701, result)

    def test_part_two(self):
        def get_result(i): return transparent_origami(read_lines(i), return_dot_count=False)
        get_result(filename)
        print("Expected: FPEKBEJL")


if __name__ == '__main__':
    unittest.main()
