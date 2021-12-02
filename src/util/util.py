from typing import Generator


def read_lines(filename: str) -> Generator[str, None, None]:
    with open(filename) as file:
        while line := file.readline().rstrip():
            if line:
                yield line


def read_mock_input(mock_input: str) -> Generator[str, None, None]:
    for line in mock_input.split("\n"):
        line = line.rstrip()
        if line:
            yield line
