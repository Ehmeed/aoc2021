import unittest
from pathlib import Path

from day12 import passage_pathing, passage_pathing_double
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay12(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return passage_pathing(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(10, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(5228, result)

    def test_part_two(self):
        def get_result(i): return passage_pathing_double(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(36, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(131228, result)


if __name__ == '__main__':
    unittest.main()
