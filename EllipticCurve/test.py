from curve import Curve

A = 1
B = 7
p = 39499
c = Curve(A, B, p)

P1 = (397, 69)
P2 = (6979, 39336)

print(c.add(P1, P2)) # Add two points
print(c.add(P1, P1)) # Point Doubling
print(c.add(c.POINT_AT_INFINITY, P2)) # Add with identity(Point at Infinity)

# x = 0
# y = 0

# while True:
#     y = c.getY(x)
#     if y != c.NO_Y:
#         break
#     x += 1

# print(x, y)
# print(c.isPointOnCurve((x, y[0])))
# print(c.isPointOnCurve((x, y[1])))
