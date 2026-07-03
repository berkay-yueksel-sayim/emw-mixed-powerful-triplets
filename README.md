# Nonexistence of consecutive powerful triplets around cubes with mixed prime factorizations

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21174127.svg)](https://doi.org/10.5281/zenodo.21174127)
**Berkay Yüksel Sayim** — Independent Researcher, Germany
berksa@tutamail.com · ORCID [0009-0004-4993-7352](https://orcid.org/0009-0004-4993-7352)

Preprint, July 2026 (v1.1) — published on Zenodo: doi:[10.5281/zenodo.21174127](https://doi.org/10.5281/zenodo.21174127). License: **CC BY 4.0**.

## Summary

A positive integer is *powerful* if every prime in its factorization occurs with exponent
at least two. The Erdős–Mollin–Walsh conjecture asserts that no three consecutive integers
are all powerful. Chan (Integers 25 (2025), #A7) excluded triples of the form
x³−1 = p³y², x³, x³+1 = q³z², and She (Integers 25 (2025), #A103) excluded
x³−1 = p²a³, x³, x³+1 = q²b³. This note closes the remaining **mixed** configurations:

> **Theorem.** There are no integers x ≥ 2, primes p, q, and integers a, b, y, z with
> x³−1 = p²a³ and x³+1 = q³z² (family M1), nor with x³−1 = p³y² and x³+1 = q²b³ (family M2).

The case analysis reduces both families to the single equation **t⁶ + t³ + 1 = 3w²**,
which is solved completely (only (t,w) = (1,±1)) via a rank-0 elliptic quotient of the
palindromic genus-2 curve (LMFDB curve 1296.k1, Cremona 1296f2). Two complementary results:
no finite congruence sieve can decide this equation, and Beckon's mod-36 constraint on
consecutive powerful triples is refined to arbitrary prime-square moduli.

## Contents of this archive

| File | Description |
|---|---|
| `main.pdf` | The paper (10 pages) |
| `main.tex` | LaTeX source |
| `ancillary/verify_identities.py` | Exact symbolic verification (SymPy) of every identity used: quotient maps, birational chain, classical invariants, wall substitutions, residue facts, conic orbit, direct scans |
| `ancillary/verify_identities_output.txt` | Output of the above (all checks pass) |
| `ancillary/wall_curves.sage` | SageMath script: integral points of the five Mordell curves; Jacobians, conductors, torsion and provable ranks of both elliptic quotients |
| `ancillary/wall_curves_output.txt` | Output of the above |
| `ancillary/beckon_sieve.py` | The residue sieve of Section 6 (standard library only): Beckon's mod-36 classes, the refinements mod 900 and mod 44100, per-prime densities |
| `ancillary/beckon_sieve_output.txt` | Output of the above |

## Reproducing the computations

```
python ancillary/verify_identities.py     # requires sympy; ends with ALL CHECKS PASSED
python ancillary/beckon_sieve.py          # standard library only
sage ancillary/wall_curves.sage           # requires SageMath (e.g. the sagemath/sagemath Docker image)
```

The elliptic-curve data can be cross-checked against the LMFDB:
curve [0,0,0,−81,243] (rank 0, trivial torsion) and curve [0,0,0,−189,999] (rank 1).

## Key claims at a glance

- Families M1/M2: 18 case-analysis leaves; 11 closed by elementary arguments,
  5 via classical Mordell-curve data (Gebel–Pethő–Zimmer 1998; Bennett–Ghadermarzi 2015; LMFDB),
  2 reduce to t⁶+t³+1 = 3w².
- t⁶+t³+1 = 3w² has only the rational solutions (1, ±1) — proof via the τ-quotient,
  whose Jacobian y² = x³−81x+243 has Mordell–Weil group {O}.
- No finite congruence covering can decide t⁶+t³+1 = 3w² (shadow-class obstruction).
- Admissible residues for consecutive powerful triples: 3/36 (Beckon), 39/900, 1209/44100;
  the admissible density decays like (log L)⁻³ — sieving alone cannot settle the conjecture.

## Version history

- **v11 (July 2026)** — editorial revision of v10; **no mathematical content changed.**
  (1) Section 5: the birational correspondence D₋ ↔ E is now written out explicitly (inverse
  maps, exceptional fibres, points at infinity), making it self-evident that no rational point
  is lost. (2) Remark 14: clarified that the k ≤ 2000 computation is illustrative only and not
  part of the proof. (3) Abstract/introduction: one overstatement neutralized and two phrasings
  made more neutral. (4) Spelling unified to American English (one instance). (5) Bibliography
  enriched with DOIs (8 entries, each verified against Crossref/zbMATH) and minor typographical
  polish. All theorems, proofs, data, and verification scripts are unchanged from v10.
- **v10 (June 2026)** — original release.
