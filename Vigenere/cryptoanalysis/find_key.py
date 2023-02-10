from freq_table import freq

def freqGenerator(yi):
    f = []
    for i in range(26): f.append([chr(i + ord('A')), 0])
    for c in yi: f[ord(c) - ord('a')][1] += 1
    n = len(yi)
    for i in range(26): f[i][1] = round(f[i][1] / n, 3)
    f.sort(key=lambda x: x[1])
    return f

def approxKi(fi):
    ki = ord(fi[-1][0]) - ord(freq[-1][0])
    if ki < 0: return ki + 26
    return ki

cipher = ""
with open('Vigenere/cipher.txt', "r") as f:
    cipher = f.read()

r = 5
y = []
key = []

for i in range(r): 
    y.append([])

for i in range(len(cipher)):
    y[i % r].append(cipher[i])

for yi in y:
    fi = freqGenerator(yi)
    key.append(approxKi(fi))

print(key)