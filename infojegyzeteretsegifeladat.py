f = open('pilotak.csv', 'r', encoding='UTF-8')
l = [sor.strip().split(';') for sor in f]
f.close()
l.remove(l[0])


    


#3.feladat:
print(f'3.feladat: {len(l)}')

#4.feladat:
print(f'4.feladat: {l[-1][0]}')

#5.feladat:
datum = '1901.01.01'
datumok = [sor for sor in l if sor[1] <= datum]
print(f'5. feladat:')
for sor in datumok:
    print(f'        {sor[0]} - ({sor[1]})')

#6.feladat:
rajtszam = [int(sor[-1]) for sor in l if sor[-1] != '']
legkisebb = min(rajtszam)
nemzetiseg = [sor[-2] for sor in l if sor[-1] == str(legkisebb)]
print(f'6.feladat: {nemzetiseg[0]}')

#7.feladat:
stat = dict()
for sor in rajtszam:
    rajtszam = str(sor[-1])
    stat[rajtszam] = stat.get(rajtszam, 0) + 1
    
szamok = []
for sor in stat.items():
        if sor[1] > 1:
            szamok.append(sor)
