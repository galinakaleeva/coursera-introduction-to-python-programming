n = int(input())
x = float(input())
i = n - 1
a = float(input())
bN = a
if n == 0:
    print(a)
else:
    while i >= 0:
        a = float(input())
        bN1 = a + x * bN
        bN = bN1
        i -= 1
    print(bN1)
