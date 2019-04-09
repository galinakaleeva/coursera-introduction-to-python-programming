line = list(map(int, input().split()))
n = 0
for i in range(len(line)):
    if line[i] > 0:
        n += 1
print(n)
