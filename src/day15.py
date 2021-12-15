from typing import Generator


def chiton(in_data: Generator[str, None, None], tiles: int = 1) -> int:
    nodes = {}
    for x, line in enumerate(list(in_data)):
        for y, value in enumerate(line):
            nodes[(x, y)] = int(value)

    last_x = list(map(lambda it: it[0], list(nodes.keys())))[-1]
    last_y = list(map(lambda it: it[1], list(nodes.keys())))[-1]
    additional_nodes = {}
    for (x, y), value in nodes.items():
        if tiles > 1:
            for x_tile in range(0, tiles):
                for y_tile in range(0, tiles):
                    if x_tile == 0 and y_tile == 0:
                        continue
                    a = x + (x_tile * (last_x + 1))
                    b = y + (y_tile * (last_y + 1))
                    additional_nodes[(a, b)] = max(1, wrap_9(value + x_tile + y_tile))
    nodes.update(additional_nodes)

    last_x = list(map(lambda it: it[0], list(nodes.keys())))[-1]
    last_y = list(map(lambda it: it[1], list(nodes.keys())))[-1]
    start = 0, 0
    target = last_x, last_y

    open = set()
    open.add(start)
    closed = set()
    current = start

    g = {start: 0}
    f = {start: get_h(start, target)}
    prev = {start: start}
    while current != target:
        neighbors = get_neighbors(current, target[0], target[1])
        neighbors = neighbors - closed
        open.update(neighbors)
        for neighbor in neighbors:
            neighbor_f = get_h(neighbor, target) + g[current]
            if neighbor not in f or neighbor_f < f[neighbor]:
                f[neighbor] = neighbor_f
                prev[neighbor] = current
        closed.add(current)
        open.remove(current)
        current = sorted(open, key=f.get)[0]
        g[current] = g[prev[current]] + nodes[current]

    return g[target]


def wrap_9(it):
    return it if it <= 9 else it % 9


def get_h(point, target):
    return ((target[0] - point[0]) ** 2 + (target[1] - point[1]) ** 2) ** (1 / 2)


def get_neighbors(p, x_max, y_max):
    n = [
        (p[0], p[1] + 1),
        (p[0], p[1] - 1),
        (p[0] + 1, p[1]),
        (p[0] - 1, p[1]),
    ]
    return set(filter(lambda it: 0 <= it[0] <= x_max and 0 <= it[1] <= y_max, n))
