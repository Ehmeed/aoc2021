import unittest
from pathlib import Path

from util.util import read_lines
from day03 import binary_diagnostic, binary_diagnostic_oxygen

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay3(unittest.TestCase):

    def test_part_one(self):
        def get_result(i): return binary_diagnostic(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(198, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(841526, result)

    def test_part_two(self):
        def get_result(i): return binary_diagnostic_oxygen(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(230, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(4790390, result)


if __name__ == '__main__':
    unittest.main()
