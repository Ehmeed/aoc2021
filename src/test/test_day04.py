import unittest
from pathlib import Path

from util.util import read_lines
from day04 import giant_squid

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay4(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return giant_squid(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(4512, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(8136, result)

    def test_part_two(self):
        def get_result(i): return giant_squid(read_lines(i), last_wins=True)
        test_result = get_result(test_filename)
        self.assertEqual(1924, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(12738, result)


if __name__ == '__main__':
    unittest.main()
