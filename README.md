# MSc Computer Science: Fundamentals of Computers and Networks

An academic portfolio of number representation, Boolean logic, simple computer architecture and IPv4 networking. It preserves the January 2024 written submission and adds a small, tested set of reference calculations created in November 2026.

| Academic record | Verified detail |
|---|---|
| University and programme | Keele University, MSc Computer Science |
| Module | Fundamentals of Computers and Networks, CSC-40064 |
| Academic year | 2023/24 |
| Final module result | **88%** |
| Credit | **15 CATS**, FHEQ Level 7 |
| Original submission | Written technical answers; cover dated 16 January 2024 |

The result was checked against the owner's final academic transcript, page 2, issued 15 January 2025. It is a **module mark**, not a mark for each answer or for the 2026 reference code. The transcript remains private. The repository's `2024` suffix refers to the original 2023/24 academic year; later changes keep their actual dates.

## Explore the evidence

- [Original student submission, with personal details redacted](docs/original/student-submission-redacted.odt) — download and open in an ODT-compatible office application.
- [Coursework guide and technical review](docs/COURSEWORK.md) — what was submitted, what it demonstrates and which historical calculations need care.
- [Source provenance and privacy review](docs/original/README.md) — source hashes, redactions, preserved figures and equations.
- [Reference calculation design and validation](docs/ENGINEERING.md) — scope, assumptions, execution and limits.

No official assessment brief, marking feedback or original application source was found in the supplied archive. This repository presents the submission as student work. It does not relabel it as a university-issued brief or claim an application was delivered.

## Skills demonstrated

| Skill | Evidence in the original submission |
|---|---|
| Data representation | Hexadecimal-to-binary conversion and ASCII character decoding in Question 1(a) |
| Boolean reasoning | AND/OR circuit evaluation and a four-input truth table in Question 1(b–c) |
| Computer architecture | Register, memory and opcode reasoning; annotated 8-bit assembly and a simulator screenshot in Question 2 |
| Network calculations | Payload budgeting, packet count, serialization/propagation reasoning and checksum arithmetic in Question 3 |
| IPv4 addressing and routing | CIDR ranges, host counts and longest-prefix routing in Question 4 |
| Technical communication | Worked explanations, tables, diagrams and traceable numerical assumptions throughout |

These are evidence of academic work. The historical submission contains mistakes, including a `/22` host-count error and a serialization-delay conversion error. [The technical review](docs/COURSEWORK.md#technical-review-added-in-2026) makes these explicit while retaining the original document unchanged apart from privacy redactions.

## Run the 2026 reference calculations

Use Python 3.10 or later. No packages, account, API key or network connection are required after downloading the repository.

```sh
python reference_calculations.py
python -m unittest discover -s tests -v
```

The demonstration prints 11,108 packets for the stated 5 MiB payload model, **0.08192 ms** to serialize 1,024 bytes at 100 Mb/s, **1,022 host addresses** for `192.168.28.0/22`, interface `b` for the original routing example, and the checksum arithmetic. These are small offline calculations, not a network simulator or desktop application. On Windows, `py -3` may be used in place of `python`.

The code, tests, documentation and privacy maintenance were created on **14 November 2026 with AI assistance**. They were not part of the assessed January 2024 submission.

## University context

Keele's [2023/24 Computer Science taught-masters programme specification](https://www.keele.ac.uk/media/keeleuniversity/sas/qa/pgtprogrammespecifications/pgtprogspecs2023-24/Programme-Specification-Computer-Science-Taught-Masters-2023-24.pdf) lists CSC-40064 as a 15-credit module and maps it to computing principles, theory and practice, and information processing and communication. This is programme context, not the missing assessment brief. The archived 2023/24 module-page URL could not be retrieved during review; later-year assessment details are not substituted for it.

Original coursework and university/third-party figures retain their respective ownership. No blanket licence is asserted for these materials.
