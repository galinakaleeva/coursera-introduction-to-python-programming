a = list(map(int, input().split()))
n = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        n += 1
print(n)
