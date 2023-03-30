from crypt import encrypt

def isValid(guessed_k0, guessed_k1, plain_cipher_pairs):
    for ((input0, input1), (output0, output1)) in plain_cipher_pairs:
        if encrypt(input0, guessed_k0, guessed_k1) != output0:
            return False
        if encrypt(input1, guessed_k0, guessed_k1) != output1:
            return False
    return True