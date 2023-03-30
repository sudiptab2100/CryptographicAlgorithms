from crypt import *
from libs import *

def compress(h, m):
    e_keys = []
    [e_keys.append(m[i: i + 16]) for i in range(5)]
    h = str_xor(h, encrypt(h, e_keys))
    return h

def gen_hash(target):
    m_all, n = fileToBit20(target)

    h = '0' * 16
    for i in range(0, n, 20):
        m = m_all[i: i + 20]
        h = compress(h, m)
    
    return hexify(h)

print(gen_hash('Hash/msg.txt'))
print(gen_hash('Hash/Davies-Meyer_hash.svg'))