s = input()
leftN = s.find('h')
rightN = s.rfind('h')
sub = s[leftN + 1:rightN]
if sub.find('h') != -1:
    subNew = sub.replace('h', 'H')
    print(s[:leftN + 1] + subNew + s[rightN:])
else:
    print(s)
