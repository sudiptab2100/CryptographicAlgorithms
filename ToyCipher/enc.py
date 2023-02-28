from libs import *
from creds import sub_keys as e_keys, dec_sub_keys as d_keys

def encrypt(msg, keys):
    op = ''
    n = len(msg)
    for i in range(n // 16):
        sub_msg = "".join(msg[i * 16: (i + 1) * 16])
        for j in range(3):
            sub_key = keys[j]
            mix = KeyMixing(sub_key, sub_msg)
            sbx = SBox(mix)
            sub_msg = Permutation(sbx)
        op += KeyMixing(keys[4], SBox(KeyMixing(keys[3], sub_msg)))
    return op
    
def decrypt(cipher, keys):
    op = ''
    n = len(cipher)
    for i in range(n // 16):
        sub_msg = cipher[i * 16: (i + 1) * 16]
        sub_msg = KeyMixing(keys[4], sub_msg)
        sub_msg = SBox(sub_msg, reverse=True)
        sub_msg = KeyMixing(keys[3], sub_msg)
        for j in range(2, -1, -1):
            sub_key = keys[j]
            sub_msg = Permutation(sub_msg, reverse=True)
            sub_msg = SBox(sub_msg, reverse=True)
            sub_msg = KeyMixing(sub_key, sub_msg)
        op += sub_msg
    return op

msg = fileToBit16('ToyCipher/msg.txt')
cipher = encrypt(msg, e_keys)
dec_msg = decrypt(cipher, e_keys)

bcipher = bitStrToByteArr(cipher)
bmsg = bitStrToByteArr(dec_msg)

bitsToFile('ToyCipher/cipher.txt', bcipher)
bitsToFile('ToyCipher/dec_msg.txt', bmsg)