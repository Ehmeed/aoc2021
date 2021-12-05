from pathlib import Path
from typing import Generator

from util.util import read_lines
import re
from collections import defaultdict

filename = Path(__file__).stem

_line_pattern = re.compile("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")


def hydrothermal_venture(in_data: Generator[str, None, None]) -> int:
    counter = defaultdict(int)
    for line in in_data:
        x1, y1, x2, y2 = _line_pattern.match(line).groups()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 == x2:
            y1, y2 = sorted([y1, y2])
            for y_n in range(y1, y2 + 1):
                count = counter[(x1, y_n)]
                counter[(x1, y_n)] = count + 1
        elif y1 == y2:
            x1, x2 = sorted([x1, x2])
            for x_n in range(x1, x2 + 1):
                count = counter[(x_n, y1)]
                counter[(x_n, y1)] = count + 1
    return len([it for it in counter.values() if it >= 2])


def hydrothermal_venture_all(in_data: Generator[str, None, None]) -> int:
    counter = defaultdict(int)
    for line in in_data:
        x1, y1, x2, y2 = _line_pattern.match(line).groups()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 == x2:
            y1, y2 = sorted([y1, y2])
            for y_n in range(y1, y2 + 1):
                count = counter[(x1, y_n)]
                counter[(x1, y_n)] = count + 1
        elif y1 == y2:
            x1, x2 = sorted([x1, x2])
            for x_n in range(x1, x2 + 1):
                count = counter[(x_n, y1)]
                counter[(x_n, y1)] = count + 1
        else:
            if x1 < x2:
                x_step = 1
                x_add = 1
            else:
                x_step = -1
                x_add = -1
            if y1 < y2:
                y_step = 1
                y_add = 1
            else:
                y_step = -1
                y_add = -1

            x_range = range(x1, x2 + x_add, x_step)
            y_range = range(y1, y2 + y_add, y_step)

            for x, y in zip(x_range, y_range):
                count = counter[(x, y)]
                counter[(x, y)] = count + 1

    return len([it for it in counter.values() if it >= 2])


if __name__ == "__main__":
    print(hydrothermal_venture(read_lines(filename)))
    print(hydrothermal_venture_all(read_lines(filename)))
