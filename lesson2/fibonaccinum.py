f = int(input())
prevPrev = 0
prev = 1
if f == 0:
    print(0)
if f == 1:
    print('1 or 2')
if f > 1:
    i = 2
    while prev < f:
        prev, prevPrev = prev + prevPrev, prev
        i += 1
if prev == f:
    print(i - 1)
else:
    print(-1)
