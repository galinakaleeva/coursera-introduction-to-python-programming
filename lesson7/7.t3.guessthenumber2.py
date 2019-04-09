inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
s = set(range(int(inputFile.readline()) + 1)) - {0}
tempLineQuest = inputFile.readline().strip()
answers = []
while tempLineQuest != 'HELP':
    currentSet = set(map(int, tempLineQuest.split()))
    if len(currentSet & s) <= len(s) // 2:
        answers.append('NO')
        s -= currentSet
    else:
        answers.append('YES')
        s &= currentSet
    tempLineQuest = inputFile.readline().strip()
for answer in answers:
    print(answer, file=outputFile)
print(*sorted(s), file=outputFile)
inputFile.close()
outputFile.close()
