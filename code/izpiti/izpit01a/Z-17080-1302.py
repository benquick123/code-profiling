def migracije(ime_datoteke):
    for vrstica in open(ime_datoteke):
        vrstica = vrstica.strip().split()
        koliko = int(vrstica[0][:-1])
        od_kod = vrstica[1]
        kam = vrstica[3]

def zakladi(navodila):
    navodilo = []
    for a in navodila:
        a.append(navodilo)
    x0, y0 = zacetek