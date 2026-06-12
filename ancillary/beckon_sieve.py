"""Residue refinement of Beckon's condition (Proposition in Section 6).

For a triple (n, n+1, n+2) of powerful numbers, no member may have p-adic
valuation exactly 1. A residue r mod M (M a product of prime squares) is
*admissible* if for no prime p with p^2 | M and no i in {0,1,2} the value
(r+i) mod p^2 is divisible by p but not by p^2.

Requires: Python 3 standard library only. Run:  python beckon_sieve.py
Expected: mod 36 -> [7, 27, 35] (Beckon); mod 900 -> 39 classes; mod 44100 -> 1209 classes;
per-prime admissible fraction (p^2-3p+3)/p^2 for p >= 5, 1/4 for p=2, 1/3 for p=3.
"""
import hashlib
from fractions import Fraction


def survivors(modulus, primes):
    bad = []
    for p in primes:
        p2 = p * p
        forbidden = {p * j for j in range(1, p) }  # v_p == 1 residues mod p^2
        bad.append((p2, forbidden))
    out = []
    for r in range(modulus):
        ok = True
        for p2, forbidden in bad:
            if any((r + i) % p2 in forbidden for i in range(3)):
                ok = False
                break
        if ok:
            out.append(r)
    return out


def sha(lst):
    return hashlib.sha256(",".join(map(str, lst)).encode()).hexdigest()


s36 = survivors(36, [2, 3])
print("mod 36   :", s36, "(Beckon: [7, 27, 35])")
assert s36 == [7, 27, 35]

s900 = survivors(900, [2, 3, 5])
print("mod 900  : count =", len(s900), " first10 =", s900[:10], " sha256 =", sha(s900))

s44100 = survivors(44100, [2, 3, 5, 7])
print("mod 44100: count =", len(s44100), " first10 =", s44100[:10], " sha256 =", sha(s44100))

print("\nper-prime admissible fractions (windows of length 3 avoiding v_p = 1):")
prod = Fraction(1)
for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
    if p == 2:
        frac = Fraction(1, 4)      # n odd and n+1 = 0 mod 4
    elif p == 3:
        frac = Fraction(3, 9)      # windows avoiding {3,6} mod 9
    else:
        frac = Fraction(p * p - 3 * (p - 1), p * p)
    count = len(survivors(p * p if p > 2 else 4, [p]))
    assert Fraction(count, p * p if p > 2 else 4) == frac, p
    prod *= frac
    print(f"  p={p:2d}: {frac}  (verified by direct count)")
print("product over p <= 47:", prod, "~", float(prod))
print("Note: the product tends to 0 like (log L)^{-3} (Mertens); no finite sieve decides the conjecture.")
