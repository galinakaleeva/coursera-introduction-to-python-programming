maxLength = 1
lengthIncrease = 1
lengthDecrease = 1
previous = int(input())
if previous == 0:
    current = 0
else:
    current = int(input())
flagIncrease = 0
flagDecrease = 0
if previous < current:
    lengthIncrease += 1
    flagIncrease = 1
elif previous > current:
    lengthDecrease += 1
    flagDecrease = 1
if lengthDecrease > lengthIncrease:
    if lengthDecrease > maxLength:
        maxLength = lengthDecrease
else:
    if lengthIncrease > maxLength:
        maxLength = lengthIncrease
previous = current
if current != 0:
    current = int(input())
while current != 0:
    if previous == current:
        flagDecrease, flagIncrease = 0, 0
    elif previous < current and flagIncrease == 1:
        lengthIncrease += 1
    elif previous > current and flagDecrease == 1:
        lengthDecrease += 1
    elif previous > current and flagIncrease == 1:
        flagIncrease, flagDecrease = 0, 1
        lengthDecrease = 2
    elif previous < current and flagDecrease == 1:
        lengthIncrease = 2
        flagIncrease, flagDecrease = 1, 0
    if lengthIncrease > lengthDecrease:
        if lengthIncrease > maxLength:
            maxLength = lengthIncrease
    else:
        if lengthDecrease > maxLength:
            maxLength = lengthDecrease
    previous = current
    current = int(input())
print(maxLength)
