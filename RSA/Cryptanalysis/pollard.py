n = int(input("n: "))
B = int(input("B: "))

def gcd(m, n):
    if m < n:
        m, n = n, m
    while (m % n != 0):
        m, n = n, m % n
    return n

def pollard(n, B):
    a = 2
    for j in range(2, B): 
        a = pow(a, j, n)
        import sys
        sys.stdout.write("\033[F")
        print(f"Iterated: {j + 1} / {B}, {round(((j + 1) * 100) / B, 2)}%")
    p = gcd(a - 1, n)
    if 1 < p < n:
        return p
    return -1

print()
p = pollard(n, B)
if p != -1:
    q = n // p
    print(f"p: {p}")
    print(f"q: {q}")
else: print("Factors Not Found")

# n = 207514406707113315160524254481635516179942749881353194595949337608273631801912058663031
# B = 3500000

# p = 2298993491
# q = 90263155384946374848402845905071558195178356806123377839502259647012472468941