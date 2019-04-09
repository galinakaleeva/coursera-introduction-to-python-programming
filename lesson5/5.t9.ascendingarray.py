def IsAscending(a):
    i = 1
    NumOfAsc = 0
    n = len(a)
    while i < n:
        NumOfAsc += int(a[i] > a[i - 1])
        i += 1
    return NumOfAsc == n - 1


array = list(map(int, input().split()))
if IsAscending(array):
    print('YES')
else:
    print('NO')
