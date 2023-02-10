import random

l = []
for i in range(ord('a'), ord('z') + 1):
    l.append(chr(i))

random.shuffle(l)

dec_key = dict()
enc_key = dict()
for i in range(ord('a'), ord('z') + 1):
    dec_key[l[i - ord('a')]] = chr(i)
    enc_key[chr(i)] = l[i - ord('a')]

print(enc_key)
print()
print(dec_key)