import random
from crypt import *

def generate(input_diff, num, key):
    pairs = []
    for input0 in random.sample(range(16), num):
        input1 = input0 ^ input_diff
        output0 = encrypt(input0, key[0], key[1])
        output1 = encrypt(input1, key[0], key[1])
        pairs.append(((input0, input1), (output0, output1)))
    return pairs