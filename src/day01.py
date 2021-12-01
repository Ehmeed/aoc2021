import sys
from collections import deque

filename = '../input/day01'


def count_increasing_sliding_windows(window_size: int) -> int:
    queue = deque()
    n_increases = 0
    last_sum = sys.maxsize
    with open(filename) as file:
        while line := file.readline().rstrip():
            if line:
                queue.append(int(line))
                if len(queue) == window_size:
                    current_sum = sum(queue)
                    if current_sum > last_sum:
                        n_increases += 1
                    last_sum = current_sum
                    queue.popleft()

    return n_increases


print(count_increasing_sliding_windows(window_size=1))
print(count_increasing_sliding_windows(window_size=3))
