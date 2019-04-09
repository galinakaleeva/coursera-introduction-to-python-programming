# 4.t12.cubes old
from math import ceil


def cubes(n):
    i1 = ceil(n**(1/3))
    while i1 >= 0:
        j1 = i1**3
        i2 = ceil(max(0, (n - j1))**(1/3))
        while i2 >= 0:
            j2 = j1 + i2**3
            i3 = ceil(max(0, (n - j2))**(1/3))
            while i3 >= 0:
                j3 = j2 + i3**3
                i4 = ceil(max(0, (n - j3))**(1/3))
                while i4 >= 0:
                    j4 = j3 + i4**3
                    i5 = ceil(max(0, (n - j4))**(1/3))
                    while i5 >= 0:
                        j5 = j4 + i5**3
                        i6 = ceil(max(0, (n - j5))**(1/3))
                        while i6 >= 0:
                            j6 = j5 + i6**3
                            i7 = ceil(max(0, (n - j6))**(1/3))
                            while i7 >= 0:
                                j7 = j6 + i7**3
                                if j7 == n:
                                    return i1, i2, i3, i4, i5, i6, i7
                                i7 -= 1
                            i6 -= 1
                        i5 -= 1
                    i4 -= 1
                i3 -= 1
            i2 -= 1
        i1 -= 1
    return 0


n = int(input())
if cubes(n) == 0:
    print(0)
else:
    i1, i2, i3, i4, i5, i6, i7 = cubes(n)
    if i1 != 0:
        print(i1, end=' ')
    if i2 != 0:
        print(i2, end=' ')
    if i3 != 0:
        print(i3, end=' ')
    if i4 != 0:
        print(i4, end=' ')
    if i5 != 0:
        print(i5, end=' ')
    if i6 != 0:
        print(i6, end=' ')
    if i7 != 0:
        print(i7)
x = 1
while x < 1000:
    if cubes(x) == 0:
        print('NOdecomposition', x)
    else:
        j1, j2, j3, j4, j5, j6, j7 = cubes(x)
        if x != j1**3 + j2**3 + j3**3 + j4**3 + j5**3 + j6**3 + j7**3:
            print('NOequality', x)
    x += 1
