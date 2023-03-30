import random
from crypt import *
from creds import *
import pair_generator
from get_distribution import ip_diff, op_diff
from key_validator import *
import intermediate_values


def find_good_pair(pairs, output_diff):
    print("[*] Searching for good pairs.")
    for ((input0, input1), (output0, output1)) in pairs:
        if output0 ^ output1 == output_diff:
            return ((input0, input1), (output0, output1))
    raise Exception("No good pair found.")

def recover_key(pairs, intermediate_values):
    for (p0, p1) in intermediate_values:
        guessed_k0 = p0 ^ good_p0
        guessed_k1 = sbox[p0] ^ good_c0
        if isValid(guessed_k0, guessed_k1, pairs):
            print("\t%s %s <-- Recovered key" % (guessed_k0, guessed_k1))
        else:
            print("\t%s %s" % (guessed_k0, guessed_k1))


print("[*] Real key: %s %s" % (key[0], key[1]))
intermediate_values = intermediate_values.get(ip_diff, op_diff)
print("[*] Possible intermediate values: " + str(intermediate_values))
pairs = pair_generator.generate(ip_diff, 3, key)
((good_p0, good_p1), (good_c0, good_c1)) = find_good_pair(pairs, 11)
print("[*] Found a good pair: " + str(((good_p0, good_p1), (good_c0, good_c1))))
print("[*] Brute-Forcing remaining key space")
recover_key(pairs, intermediate_values)