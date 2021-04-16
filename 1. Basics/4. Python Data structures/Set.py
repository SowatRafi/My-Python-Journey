def printingMethod(whatever):
    x = 0
    for i in whatever:
        x += 1
        print(x, i)


love = {'Bikes', 'Mobiles', 'Laptops', 'Desktops'}
PC_Brans = set(('HP', 'Lenovo', 'Dell', 'Asus'))

printingMethod(love)
printingMethod(PC_Brans)
print(type(love))
print(type(PC_Brans))