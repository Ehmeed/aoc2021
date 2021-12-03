from typing import Generator

INPUT_ROOT = '/home/ehmeed/repos/aoc2021/input/'


def read_lines(filename: str) -> Generator[str, None, None]:
    with open(INPUT_ROOT + filename) as file:
        while line := file.readline().rstrip():
            if line:
                yield line
