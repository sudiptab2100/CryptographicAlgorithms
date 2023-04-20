import sys

def encrypt(m, e, n, display_progress=False):
    cipher = []
    total = len(m)
    print()
    for i in range(total): 
        cipher.append(pow(m[i], e, n))
        if display_progress:
            sys.stdout.write("\033[F")
            print(f"Encrypted: {i + 1} / {total}, {round(((i + 1) * 100) / total, 2)}%")
    return cipher

def decrypt(c, d, n, display_progress=False):
    msg = []
    total = len(c)
    print()
    for i in range(total): 
        msg.append(pow(c[i], d, n))
        if display_progress:
            sys.stdout.write("\033[F")
            print(f"Decrypted: {i + 1} / {total}, {round(((i + 1) * 100) / total, 2)}%")
    return msg