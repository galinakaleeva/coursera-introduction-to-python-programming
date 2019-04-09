s1 = input()
num1 = s1.find('f')
if num1 != -1:
    print(num1)
    s2 = s1[num1 + 1:]
    len2 = len(s2)
    if s2.find('f') != -1:
        s2 = s2[::-1]
        num2 = s2.find('f')
        print(num1 + len2 - num2)
