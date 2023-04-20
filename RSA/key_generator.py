import json

def KSA(seed, N=1024):
    key = bin(int.from_bytes(seed.encode(), 'big'))[2:]
    S = []
    n = len(key)
    for i in range(N):
        S.append(i)
    j = 0
    for i in range(N):
        j = (j + S[i] + ord(key[i % n])) % N
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, N=1024):
    i = 0
    j = 0
    while(True):
        i = (i + 1) % N
        j = (j + S[i]) % N

        S[i], S[j] = S[j], S[i]
        z = S[(S[i] + S[j]) % N]
        yield z % 2

def isMillerRabinPrime(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    
    for trials in range(5):
        import random
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1: return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

def isPrime(num):
    if (num < 2): return False

    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes: return True
    
    for prime in lowPrimes:
        if (num % prime == 0): return False

    return isMillerRabinPrime(num)

def generateNBitRandom(seed, N):
    S = KSA(seed, N)
    nextRandom = PRGA(S, N)
    while True:
        op = ""
        for i in range(N): op += str(next(nextRandom))
        yield op

def generateLargePrime(start, keysize=1024):
    num = start
    while True:
        if isPrime(num): return num
        else: num += 2

def modInverse(A, M):
    m0 = M
    y = 0
    x = 1

    if (M == 1):
        return 0

    while (A > 1):
        q = A // M
        t = M
        M = A % M
        A = t
        t = y

        y = x - q * y
        x = t

    if (x < 0): x = x + m0
    
    return x



keySize = int(input('Key Size: '))
seed = input('Seed: ')

nextRandom = generateNBitRandom(seed, keySize - 2)

p = generateLargePrime(int('1' + next(nextRandom) + '1', 2), keySize)
q = generateLargePrime(int('1' + next(nextRandom) + '1', 2), keySize)
n = p * q
phi_n = (p - 1) * (q - 1)

while True:
    e = int(next(nextRandom) + next(nextRandom), 2)
    try:
        d = modInverse(e, phi_n)
        
        print("p:", hex(p))
        print("q:", hex(q))
        print("n:", hex(n))
        print("phi(n):", hex(phi_n))
        print("e:", hex(e))
        print("d:", hex(d))

        creds = dict()
        creds['key_size'] = keySize
        creds['p'] = hex(p)
        creds['q'] = hex(q)
        creds['n'] = hex(n)
        creds['phi_n'] = hex(phi_n)
        creds['e'] = hex(e)
        creds['d'] = hex(d)
        with open("RSA/creds.json", "w") as outfile: json.dump(creds, outfile)

        break

    except: e += 1
