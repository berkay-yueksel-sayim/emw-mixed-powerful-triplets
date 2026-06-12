# Nonexistence of consecutive powerful triplets around cubes with mixed prime factorizations

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20654530.svg)](https://doi.org/10.5281/zenodo.20654530)

**Berkay Yüksel Sayim** — Independent Researcher, Germany
berksa@tutamail.com · ORCID [0009-0004-4993-7352](https://orcid.org/0009-0004-4993-7352)

Preprint, June 2026 — published on Zenodo: [doi:10.5281/zenodo.20654530](https://doi.org/10.5281/zenodo.20654530)
License: **CC BY 4.0**.

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

## Contents

| File | Description |
|---|---|
| `main.pdf` | The paper (10 pages) |
| `main.tex` | LaTeX source |
| `ancillary/verify_identities.py` | Exact symbolic verification (SymPy) of every identity used |
| `ancillary/verify_identities_output.txt` | Output (all checks pass) |
| `ancillary/wall_curves.sage` | SageMath: Mordell integral points; Jacobians, torsion, provable ranks |
| `ancillary/wall_curves_output.txt` | Output |
| `ancillary/beckon_sieve.py` | The residue sieve of Section 6 (standard library only) |
| `ancillary/beckon_sieve_output.txt` | Output |

## Reproducing the computations
```
python ancillary/verify_identities.py     # requires sympy; ends with ALL CHECKS PASSED
python ancillary/beckon_sieve.py          # standard library only
sage ancillary/wall_curves.sage           # requires SageMath (e.g. the sagemath/sagemath Docker image)
```

Cross-check against the LMFDB: curve [0,0,0,-81,243] (rank 0, trivial torsion)
and curve [0,0,0,-189,999] (rank 1).

## How to cite

> Sayim, B. Y. (2026). *Nonexistence of consecutive powerful triplets around cubes with
> mixed prime factorizations* (1.0). Zenodo. https://doi.org/10.5281/zenodo.20654530
