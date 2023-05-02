import math

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

def wiener_attack(N, e):
    result = [0, 0]
    phiN = N - 1
    d = 0

    # Compute continued fractions until convergence
    cf = continued_fraction(phiN, e)
    for k in cf:
        # Compute numerator and denominator of the next convergent
        if result == [0, 0]:
            num = k
            den = 1
        elif result[1] == 0:
            num = k
            den = 1
        else:
            num = k * result[0] + result[1]
            den = result[0]

        # Compute candidate private key
        candidateD = modInverse(e, num * den) * num

        # Check if candidate is correct
        candidateN = pow(N, candidateD, phiN)
        if candidateN == 1:
            d = candidateD
            break

        result[0] = num
        result[1] = den

    if d == 0:
        raise ValueError("Failed to find private key")

    return [d, phiN // d]

N = 160523347
e = 60728973
factors = wiener_attack(N, e)

print("p = " + str(factors[0]))
print("q = " + str(factors[1]))
