from math import ceil


def IsPrime(n):
    i = 2
    while i <= n ** (1 / 2):
        if n % i == 0:
            return False
        i += 1
    return True


def Lagrange(n):
    if IsPrime(n):
        i = 0
        while i <= ceil(n**(1/2)):
            j = 0
            while j <= ceil(n**(1/2)):
                k = 0
                while k <= ceil(n**(1/2)):
                    m = 0
                    while m <= ceil(n**(1/2)):
                        if i**2 + j**2 + k**2 + m**2 == n:
                            return i, j, k, m
                        m += 1
                    k += 1
                j += 1
            i += 1
    div1 = int(n**(1/2))
    while div1 > 1:
        if n % div1 == 0:
            div2 = n // div1
            break
        div1 -= 1
    n1, n2, n3, n4 = Lagrange(div1)
    m1, m2, m3, m4 = Lagrange(div2)
    nm1 = abs(n1 * m1 + n2 * m2 + n3 * m3 + n4 * m4)
    nm2 = abs(-n1 * m2 + n2 * m1 - n3 * m4 + n4 * m3)
    nm3 = abs(-n1 * m3 + n3 * m1 - n4 * m2 + n2 * m4)
    nm4 = abs(-n1 * m4 + n4 * m1 - n2 * m3 + n3 * m2)
    return nm1, nm2, nm3, nm4


n = int(input())
a, b, c, d = Lagrange(n)
if a != 0:
    print(a, end=' ')
if b != 0:
    print(b, end=' ')
if c != 0:
    print(c, end=' ')
if d != 0:
    print(d)
