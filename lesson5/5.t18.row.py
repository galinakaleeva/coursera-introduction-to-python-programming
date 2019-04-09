a = list(map(int, input().split()))
p = int(input())
i = 0
l = len(a)
while i < l and a[i] >= p:
    i += 1
print(i + 1)
