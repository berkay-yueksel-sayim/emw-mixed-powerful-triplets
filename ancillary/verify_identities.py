"""Exact symbolic verification of the identities used in the paper
"Nonexistence of consecutive powerful triplets around cubes with mixed prime factorizations".

Requires: sympy (any recent version). Run:  python verify_identities.py
Expected output: every line ends with "OK" and the final line reads "ALL CHECKS PASSED".
"""
import sympy as sp


def check(name, cond):
    print(f"{name}: {'OK' if cond else 'FAILED'}")
    assert cond, name


x, t, u, T, S, X, Y, s = sp.symbols("x t u T S X Y s")

# --- Section 5, Lemma (quotients): auxiliary factorizations -----------------
check("u^3-3u+2 == (u-1)^2 (u+2)", sp.expand((u - 1) ** 2 * (u + 2) - (u**3 - 3 * u + 2)) == 0)
check("u^3-3u-2 == (u+1)^2 (u-2)", sp.expand((u + 1) ** 2 * (u - 2) - (u**3 - 3 * u - 2)) == 0)

# --- Section 5, Lemma (quotients): the two exact identities on the curve ----
# On C: Y^2 = f(t) := 3 t^6 + 3 t^3 + 3, with u = t + 1/t,
#   V = Y (t+1)/t^2  satisfies V^2 = 3 (u+2)(u^3-3u+1) =: q_plus(u),
#   W = Y (t-1)/t^2  satisfies W^2 = 3 (u-2)(u^3-3u+1) =: q_minus(u).
f = 3 * t**6 + 3 * t**3 + 3
uu = t + 1 / t
q_plus = 3 * (uu + 2) * (uu**3 - 3 * uu + 1)
q_minus = 3 * (uu - 2) * (uu**3 - 3 * uu + 1)
check("V^2 identity (sigma quotient)", sp.simplify(f * (t + 1) ** 2 / t**4 - q_plus) == 0)
check("W^2 identity (tau quotient)", sp.simplify(f * (t - 1) ** 2 / t**4 - q_minus) == 0)
# Equivalent polynomial form:
check(
    "(t+1)^2 (t^6+t^3+1) == t^4 (u+2)(u^3-3u+1)",
    sp.simplify((t + 1) ** 2 * (t**6 + t**3 + 1) - t**4 * (uu + 2) * (uu**3 - 3 * uu + 1)) == 0,
)
check(
    "(t-1)^2 (t^6+t^3+1) == t^4 (u-2)(u^3-3u+1)",
    sp.simplify((t - 1) ** 2 * (t**6 + t**3 + 1) - t**4 * (uu - 2) * (uu**3 - 3 * uu + 1)) == 0,
)

# --- Section 5, proof of the Theorem: the birational chain to E -------------
# D_-: W^2 = 3(u-2)(u^3-3u+1); substitute u = 2 + 1/T, W = S/T^2:
q = 3 * (u - 2) * (u**3 - 3 * u + 1)
lhs = (S / T**2) ** 2 - q.subs(u, 2 + 1 / T)
cubic = S**2 - (9 * T**3 + 27 * T**2 + 18 * T + 3)
check("u=2+1/T, W=S/T^2 gives S^2 = 9T^3+27T^2+18T+3", sp.simplify(lhs - cubic / T**4) == 0)
# (x, y) = (9T+9, 9S) gives y^2 = x^3 - 81x + 243:
e = (9 * S) ** 2 - ((9 * T + 9) ** 3 - 81 * (9 * T + 9) + 243)
check("(x,y)=(9T+9,9S) gives y^2 = x^3-81x+243", sp.expand(e - 81 * cubic) == 0)

# --- Section 5, classical invariants of q_minus ------------------------------
a4, b4, c4, d4, e4 = 3, -6, -9, 21, -6  # q_minus(u) = 3u^4-6u^3-9u^2+21u-6
I = 12 * a4 * e4 - 3 * b4 * d4 + c4**2
J = 72 * a4 * c4 * e4 + 9 * b4 * c4 * d4 - 27 * a4 * d4**2 - 27 * b4**2 * e4 - 2 * c4**3
check("I = 243, J = -6561 for q_minus", (I, J) == (243, -6561))

# --- Sections 3-4: wall substitutions and residue facts ----------------------
check("(u^3+1)^2-(u^3+1)+1 == u^6+u^3+1", sp.expand((u**3 + 1) ** 2 - (u**3 + 1) + 1 - (u**6 + u**3 + 1)) == 0)
check("(s^3-1)^2+(s^3-1)+1 == s^6-s^3+1", sp.expand((s**3 - 1) ** 2 + (s**3 - 1) + 1 - (s**6 - s**3 + 1)) == 0)
check("squares mod 9 == {0,1,4,7}", {(k * k) % 9 for k in range(9)} == {0, 1, 4, 7})
check("cubes mod 9 == {0,1,8}", {(k**3) % 9 for k in range(9)} == {0, 1, 8})
check("cubes of 1+3k mod 27 in {1,10,19}", {((1 + 3 * k) ** 3) % 27 for k in range(27)} == {1, 10, 19})
check(
    "x = 1+3k => x^2+x+1 == 3 mod 9; x = -1+3k => x^2-x+1 == 3 mod 9",
    all(((1 + 3 * k) ** 2 + (1 + 3 * k) + 1) % 9 == 3 for k in range(9))
    and all(((-1 + 3 * k) ** 2 - (-1 + 3 * k) + 1) % 9 == 3 for k in range(9)),
)

# --- Remark (no congruence sieve): the conic orbit ---------------------------
# Solutions of z^2+z+1 = 3w^2 form one bi-infinite orbit of z_{k+1} = 14 z_k - z_{k-1} + 6.
LIM = 10**6
brute = []
for z in range(-LIM, LIM + 1):
    val = z * z + z + 1
    if val % 3 == 0:
        w2 = val // 3
        r = sp.integer_nthroot(w2, 2)
        if r[1]:
            brute.append(z)
brute = sorted(set(brute))
seq = [-2, 1]
while abs(seq[-1]) <= LIM:
    seq.append(14 * seq[-1] - seq[-2] + 6)
back = [-2, 1]
while abs(back[0]) <= LIM:
    back.insert(0, 14 * back[0] - back[1] + 6)
orbit = sorted(set(v for v in back + seq if abs(v) <= LIM))
check("conic solutions |z|<=1e6 == recurrence orbit", brute == orbit)
# Cube check along the recurrence (exact integer arithmetic):
zs = [-2, 1]
cubes = []
for _ in range(2000):
    zs.append(14 * zs[-1] - zs[-2] + 6)
for z in zs:
    r = sp.integer_nthroot(abs(z), 3)
    if r[1] and (r[0] ** 3 == z or -(r[0] ** 3) == z):
        cubes.append(z)
check("only cube among z_k (k<=2000, forward branch) is z=1", set(c for c in cubes if c != 0) == {1})

# --- The wall equation itself: direct integer scan ---------------------------
sols = []
for tt in range(-10**4, 10**4 + 1):
    val = tt**6 + tt**3 + 1
    if val % 3 == 0:
        r = sp.integer_nthroot(val // 3, 2)
        if r[1]:
            sols.append((tt, r[0]))
check("t^6+t^3+1=3w^2 has only t=1 for |t|<=1e4", [p[0] for p in sols] == [1])

print("ALL CHECKS PASSED")
