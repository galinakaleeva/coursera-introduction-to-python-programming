a = int(input())
b = int(input())
c = int(input())
i = 2
minDist = 0
numMax = 0
while c != 0:
    if a < b > c:
        if numMax > 0:
            dist = i - numMax
        numMax = i
        if 0 < dist < minDist:
            minDist = dist
    i += 1
    a = b
    b = c
    c = int(input())
print(minDist)
