import numpy as np
from creds import *

def dec(cipher, k, r):
    fc = []
    op = ""
    for c in cipher:
        fc.append(ord(c) - ord('a'))
    pad = r - len(fc) % r
    for i in range(pad):
        fc.append(0)
    for i in range(0, len(fc), r):
        slab = fc[i: i + r]
        eslab = np.dot(slab, k)
        # print(slab, eslab)
        for e in eslab:
            op += chr(e % 26 + ord('a'))
    return op[:-r]
    


cipher = ""
with open('Hill/cipher.txt', "r") as f:
    cipher = f.read()

msg = dec(cipher, dec_key, r)

with open("Hill/dec_msg.txt", "w") as f:
    f.write(msg)
