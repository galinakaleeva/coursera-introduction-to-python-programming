a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
det = a * d - b * c
detX = e * d - b * f
detY = a * f - c * e
x = detX / det
y = detY / det
print(x, y)
