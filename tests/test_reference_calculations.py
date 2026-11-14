"""Independent worked values and boundary cases for the 2026 examples."""

from fractions import Fraction
import unittest

from reference_calculations import (
    internet_checksum_words, longest_prefix_match, packet_count,
    serialization_delay_ms, subnet_summary,
)


class ReferenceCalculationTests(unittest.TestCase):
    def test_packet_count_requires_a_whole_final_packet(self):
        self.assertEqual(packet_count(5 * 1024**2, 512, 40), 11108)
        self.assertEqual(packet_count(944, 512, 40), 2)
        self.assertEqual(packet_count(945, 512, 40), 3)
        self.assertEqual(packet_count(0, 512, 40), 0)

    def test_packet_budget_rejects_invalid_units_or_payload(self):
        for args in [(-1, 512, 40), (1, 0, 0), (1, 40, 40), (1, 40, 41), (1, 512, -1), (True, 512, 40), (1.5, 512, 40)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                packet_count(*args)

    def test_serialization_uses_bits_and_milliseconds(self):
        self.assertEqual(serialization_delay_ms(1024, 100_000_000), Fraction(256, 3125))
        self.assertEqual(serialization_delay_ms(1000, 1_000_000), 8)
        self.assertEqual(serialization_delay_ms(0, 1_000_000), 0)
        for size, rate in [(1, 0), (-1, 1), (1, True)]:
            with self.subTest(size=size, rate=rate), self.assertRaises(ValueError):
                serialization_delay_ms(size, rate)

    def test_subnet_fixes_historical_host_count(self):
        result = subnet_summary("192.168.28.0/22")
        self.assertEqual(result["total_addresses"], 1024)
        self.assertEqual(result["host_addresses"], 1022)
        self.assertEqual(result["first_address"], "192.168.28.0")
        self.assertEqual(result["last_address"], "192.168.31.255")

    def test_ipv4_boundaries_without_enumerating_large_networks(self):
        self.assertEqual(subnet_summary("0.0.0.0/0")["host_addresses"], 2**32 - 2)
        self.assertEqual(subnet_summary("192.0.2.0/31")["host_addresses"], 2)
        self.assertEqual(subnet_summary("192.0.2.1/32")["host_addresses"], 1)
        for cidr in ["192.168.28.1/22", "2001:db8::/32", "192.0.2.0/33"]:
            with self.subTest(cidr=cidr), self.assertRaises(ValueError):
                subnet_summary(cidr)

    def test_routing_chooses_specific_prefix_regardless_of_order(self):
        routes = [("0.0.0.0/0", "default"), ("160.5.0.0/16", "broad"), ("160.5.60.0/22", "b"), ("160.5.63.0/24", "specific")]
        expected = ("160.5.63.0/24", "specific")
        self.assertEqual(longest_prefix_match("160.5.63.7", routes), expected)
        self.assertEqual(longest_prefix_match("160.5.63.7", reversed(routes)), expected)
        self.assertEqual(longest_prefix_match("203.0.113.1", routes), ("0.0.0.0/0", "default"))
        self.assertIsNone(longest_prefix_match("203.0.113.1", []))

    def test_original_routing_example_and_ambiguous_duplicates(self):
        routes = [("160.5.16.0/24", "a"), ("160.5.60.0/22", "b"), ("160.5.224.0/20", "c"), ("0.0.0.0/0", "d")]
        self.assertEqual(longest_prefix_match("160.5.63.7", routes), ("160.5.60.0/22", "b"))
        with self.assertRaises(ValueError):
            longest_prefix_match("192.0.2.1", [("0.0.0.0/0", "a"), ("0.0.0.0/0", "b")])

    def test_checksum_end_around_carry_and_received_error(self):
        words = [0xA680, 0xE182]
        self.assertEqual(internet_checksum_words(words), 0x77FC)
        self.assertEqual(internet_checksum_words(words + [0x77FC]), 0)
        self.assertEqual(internet_checksum_words(words + [0x77DC]), 0x0020)
        self.assertEqual(internet_checksum_words([0xFFFF, 0x0001]), 0xFFFE)
        for word in [-1, 65536, True, 0.5]:
            with self.subTest(word=word), self.assertRaises(ValueError):
                internet_checksum_words([word])


if __name__ == "__main__":
    unittest.main()
