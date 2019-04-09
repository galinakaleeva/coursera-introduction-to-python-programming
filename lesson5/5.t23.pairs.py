a = list(map(int, input().split()))
n = 0
l = len(a)
for i in range(l):
    for j in range(i + 1, l):
        if a[i] == a[j]:
            n += 1
print(n)
