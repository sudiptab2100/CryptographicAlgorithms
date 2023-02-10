import numpy as np
from creds import *

def enc(m, k, r):
    fm = []
    op = ""
    for c in m:
        fm.append(ord(c) - ord('a'))
    pad = r - len(fm) % r
    for i in range(pad):
        fm.append(0)
    for i in range(0, len(fm), r):
        slab = fm[i: i + r]
        eslab = np.dot(slab, k)
        # print(slab, eslab)
        for e in eslab:
            op += chr(e % 26 + ord('a'))
    return op[:-r]
    


msg = ""
with open('Hill/msg.txt', "r") as f:
    msg = f.read()

cipher = enc(msg, enc_key, r)

with open("Hill/cipher.txt", "w") as f:
    f.write(cipher)

# msg = "big"
# cipher = enc(msg, enc_key, r)
# print(cipher)
