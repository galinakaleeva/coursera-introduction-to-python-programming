inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
dist = list(map(int, inputFile.readline().split()))
price = list(map(int, inputFile.readline().split()))
dist.sort()
price.sort(reverse=True)
money = 0
for i in range(len(dist)):
    money += dist[i] * price[i]
print(money, file=outputFile)
inputFile.close()
outputFile.close()
