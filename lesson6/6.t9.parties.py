inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
tmpLine = inputFile.readline()
parties = [inputFile.readline().strip()]
tmpLine = inputFile.readline().strip()
n = 1  # number of parties
while tmpLine != 'VOTES:':
    parties.append(tmpLine)
    n += 1
    tmpLine = inputFile.readline().strip()
votes = [0] * n
voters = 0
for line in inputFile:
    voters += 1
    for i in range(n):
        if line.strip() == parties[i]:
            votes[i] += 1
for i in range(n):
    if votes[i] / voters >= 0.07:
        print(parties[i], file=outputFile)
inputFile.close()
outputFile.close()
