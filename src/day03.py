from typing import Generator
from collections import defaultdict

def binary_diagnostic(in_data: Generator[str, None, None]) -> int:
    counter = defaultdict(int)
    lines_count = 0
    for line in in_data:
        lines_count += 1
        for idx, digit in enumerate(line):
            counter[idx] += int(digit)
    gamma = 0
    epsilon = 0
    idx = 0
    for count in reversed(counter.values()):
        inc = 2 ** idx
        if count >= lines_count / 2:
            gamma += inc
        else:
            epsilon += inc
        idx += 1
    return int(gamma) * int(epsilon)


def binary_diagnostic_oxygen(in_data: Generator[str, None, None]) -> int:
    lines = []

    for line in in_data:
        lines.append(line)

    oxygen_number = _do_filter(lines)
    scrubber_number = _do_filter(lines, invert=True)
    return int(oxygen_number, 2) * int(scrubber_number, 2)


def _do_filter(lines, invert=False):
    n = 0
    while len(lines) > 1:
        lines_count = len(lines)
        s = 0
        for line in lines:
            s += int(line[n])
        if s >= lines_count / 2:
            f = "1"
        else:
            f = "0"
        if invert:
            lines = [line for line in lines if line[n] != f]
        else:
            lines = [line for line in lines if line[n] == f]
        n += 1
    assert len(lines) == 1
    return lines[0]
