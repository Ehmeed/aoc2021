import unittest
from pathlib import Path

from day17 import tricky_shot
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay17(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return tricky_shot(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(45, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(5778, result)

    def test_part_two(self):
        def get_result(i): return tricky_shot(read_lines(i), return_max_y=False)
        test_result = get_result(test_filename)
        self.assertEqual(112, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(2576, result)


if __name__ == '__main__':
    unittest.main()
