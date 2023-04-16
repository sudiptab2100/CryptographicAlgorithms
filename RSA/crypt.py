def encrypt(m, e, n):
    cipher = []
    for _ in m: cipher.append(pow(_, e, n))
    return cipher

def decrypt(c, d, n):
    msg = []
    for _ in c: msg.append(pow(_, d, n))
    return msg
