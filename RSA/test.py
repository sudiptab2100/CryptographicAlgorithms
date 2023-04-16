from crypt import *
import json
import pickle


creds = json.load(open('RSA/creds.json'))
n = int(creds['n'], 16)
e = int(creds['e'], 16)
d = int(creds['d'], 16)

with open("RSA/IITJammu.png", "rb") as f: 
    m = f.read()
    c = encrypt(m, e, n)
    with open("RSA/cipher", "wb") as op: pickle.dump(c, op)
print('Encrypted')

with open("RSA/cipher", "rb") as f:
    c = pickle.load(f)
    dm = decrypt(c, d, n)
    with open("RSA/decrypted_IITJammu.png", "wb") as op: op.write(bytearray(dm))
print('Decrypted')
