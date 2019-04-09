a = list(map(int, input().split()))
k = int(input())
for i in range(k, len(a) - 1):
    a[i] = a[i + 1]
a.pop()
print(*a)
