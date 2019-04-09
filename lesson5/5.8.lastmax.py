line = list(map(int, input().split()))
candMax = line[len(line) - 1]
candNum = len(line) - 1
for i in range(len(line) - 1, -1, -1):
    if line[i] > candMax:
        candMax = line[i]
        candNum = i
print(' '.join(map(str, [candMax, candNum])))
