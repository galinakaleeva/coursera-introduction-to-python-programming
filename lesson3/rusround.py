import math

x = float(input())
if x - math.floor(x) < 0.5:
    print(math.floor(x))
else:
    print(math.floor(x) + 1)
