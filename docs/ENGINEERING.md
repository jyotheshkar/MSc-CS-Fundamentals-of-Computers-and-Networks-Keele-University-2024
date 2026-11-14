# Reference calculations: design and validation

## Purpose and boundary

The original deliverable was written academic work. The repository therefore preserves that work as evidence and adds a small offline Python reference file, created with AI assistance on **14 November 2026**, to investigate selected arithmetic and protocol concepts. There is no original deployed application to recover, no database, no service and no GUI claim.

The public files have three roles:

| Layer | Files | Responsibility |
|---|---|---|
| Historical evidence | `docs/original/student-submission-redacted.odt`, `provenance.json` | Preserve the academic answers and record privacy changes and source/output hashes |
| Explanation | `README.md`, `docs/COURSEWORK.md` | Establish module context, evidence locations, corrections and honest limits |
| Reproducible reference | `reference_calculations.py`, `tests/test_reference_calculations.py` | Demonstrate five bounded calculations and check known values and edge cases |

Keeping the layers separate prevents a correction made in 2026 from being attributed to the 2024 assessment. The tests check the new calculations; they do not retrospectively validate or regrade the whole submission.

## Design choices

**Pure functions, explicit units.** Byte counts and bit rates have named parameters. Integer validation rejects booleans, fractions, negative sizes, nonpositive rates and unusable payload budgets. Packet count uses integer ceiling division; it does not round a fractional packet down. `Fraction` retains exact serialization-delay arithmetic until presentation.

**Use a maintained standard-library parser.** `IPv4Address` and `IPv4Network(..., strict=True)` validate IPv4 data. Host bits in a network address cause an error rather than silently changing the input. Host counts are calculated in constant space, including for `/0`; no address list is materialized. `/31` and `/32` follow Python's documented host conventions and do not imply an Ethernet deployment policy.

**Small, understandable routing model.** The route function parses every candidate, selects the greatest matching prefix length and rejects duplicate prefixes. This avoids inventing a tie-break policy. It models neither administrative distance nor route metrics, policy routing, ECMP, dynamic updates or interface health. Runtime and memory grow linearly with the supplied route table; a router-scale trie would require a separate design.

**Checksum arithmetic is explicit.** Each input is an already-decoded unsigned 16-bit word. Addition folds end-around carry and complements the result. It does not construct IP/UDP headers or pseudo-headers, encode odd-length byte strings or implement UDP zero-checksum transmission rules. An all-zero checksum result from a supplied word list is an arithmetic check, not proof that a live UDP datagram is valid or secure.

**No unnecessary infrastructure.** The examples use the Python standard library, perform no network requests and write no files when run. No credentials, dependency installation or server is needed. Reproducibility is provided by small fixed examples and tests rather than a dashboard with unsupported claims of deployment.

## Function contracts

| Function | Input and output | Main limit |
|---|---|---|
| `packet_count(total_bytes, mtu_bytes, overhead_bytes)` | Nonnegative byte count, positive MTU and `0 <= overhead < MTU`; integer packet count | Fixed-payload exercise model; excludes actual fragmentation alignment, retransmission and framing |
| `serialization_delay_ms(packet_bytes, bit_rate_bps)` | Nonnegative bytes, positive integer bits/second; exact `Fraction` milliseconds | Serialization only; no propagation, queues, processing or handshakes |
| `subnet_summary(cidr)` | Canonical IPv4 CIDR; range, total and host counts in a dictionary | No IPv6 or operational address-reservation policy |
| `longest_prefix_match(destination, routes)` | IPv4 destination and `(CIDR, interface)` pairs; `(network, interface)` or `None` | Unique prefixes; no metrics or policy routing |
| `internet_checksum_words(words)` | Iterable of 16-bit unsigned integers; complemented 16-bit word | Arithmetic only; caller must supply the correct protocol coverage |

## Running and checking

From the repository root, with Python 3.10 or later:

```sh
python reference_calculations.py
python -m unittest discover -s tests -v
```

On Windows, `py -3` may replace `python`. Downloading the source ZIP from GitHub is sufficient; extract it first and open a terminal in the extracted directory. There is no installer because this repository supplies an evidence archive and Python study examples rather than a desktop application.

Verification performed on 14 November 2026 with Python 3.11.15:

- Eight unit tests check fixed worked values, rounding at payload boundaries, invalid input, exact unit conversion, `/0`, `/22`, `/31` and `/32`, canonical CIDRs, route order, default/no route, duplicate routes, carry wrapping and correct/incorrect checksums.
- The demonstration was executed and checked against the documented results.
- All public Markdown links to local files were checked. Python syntax compilation passed.
- ZIP CRC, all XML parsing, local image/equation references and source/output SHA-256 were checked for the redacted ODT. All non-cover academic body elements, six embedded images and 30 MathML objects match the source. See [provenance](original/provenance.json).
- All 15 original PDF pages and six embedded image files were visually inspected. An ODT office renderer was unavailable, so the final redacted ODT's layout was not rendered; its structure and academic content were checked.

## Maintenance and evidence integrity

Keep the January 2024 source untouched. Publish only the redacted derivative. If the derivative changes, rerun a privacy review, update `provenance.json` and verify its hash. Inspect all ZIP members, including `media/` images, MathML objects, metadata and settings; searching only `Pictures/` is insufficient for this source.

The source archive's code mismatch is documented rather than silently normalized: the private filename used CSC-20043, while the cover and transcript identify CSC-40064. The 2023/24 programme specification is the verified official context; no official assessment brief or individual-answer marking feedback was available.
