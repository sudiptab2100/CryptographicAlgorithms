from creds import *
def dec(c, k, r):
    op = ""
    for i in range(len(c)):
        k_i = k[i % r]
        op += chr((ord(c[i]) - ord('a') - k_i) % 26 + ord('a'))
    return op

cipher = ""
with open('Vigenere/cipher.txt', "r") as f:
    cipher = f.read()

msg = dec(cipher, key, r)

with open("Vigenere/dec_msg.txt", "w") as f:
    f.write(msg)