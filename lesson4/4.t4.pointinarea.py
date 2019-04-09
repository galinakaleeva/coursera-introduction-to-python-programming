def IsPointInArea(x, y):
    upL1 = y >= 2 * x + 2
    underL1 = y <= 2 * x + 2
    upL2 = y >= -x
    underL2 = y <= -x
    inCircle = (x + 1)**2 + (y - 1)**2 <= 4
    outCircle = (x + 1)**2 + (y - 1)**2 >= 4
    return upL1 and upL2 and inCircle or underL1 and underL2 and outCircle


x = float(input())
y = float(input())
if IsPointInArea(x, y):
    print('YES')
else:
    print('NO')
