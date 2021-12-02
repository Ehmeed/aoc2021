import unittest

from util.util import read_mock_input
from day02 import final_position_multiplied, final_position_multiplied_with_aim


class TestDay2(unittest.TestCase):

    def test_part_one(self):
        mock_input_data = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
        mock_input = read_mock_input(mock_input_data)
        final_position = final_position_multiplied(mock_input)
        self.assertEqual(final_position, 150)

    def test_part_two(self):
        mock_input_data = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
        mock_input = read_mock_input(mock_input_data)
        final_position = final_position_multiplied_with_aim(mock_input)
        self.assertEqual(final_position, 900)

if __name__ == '__main__':
    unittest.main()
