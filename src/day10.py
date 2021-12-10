from typing import Generator
from collections import deque


def syntax_scoring(in_data: Generator[str, None, None]) -> int:
    pairs = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>',
    }
    points = {
        '}': 1197,
        ']': 57,
        ')': 3,
        '>': 25137,
    }
    opening = list(pairs.keys())
    total_points = 0
    for line in in_data:
        stack = deque()
        for l in list(line):
            if l in opening:
                stack.append(l)
            elif pairs[stack.pop()] == l:
                pass
            else:
                total_points += points[l]
                break

    return total_points


def syntax_scoring_autocomplete(in_data: Generator[str, None, None]) -> int:
    pairs = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>',
    }
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    opening = list(pairs.keys())
    scores = []
    for line in in_data:
        stack = deque()
        for l in list(line):
            if l in opening:
                stack.append(l)
            elif pairs[stack.pop()] == l:
                pass
            else:
                break
        else:
            if len(stack) > 0:
                score = 0
                while len(stack) > 0:
                    missing_a_pair = stack.pop()
                    score *= 5
                    score += points[pairs[missing_a_pair]]

                scores.append(score)

    return sorted(scores)[int(len(scores)/2)]
