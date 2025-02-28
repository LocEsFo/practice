def result(m, t):
    summa = 0
    g = m
    for i in range(3):
        x = 0
        o = 0
        while x <= m:
            x = t[o]
            o += 1
            if x > m and o < 1:
                return -1
        m -= t[o-2]
        summa +=t[o-2]
    if summa != g and m < 0:
        return -1
    else:
        return summa

two = []
for i in range(72):
    two.append(2**i)

cout = 0

days = int(input('Введите количество дней '))
for i in range(days):
    while cout != -1:
        money = int(input('Введите количество бурлей на день '))
        print(result(money, two))
        cout = result(money,two)