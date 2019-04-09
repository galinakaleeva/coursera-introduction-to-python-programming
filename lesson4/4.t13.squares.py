def squares():
    global flag
    n = int(input())
    if n != 0:
        squares()
        if n**(1/2) % 1 == 0:
            print(n, end=' ')
            flag += 1


flag = 0
squares()
if flag == 0:
    print(flag)
