def enc(m, k):
    a, b = k
    cipher = ""
    for _ in m:
        if('a' <= _ <= 'z'): cipher += chr((((ord(_) - ord('a')) * a + b) % 26) + ord('a'))
        elif('A' <= _ <= 'Z'): cipher += chr((((ord(_) - ord('A')) * a + b) % 26) + ord('A'))
    return cipher

print(enc("abcdefghijklmnopqrstuvwxyz", (7, 6)))