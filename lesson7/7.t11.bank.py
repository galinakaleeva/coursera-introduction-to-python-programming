inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
accounts = {}
for data in inFile:
    l = data.split()
    if l[0] == 'TRANSFER':
        accounts[l[1]] = accounts.get(l[1], 0) - int(l[3])
        accounts[l[2]] = accounts.get(l[2], 0) + int(l[3])
    elif l[0] == 'BALANCE':
        if l[1] in accounts:
            print(accounts[l[1]], file=outFile)
        else:
            print('ERROR', file=outFile)
    elif l[0] == 'INCOME':
        for acc in accounts:
            if accounts[acc] > 0:
                accounts[acc] += int(accounts[acc] * int(l[1]) / 100)
    elif l[0] == 'DEPOSIT':
        accounts[l[1]] = accounts.get(l[1], 0) + int(l[2])
    elif l[0] == 'WITHDRAW':
        accounts[l[1]] = accounts.get(l[1], 0) - int(l[2])
inFile.close()
outFile.close()
