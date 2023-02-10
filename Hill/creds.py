from sympy import Matrix

r = 3
enc_key = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

dec_key = Matrix(enc_key).inv_mod(26).tolist()