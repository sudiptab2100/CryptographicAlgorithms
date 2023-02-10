from creds import dec_key

def dec(c, k):
    op = ""
    for i in c:
        if i == ' ':
            op += i
            continue
        si = i.lower()
        op += k[ord(si) - ord('a')][0]
    return op

cipher = ""
with open('Substitution/cipher.txt', "r") as f:
    cipher = f.read()

msg = dec(cipher, dec_key)

with open("Substitution/dec_msg.txt", "w") as f:
    f.write(msg)