from creds import *
from libs import *

def dec(cipher_bin, key, iv):
    op = ''
    cipher_bin_len = len(cipher_bin)

    init(iv, key)
    z = genKeyStream()

    for b in cipher_bin:
        op += str(int(b) ^ next(z))

    op = toStr(op)
    return op

cipher = ""
with open('Grain/cipher.txt', "r") as f:
    cipher = f.read()

msg = dec(cipher, key, iv)
with open('Grain/dec_msg.txt', "w") as f:
    f.write(msg)