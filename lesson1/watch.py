n = int(input())
hours = (n // (60 * 60)) % 24
minutes = n // 60 % 60
seconds = n % 60
print(str(hours), ':', str(minutes // 10), str(minutes % 10), sep='', end='')
print(':', str(seconds // 10), str(seconds % 10), sep='')
