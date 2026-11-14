# Coursework guide

## What the archive contains

The supplied archive contains a PDF and editable ODT version of a student submission. The cover identifies **CSC-40064-2023-SEM1-A**, FHEQ Level 7, dated **16 January 2024**. Although the private source filenames used CSC-20043, the cover and verified transcript support the CSC-40064 mapping. The source PDF has 15 pages, including a final blank page.

The public [redacted ODT](original/student-submission-redacted.odt) retains the academic answers, six embedded images and 30 MathML equation objects. It removes personal cover details and document metadata. It is a historical student-authored submission, not a university-issued assessment brief, a model solution or a complete record of the teaching materials.

## Evidence map

Page locations below refer to the original PDF inspected during provenance review; pagination may differ when an office application opens the redacted ODT.

| Original location | Work present | What a reader can examine |
|---|---|---|
| Q1(a), pp. 2–3 | Hexadecimal, binary and ASCII conversions for `0x41`, `0x6E`, `0x44` | Relationship between hex digits, four-bit groups and the characters `A`, `n`, `D` |
| Q1(b–c), pp. 3–5 | AND/OR circuit, worked output and a 16-row truth table | `F = (W AND X) OR Y OR Z`; why input combinations change the output |
| Q2(a), pp. 5–6 | Opcodes, register/memory operations, annotated assembly and simulator screenshot | The example loads `0x10`, stores `0x05` in memory, adds it and obtains `0x15` in register A |
| Q2(b), pp. 7–8 | Character-range comparisons, conditional jumps and ASCII case conversion | A program checks `97..122`, subtracts 32 for lowercase ASCII and uses `*` otherwise |
| Q3(a–b), pp. 8–10 | MTU/payload packet count and a client–router–server delay calculation | Unit assumptions, ceiling division, serialization delay and round-trip propagation |
| Q3(c), p. 11 | Two 16-bit words and a transmitted checksum | One's-complement addition, end-around carry and detection of a failed check |
| Q4(a), pp. 11–12 | `192.168.28.0/22` subnet range | Network/broadcast addresses, host-address arithmetic and binary masks |
| Q4(b), pp. 12–14 | Four-entry route table and `160.5.63.7` | Selection of `160.5.60.0/22`, interface `b`, by longest prefix |

## Technical review added in 2026

This review is separate from the assessed answers and is not lecturer feedback. It records a few useful corrections and clarifies assumptions; it is not a line-by-line regrading of the submission.

| Historical detail | Reference interpretation |
|---|---|
| Q1(b) labels an AND truth table as “NAND”. | Its `0,0,0,1` output column is AND. NAND would invert those values. The circuit and subsequent argument use AND. |
| Q2(a) describes opcode `0C` as a memory-to-register move, while the shown code and screenshot use addition. | In the reviewed screenshot the executed source is `ADD A, [0x10]`, yielding `0x15`. Treat the opcode sentence as inconsistent; do not reconstruct a full instruction set from this answer. |
| Q2(b)'s displayed line 6 loses the `[mem]` operand. | The adjacent explanation explicitly writes `MOV A, [mem]`. The archival formatting is preserved; this repository does not claim the displayed listing is directly runnable in an arbitrary assembler. |
| Q3(a) calls `5 × 1024 × 1024` bytes “5 MB”. | The arithmetic uses **5 MiB**, or 5,242,880 bytes. With the exercise's fixed overhead of 40 bytes and 512-byte MTU, payload is 472 bytes and the integer packet count is **11,108**. This model does not implement IPv4 fragmentation rules. |
| Q3(b) gives 0.8192 ms for 1,024 bytes at 100 Mb/s. | Serialization alone is `(1024 × 8) / 100,000,000` seconds = **0.08192 ms**. The archived aggregate delay also has inconsistent rounding/multipliers. The missing full question prevents reconstructing all handshake, header and link assumptions; no replacement total is asserted. |
| Q3(c) concludes the received checksum fails. | For words `0xA680` and `0xE182`, the folded sum is `0x8803`; its complement is `0x77FC`. The supplied `0x77DC` produces `0xFFDF` when included in the folded sum, so the failure conclusion holds. A full UDP checksum also needs its protocol-defined coverage; the example only checks the supplied words. |
| Q4(a) gives 1,020 usable hosts in a `/22`. | There are `2^10 = 1,024` addresses; after excluding the network and broadcast addresses there are **1,022**, ranging from `192.168.28.1` to `192.168.31.254`. Operational reservations can reduce allocatable addresses further. |
| Q4(b) chooses interface `b`. | `160.5.63.7` belongs to `160.5.60.0/22`. This is the most specific matching route in the supplied table. The reference checks all routes, so it does not depend on table order. |

The new [reference calculations](../reference_calculations.py) make the packet, unit-conversion, subnet, route and checksum examples reproducible. They intentionally do not invent a processor emulator, full UDP packet parser, network simulator or web application.

## Sources and limitations

- [Original evidence provenance](original/README.md) distinguishes private source files, the public derivative and later documentation.
- [Keele Computer Science taught-masters programme specification, 2023/24](https://www.keele.ac.uk/media/keeleuniversity/sas/qa/pgtprogrammespecifications/pgtprogspecs2023-24/Programme-Specification-Computer-Science-Taught-Masters-2023-24.pdf) establishes programme/module context; it does not supply the missing assessment brief.
- [Python `ipaddress` reference](https://docs.python.org/3/library/ipaddress.html) documents strict network parsing, address ranges and `/31`/`/32` host conventions used by the code.
- [RFC 1071, section 1](https://www.rfc-editor.org/rfc/rfc1071) describes one's-complement checksum generation and verification.
- [RFC 1812, section 5.2.4.3](https://www.rfc-editor.org/rfc/rfc1812) gives the longest-match routing principle; the small example omits real routing policies and metrics.

No original assessment brief or marking feedback was found. The **88%** figure is the verified final module result, not an endorsement of every answer. The full transcript and unredacted sources remain private.
