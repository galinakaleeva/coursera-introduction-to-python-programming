x = 1
while x < 500:
    if cubes(x) == 0:
        print('NOdecomposition', x)
    else:
        j1, j2, j3, j4, j5, j6, j7 = cubes(x)
        if x != j1**3 + j2**3 + j3**3 + j4**3 + j5**3 + j6**3 + j7**3:
            print('NOequality', x)
    x += 1

if n < 0:
    m = -n
    if cubes(m) == 0:
        print(0)
    else:
        i1, i2, i3, i4, i5, i6, i7 = cubes(m)
        i1, i2, i3, i4, i5, i6, i7 = -i1, -i2, -i3, -i4, -i5, -i6, -i7
        s = ''
        if i1 != 0:
            s += str(i1) + ' '
        if i2 != 0:
            s += str(i2) + ' '
        if i3 != 0:
            s += str(i3) + ' '
        if i4 != 0:
            s += str(i4) + ' '
        if i5 != 0:
            s += str(i5) + ' '
        if i6 != 0:
            s += str(i6) + ' '
        if i7 != 0:
            s += str(i7)
        print(s)
elif n == 0:
    print(0)
el


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
