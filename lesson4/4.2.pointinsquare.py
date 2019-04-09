def isPointInSquare(x, y):
    x1 = (min(x, -1) == -1)
    y1 = (min(y, -1) == -1)
    x2 = (max(x, 1) == 1)
    y2 = (max(y, 1) == 1)
    return x1 and x2 and y1 and y2


x = float(input())
y = float(input())
if isPointInSquare(x, y):
    print('YES')
else:
    print('NO')
