a = list(map(int, input().split()))
maxFreq = 0
for i in range(len(a)):
    curNum = a[i]
    curFreq = 0
    for j in range(len(a)):
        if a[j] == curNum:
            curFreq += 1
    if curFreq > maxFreq:
        maxFreq = curFreq
        mostFrequentNumber = a[i]
print(mostFrequentNumber)
