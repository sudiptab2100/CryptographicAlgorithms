from creds import key
from libs import *

def enc(msg, key):
    op = ''

    msgStream = binStream(msg)
    streamLen = len(msgStream)

    S = KSA(key)
    i = j = 0
    for k in range(0, streamLen, 8):
        z, i, j = PRGA(S, i, j)
        # print(z, i, j)
        op += XOR(msgStream[k : k + 8], z)
    
    return op

msg = ""
with open('RC4/msg.txt', "r") as f:
    msg = f.read()

cipher = enc(msg, key)
# print(cipher)
with open('RC4/cipher.txt', "w") as f:
    f.write(cipher)