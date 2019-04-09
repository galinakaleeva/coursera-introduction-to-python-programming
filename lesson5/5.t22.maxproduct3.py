a = list(map(int, input().split()))
b = a[:3]
for j in range(3):
    for k in range(j, 3):
        if b[j] > b[k]:
            b[j], b[k] = b[k], b[j]
firstMax = b[2]
secMax = b[1]
thirdMax = b[0]
firstMin = b[0]
secMin = b[1]
thirdMin = b[2]
i = 3
l = len(a)
while i < l:
    if a[i] >= firstMax:
        firstMax, secMax, thirdMax = a[i], firstMax, secMax
    elif firstMax > a[i] >= secMax:
        secMax, thirdMax = a[i], secMax
    elif secMax > a[i] >= thirdMax:
        thirdMax = a[i]
    if a[i] <= firstMin:
        firstMin, secMin, thirdMin = a[i], firstMin, secMin
    elif firstMin < a[i] <= secMin:
        secMin, thirdMin = a[i], secMin
    elif secMin < a[i] <= thirdMin:
        thirdMin = a[i]
    i += 1
if firstMax <= 0:
    print(firstMax, secMax, thirdMax)
elif secMax * thirdMax > firstMin * secMin:
    print(firstMax, secMax, thirdMax)
else:
    print(firstMax, firstMin, secMin)
