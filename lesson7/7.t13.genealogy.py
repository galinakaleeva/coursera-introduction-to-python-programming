inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
childParent = {}
people = {}
n = int(inFile.readline())
for line in inFile:
    data = line.split()
    childParent[data[0]] = data[1]
    people[data[0]] = 0
    people[data[1]] = 0
for key in people:
    if key not in childParent:
        root = key
for key in people:
    deepness = 0
    current = key
    while current != root:
        current = childParent[current]
        deepness += 1
    people[key] = deepness
for man in sorted(people):
    print(man, people[man], file=outFile)
inFile.close()
outFile.close()
