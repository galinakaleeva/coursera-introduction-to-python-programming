inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
stressDict = {}
n = int(inFile.readline())
for i in range(n):
    line = inFile.readline().strip()
    lowLine = line.lower()
    if lowLine in stressDict:
        stressDict[lowLine].add(line)
    else:
        stressDict[lowLine] = {line}
mistakes = 0
for line in inFile:
    words = line.split()
    for i in range(len(words)):
        if words[i].lower() not in stressDict:
            stresses = 0
            for j in range(len(words[i])):
                if words[i][j].isupper():
                    stresses += 1
            if stresses != 1:
                mistakes += 1
        else:
            if words[i] not in stressDict[words[i].lower()]:
                mistakes += 1
print(mistakes, file=outFile)
inFile.close()
outFile.close()
