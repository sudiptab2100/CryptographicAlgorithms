import binascii

LFSR = [0] * 80
NFSR = [0] * 80

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

def clock():
    hx = 0
    fx = 0
    gx = 0
    global LFSR
    global NFSR
    for ix in range(160):
        fx = LFSR[62] ^ LFSR[51] ^ LFSR[38] ^ LFSR[23] ^ LFSR[13] ^ LFSR[0] ^ hx
        gx = hx ^ NFSR[0] ^ NFSR[63] ^ NFSR[60] ^ NFSR[52] ^ NFSR[45] ^ NFSR[37] ^ NFSR[33] ^ NFSR[28] ^ NFSR[21] ^ NFSR[15] ^ NFSR[19] ^ NFSR[0] ^ NFSR[63] & NFSR[60] ^ NFSR[37] & NFSR[33] ^ NFSR[15] & NFSR[9] ^ NFSR[60] & NFSR[52] & NFSR[45] ^ NFSR[33] & NFSR[28] & NFSR[21] ^ NFSR[63] & NFSR[45] & NFSR[28] & NFSR[9] ^ NFSR[60] & NFSR[52] & NFSR[37] & NFSR[33] ^ NFSR[63] & NFSR[60] & NFSR[21] & NFSR[15] ^ NFSR[63] & NFSR[60] & NFSR[52] & NFSR[45] & NFSR[37] ^ NFSR[33] & NFSR[28] & NFSR[21] & NFSR[15] & NFSR[9] ^ NFSR[52] & NFSR[45] & NFSR[37] & NFSR[33] & NFSR[28] & NFSR[21]
        x0 = LFSR[0]
        x1 = LFSR[25]
        x2 = LFSR[46]
        x3 = LFSR[64]
        x4 = NFSR[63]
        hx = x1 ^ x4 ^ x0 & x3 ^ x2 & x3 ^ x3 & x3 ^ x0 & x1 & x2 ^ x0 & x2 & x3 ^ x0 & x2 & x4 ^ x1 & x2 & x4 ^ x2 & x3 & x4
        LFSR[:-1] = LFSR[1:]
        LFSR[-1] = fx
        NFSR[:-1] = NFSR[1:]
        NFSR[-1] = gx

def init(iv, key):
    iv_bin = toBits(iv)
    key_bin = toBits(key)[:80]
    
    for i in range(len(iv_bin)): LFSR[i] = int(iv_bin[i])
    for i in range(64, 80): LFSR[i] = 1
    for i in range(len(key_bin)): NFSR[i] = int(key_bin[i])

    clock()

def genKeyStream():
    hx = 0
    while True:
        fx = LFSR[62] ^ LFSR[51] ^ LFSR[38] ^ LFSR[23] ^ LFSR[13] ^ LFSR[0]
        gx = NFSR[0] ^ NFSR[63] ^ NFSR[60] ^ NFSR[52] ^ NFSR[45] ^ NFSR[37] ^ NFSR[33] ^ NFSR[28] ^ NFSR[21] ^ NFSR[15] ^ NFSR[19] ^ NFSR[0] ^ NFSR[63] & NFSR[60] ^ NFSR[37] & NFSR[33] ^ NFSR[15] & NFSR[9] ^ NFSR[60] & NFSR[52] & NFSR[45] ^ NFSR[33] & NFSR[28] & NFSR[21] ^ NFSR[63] & NFSR[45] & NFSR[28] & NFSR[9] ^ NFSR[60] & NFSR[52] & NFSR[37] & NFSR[33] ^ NFSR[63] & NFSR[60] & NFSR[21] & NFSR[15] ^ NFSR[63] & NFSR[60] & NFSR[52] & NFSR[45] & NFSR[37] ^ NFSR[33] & NFSR[28] & NFSR[21] & NFSR[15] & NFSR[9] ^ NFSR[52] & NFSR[45] & NFSR[37] & NFSR[33] & NFSR[28] & NFSR[21]
        x0 = LFSR[0]
        x1 = LFSR[25]
        x2 = LFSR[46]
        x3 = LFSR[64]
        x4 = NFSR[63]
        hx = x1 ^ x4 ^ x0 & x3 ^ x2 & x3 ^ x3 & x3 ^ x0 & x1 & x2 ^ x0 & x2 & x3 ^ x0 & x2 & x4 ^ x1 & x2 & x4 ^ x2 & x3 & x4
        LFSR[:-1] = LFSR[1:]
        LFSR[-1] = fx
        NFSR[:-1] = NFSR[1:]
        NFSR[-1] = gx
        yield hx