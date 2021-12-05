from pathlib import Path
from typing import Generator
import re

filename = Path(__file__).stem

_command_pattern = re.compile("([a-z]+) ([0-9]+)")


def dive(in_data: Generator[str, None, None]) -> int:
    x, y = 0, 0
    for line in in_data:
        match = _command_pattern.match(line)
        if not match:
            raise ValueError(f"Unknown command: {line}")
        command, length = match.groups()
        length = int(length)
        if command == 'forward':
            x += length
        elif command == "down":
            y += length
        elif command == "up":
            y -= length
    return x * y


def dive_with_aim(in_data: Generator[str, None, None]) -> int:
    x, y, aim = 0, 0, 0
    for line in in_data:
        match = _command_pattern.match(line)
        if not match:
            raise ValueError(f"Unknown command: {line}")
        command, length = match.groups()
        length = int(length)
        if command == 'forward':
            x += length
            y += aim * length
        elif command == "down":
            aim += length
        elif command == "up":
            aim -= length
    return x * y
