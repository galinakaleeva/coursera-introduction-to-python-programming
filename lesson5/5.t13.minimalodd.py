a = list(map(int, input().split()))
n = len(a)
for i in range(n):
    if a[i] % 2 == 1:
        MinOdd = a[i]
        break
for j in range(i + 1, n):
    if a[j] % 2 == 1 and a[j] < MinOdd:
        MinOdd = a[j]
print(MinOdd)
