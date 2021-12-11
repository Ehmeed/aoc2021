from typing import Generator, Union
from itertools import product
import numpy as np
from functools import reduce


def dumbo_octopus(in_data: Generator[str, None, None], end_condition: Union[int, str]) -> int:
    octopi = np.array([list(map(int, line)) for line in in_data])
    total_flashes = 0
    step = 0
    while True:
        step += 1
        octopi += 1
        flashed_count = 1
        flashed_this_step = np.zeros(octopi.shape, dtype='int')
        while flashed_count > 0:
            over_9 = ((octopi > 9) & (flashed_this_step == 0)).astype('int')
            flashed_this_step += over_9
            flashed_count = over_9.sum()
            total_flashes += flashed_count
            if end_condition == 'all' and flashed_this_step.all():
                return step
            flashed = np.pad(over_9, 1, mode='constant', constant_values=0)
            octopi += reduce(
                lambda acc, el: acc + np.roll(flashed, (el[0], el[1]), (1, 0)),
                product([-1, 0, 1], repeat=2),
                np.zeros(flashed.shape, dtype='int'))[1:-1, 1:-1]
        octopi *= np.invert(flashed_this_step.astype('bool'))
        if end_condition == step:
            return total_flashes
