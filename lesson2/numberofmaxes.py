current = int(input())
maxNumber = current
number = 0
while current != 0:
    if current == maxNumber:
        number += 1
    elif current > maxNumber:
        number = 1
        maxNumber = current
    current = int(input())
print(number)
