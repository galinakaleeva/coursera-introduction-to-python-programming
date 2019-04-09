n = int(input())
i = 1
while i <= n:
    if i < n < 2 * i:
        print('NO')
        i = n + 1
    elif i == n:
        print('YES')
        i = n + 1
    else:
        i *= 2
