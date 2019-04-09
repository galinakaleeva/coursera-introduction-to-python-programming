p = int(input())
x = int(input())
y = int(input())
dep = (100 * x + y) + (100 * x + y) * p / 100
dep = int(dep)
print(dep // 100, dep % 100)
