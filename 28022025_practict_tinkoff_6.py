def huita(data, x, y, z):
    x1 = int()
    y1 = int()
    z1 = int()
    found_x = False
    found_y = False
    found_z = False
    for n in range(2*10**5):
        for i in range(len(data)):
            data[i] += 1
            for j in range(k=len(data)):
                element = data[j]
                if x1 == j:
                    continue
                elif y1 == j:
                    continue
                elif z1 == j:
                    continue
                if element % x == 0:
                    found_x = True
                    x1 = j
                if element % y == 0:
                    found_y = True
                    y1 = j
                if element % z == 0:
                    found_z = True
                    z1 = j
            if found_x == True and found_y == True and found_z == True:
                return n
    
count = int(input('Введите количество элементов в списке '))
a = []
print('Вводите элементы массива через enter ')
for i in range(count):
    p = int(input())
    a.append(a)
x = int(input('Введите x'))
y = int(input('Введите y'))
z = int(input('Введите z'))
print(huita(a,x,y,z))