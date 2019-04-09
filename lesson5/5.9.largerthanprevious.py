series = list(map(int, input().split()))
for i in range(1, len(series)):
    if series[i] > series[i-1]:
        print(series[i], end=' ')
print()
