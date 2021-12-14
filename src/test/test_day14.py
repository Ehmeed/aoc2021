import unittest
from pathlib import Path

from day14 import extended_polymerization
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay14(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return extended_polymerization(read_lines(i), steps=10)
        test_result = get_result(test_filename)
        self.assertEqual(1588, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(3906, result)

    def test_part_two(self):
        def get_result(i): return extended_polymerization(read_lines(i), steps=40)
        test_result = get_result(test_filename)
        self.assertEqual(2188189693529, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(4441317262452, result)


if __name__ == '__main__':
    unittest.main()
