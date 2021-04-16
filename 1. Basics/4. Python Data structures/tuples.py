schools = ('Kids Campus', 'Daffodil International School', 'Tangail Cadet School', 'Kodalia Govt. Primary School', 'Birkasra Primary School', "Bindubashini Govt. Boys' High School")

def printingMethod(whatever):
    x = 0
    for i in whatever:
        x += 1
        print(x, i)


printingMethod(schools)
print('\n' + schools[5] + '\n')

college = tuple(("Mahmudul Hasan College", "Govt. Shamsul Haque College"))
printingMethod(college)