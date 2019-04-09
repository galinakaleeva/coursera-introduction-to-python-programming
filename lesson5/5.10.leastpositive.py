series = list(map(int, input().split()))
least = 1000
for i in range(len(series)):
    if 0 < series[i] < least:
        least = series[i]
print(least)
