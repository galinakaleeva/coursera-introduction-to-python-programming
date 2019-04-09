k = int(input())  # number of meatballs on pan
m = int(input())  # minutes per side
n = int(input())  # total number of meatballs
if n < k:
    print(2 * m)
elif (2 * n * m) % (k * m) == 0:
    print(2 * n * m // k)
else:
    print(2 * m * n // (k * m) * m + m)
