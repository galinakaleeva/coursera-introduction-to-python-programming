inputFile = open('input.txt', 'r', encoding='utf8')
maxMark9, maxMark10, maxMark11 = 0, 0, 0
for line in inputFile:
    curMark = int(line.split()[3])
    form = line.split()[2]
    if form == '9' and curMark > maxMark9:
        maxMark9 = curMark
    if form == '10' and curMark > maxMark10:
        maxMark10 = curMark
    if form == '11' and curMark > maxMark11:
        maxMark11 = curMark
print(maxMark9, maxMark10, maxMark11)
