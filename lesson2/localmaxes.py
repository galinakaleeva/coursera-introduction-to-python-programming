a = int(input())
b = int(input())
c = int(input())
i = 2
minDist = 0
numMax = 0
dist = 0
while c != 0:
    if a < b > c:
        if numMax > 0:
            dist = i - numMax
        numMax = i
        if minDist == 0 and dist > 0:
            minDist = dist
        if 0 < dist < minDist:
            minDist = dist
    i += 1
    a = b
    b = c
    c = int(input())
print(minDist)
