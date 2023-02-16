from creds import key
from libs import *

def dec(cipherStream, key):
    op = ''

    # cipherStream = binStream(msg)
    streamLen = len(cipherStream)

    S = KSA(key)
    i = j = 0
    for k in range(0, streamLen, 8):
        z, i, j = PRGA(S, i, j)
        # print(z, i, j)
        c = chr(int(XOR(cipherStream[k : k + 8], z), 2))
        op += c
    
    return op

cipher = ""
with open('RC4/cipher.txt', "r") as f:
    cipher = f.read()

msg = dec(cipher, key)
# print(cipher)
with open('RC4/dec_msg.txt', "w") as f:
    f.write(msg)