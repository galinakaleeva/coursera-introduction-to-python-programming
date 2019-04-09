a = list(map(int, input().split()))
currentSet = set()
for i in range(len(a)):
    if a[i] in currentSet:
        print('YES')
    else:
        print('NO')
    currentSet.add(a[i])
