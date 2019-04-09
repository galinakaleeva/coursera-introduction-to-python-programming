n = int(input())
prevPrev = 0
prev = 1
if n == 0:
    print(prevPrev)
if n == 1:
    print(prev)
if n > 1:
    i = 2
    while i <= n:
        prev, prevPrev = prev + prevPrev, prev
        i += 1
    print(prev)
