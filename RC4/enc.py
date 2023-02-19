from creds import key
from libs import *

def enc(msg, key):
    op = ''

    msgStream = binStream(msg)
    streamLen = len(msgStream)

    S = KSA(key)
    k = 0
    for z in PRGA(S):
        op += XOR(msgStream[k : k + 8], z)
        k += 8
        if k >= streamLen: break
    
    return op

msg = ""
with open('RC4/msg.txt', "r") as f:
    msg = f.read()

cipher = enc(msg, key)
with open('RC4/cipher.txt', "w") as f:
    f.write(cipher)