# A .082 N .067
# B .015 O .075
# C .028 P .019
# D .043 Q .001
# E .127 R .060
# F .022 S .063
# G .020 T .091
# H .061 U .028
# I .070 V .010
# J .002 W .023
# K .008 X .001
# L .040 Y .020
# M .024 Z .001

freq = [
    ['A', .082], ['B', .015], ['C', .028], ['D', .043], ['E', .127],
    ['F', .022], ['G', .020], ['H', .061], ['I', .070], ['J', .002],
    ['K', .008], ['L', .040], ['M', .024], ['N', .067], ['O', .075],
    ['P', .019], ['Q', .001], ['R', .060], ['S', .063], ['T', .091],
    ['U', .028], ['V', .010], ['W', .023], ['X', .001], ['Y', .020],
    ['Z', .001]
]

freq.sort(key=lambda x: x[1])

# [print(_) for _ in freq]






# msg = ""
# with open('Vigenere/msg.txt', "r") as f:
#     msg = f.read()
# freq_m = [0] * 26
# for c in msg:
#     freq_m[ord(c) - ord('a')] += 1
# n = len(msg)
# for i in range(26):
#     print(chr(i + ord('A')), round(freq_m[i] / len(msg), 3), freq[i][1])
