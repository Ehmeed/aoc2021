from typing import Generator
from collections import Counter, defaultdict


def lanternfish(in_data: Generator[str, None, None], days: int) -> int:
    fish = list(map(int, next(in_data).split(",")))
    fish = Counter(fish)
    for _ in range(days):
        new_fish = defaultdict(int)
        for dtr, count in fish.items():
            new_dtr = dtr - 1
            if new_dtr < 0:
                new_fish[8] += count
                new_fish[6] += count
            else:
                new_fish[new_dtr] += count
        fish = new_fish
    return sum(fish.values())
