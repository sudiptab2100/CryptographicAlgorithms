def fileToBit16(target):
    bytess = ""
    with open(target, "rb") as f:
        bytess = f.read()
    op = ""
    for b in bytess: op += str(bin(b)[2:]).zfill(8)
    if len(bytess) % 2 != 0: op += '0' * 8
    return op

def bitStrToByteArr(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def bitsToFile(target, bytefile):
    with open(target, "wb") as f:
        f.write(bytefile)

def KeyMixing(sub_key, sub_msg):
    assert len(sub_key) == len(sub_msg)
    xor = bin(int(sub_key, 2) ^ int(sub_msg, 2))[2:]
    return xor.zfill(len(sub_key))

def SBox(input, reverse=False):
    smap = [
        0xE, 0x4, 0xD, 0x1, 
        0x2, 0xF, 0xB, 0x8, 
        0x3, 0xA, 0x6, 0xC, 
        0x5, 0x9, 0x0, 0x7
    ]

    op = ''
    for i in range(4):
        ip = int(input[i * 4: (i + 1) * 4], 2)
        t = bin(smap[ip])[2:]
        if reverse:
            t = bin(smap.index(ip))[2:]
        op += t.zfill(4)

    return op

def Permutation(input, reverse=False):
    pmap = [
        0x0, 0x4, 0x8, 0xC, 
        0x1, 0x5, 0x9, 0xD, 
        0x2, 0x6, 0xA, 0xE,
        0x3, 0x7, 0xB, 0xF
    ]

    op = ""
    if reverse:
        for i in range(16): op += input[pmap.index(i)]
    else:
        for i in range(16): op += input[pmap[i]]

    return op
