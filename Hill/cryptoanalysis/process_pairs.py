from sympy import Matrix

def process(pair, r):
    m = []
    c = []
    for p in pair:
        tm = [0] * r
        tc = [0] * r
        for i in range(r):
            tm[i] = ord(p[0][i]) - ord('a')
            tc[i] = ord(p[1][i]) - ord('a')
        m.append(tm)
        c.append(tc)
    return m, c

def mod26inv(m):
    return Matrix(m).inv_mod(26).tolist()

def mod26mult(a, b):
    op = (Matrix(a) * Matrix(b)) % 26
    return op.tolist()

# from plain_to_cipher import *
# m = process(pc_pair, r)[0]
# print(mod26inv(m))
