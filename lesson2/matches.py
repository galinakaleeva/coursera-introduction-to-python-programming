l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
onetwo = (l1 <= l2 <= r1 or l2 <= l1 <= r2)  # first crosses second
onethree = (l1 <= l3 <= r1 or l3 <= l1 <= r3)
twothree = (l3 <= l2 <= r3 or l2 <= l3 <= r2)
if (onetwo and onethree) or (onetwo and twothree) or (onethree and twothree):
    print(0)
elif twothree:
    print(1)
elif r1 - l1 >= l2 - r3 > 0 or r1 - l1 >= l3 - r2 > 0:
    print(1)
elif onethree:
    print(2)
elif r2 - l2 >= l1 - r3 > 0 or r2 - l2 >= l3 - r1 > 0:
    print(2)
elif onetwo:
    print(3)
elif r3 - l3 >= l1 - r2 > 0 or r3 - l3 >= l2 - r1 > 0:
    print(3)
else:
    print(-1)
