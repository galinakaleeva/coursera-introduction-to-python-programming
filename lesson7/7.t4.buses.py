a = list(map(int, input().split()))
if a[0] < a[1]:
    bus1 = set(range(a[0], a[1] + 1))
else:
    bus1 = set(range(a[1], a[0] + 1))
if a[2] < a[3]:
    bus2 = set(range(a[2], a[3] + 1))
else:
    bus2 = set(range(a[3], a[2] + 1))
print(len(bus1 & bus2))
