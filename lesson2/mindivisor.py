n = int(input())
i = n - 1
divisor = n
while i > 1:
    if n % i == 0:
        divisor = i
    i -= 1
print(divisor)
