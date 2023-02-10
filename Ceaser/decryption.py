def dec(c, k):
    m = ""
    for _ in c:
        if('a' <= _ <= 'z'): m += chr(((ord(_) - ord('a') - k) % 26) + ord('a'))
        if('A' <= _ <= 'Z'): m += chr(((ord(_) - ord('A') - k) % 26) + ord('A'))
    return m

print(dec("lnwbimt", 19))