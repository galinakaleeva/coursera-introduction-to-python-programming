a = list(map(int, input().split()))
if a[0] >= a[1]:
    firstMax = a[0]
    secMax = a[1]
    firstMin = a[1]
    secMin = a[0]
else:
    firstMax = a[1]
    secMax = a[0]
    firstMin = a[0]
    secMin = a[1]
i = 2
l = len(a)
while i < l:
    if a[i] >= firstMax:
        secMax, firstMax = firstMax, a[i]
    elif firstMax > a[i] >= secMax:
        secMax = a[i]
    if a[i] <= firstMin:
        firstMin, secMin = a[i], firstMin
    elif firstMin < a[i] <= secMin:
        secMin = a[i]
    i += 1
if firstMax * secMax > firstMin * secMin:
    print(secMax, firstMax)
else:
    print(firstMin, secMin)
