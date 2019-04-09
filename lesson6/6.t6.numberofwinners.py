inputFile = open('input.txt', 'r', encoding='utf8')
maxMark9, maxMark10, maxMark11 = -1, -1, -1
numWin9, numWin10, numWin11 = 1, 1, 1
for line in inputFile:
    curMark = int(line.split()[3])
    form = line.split()[2]
    if form == '9':
        if curMark > maxMark9:
            maxMark9 = curMark
            numWin9 = 1
        elif curMark == maxMark9:
            numWin9 += 1
    if form == '10':
        if curMark > maxMark10:
            maxMark10 = curMark
            numWin10 = 1
        elif curMark == maxMark10:
            numWin10 += 1
    if form == '11':
        if curMark > maxMark11:
            maxMark11 = curMark
            numWin11 = 1
        elif curMark == maxMark11:
            numWin11 += 1
print(numWin9, numWin10, numWin11)
