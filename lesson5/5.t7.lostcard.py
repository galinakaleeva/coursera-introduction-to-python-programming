n = int(input())
correctSum = n * (n + 1) // 2
wrongSum = 0
for i in range(n - 1):
    wrongSum += int(input())
lost = correctSum - wrongSum
print(lost)
