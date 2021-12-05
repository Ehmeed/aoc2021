from typing import Generator


def giant_squid(in_data: Generator[str, None, None], last_wins=False) -> int:
    rows = 5
    lines = [it.rstrip() for it in in_data]
    numbers = list(map(int, lines[0].split(",")))

    boards = []
    n_boards = 1 + int((len(lines) - 2) / (rows + 1))
    for n in range(n_boards):
        boards.append(_load_board(lines[2 + (rows + 1) * n:]))

    n_winners = 0
    drawn = numbers[:rows]
    for number in numbers[rows:]:
        drawn.append(number)
        closed_boards = []
        for board_id, board in enumerate(boards):
            for row in board:
                if _is_winning(row, drawn):
                    board_score = score(board, drawn)
                    if not last_wins or n_winners == n_boards - 1:
                        return board_score
                    closed_boards.append(board_id)
            for n_col in range(len(board[0])):
                col = []
                for row in board:
                    col.append(row[n_col])
                if _is_winning(col, drawn):
                    board_score = score(board, drawn)
                    if not last_wins or n_winners == n_boards - 1:
                        return board_score
                    closed_boards.append(board_id)

        closed_boards = set(closed_boards)
        n_winners += len(closed_boards)
        for index in sorted(list(closed_boards), reverse=True):
            del boards[index]
    return -1


def score(board, drawn):
    us = 0
    for row in board:
        for number in row:
            if number not in drawn:
                us += number

    return us * drawn[-1]


def _is_winning(numbers, drawn):
    for number in numbers:
        if number not in drawn:
            return False
    return True


def _load_board(in_data) -> list[list[int]]:
    board = []
    for line in in_data:
        if not line:
            break
        board.append(list(map(int, [it for it in line.split(" ") if it])))
    return board
