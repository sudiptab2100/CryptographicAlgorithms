from crypt import *
from libs import *

print_intermediate = True

def compress(h, m):
    e_keys = []
    [e_keys.append(m[i: i + 16]) for i in range(5)]
    h = str_xor(h, encrypt(h, e_keys))
    return h

def gen_hash(target):
    m_all, n = fileToBit19(target)

    h = '0' * 16
    
    if print_intermediate:
        print('\n\t     h_0:', h)
        print('\n\t     Msg:\t\t      h_i:\n')
    
    for i in range(0, n, 19):
        m = m_all[i: i + 19]
        if i == 0: m = '0' + m
        else: m = '1' + m
        h = compress(h, m)
        if print_intermediate: print('\t    ', m, '-->', h)
    
    print('\n\t [X] Hash: ' + hexify(h) + '\n')

print("\n\t [X] Construction: Merkle-Damgard")
print("\t [X] PGV Scheme: Davies-Meyer")

gen_hash('Hash/msg.txt')
# gen_hash('Hash/Davies-Meyer_hash.svg')