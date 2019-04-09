p = int(input())
x = int(input())
y = int(input())
k = int(input())
while k > 0:
    dep = (100 * x + y) + (100 * x + y) * p / 100
    dep = int(dep)
    x = dep // 100
    y = dep % 100
    k -= 1
print(x, y)
