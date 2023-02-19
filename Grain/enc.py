from creds import *
from libs import *

def enc(msg, key, iv):
    op = ''
    msg_bin = toBits(msg)
    msg_bin_len = len(msg_bin)

    init(iv, key)
    z = genKeyStream()

    for b in msg_bin:
        op += str(int(b) ^ next(z))
    
    return op

msg = ""
with open('Grain/msg.txt', "r") as f:
    msg = f.read()

cipher = enc(msg, key, iv)
with open('Grain/cipher.txt', "w") as f:
    f.write(cipher)