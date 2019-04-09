n = int(input())
sum = 1
i = 2
while i <= n:
    sum += (1 / i**2)
    i += 1
print(sum)
