s = input()
leftN = s.find('h')
rightN = s.rfind('h')
sub = s[leftN + 1:rightN]
print(s[:leftN + 1] + sub * 2 + s[rightN:])
