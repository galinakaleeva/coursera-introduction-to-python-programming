prev = int(input())  # current
cur = int(input())  # previous
maxLen = 1
lenInc = 1
lenDec = 1
flag = 0
while cur != 0:
    if cur > prev:
        if flag < 0:
            lenDec += 1
        else:
            lenDec = 2
            flag = -1
    elif cur < prev:
        if flag > 0:
            lenInc += 1
        else:
            lenInc = 2
            flag = 1
    else:
        flag = 0
    if max(lenInc, lenDec) > maxLen:
        maxLen = max(lenInc, lenDec)
    prev = cur
    cur = int(input())
print(maxLen)
