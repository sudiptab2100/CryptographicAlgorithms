from crypt import sbox
import numpy as np

def gen_dist():
    print("[*] Computing difference distribution table.")
    diff_dist_table = [[0 for x in range(16)] for y in range(16)]
    for in_diff in range(16):
        for input0 in range(16):
            input1 = input0 ^ in_diff
            out_diff = sbox[input0] ^ sbox[input1]
            diff_dist_table[in_diff][out_diff] = diff_dist_table[in_diff][out_diff] + 1
    return diff_dist_table

diff_dist_table = gen_dist()
temp = np.array(diff_dist_table[1:])
# [print(_) for _ in diff_dist_table]
a = np.array(temp)
indices = np.where(a == a.max())
index = []
for i in indices: index.append(i[0])
print(f"\t* input diff = {index[0] + 1}\n\t* output diff = {index[1]}\n")
ip_diff = index[0] + 1
op_diff = index[1]
# 16  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
# 0   0  0  4  2  0  0  2  0  4  0  0  0  2  2  0
# 0   4  0  6  0  2  0  0  0  0  2  0  2  0  0  0
# 0   0  4  0  0  0  2  2  0  0  4  0  0  0  2  2
# 0   2  0  0  0  0  0  2  2  0  0  0  0  4  2  4
# 0   2  2  0  2  0  2  0  0  2  2  0  2  0  2  0
# 0   0  0  0  4  0  0  0  0  0  0  4  4  0  4  0
# 0   0  2  2  0  2  0  2  2  2  0  0  0  2  0  2
# 0   2  2  0  0  2  0  2  0  2  2  0  0  2  0  2
# 0   2  0  0  4  0  4  2  2  0  0  0  0  0  2  0
# 0   0  2  2  2  0  2  0  2  2  0  0  2  0  2  0
# 0   0  0  0  0  4  0  4  0  0  0  4  0  4  0  0
# 0   0  4  0  0  2  2  0  4  0  0  0  2  0  0  2
# 0   0  0  0  0  0  4  0  0  0  0  8  0  0  0  4
# 0   4  0  0  2  2  0  0  0  4  0  0  2  2  0  0
# 0   0  0  2  0  2  0  0  4  0  6  0  2  0  0  0