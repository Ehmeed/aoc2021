import unittest
from pathlib import Path

from day07 import treachery_of_whales, treachery_of_whales_progressive
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay07(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return treachery_of_whales(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(37, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(328187, result)

    def test_part_two(self):
        def get_result(i): return treachery_of_whales_progressive(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(168, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(91257582, result)


if __name__ == '__main__':
    unittest.main()
