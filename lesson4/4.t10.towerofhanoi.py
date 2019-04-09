def move(n, x, y):
    if n == 1:
        print(1, x, y)
    elif n > 1:
        move(n - 1, x, 6 - x - y)
        print(n, x, y)
        move(n - 1, 6 - x - y, y)


move(int(input()), 1, 3)
