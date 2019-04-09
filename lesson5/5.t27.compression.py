a = list(map(int, input().split()))
i = 0
l = len(a)
numZeros = 0
flag = 0
while i < l:
    if a[i] != 0 and flag == 0:
        i += 1
    elif a[i] != 0 and flag != 0:
        a[numZero], a[i] = a[i], a[numZero]
        numZero += 1
        i += 1
    elif a[i] == 0 and flag == 0:
        numZero = i
        flag = 1
        i += 1
    elif a[i] == 0 and flag == 1:
        i += 1
print(*a)
