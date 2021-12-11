import unittest
from pathlib import Path

from day11 import dumbo_octopus
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay11(unittest.TestCase):
    def test_part_one(self):
        def get_result(i): return dumbo_octopus(read_lines(i), end_condition=100)
        test_result = get_result(test_filename)
        self.assertEqual(1656, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(1700, result)

    def test_part_two(self):
        def get_result(i): return dumbo_octopus(read_lines(i), end_condition='all')
        test_result = get_result(test_filename)
        self.assertEqual(195, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(273, result)


if __name__ == '__main__':
    unittest.main()
