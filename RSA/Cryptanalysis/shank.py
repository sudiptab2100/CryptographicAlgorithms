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

def shanks_algorithm(G, g, x):
    n = G
    m = math.ceil(math.sqrt(n))

    g_mj = []
    for j in range(m):
        g_mj.append((j, pow(g, j * m, n)))
    g_mj.sort(key=lambda x: x[1])

    g_inv = modInverse(g, n)
    xg_inv_i = []
    for i in range(m):
        xg_inv_i.append((i, (x * pow(g_inv, i, n)) % n))
    xg_inv_i.sort(key=lambda x: x[1])

    for (j, y1) in g_mj:
        for (i, y2) in xg_inv_i:
            if y1 == y2:
                return (m * j + i) % n
    
    return None


G = 29
g = 2
x = 15
r = shanks_algorithm(29, 2, 15)
print(r)