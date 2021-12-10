import unittest
from pathlib import Path

from day10 import syntax_scoring, syntax_scoring_autocomplete
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay10(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return syntax_scoring(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(26397, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(364389, result)

    def test_part_two(self):
        def get_result(i): return syntax_scoring_autocomplete(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(288957, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(2870201088, result)


if __name__ == '__main__':
    unittest.main()
