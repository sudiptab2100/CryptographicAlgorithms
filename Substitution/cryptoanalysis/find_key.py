from freq_table import *

def freqGenerator(cipher, n):
    f = []
    for i in range(26): f.append([chr(i + ord('A')), 0])
    for c in cipher: 
        if c == ' ': continue
        if 'A' <= c <= 'Z': c = c.lower()
        # print(ord(c) - ord('a'), c)
        f[ord(c) - ord('a')][1] += 1
    for i in range(26): f[i][1] = round(f[i][1] / n, 3)
    f.sort(key=lambda x: x[1])
    return f


cipher = ""
with open('Substitution/cipher.txt', "r") as f:
    cipher = f.read()


f = open("Substitution/cryptoanalysis/analyzed.txt", "w")

n = len(cipher)

f.write("\n\nKeys\n\n")
cipherFreq = freqGenerator(cipher, n)
key = []
# count = 0
for i in range(26):
    # print("%-2c %-1.3f | %-2c %-1.3f" % (freq[i][0], freq[i][1], cipherFreq[i][0], cipherFreq[i][1]))
    key.append([freq[i][0], cipherFreq[i][0]])
    # if freq[i][0] == cipherFreq[i][0]: count += 1

key.sort(key=lambda x: x[0])
for i in range(26):
    f.write("%-2c | %-2c | \n" % (key[i][0], key[i][1]))
print(key)
# print(count)

# f.write("\n\nDigrams\n\n")
# di_dict = dict()
# for i in range(n - 1):
#     digram = cipher[i: i + 2]
#     if digram in di_dict.keys():
#         di_dict[digram] += 1
#     else: di_dict[digram] = 0

# digs = []
# for k in di_dict.keys():
#     digs.append([k, di_dict[k]])
# digs.sort(key=lambda x: x[1], reverse=True)
# for i in range(30):
#     f.write("%-4s | %-4s\n" % (digrams[i], digs[i][0]))
# # print(digs[:30])

# f.write("\n\nTrigrams\n\n")
# tri_dict = dict()
# for i in range(n - 2):
#     trigram = cipher[i: i + 3]
#     if trigram in tri_dict.keys():
#         tri_dict[trigram] += 1
#     else: tri_dict[trigram] = 0

# trigs = []
# for k in tri_dict.keys():
#     trigs.append([k, tri_dict[k]])
# trigs.sort(key=lambda x: x[1], reverse=True)
# for i in range(12):
#     f.write("%-4s | %-4s\n" % (trigrams[i], trigs[i][0]))
# # print(trigs[:12])

f.close()