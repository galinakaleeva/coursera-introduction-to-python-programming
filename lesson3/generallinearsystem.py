a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if c != 0:
    if b - d * a / c != 0:
        y = (e - f * a / c) / (b - d * a / c)
        x = (f - d * y) / c
        print(2, x, y)
    elif e - f * a / c != 0:
        print(0)
    elif d != 0:
        print(1, -c / d, f / d)
    else:
        print(3, f / c)
elif a != 0:
    if d != 0:
        y = f / d
        x = (e - b * y) / a
        print(2, x, y)
    elif f != 0:
        print(0)
    elif b != 0:
        print(1, -a / b, e / b)
    else:
        print(3, e / a)
else:
    if d != 0:
        if e - f * b / d != 0:
            print(0)
        else:
            print(4, f / d)
    elif f != 0:
        print(0)
    elif b != 0:
        print(4, e / b)
    elif e != 0:
        print(0)
    else:
        print(5)
