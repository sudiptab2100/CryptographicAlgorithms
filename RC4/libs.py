N = 256

def KSA(key):
    S = []
    n = len(key)
    for i in range(N):
        S.append(i)
    j = 0
    for i in range(N):
        j = (j + S[i] + ord(key[i % n])) % N
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    i = 0
    j = 0
    while(True):
        i = (i + 1) % N
        j = (j + S[i]) % N

        S[i], S[j] = S[j], S[i]
        z = S[(S[i] + S[j]) % N]
        yield z