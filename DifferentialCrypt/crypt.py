sbox = [12, 2, 13, 14, 3, 10, 0, 9, 5, 8, 15, 11, 4, 7, 1, 6]

def round_function(input, key):
    return sbox[key ^ input]

def encrypt(input, key0, key1):
    return round_function(input, key0) ^ key1