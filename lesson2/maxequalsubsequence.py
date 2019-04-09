maxLength = 1
length = 1
current = int(input())
prev = 0
while current != 0:
    if current == prev:
        length += 1
        if length > maxLength:
            maxLength = length
    else:
        length = 1
    prev = current
    current = int(input())
print(maxLength)
