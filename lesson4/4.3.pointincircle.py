def isPointInCircle(x, y, xc, yc, r):
    dist = ((x - xc)**2 + (y - yc)**2)**(1/2)
    return dist <= r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if isPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
