import random

l = []
for i in range(26): l.append(chr(i + ord('a')))

random.shuffle(l)

key = []
for i in range(26):
    key.append([chr(ord('a') + i), l[i]])

print(key)
print()
key.sort(key=lambda x: x[1])
print(key)