a = list(map(int, input().split()))
n = len(a)
for i in range(n // 2):
    a[i], a[n - 1 - i] = a[n - 1 - i], a[i]
print(*a)
