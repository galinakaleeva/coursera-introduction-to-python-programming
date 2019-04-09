def ReduceFraction(n, m):
    if gcd(n, m) == 1:
        return n, m
    return n // gcd(n, m), m // gcd(n, m)


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
m = int(input())
n, m = ReduceFraction(n, m)
print(n, m)
