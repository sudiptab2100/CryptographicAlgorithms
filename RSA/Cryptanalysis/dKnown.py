def DEC_EXP(n, e, d):
    s = 0
    r = e * d - 1
    while r % 2 == 0:
        s += 1
        r //= 2

    import random
    w = random.randint(1, n-1)

    import math
    x = math.gcd(w, n)

    if 1 < x < n:
        return x, w

    v = pow(w, r, n)
    
    if v == 1:
        return None, w

    while v != 1:
        v0 = v
        v = pow(v, 2, n)
        if v0 == -1 % n:
            return None, w
        else:
            x = math.gcd(v0 + 1, n)
            if 1 < x < n:
                return x, w
            else: 
                return None, w

n = int(input('n: '))
e = int(input('e: '))
d = int(input('d: '))

p, w = DEC_EXP(n, e, d)
while p == None:
    p, w = DEC_EXP(n, e, d)

print('\nResults:\n')
print(f"p = {p}")
print(f"q = {n // p}")
print(f"n = {(n // p) * p}")
print(f"w = {w}")

    

# n = 25777
# e = 16971
# d = 3

# n = 3233
# e = 17
# d = 2753

# n = 36581
# e = 4679
# d = 14039