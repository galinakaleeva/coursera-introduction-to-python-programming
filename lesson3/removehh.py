s1 = input()
num1 = s1.find('h')
s2 = s1[num1 + 1:]
len2 = len(s2)
s2 = s2[::-1]
num2 = s2.find('h')
num2 = num1 + len2 - num2
print(s1[:num1] + s1[num2 + 1:])
