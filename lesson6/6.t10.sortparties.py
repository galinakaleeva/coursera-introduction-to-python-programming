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
parties.sort(reverse=True)
votes = []
for i in range(n):
    votes.append([0, i])
voters = 0
for line in inputFile:
    voters += 1
    for i in range(n):
        if line.strip() == parties[i]:
            votes[i][0] += 1
votes.sort(reverse=True)
for i in range(n):
    print(parties[votes[i][1]], file=outputFile)
inputFile.close()
outputFile.close()
