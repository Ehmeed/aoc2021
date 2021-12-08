from typing import Generator


def seven_segment_search(in_data: Generator[str, None, None]) -> int:
    udc = [2, 3, 4, 7]
    total_unique_output_digits = 0
    for line in in_data:
        signals, outputs = line.split(" | ")
        outputs = outputs.split(" ")
        unique_output_digits = [it for it in outputs if len(it) in udc]
        total_unique_output_digits += len(unique_output_digits)
    return total_unique_output_digits


def seven_segment_search_sum(in_data: Generator[str, None, None]) -> int:
    d_lens = {
        2: {1},
        3: {7},
        4: {4},
        5: {2, 3, 5},
        6: {0, 6, 9},
        7: {8}
    }
    decoded = []
    # 1 4 7 8
    for line in in_data:
        candidates = [set(range(10)) for _ in range(10)]
        signals, outputs = line.split(" | ")
        signals = signals.split(" ")
        outputs = outputs.split(" ")
        for idx, signal in enumerate(signals):
            candidates[idx] &= d_lens[len(signal)]

        one_signal = signals[candidates.index({1})]

        for idx, signal in enumerate(signals):
            if candidates[idx] == {2, 3, 5}:
                candidates[idx] = {2, 5}
                if len(set(one_signal) & set(signal)) == 2:
                    candidates[idx] = {3}

        three_signal = signals[candidates.index({3})]
        for idx, signal in enumerate(signals):
            if candidates[idx] == {0, 6, 9}:
                candidates[idx] = {0, 6}
                if len(set(three_signal) & set(signal)) == 5:
                    candidates[idx] = {9}

        nine_signal = signals[candidates.index({9})]
        for idx, signal in enumerate(signals):
            if candidates[idx] == {2, 5}:
                candidates[idx] = {5}
                if len(set(nine_signal) & set(signal)) == 4:
                    candidates[idx] = {2}

        five_signal = signals[candidates.index({5})]
        for idx, signal in enumerate(signals):
            if candidates[idx] == {0, 6}:
                candidates[idx] = {0}
                if len(set(five_signal) & set(signal)) == 5:
                    candidates[idx] = {6}

        signals = ["".join(sorted(signal)) for signal in signals]
        outputs = ["".join(sorted(output)) for output in outputs]
        number = ""
        for output in outputs:
            number += str(next(iter(candidates[signals.index(output)])))
        decoded.append(int(number))
    return sum(decoded)
