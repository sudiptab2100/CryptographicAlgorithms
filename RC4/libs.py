def binStream(s):
    return ''.join(format(i, '08b') for i in bytearray(s, encoding ='utf-8'))

def __bitXOR(b1, b2):
    if b1 != b2: return '1'
    return '0'

def XOR(b1, b2):
    op = ''
    if len(b1) != len(b2): return
    for i in range(len(b1)):
        op += __bitXOR(b1[i], b2[i])
    return op

def KSA(key):
    S = []
    n = len(key)
    for i in range(256):
        S.append(i)
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % n])) % 256
        S[i], S[j] = S[j], S[i]
    return S
# for i := 0 to 255 do
# j := (j + S[i] + k[i mod (size of k)]) mod 256
# Swap (S[i], S[j])

# from creds import key
# print(KSA(key))

# Pseudorandom Generation Algorithm (PRGA): Output: z
# begin
# i := 0
# j := 0
# while(1)
#   i := (i + 1) mod 256
#   j := (j + S[i]) mod 256
#   Swap(S[i], S[j])
#   z := S[(S[i] + S[j]) mod 256]
# do
# end

def PRGA(S, i, j):
    i = (i + 1) % 256
    j = (j + S[i]) % 256

    S[i], S[j] = S[j], S[i]
    z = S[(S[i] + S[j]) % 256]
    return format(z, '08b'), i, j


# print(XOR('1011', '1100'))