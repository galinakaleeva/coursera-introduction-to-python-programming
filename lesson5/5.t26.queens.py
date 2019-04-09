a = list(map(int, input().split()))
for i in range(7):
    b = list(map(int, input().split()))
    a.append(b[0])
    a.append(b[1])
flag = 0
for i in range(8):
    for j in range(i + 1, 8):
        sameRow = a[2 * i] == a[2 * j]
        sameCol = a[2 * i + 1] == a[2 * j + 1]
        sameDiag = abs(a[2 * i] - a[2 * j]) == abs(a[2 * i + 1] - a[2 * j + 1])
        if sameRow or sameCol or sameDiag:
            flag = 1
if flag == 1:
    print('YES')
else:
    print('NO')
