current = int(input())
number = 0
while current != 0:
    if current % 2 == 0:
        number += 1
    current = int(input())
print(number)
