first = float(input())
total = float(input())
current = first
day = 1
while current < total:
    day += 1
    current *= 1.1
print(day)
