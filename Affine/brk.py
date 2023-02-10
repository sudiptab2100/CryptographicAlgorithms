def inv(a):
    for i in range(1, 26):
        if (i * a) % 26 == 1: return i

def dec(m, k):
    a, b = k
    cipher = ""
    for _ in m:
        if('a' <= _ <= 'z'): cipher += chr((((ord(_) - ord('a') - b) * inv(a)) % 26) + ord('a'))
        elif('A' <= _ <= 'Z'): cipher += chr((((ord(_) - ord('A') - b) * inv(a)) % 26) + ord('A'))
    return cipher

def brk(c):
    i = 1
    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        for b in range(26):
            print(i, a, b, dec(c, (a, b)))
            i += 1

print(brk("gnubipwdkryfmtahovcjqxelsz"))