import sys
from collections import deque
from pathlib import Path
from typing import Generator
from util.util import read_lines

filename = Path(__file__).stem


def count_increasing_sliding_windows(in_data: Generator[str, None, None], window_size: int) -> int:
    queue = deque()
    n_increases = 0
    last_sum = sys.maxsize
    for line in in_data:
        queue.append(int(line))
        if len(queue) == window_size:
            current_sum = sum(queue)
            if current_sum > last_sum:
                n_increases += 1
            last_sum = current_sum
            queue.popleft()

    return n_increases


if __name__ == "__main__":
    print(count_increasing_sliding_windows(in_data=read_lines(filename), window_size=1))
    print(count_increasing_sliding_windows(in_data=read_lines(filename), window_size=3))
