n = int(input())
series = list(map(int, input().split()))
theNumber = int(input())
distance = abs(theNumber - series[0])
candidate = series[0]
for i in range(n):
    if abs(theNumber - series[i]) < distance:
        distance = abs(theNumber - series[i])
        candidate = series[i]
print(candidate)
