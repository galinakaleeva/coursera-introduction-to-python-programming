n = int(input())
numberOfZeros = 0
for i in range(n):
    if int(input()) == 0:
        numberOfZeros += 1
print(numberOfZeros)
