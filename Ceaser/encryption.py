def enc(m, k):
    cipher = ""
    for _ in m:
        if('a' <= _ <= 'z'): cipher += chr(((ord(_) - ord('a') + k) % 26) + ord('a'))
        if('A' <= _ <= 'Z'): cipher += chr(((ord(_) - ord('A') + k) % 26) + ord('A'))
    return cipher

print(enc("sudipta", 19))