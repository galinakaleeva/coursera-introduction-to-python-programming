a = int(input())
b = int(input())
max = 2**(a - b) // 1 * a * 2**(b - a) + 2**(b - a) // 1 * b * 2**(a - b)
tail = 2**(a - b) // 1 * (2**(b-a) // 1) * a
max = int(max - tail)
print(max)
