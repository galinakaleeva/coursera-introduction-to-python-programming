k = int(input())
n = 1
number = 0
while n <= k:
    i = n
    inv = 0
    while i != 0:
        inv = inv * 10 + i % 10
        i = i // 10
    if n == inv:
        number += 1
    n += 1
print(number)
