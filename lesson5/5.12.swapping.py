a = list(map(int, input().split()))
b = []
for i in range(len(a) // 2):
    b.append(a[2 * i + 1])
    b.append(a[2 * i])
if len(a) % 2 == 1:
    b.append(a.pop())
print(*b)
