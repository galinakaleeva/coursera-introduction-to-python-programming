a = int(input())
b = int(input())
c = int(input())
d = int(input())
if c == 0:
    if a == b == 0:
        print('INF')
    elif a == 0 and b != 0:
        print('NO')
    else:
        if -b / a == -b // a:
            print(-b // a)
        else:
            print('NO')
else:
    if a == b == 0:
        print('INF')
    elif a == 0 and b != 0:
        print('NO')
    else:
        if b / a != d / c and -b / a == -b // a:
            print(-b // a)
        else:
            print('NO')
