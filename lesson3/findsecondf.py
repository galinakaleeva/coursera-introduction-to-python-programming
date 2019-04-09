s1 = input()
num1 = s1.find('f')
if num1 == -1:
    print(-2)
else:
    s2 = s1[num1 + 1:]
    num2 = s2.find('f')
    if num2 == -1:
        print(-1)
    else:
        num2 = num1 + num2 + 1
        print(num2)
