from math import isqrt

class Curve:

    POINT_AT_INFINITY = float("inf")
    NO_Y = -901
    NOT_ON_CURVE = -902

    # y^2 = x^3 + A*x + B over Field Fp where p is prime
    def __init__(self, A, B, p):
        self.A = A
        self.B = B
        self.p = p
    
    # P = (x, y)
    def isPointOnCurve(self, P):
        if P == self.POINT_AT_INFINITY: return True

        x, y = P
        _y2 = (x ** 3 + self.A * x + self.B) % self.p
        if _y2 == pow(y, 2, self.p):
            return True
        return False
    
    # checking if a int is a square of any int
    def __isSquareNum(self, num) -> bool:
        return num == isqrt(num) ** 2
    
    # get y for some x on the curve
    def getY(self, x):
        y2 = (pow(x, 3, self.p) + self.A * x + self.B) % self.p

        if not self.__isSquareNum(y2):
            return self.NO_Y
        
        _y = isqrt(y2)
        if _y == 0: 
            return [_y]
        return [_y, self.p - _y]

    # A^-1 ~ 1 mod M
    def __modInverse(self, A, M):
        if A < 0:
            A += M
        
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
    
    # P = P1 + P2
    def add(self, P1, P2):
        assert (self.isPointOnCurve(P1) and self.isPointOnCurve(P2)), "Point(s) Not On Curve"

        if P1 == self.POINT_AT_INFINITY: 
            return P2
        elif P2 == self.POINT_AT_INFINITY: 
            return P1
        
        (x1, y1), (x2, y2) = P1, P2
        m = 0
        if P1 == P2:
            if y1 == 0: 
                return self.POINT_AT_INFINITY
            
            m = (3 * x1 ** 2 + self.A) * self.__modInverse(2 * y1, self.p)
        else:
            if x1 == x2: 
                return self.POINT_AT_INFINITY
            
            m = ((y2 - y1) * self.__modInverse((x2 - x1), self.p)) % self.p
        
        x3 = (m ** 2 - (x1 + x2)) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        P = (x3, y3)

        return P
