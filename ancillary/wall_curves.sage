# Elliptic-curve computations for the paper
# "Nonexistence of consecutive powerful triplets around cubes with mixed prime factorizations".
#
# Run:  sage wall_curves.sage     (verified with SageMath 10.x)
#
# Part (a): complete lists of integral points on the five Mordell curves used
#           in Sections 3-4 (Lemma on Mordell curves).
# Part (b): the two elliptic quotients of the genus-2 curve Y^2 = 3t^6+3t^3+3
#           (Section 5): classical invariants, Jacobians, conductor, torsion,
#           and Mordell-Weil rank with proof=True.
# Expected results are stated in comments.

print("=" * 64)
print("(a) Mordell curves Y^2 = X^3 + k : integral points (both signs)")
print("=" * 64)
# Expected: k=2: [(-1,+-1)]; k=-2: [(3,+-5)]; k=54: [(3,+-9)]; k=-54: [(7,+-17)]; k=-162: []
for k in [2, -2, 54, -54, -162]:
    E = EllipticCurve([0, 0, 0, 0, k])
    print("k =", k, "->", E.integral_points(both_signs=True))

print()
print("=" * 64)
print("(b) Elliptic quotients of Y^2 = 3t^6 + 3t^3 + 3  (u = t + 1/t)")
print("=" * 64)
R.<u> = QQ[]
quartics = {
    "D+ (sigma quotient)": 3*(u+2)*(u^3-3*u+1),   # expected: rank 1 (LMFDB 1296.b1, Cremona 1296l2)
    "D- (tau quotient)":   3*(u-2)*(u^3-3*u+1),   # expected: rank 0, trivial torsion
                                                  # (LMFDB 1296.k1, Cremona 1296f2) -> E(Q) = {O}
}
for name, q in quartics.items():
    print("-" * 64)
    print(name, ": v^2 =", q)
    a, b, c, d, e = q[4], q[3], q[2], q[1], q[0]
    I = 12*a*e - 3*b*d + c^2
    J = 72*a*c*e + 9*b*c*d - 27*a*d^2 - 27*b^2*e - 2*c^3
    Ejac = EllipticCurve([0, 0, 0, -27*I, -27*J])
    Emin = Ejac.minimal_model()
    print("  invariants: I =", I, " J =", J)
    print("  Jacobian:", Ejac.ainvs(), " minimal model:", Emin.ainvs())
    print("  conductor:", Emin.conductor(), " Cremona label:", Emin.cremona_label())
    print("  torsion:", Emin.torsion_subgroup().invariants())
    print("  rank (proof=True):", Emin.rank(proof=True))

print()
print("=" * 64)
print("(b2) consistency: rational points of small height on the quartics")
print("=" * 64)
# Expected: D- has exactly one point (u, w) = (2, 0) in this range;
#           D+ (rank 1) has several, e.g. (-2,0), (-1,3), (2,6), (-19/11, 111/121).
for name, q in quartics.items():
    found = []
    for den in range(1, 25):
        for num in range(-60*den, 60*den + 1):
            uu = QQ(num)/QQ(den)
            val = q(uu)
            if val >= 0 and val.is_square():
                found.append((uu, val.sqrt()))
    print(name, "->", sorted(set(found)))
