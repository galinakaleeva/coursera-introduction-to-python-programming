a = int(input())
b = int(input())
c = int(input())
res = 0
if a == b:
    if b == c:
        res = 3
    else:
        res = 2
else:
    if a == c or b == c:
        res = 2
print(res)
