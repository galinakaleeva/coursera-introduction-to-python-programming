current = int(input())
prev = current
number = 0
while current != 0:
    if current > prev:
        number += 1
    prev = current
    current = int(input())
print(number)
