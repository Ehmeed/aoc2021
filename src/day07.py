from typing import Generator
import statistics
import numpy as np
from functools import lru_cache


def treachery_of_whales(in_data: Generator[str, None, None]) -> int:
    positions = list(map(int, next(in_data).split(",")))
    median = round(statistics.median(positions))
    return sum([abs(it - median) for it in positions])


def treachery_of_whales_progressive(in_data: Generator[str, None, None]) -> int:
    positions = list(map(int, next(in_data).split(",")))
    max_pos = max(positions)
    costs = []
    for position in positions:
        pos_costs = []
        for idx in range(max_pos + 1):
            pos_costs.append(sum_below(abs(position - idx)))
        costs.append(pos_costs)

    costs_sum = np.array(costs).sum(axis=0)
    return costs_sum[np.argmin(costs_sum)]


@lru_cache(maxsize=1_000_000)
def sum_below(i: int) -> int:
    return sum(range(0, i + 1))
