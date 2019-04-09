inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
s = set(range(int(inputFile.readline()) + 1)) - {0}
tempLineQuest = inputFile.readline().strip()
while tempLineQuest != 'HELP':
    tempLineAns = inputFile.readline().strip()
    currentSet = set(map(int, tempLineQuest.split()))
    if tempLineAns == 'NO':
        s -= currentSet
    elif tempLineAns == 'YES':
        s &= currentSet
    tempLineQuest = inputFile.readline().strip()
print(*sorted(s), file=outputFile)
inputFile.close()
outputFile.close()
