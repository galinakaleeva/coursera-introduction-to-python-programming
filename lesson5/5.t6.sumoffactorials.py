n = int(input())
Sum = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    Sum += factorial
print(Sum)
