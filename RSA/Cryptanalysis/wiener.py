import math
from fractions import Fraction as frac
from sympy import Symbol, solve

def modInverse(A, M):
    m0 = M
    y = 0
    x = 1

    if (M == 1):
        return 0

    while (A > 1):
        q = A // M
        t = M
        M = A % M
        A = t
        t = y
        
        y = x - q * y
        x = t
    
    if (x < 0): x = x + m0
    
    return x

def continued_fraction(a, b):
    q = a // b
    r = a % b
    if r == 0:
        return [q]
    else:
        cf = continued_fraction(b, r)
        result = [q] + cf
        return result

def rev_continued_fraction(cf):
    if cf == [0]: return 0
    rev_cf = cf[::-1]
    d = rev_cf[0]
    op = frac(1, d)
    for n in rev_cf[1: ]:
        op += n
        op = 1 / op
    
    return op

def wiener(N, e):
    cf = continued_fraction(N, e)
    cf_len = len(cf)
    d_max = pow(N, 1 / 4) / 3

    for i in range(0, cf_len):
        f = rev_continued_fraction(cf[: i + 1])
        k, d = f.numerator, f.denominator
        if d < d_max: 
            phiN = (e * d - 1) / k
            
            x = Symbol('x')
            expression = x ** 2 - (N - phiN + 1) * x + N
            roots = solve(expression, dict=False)
            p, q = int(roots[0]), int(roots[1])
            if N == p * q:
                return [p, q]
    
    return None


N = int(input("N: "))
e = int(input("e: "))

factors = wiener(N, e)

if factors != None:
    print("p = " + str(factors[0]))
    print("q = " + str(factors[1]))

# N = 90581
# e = 17993

# N = 160523347
# e = 60728973

# N = 317940011
# e = 77537081
