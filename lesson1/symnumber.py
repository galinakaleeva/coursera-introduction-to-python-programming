n = int(input())
a = n // 1000
b = n // 100 % 10
c = n % 100 // 10
d = n % 10
print(1 + (a - d) ** 2 + (b - c) ** 2)
