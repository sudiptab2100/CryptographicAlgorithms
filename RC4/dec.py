from creds import key
from libs import *

def dec(cipherStream, key):
    op = ''
    streamLen = len(cipherStream)

    S = KSA(key)
    k = 0
    for z in PRGA(S):
        op += chr(int(XOR(cipherStream[k : k + 8], z), 2))
        k += 8
        if k >= streamLen: break
    
    return op

cipher = ""
with open('RC4/cipher.txt', "r") as f:
    cipher = f.read()

msg = dec(cipher, key)
with open('RC4/dec_msg.txt', "w") as f:
    f.write(msg)