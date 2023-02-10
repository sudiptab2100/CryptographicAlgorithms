from creds import enc_key
from get_msg import msg

def enc(m, k):
    op = ""
    for i in m:
        if i == ' ': 
            op += i
            continue
        op += k[ord(i) - ord('a')][1]
    return op

cipher = enc(msg, enc_key)

with open("Substitution/cipher.txt", "w") as f:
    f.write(cipher)