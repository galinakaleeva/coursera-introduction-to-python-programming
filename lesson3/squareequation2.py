from math import sqrt

a = float(input())
b = float(input())
c = float(input())
epsilon = 5 * 10**-9
if a != 0:
    D = b**2 - 4 * a * c
    if abs(D) < epsilon:
        print(1, -b / (2 * a))
    elif D > epsilon:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        if x1 < x2:
            print(2, x1, x2)
        else:
            print(2, x2, x1)
    else:
        print(0)
elif b != 0:
    x = -c / b
    print(1, x)
elif c != 0:
    print(0)
else:
    print(3)
