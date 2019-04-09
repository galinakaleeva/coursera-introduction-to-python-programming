price = float(input())
price *= 100
price = round(price)
rubles = price // 100
cents = price % 100
print(rubles, cents)
