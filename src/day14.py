from typing import Generator
from collections import Counter, defaultdict
import re

from more_itertools import windowed

rule_regex = re.compile("(.)(.) -> (.)")


def extended_polymerization(in_data: Generator[str, None, None], steps: int) -> int:
    counter = Counter(list(windowed(next(in_data), n=2)))
    left_most = list(counter.keys())[0][0]
    right_most = list(counter.keys())[-1][-1]
    next(in_data)
    rules = {}
    for line in in_data:
        a, b, p = rule_regex.match(line).groups()
        rules[(a, b)] = p
    for step in range(steps):
        new_counter = defaultdict(int)
        for pair, pair_count in counter.items():
            if rule := rules[pair]:
                new_counter[pair[0], rule] += pair_count
                new_counter[rule, pair[1]] += pair_count
            else:
                new_counter[pair] = pair_count
        counter = new_counter

    total = defaultdict(int)
    for key, value in counter.items():
        total[key[0]] += value
        total[key[1]] += value
    total[left_most] += 1
    total[right_most] += 1
    total = {key: value / 2 for key, value in total.items()}

    return int(max(total.values()) - min(total.values()))
