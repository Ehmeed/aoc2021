import unittest
from pathlib import Path

from day18 import snailfish, _parse_number, _explode, _tolist, _split, _add, _magnitude, snailfish_largest_magnitude
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay18(unittest.TestCase):
    def test_part_one(self):
        for input, expected in [
            ('[[[[[9,8],1],2],3],4]', '[[[[0,9],2],3],4]'),
            ('[7,[6,[5,[4,[3,2]]]]]', '[7,[6,[5,[7,0]]]]'),
            ('[[6,[5,[4,[3,2]]]],1]', '[[6,[5,[7,0]]],3]'),
            ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),
            ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')
        ]:
            n = _parse_number(eval(input))
            nr = _tolist(_explode(n)[0])
            expected = _tolist(_parse_number(eval(expected)))
            self.assertEqual(expected, nr)
            pass

        a = [[[[4, 3], 4], 4], [7, [[8, 4], 9]]]
        b = [1, 1]

        r = _add(_parse_number(a), _parse_number(b))
        self.assertEqual([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], _tolist(r))

        self.assertEqual(143, _magnitude(_parse_number([[1, 2], [[3, 4], 5]])))
        self.assertEqual(1384, _magnitude(_parse_number([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])))
        self.assertEqual(445, _magnitude(_parse_number([[[[1, 1], [2, 2]], [3, 3]], [4, 4]])))
        self.assertEqual(791, _magnitude(_parse_number([[[[3, 0], [5, 3]], [4, 4]], [5, 5]])))
        self.assertEqual(1137, _magnitude(_parse_number([[[[5, 0], [7, 4]], [5, 5]], [6, 6]])))
        self.assertEqual(3488, _magnitude(_parse_number([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])))

        def get_result(i): return snailfish(read_lines(i))

        test_result = get_result(test_filename)
        self.assertEqual(4140, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(3734, result)

    def test_part_two(self):
        def get_result(i): return snailfish_largest_magnitude(read_lines(i))
        test_result = get_result(test_filename)
        self.assertEqual(3993, test_result)

        result = get_result(filename)
        print(result)
        self.assertEqual(4837, result)


if __name__ == '__main__':
    unittest.main()
