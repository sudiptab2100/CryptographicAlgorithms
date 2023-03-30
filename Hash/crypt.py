def KeyMixing(sub_key, sub_msg):
    assert len(sub_key) == len(sub_msg)
    xor = bin(int(sub_key, 2) ^ int(sub_msg, 2))[2:]
    return xor.zfill(len(sub_key))

def SBox(input):
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
        op += t.zfill(4)

    return op

def Permutation(input):
    pmap = [
        0x0, 0x4, 0x8, 0xC, 
        0x1, 0x5, 0x9, 0xD, 
        0x2, 0x6, 0xA, 0xE,
        0x3, 0x7, 0xB, 0xF
    ]

    op = ""
    for i in range(16): op += input[pmap[i]]

    return op

def encrypt(msg, keys):
    op = ''
    n = len(msg)
    for i in range(n // 16):
        sub_msg = "".join(msg[i * 16: (i + 1) * 16])
        for j in range(3):
            sub_key = keys[j]
            mix = KeyMixing(sub_key, sub_msg)
            sbx = SBox(mix)
            sub_msg = Permutation(sbx)
        op += KeyMixing(keys[4], SBox(KeyMixing(keys[3], sub_msg)))
    return op
