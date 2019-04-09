from math import sqrt

a = float(input())
b = float(input())
c = float(input())
epsilon = 5 * 10**-9
D = b**2 - 4 * a * c
if abs(D) < epsilon:
    print(-b / (2 * a))
elif D > epsilon:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
