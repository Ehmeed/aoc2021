import unittest
from pathlib import Path

from util.util import read_lines
from day02 import dive, dive_with_aim

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay2(unittest.TestCase):

    def test_part_one(self):
        def get_result(i): return dive(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(150, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(1762050, result)

    def test_part_two(self):
        def get_result(i): return dive_with_aim(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(900, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(1855892637, result)


if __name__ == '__main__':
    unittest.main()
