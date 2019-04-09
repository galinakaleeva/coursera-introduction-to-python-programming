x = int(input())
y = int(input())
if x <= y and (x - 1) % (y - x + 1) == 0:
    print('YES')
else:
    print('NO')
