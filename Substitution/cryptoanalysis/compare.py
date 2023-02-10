cipher = ""
with open('Substitution/cipher.txt', "r") as f:
    cipher = f.read()

msg = ""
with open('Substitution/dec_msg.txt', "r") as f:
    msg = f.read()

c = cipher.split(" ")
m = msg.split(" ")

n = len(c)
op = ""
if n == len(m):
    for i in range(n):
        t = f"[{m[i]} {c[i]}] "
        op += t

with open("Substitution/cryptoanalysis/comparison.txt", "w") as f:
    f.write(op)