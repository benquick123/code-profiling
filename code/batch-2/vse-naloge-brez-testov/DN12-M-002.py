def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    slovar = {}
    i = 1
    for vrstica in datoteka:
        vrstica = vrstica.strip()
        vrstica = vrstica.split()
        vrstica = [int(y) for y in vrstica]
        for y in vrstica:
            if y == min(vrstica):
                break
            else:
                vrstica = vrstica[1:] +[vrstica[0]]
        slovar[i] = vrstica
        i += 1
    return slovar

def mozna_pot(pot, zemljevid):
    moznaPot = True
    seznam = []
    for x, y in zemljevid.items():
        if len(y) < 2:
            seznam.append(x)
    if pot[0] not in seznam or pot[-1] not in seznam:
        moznaPot = False
    if len(pot) > 2 and pot[0] in zemljevid[pot[1]]:
        for y in pot[1:]:
            if y == pot[-1]:
                break
            if y == pot[pot.index(y)+1] or y in seznam or y not in zemljevid[pot[pot.index(y)+1]]:
                moznaPot = False
                break
    else:
        for y in pot:
            if y == pot[-1]:
                break
            if y == pot[pot.index(y)+1] or y in seznam or y not in zemljevid[pot[pot.index(y)+1]]:
                moznaPot = False
                break
    return moznaPot

def hamiltonova(pot, zemljevid):
    hamilton = False
    seznam = []
    for x, y in zemljevid.items():
        if len(y) < 2:
            seznam.append(x)
    if mozna_pot(pot, zemljevid):
        hamilton = True
    if len(pot) + (len(seznam) - 2) == len(zemljevid):
        hamilton = True
    else: hamilton = False
    for y in pot:
        if pot.count(y) > 1:
            hamilton = False
            break
    return hamilton

def navodila(pot, zemljevid):
    navodilaa = []
    seznam = []
    for x, y in zemljevid.items():
        if len(y) < 2:
            seznam.append(x)
    if pot[0] not in seznam and pot[-1] not in seznam:
        return False
    counter = 1
    for y in pot[1:]:
        if y == pot[-1]:
            break
        navodilaa.append((zemljevid[y].index(pot[counter+1]) - zemljevid[y].index(pot[counter-1])) % len(zemljevid[y]))
        counter += 1
    return navodilaa



