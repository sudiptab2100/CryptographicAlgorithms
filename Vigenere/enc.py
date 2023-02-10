from creds import *
def enc(m, k, r):
    op = ""
    for i in range(len(m)):
        k_i = k[i % r]
        op += chr((ord(m[i]) - ord('a') + k_i) % 26 + ord('a'))
    return op

msg = ""
with open('Vigenere/msg.txt', "r") as f:
    msg = f.read()

cipher = enc(msg, key, r)

with open("Vigenere/cipher.txt", "w") as f:
    f.write(cipher)