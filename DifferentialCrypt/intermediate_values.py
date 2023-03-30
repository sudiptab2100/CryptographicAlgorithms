from crypt import sbox

def get(input_diff, output_diff):
    good_pairs = []
    for input0 in range(16):
        input1 = input0 ^ input_diff
        if sbox[input0] ^ sbox[input1] == output_diff:
            good_pairs.append([input0, input1])
    return good_pairs
