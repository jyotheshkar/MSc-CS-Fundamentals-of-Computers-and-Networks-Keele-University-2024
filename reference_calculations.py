"""Small networking reference calculations added in November 2026.

These explain selected January 2024 coursework concepts. They are not the
submitted coursework, a network simulator or a complete UDP implementation.
Only the Python standard library is used; running the file performs no I/O
other than printing its fixed demonstration results.
"""

from fractions import Fraction
from ipaddress import IPv4Address, IPv4Network
import json


def _integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")


def packet_count(total_bytes, mtu_bytes, overhead_bytes):
    """Ceiling division for a fixed payload budget, not IP fragmentation."""
    _integer(total_bytes, "total_bytes")
    _integer(mtu_bytes, "mtu_bytes", 1)
    _integer(overhead_bytes, "overhead_bytes")
    if overhead_bytes >= mtu_bytes:
        raise ValueError("overhead_bytes must be smaller than mtu_bytes")
    payload = mtu_bytes - overhead_bytes
    return (total_bytes + payload - 1) // payload


def serialization_delay_ms(packet_bytes, bit_rate_bps):
    """Return exact milliseconds to serialize bytes at a fixed bit rate.

    Excludes propagation, queuing, processing, handshakes and retransmissions.
    Fraction avoids rounding the unit conversion before displaying a result.
    """
    _integer(packet_bytes, "packet_bytes")
    _integer(bit_rate_bps, "bit_rate_bps", 1)
    return Fraction(packet_bytes * 8 * 1000, bit_rate_bps)


def subnet_summary(cidr):
    """IPv4 address range and host count following ipaddress.hosts rules.

    /31 uses point-to-point semantics, /32 is a single address. The count
    makes no allowance for reserved gateway, DHCP or operational addresses.
    Non-canonical CIDRs with host bits set are rejected, not normalized.
    """
    network = IPv4Network(cidr, strict=True)
    return {
        "network": str(network),
        "first_address": str(network.network_address),
        "last_address": str(network.broadcast_address),
        "total_addresses": network.num_addresses,
        "host_addresses": network.num_addresses - 2 if network.prefixlen < 31 else network.num_addresses,
    }


def longest_prefix_match(destination, routes):
    """Return (network, interface), or None; routes are (CIDR, name) pairs.

    Duplicate network prefixes are rejected: this example does not model
    route metrics, policy routing, equal-cost multipath or failed interfaces.
    """
    address = IPv4Address(destination)
    seen = set()
    best = None
    for cidr, interface in routes:
        network = IPv4Network(cidr, strict=True)
        if network in seen:
            raise ValueError(f"duplicate route prefix: {network}")
        if not isinstance(interface, str) or not interface.strip():
            raise ValueError("interface must be a non-empty string")
        seen.add(network)
        if address in network and (best is None or network.prefixlen > best[0].prefixlen):
            best = (network, interface)
    return (str(best[0]), best[1]) if best else None


def internet_checksum_words(words):
    """One's-complement checksum of supplied unsigned 16-bit words.

    Each word is already decoded in network byte order. This arithmetic
    example does not construct a UDP pseudo-header, handle odd input bytes
    or implement UDP's zero-checksum transmission convention.
    """
    total = 0
    for word in words:
        _integer(word, "word")
        if word > 0xFFFF:
            raise ValueError("word must fit in 16 bits")
        total += word
        total = (total & 0xFFFF) + (total >> 16)
    return (~total) & 0xFFFF


def demonstration():
    routes = [
        ("160.5.16.0/24", "a"), ("160.5.60.0/22", "b"),
        ("160.5.224.0/20", "c"), ("0.0.0.0/0", "d"),
    ]
    words = [0xA680, 0xE182]
    return {
        "edition": "2026 reference calculations; original 2024 submission is separate",
        "packets_for_5_MiB_with_512_byte_MTU_and_40_byte_overhead": packet_count(5 * 1024**2, 512, 40),
        "serialization_ms_for_1024_bytes_at_100_Mbps": float(serialization_delay_ms(1024, 100_000_000)),
        "subnet": subnet_summary("192.168.28.0/22"),
        "route_for_160.5.63.7": longest_prefix_match("160.5.63.7", routes),
        "checksum_for_two_words": f"0x{internet_checksum_words(words):04X}",
        "provided_checksum_0x77DC_passes_word_sum": internet_checksum_words(words + [0x77DC]) == 0,
    }


if __name__ == "__main__":
    print(json.dumps(demonstration(), indent=2))
