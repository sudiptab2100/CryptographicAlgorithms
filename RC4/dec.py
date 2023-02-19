from creds import key
from libs import *

def dec(cipher, key):
    op = ''
    cipherLen = len(cipher)

    S = KSA(key)
    k = 0
    for z in PRGA(S):
        op += chr(ord(cipher[k]) ^ z)
        k += 1
        if k >= cipherLen: break
    
    return op

cipher = ""
with open('RC4/cipher.txt', "rb") as f:
    cipher = f.read()

msg = dec(cipher.decode('utf-8'), key)
with open('RC4/dec_msg.txt', "w") as f:
    f.write(msg)