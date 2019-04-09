a = int(input())
b = int(input())
r = a % b
print('YES' * (1 - r), 'NO' * (1 - int(10**(-r) // 1)), sep='')
