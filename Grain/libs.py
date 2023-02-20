import binascii

Y = [0] * 80
X = [0] * 80

def breakInSlabs(s, n):
    s_len = len(s)
    till = (s_len // n) * n
    extra = s_len % n
    # print(extra)
    for i in range(0, till, n):
        yield s[i: i + n]

def toBits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def toStr(bits, encoding='utf-8', errors='surrogatepass'):
    op = ''
    slabs = breakInSlabs(bits, 8)
    for slab in slabs:
        n = int(slab, 2)
        c = chr(n)
        op += c
    
    return op

def g(X):
    return X[0] ^ X[63] ^ X[60] ^ X[52] ^ X[45] ^ X[37] ^ X[33] ^ X[28] ^ X[21] ^ X[15] ^ X[19] ^ X[0] ^ X[63] & X[60] ^ X[37] & X[33] ^ X[15] & X[9] ^ X[60] & X[52] & X[45] ^ X[33] & X[28] & X[21] ^ X[63] & X[45] & X[28] & X[9] ^ X[60] & X[52] & X[37] & X[33] ^ X[63] & X[60] & X[21] & X[15] ^ X[63] & X[60] & X[52] & X[45] & X[37] ^ X[33] & X[28] & X[21] & X[15] & X[9] ^ X[52] & X[45] & X[37] & X[33] & X[28] & X[21]

def f(Y):
    return Y[62] ^ Y[51] ^ Y[38] ^ Y[23] ^ Y[13] ^ Y[0]

def h(X, Y):
    x0 = Y[0]
    x1 = Y[25]
    x2 = Y[46]
    x3 = Y[64]
    x4 = X[63]
    return x1 ^ x4 ^ x0 & x3 ^ x2 & x3 ^ x3 & x3 ^ x0 & x1 & x2 ^ x0 & x2 & x3 ^ x0 & x2 & x4 ^ x1 & x2 & x4 ^ x2 & x3 & x4

def clock():
    hxy = 0
    fy = 0
    gx = 0

    global Y
    global X

    for ix in range(160):
        fy = f(Y) ^ hxy
        gx = hxy ^ g(X)
        hxy = h(X, Y)

        Y[:-1] = Y[1:]
        Y[-1] = fy
        X[:-1] = X[1:]
        X[-1] = gx

def init(iv, key):
    iv_bin = toBits(iv)[:80]
    key_bin = toBits(key)[:80]
    
    for i in range(len(iv_bin)): Y[i] = int(iv_bin[i])
    for i in range(64, 80): Y[i] = 1

    for i in range(len(key_bin)): X[i] = int(key_bin[i])

    clock()

def genKeyStream():
    hxy = 0
    while True:
        fy = f(Y)
        gx = g(X)
        hxy = h(X, Y)

        Y[:-1] = Y[1:]
        Y[-1] = fy
        X[:-1] = X[1:]
        X[-1] = gx

        yield hxy