# 1 1
# 3 9
# 5 21
# 7 15
# 9 3
# 11 19
# 15 7
# 17 23
# 19 11
# 21 5
# 23 17
# 25 25

def inv(a):
    for i in range(1, 26):
        if (i * a) % 26 == 1: return i

def dec(c, k):
    a, b = k
    m = ""
    for _ in c:
        if('a' <= _ <= 'z'): m += chr((((ord(_) - ord('a') - b) * inv(a)) % 26) + ord('a'))
        elif('A' <= _ <= 'Z'): m += chr((((ord(_) - ord('A') - b) * inv(a)) % 26) + ord('A'))
    return m

print(dec("gnubipwdkryfmtahovcjqxelsz", (7, 6)))