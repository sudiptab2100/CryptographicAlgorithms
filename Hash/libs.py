def fileToBit19(target):
    bdata = ""
    with open(target, "rb") as f:
        bdata = f.read()
    op = ""
    for b in bdata: op += str(bin(b)[2:])
    pad = 19 - len(op) % 19
    if pad != 19: op += '0' * pad
    return op, len(op)

def str_xor(s1, s2):
    n = len(s1) 
    assert n == len(s2)

    op = ''
    for i in range(n):
        op += str(int(s1[i]) ^ int(s2[i]))
    return op

def hexify(s1):
    l = len(s1)
    assert l % 4 == 0

    op = ''
    for i in range(0, l, 4):
        nib = int(s1[i: i + 4], 2)
        op += hex(nib)[2:]
    return '0x' + op
