import random

def cash(d):
    mass = []
    for i in range(d):
        mass.append(random.randint(1, 1000))
    return mass

def result(m, t):
    mmm = []
    for i in range(len(m)):
        u = m[i]
        summa = 0
        for j in range(3):
            x = 0
            k = 0
            while x < u:
                x = t[k]
                k += 1
            summa += t[k - 2]
            u -= t[k - 2]
        if u < 1 and summa != m[i]:
            mmm.append(-1)
            break
        else: mmm.append(summa)
    return mmm    

two = []

for i in range(72):
    two.append(2**i)
    
days = random.randint(1, 10)
money = cash(days)
l = result(money, two)
for i in range(len(money)):
    print(money[i], l[i])