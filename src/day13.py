from typing import Generator
import numpy as np


def transparent_origami(in_data: Generator[str, None, None], return_dot_count: bool) -> int:
    points_raw = []
    folds = []
    max_x = 0
    max_y = 0
    m_max = np.vectorize(max)
    for line in in_data:
        if ',' in line:
            x, y = line.split(",")
            x, y = int(x), int(y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            points_raw.append((x, y))
        elif '=' in line:
            axis, value = line[len("fold along "):].split("=")
            folds.append((axis, int(value)))

    points = np.zeros(shape=(max_y + 1, max_x + 1))
    for x, y in points_raw:
        points[y][x] = 1
    for idx, fold in enumerate(folds):
        if return_dot_count and idx == 1:
            return int(points.sum())
        axis, value = fold
        if axis == 'y':
            top = points[:value, :]
            bottom = points[value + 1:, :][::-1, ::]
            diff = top.shape[0] - bottom.shape[0]
            if diff > 0:
                bottom = np.vstack([np.zeros(shape=(diff, points.shape[1])), bottom])
            elif diff < 0:
                bottom = bottom[abs(diff):, :]
            points = m_max(top, bottom)

        else:
            left = points[:, :value]
            right = points[:, value + 1:][::, ::-1]
            diff = left.shape[1] - right.shape[1]
            if diff > 0:
                right = np.hstack([np.zeros(shape=(points.shape[0], diff)), right])
            elif diff < 0:
                right = right[:, abs(diff):]
            points = m_max(left, right)
    _print(points)


def _print(points):
    for y in range(len(points)):
        for x in range(len(points[0])):
            if int(points[y][x]) == 1:
                print('#', end='')
            else:
                print('.', end='')

        print()
