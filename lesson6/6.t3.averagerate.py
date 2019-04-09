inputFile = open('input.txt', 'r', encoding='utf8')
sum9, sum10, sum11 = 0, 0, 0
n9, n10, n11 = 0, 0, 0
for line in inputFile:
    form = line.split()[2]
    mark = int(line.split()[3])
    if form == '9':
        sum9 += mark
        n9 += 1
    elif form == '10':
        sum10 += mark
        n10 += 1
    elif form == '11':
        sum11 += mark
        n11 += 1
print(sum9 / n9, sum10 / n10, sum11 / n11)
