import unittest
from pathlib import Path

from day08 import seven_segment_search, seven_segment_search_sum
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay08(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return seven_segment_search(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(26, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(237, result)

    def test_part_two(self):
        def get_result(i): return seven_segment_search_sum(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(61229, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(1009098, result)


if __name__ == '__main__':
    unittest.main()
