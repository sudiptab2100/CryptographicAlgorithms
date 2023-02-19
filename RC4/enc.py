from creds import key
from libs import *

def enc(msg, key):
    op = ''
    msgLen = len(msg)

    S = KSA(key)
    k = 0
    for z in PRGA(S):
        op += chr(ord(msg[k]) ^ z)
        k += 1
        if k >= msgLen: break
    
    return op

msg = ""
with open('RC4/msg.txt', "r") as f:
    msg = f.read()

cipher = enc(msg, key)
with open('RC4/cipher.txt', "wb") as f:
    f.write(cipher.encode('utf-8'))