def printingMethod(whatever):
    x = 0
    for i in whatever:
        x += 1
        print(f'{x}: {i}')


laptop_Brans = {'HP', 'Lenovo', 'Dell', 'Asus'}

laptop_Brans.add('Apple')  # Adding single item
laptop_Brans.update(['Acer', 'Samsung', 'MSI', 'Razer'])  # Adding multiple items
laptop_Brans.remove('Samsung')  # Removing a item
laptop_Brans.clear()  # Clear everything

printingMethod(laptop_Brans)

bikes = {"Yamaha MT15", 'Yamaha XSR155', "Honda CBR"}

printingMethod(bikes)

del bikes  # Deleted
print(bikes)  # Will give a error

