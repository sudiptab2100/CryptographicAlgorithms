from plain_to_cipher import *
from process_pairs import *

m, c = process(pc_pair, r)
mInv = mod26inv(m)
key = mod26mult(mInv, c)

# print(m)
# print(c)
# print(mInv)
# print(key)

print('Key:')
for i in range(r):
    for j in range(r):
        print("%3i" % key[i][j], end=' ')
    print()
