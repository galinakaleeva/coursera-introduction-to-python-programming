a = list(map(int, input().split()))
b = a.copy()
c = []
n = len(a)
for i in range(n):
    c.append(b.pop())
print(*c)
