from functools import reduce
from typing import Generator, Tuple


def packet_decoder(in_data: Generator[str, None, None], return_version=True) -> int:
    line = next(in_data)
    expected_len = len(line) * 4
    line = bin(int(line, 16))[2:]
    line = ((expected_len - len(line)) * "0") + line

    if return_version:
        value, _ = parse_packet_version(line)
    else:
        value, _ = parse_packet_full(line)
    return value


def parse_packet_full(line) -> Tuple[int, str]:
    packet_value = 0
    if not line or int(line, 2) == 0:
        return packet_value, ""
    version, line = head(line, 3)
    type_id, line = head(line, 3)
    type_id = int(type_id, 2)
    if type_id == 4:
        literal_value = ''
        while True:
            group, line = head(line, 5)
            group_prefix, group_value = head(group, 1)
            literal_value += group_value
            if group_prefix == "0":
                break
        return int(literal_value, 2), line
    else:
        length_type_id, line = head(line, 1)
        subpacket_values = []
        if length_type_id == "0":
            total_subpacket_length, line = head(line, 15)
            total_subpacket_length = int(total_subpacket_length, 2)
            expected_len_left = len(line) - total_subpacket_length
            while len(line) > expected_len_left:
                subpacket_value, line = parse_packet_full(line)
                subpacket_values.append(subpacket_value)
        else:
            subpacket_count, line = head(line, 11)
            subpacket_count = int(subpacket_count, 2)
            for _ in range(subpacket_count):
                subpacket_value, line = parse_packet_full(line)
                subpacket_values.append(subpacket_value)

        if type_id == 0:
            return sum(subpacket_values), line
        elif type_id == 1:
            return reduce(lambda a, b: a*b, subpacket_values), line
        elif type_id == 2:
            return min(subpacket_values), line
        elif type_id == 3:
            return max(subpacket_values), line
        elif type_id == 5:
            return 1 if subpacket_values[0] > subpacket_values[1] else 0, line
        elif type_id == 6:
            return 1 if subpacket_values[0] < subpacket_values[1] else 0, line
        elif type_id == 7:
            return 1 if subpacket_values[0] == subpacket_values[1] else 0, line
    return packet_value, line


def parse_packet_version(line) -> Tuple[int, str]:
    if not line or int(line, 2) == 0:
        return 0, ""
    version_sum = 0
    version, line = head(line, 3)
    type_id, line = head(line, 3)
    version_sum += int(version, 2)
    type_id = int(type_id, 2)
    if type_id == 4:
        packet_value = ''
        while True:
            group, line = head(line, 5)
            group_prefix, group_value = head(group, 1)
            packet_value += group_value
            if group_prefix == "0":
                break
        packet_value = int(packet_value, 2)
    else:
        length_type_id, line = head(line, 1)
        if length_type_id == "0":
            total_subpacket_length, line = head(line, 15)
            total_subpacket_length = int(total_subpacket_length, 2)
            while len(line) > 0:
                version_value, line = parse_packet_version(line)
                version_sum += version_value
        else:
            subpacket_count, line = head(line, 11)
            subpacket_count = int(subpacket_count, 2)
            for _ in range(subpacket_count):
                version_value, line = parse_packet_version(line)
                version_sum += version_value
    return version_sum, line


def head(it: str, n: int) -> Tuple[str, str]:
    return it[:n], it[n:]
