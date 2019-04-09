a = list(map(int, input().split()))
candMax = a[0]
candNum = 0
for i in range(len(a)):
    if a[i] > candMax:
        candMax = a[i]
        candNum = i
print(' '.join(map(str, [candMax, candNum])))
