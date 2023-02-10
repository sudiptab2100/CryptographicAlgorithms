cipher = ""
with open('Vigenere/cipher.txt', "r") as f:
    cipher = f.read()
# cipher = "onceuponatimetherewasacownamedbellawholivedonasmallfarmwithherfamilyandfriends"
r = 1
while True:
    y = []
    for i in range(r): y.append([])
    for i in range(len(cipher)):
        y[i % r].append(cipher[i])
    
    print(f"r = {r}")
    for i in y:
        v = 0
        freq = [0] * 26
        len_i = len(i)
        for _ in i:
            freq[ord(_) - ord('a')] += 1
        ic = 0
        for _ in freq:
            ic += (_ / len_i) ** 2
        print(ic)

    r += 1
    if r == 20: break

# msg = ""
# with open('Vigenere/msg.txt', "r") as f:
#     msg = f.read()
# freq = [0] * 26
# for c in msg:
#     freq[ord(c) - ord('a')] += 1
# ic = 0
# for _ in freq:
#     ic += (_ / len(msg)) ** 2
# print(ic)