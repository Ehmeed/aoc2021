from typing import Generator, Set
from collections import defaultdict, deque


def passage_pathing(in_data: Generator[str, None, None]) -> int:
    paths: dict[str, list[str]] = defaultdict(list)
    for line in in_data:
        f, t = line.split("-")
        paths[f].append(t)
        paths[t].append(f)

    valid_paths = []
    to_visit = deque([['start']])
    while to_visit:
        current_path = to_visit.pop()
        next_to_visit = current_path[-1]

        if next_to_visit == 'end':
            valid_paths.append(list(current_path))
        else:
            for path_from_here in paths[next_to_visit]:
                if path_from_here not in current_path or path_from_here.lower() != path_from_here:
                    to_visit.append(list(current_path) + [path_from_here])

    return len(valid_paths)


def passage_pathing_double(in_data: Generator[str, None, None]) -> int:
    paths: dict[str, list[str]] = defaultdict(list)
    for line in in_data:
        f, t = line.split("-")
        if t != 'start':
            paths[f].append(t)
        if f != 'start':
            paths[t].append(f)

    valid_paths = []
    to_visit = deque([(['start'], False)])
    while to_visit:
        current_path, did_double_visit = to_visit.pop()
        next_to_visit = current_path[-1]
        if next_to_visit == 'end':
            valid_paths.append(current_path)
        else:
            for path_from_here in paths[next_to_visit]:
                if path_from_here not in current_path or path_from_here.lower() != path_from_here or not did_double_visit:
                    dw = path_from_here.lower() == path_from_here and path_from_here in current_path or did_double_visit
                    to_visit.append((current_path + [path_from_here], dw))

    return len(valid_paths)
