from typing import Generator
from functools import reduce


def smoke_basin(in_data: Generator[str, None, None]) -> int:
    lines = []
    s = 0
    for line in in_data:
        lines.append(list(map(int, line)))
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            p = lines[x][y]
            if x <= len(lines) - 2 and p >= lines[x + 1][y]:
                continue
            if x > 0 and p >= lines[x - 1][y]:
                continue
            if y <= len(lines[0]) - 2 and p >= lines[x][y + 1]:
                continue
            if y > 0 and p >= lines[x][y - 1]:
                continue
            s += p + 1
    return s


def smoke_basin_sizes(in_data: Generator[str, None, None]) -> int:
    lines = []
    basins = []
    for line in in_data:
        lines.append(list(map(int, line)))
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            p = lines[x][y]
            if x <= len(lines) - 2 and p >= lines[x + 1][y]:
                continue
            if x > 0 and p >= lines[x - 1][y]:
                continue
            if y <= len(lines[0]) - 2 and p >= lines[x][y + 1]:
                continue
            if y > 0 and p >= lines[x][y - 1]:
                continue
            basins.append(len(_flood(x, y, lines)))

    return reduce(lambda a,b: a*b, sorted(basins)[-3:])


def _flood(x, y, lines):
    p = lines[x][y]
    if p == 9:
        return []
    basin = [p]
    lines[x][y] = 9
    if x <= len(lines) - 2 and p < lines[x + 1][y]:
        basin.extend(_flood(x+1, y, lines))
    if x > 0 and p < lines[x - 1][y]:
        basin.extend(_flood(x -1, y, lines))
    if y <= len(lines[0]) - 2 and p < lines[x][y + 1]:
        basin.extend(_flood(x, y + 1, lines))
    if y > 0 and p < lines[x][y - 1]:
        basin.extend(_flood(x, y - 1, lines))

    return basin
