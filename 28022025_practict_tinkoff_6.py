def huita(data, x, y, z):
    x1 = int()
    y1 = int()
    z1 = int()
    found_x = False
    found_y = False
    found_z = False
    deystviy = {}
    for j in range(data):
        element = data[j]
        if element % x == 0:
            found_x = True
            x1 = j
        if element % y == 0:
            found_y = True
            y1 = j
        if element % z == 0:
            found_z = True
            z1 = j
    for i in range(len(data)):
        
    
count, x, y, z = map(int, input().split)
a = (int, input().split)
print(huita(a,x,y,z))