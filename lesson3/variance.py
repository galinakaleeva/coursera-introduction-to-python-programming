from math import sqrt

sumSq = 0
sumX = 0
x = int(input())
n = 0
while x != 0:
    n += 1
    sumX += x
    sumSq += (x**2)
    x = int(input())
s = sumX / n
variance = sqrt((sumSq + n * s**2 - 2 * s * sumX) / (n - 1))
print(variance)
