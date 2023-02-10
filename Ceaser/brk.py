def tryDec(c, k):
    cipher = ""
    for _ in c:
        if('a' <= _ <= 'z'): cipher += chr(((ord(_) - ord('a') - k) % 26) + ord('a'))
        if('A' <= _ <= 'Z'): cipher += chr(((ord(_) - ord('A') - k) % 26) + ord('A'))
    return cipher

def brk(c):
    for k in range(26):
        print("Key = " + str(k) + ", Msg = " + tryDec(c, k))

brk("lnwbimt")