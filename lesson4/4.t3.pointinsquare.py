def IsPointInSquare(x, y):
    c1 = y <= x + 1
    c2 = y >= x - 1
    c3 = y <= -x + 1
    c4 = y >= -x - 1
    return c1 and c2 and c3 and c4


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
