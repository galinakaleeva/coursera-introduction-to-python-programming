current = int(input())
max = current
current = int(input())
secondMax = current
if secondMax > max:
    secondMax, max = max, secondMax
current = int(input())
while current != 0:
    if current >= max:
        secondMax, max = max, current
    elif max > current > secondMax:
        secondMax = current
    current = int(input())
print(secondMax)
