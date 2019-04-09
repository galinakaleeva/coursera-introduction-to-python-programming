number = int(input())
maxNumber = number
while number != 0:
    if number > maxNumber:
        maxNumber = number
    number = int(input())
print(maxNumber)
