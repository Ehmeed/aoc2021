import unittest
from pathlib import Path

from day16 import packet_decoder
from util.util import read_lines

test_filename = Path(__file__).stem
filename = test_filename[len("test_"):]


class TestDay16(unittest.TestCase):
    def test_part_one(self):
        test_result = packet_decoder(iter(["8A004A801A8002F478"]))
        self.assertEqual(16, test_result)
        test_result = packet_decoder(iter(["620080001611562C8802118E34"]))
        self.assertEqual(12, test_result)
        test_result = packet_decoder(iter(["C0015000016115A2E0802F182340"]))
        self.assertEqual(23, test_result)
        test_result = packet_decoder(iter(["A0016C880162017C3686B18A3D4780"]))
        self.assertEqual(31, test_result)

        result = packet_decoder(read_lines(filename))
        print(result)
        self.assertEqual(957, result)

    def test_part_two(self):
        self.assertEqual(3, packet_decoder(iter(["C200B40A82"]), return_version=False))
        self.assertEqual(54, packet_decoder(iter(["04005AC33890"]), return_version=False))
        self.assertEqual(7, packet_decoder(iter(["880086C3E88112"]), return_version=False))
        self.assertEqual(9, packet_decoder(iter(["CE00C43D881120"]), return_version=False))
        self.assertEqual(1, packet_decoder(iter(["D8005AC2A8F0"]), return_version=False))
        self.assertEqual(0, packet_decoder(iter(["F600BC2D8F"]), return_version=False))
        self.assertEqual(0, packet_decoder(iter(["9C005AC2F8F0"]), return_version=False))
        self.assertEqual(1, packet_decoder(iter(["9C0141080250320F1802104A08"]), return_version=False))

        result = packet_decoder(read_lines(filename), return_version=False)
        print(result)
        self.assertEqual(744953223228, result)

if __name__ == '__main__':
    unittest.main()
