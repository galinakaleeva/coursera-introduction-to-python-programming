def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
a = distance(x2, y2, x3, y3)
b = distance(x1, y1, x3, y3)
c = distance(x1, y1, x2, y2)
p = a + b + c
print(p)
