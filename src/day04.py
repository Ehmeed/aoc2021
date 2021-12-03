from pathlib import Path
from typing import Generator

from util.util import read_lines

filename = Path(__file__).stem


def day4(in_data: Generator[str, None, None]) -> int:
    return 0



if __name__ == "__main__":
    print(day4(read_lines(filename)))
