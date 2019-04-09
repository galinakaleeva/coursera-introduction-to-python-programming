a = int(input())
b = int(input())
for i in range(a, b + 1):
    d = str(i)
    if d[0] == d[3] and d[1] == d[2]:
        print(i)
