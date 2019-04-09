inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
consumers = {}
for l in inFile:
    name, item, number = l.split()[0], l.split()[1], int(l.split()[2])
    if name not in consumers:
        consumers[name] = {}
        consumers[name][item] = consumers[name].get(item, 0) + number
    else:
        consumers[name][item] = consumers[name].get(item, 0) + number
for name in sorted(consumers):
    print(name, ':', sep='', file=outFile)
    for item in sorted(consumers[name]):
        print(item, consumers[name][item], file=outFile)
inFile.close()
outFile.close()
