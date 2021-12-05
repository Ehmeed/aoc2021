import unittest
from pathlib import Path

from dayN import day_n
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDayN(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return day_n(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(999, test_result)

        result = get_result(filename)
        print(result)
        # self.assertEqual(None, result)

    def test_part_two(self):
        def get_result(i): return day_n(read_lines(i))
        test_result = get_result(test_filename)
        # self.assertEqual(None, test_result)

        result = get_result(filename)
        print(result)
        # self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
