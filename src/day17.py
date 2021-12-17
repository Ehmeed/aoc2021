from typing import Generator, Tuple
import re
from collections import namedtuple

pattern = re.compile("target area: x=([-0-9]+)\.\.([-0-9]+), y=([-0-9]+)..([-0-9]+)")

Position = namedtuple('Position', 'x y')
Velocity = namedtuple('Velocity', 'x y')


def tricky_shot(in_data: Generator[str, None, None], return_max_y: bool = True) -> int:
    x1, x2, y1, y2 = map(int, pattern.match(next(in_data)).groups())
    velocities = [Velocity(x, y) for x in range(x2+1) for y in range(y1, -y1)]

    results = []
    for velocity in velocities:
        position = Position(0, 0)
        max_y = position.y
        while not ((velocity.x == 0 and position.y < y1) or (velocity.x >= 0 and position.x > x2)):
            position, velocity = _step(position, velocity)
            max_y = max(max_y, position.y)
            if x1 <= position.x <= x2 and y1 <= position.y <= y2:
                results.append((max_y, velocity))
                break

    if return_max_y:
        return sorted(results, key=lambda it: it[0])[-1][0]
    else:
        return len(results)


def _step(position: Position, velocity: Velocity) -> Tuple[Position, Velocity]:
    new_position = Position(position.x + velocity.x, position.y + velocity.y)
    new_vel_x = 0
    if velocity.x > 0:
        new_vel_x = velocity.x - 1
    elif velocity.x < 0:
        new_vel_x = velocity.x + 1
    new_velocity = Velocity(new_vel_x, velocity.y - 1)
    return new_position, new_velocity
