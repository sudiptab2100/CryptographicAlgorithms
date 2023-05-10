import math

def primeFactors(n, B):
    c = 2
    op = []
    while(n > 1):
        if(n % c == 0):
            # print(c, end=" ")
            op.append(c)
            n = n / c
        else:
            c = c + 1
    
    freq = [0] * len(B)
    for i in range(len(B)):
        for j in op:
            if j == B[i]:
                freq[i] += 1
    return (op, freq)

def magic_eqn(p, g, B):
    n = len(B)
    pv = 1
    while n > 0 and pv < p:
        v = pow(g, pv, p)
        pv += 1

        # print(math.log(v, g), int(math.log(v, g)))
        lg = math.log(v, g)
        if lg - int(lg) <= 0.000000000000004: continue
        # else: print(lg - int(lg))
        factors, hj = primeFactors(v, B)
        isInB = True
        for f in factors:
            if f not in B:
                isInB = False
                break
        
        if isInB:
            # print(pv - 1)
            print(hj, [pv - 1])
            n -= 1

def lucky_exp(p, g, x, B):
    for i in range(p):
        v = (x * pow(g, i, p)) % p
        factors, hj = primeFactors(v, B)
        isInB = True
        for f in factors:
            if f not in B:
                isInB = False
                break
        
        if isInB:
            print(hj, [i])
            break

B = [2, 3, 5, 7, 11]

p = 10007
g = 5
x = 9451

# p = 227
# g = 2
# x = 173

magic_eqn(p, g, B)
print()
lucky_exp(p, g, x, B)