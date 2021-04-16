def printingMethod(whatever):
    x = 0
    for k, v in whatever.items():
        if x == 0:
            x += 1
            print()

        print(f'{k}: {v}')


myPhone = {
    'Brand': 'OnePlus',
    'Model': '8T',
    'Released Date': 'October 16, 2020',
    'Android version': 'android 11',
    'Display': '6.55"',
    'Memory': '256GB',
    'RAM': '12GB',
    'CPU': "Qualcomm SM8250 Snapdragon 865 5G (7 nm+)",
    'GPU': 'Adreno 650',
    'Selfie Camera': '16 MP, f/2.4, (wide), 1/3.06", 1.0µm',
    'Main-Camera 1': '48 MP, f/1.7, 26mm (wide), 1/2.0", 0.8µm, PDAF, OIS',
    'Main-Camera 2': '16 MP, f/2.2, 14mm, 123˚ (ultrawide), 1/3.6", 1.0µm',
    'Main-Camera 3': '5 MP, f/2.4, (macro)',
    'Main-Camera 4': '2 MP, f/2.4, (depth)',
    'Battery': 'Li-Po 4400 mAh, non-removable',
    'Color': "Aquamarine Green"
}

print(len(myPhone))

print(myPhone['Battery'])
myPhone['Battery'] = 'Li-Po 4500 mAh, non-removable'
print(myPhone['Battery'])

print(myPhone.get('Main-Camera 1'))
myPhone.update({'Color': "Lunar Silver", 'Battery': 4500})
print(myPhone.get('Color'))
print(myPhone.get('Battery'))

key = myPhone.keys()
print(f'\n{key}')
myPhone.popitem()  # Deleting the last index
myPhone.pop('Android version')  # Deleting the selected index
printingMethod(myPhone)

print(f'\n{len(myPhone)}')
myPhone.clear()
print(len(myPhone))

del myPhone