maxLength = 1
lengthIncrease = 1
lengthDecrease = 1
prePrevious = int(input())
previous = int(input())
if prePrevious < previous:
    lengthIncrease += 1
elif prePrevious > previous:
    lengthDecrease += 1
if lengthDecrease > lengthIncrease and lengthDecrease > maxLength:
    maxLength = lengthDecrease
if lengthIncrease > lengthDecrease and lengthIncrease > maxLength:
    maxLength = lengthIncrease
current = int(input())
while current != 0:
    if prePrevious < previous < current:
        lengthIncrease += 1
        if lengthIncrease > maxLength:
            maxLength = lengthIncrease
    if prePrevious > previous > current:
        lengthDecrease += 1
        if lengthDecrease > maxLength:
            maxLength = lengthDecrease
    if prePrevious < previous > current:
        lengthDecrease = 2
        if lengthDecrease > maxLength:
            maxLength = lengthDecrease
    if prePrevious > previous < current:
        lengthIncrease = 2
        if lengthIncrease > maxLength:
            maxLength = lengthIncrease
    prePrevious = previous
    previous = current
    current = int(input())
print(maxLength)
