a = list(map(int, input().split()))
kC = list(map(int, input().split()))
k = kC[0]
C = kC[1]
a.append(0)
i = len(a) - 1
while i > k:
    a[i] = a[i - 1]
    i -= 1
a[k] = C
print(*a)
