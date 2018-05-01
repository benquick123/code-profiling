
def preberi(ime_datoteke):
    with open(ime_datoteke) as f:
        vse = f.readlines()
    krizisca = {}
    for index, vrstica in enumerate(vse):
        posamezni = []
        elementi = [int(j) for j in vrstica.split()]
        for i in range(len(elementi)):
            posamezni.append(elementi[(i + elementi.index(min(elementi))) % len(elementi)])
        krizisca[index + 1] = posamezni
    return krizisca

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1  or len(zemljevid[pot[-1]]) != 1:
        return False
    for prvi, drugi in zip(pot, pot[1:]):
        if drugi not in zemljevid[prvi]:
            return False
    for i in pot[1:-1]:
        if len(zemljevid[i]) == 1:
            return False 
    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid) and len(pot) == 2 + sum([True for i in zemljevid if len(zemljevid[i]) != 1]):
        return True
    return False

def navodila(pot, zemljevid):
    navodila_za_pot = []
    for prvi, drugi, tretji in zip(pot, pot[1:], pot[2:]):
        posamezni = []
        for i in range(len(zemljevid[drugi])):
            posamezni.append(zemljevid[drugi][(i + zemljevid[drugi].index(prvi)) % len(zemljevid[drugi])])
        navodila_za_pot.append(posamezni.index(tretji))
    return navodila_za_pot

def prevozi(zacetek, navodila, zemljevid):
    potka = [zacetek, zemljevid[zacetek][0]]
    for napotek in navodila:
        prvi = potka[-2]
        drugi = potka[-1]
        posamezni = []
        for i in range(len(zemljevid[drugi])):
            posamezni.append(zemljevid[drugi][(i + zemljevid[drugi].index(prvi)) % len(zemljevid[drugi])])
        potka.append(posamezni[napotek])
    return potka

def sosedi(doslej, zemljevid):
    sosedi = set()
    for i in doslej:
        for elementi in zemljevid[i]:
            sosedi.add(elementi)
    return sosedi - doslej

def razdalja(x, y, zemljevid):
    doslej = set([x])
    razdalja = 0
    while y not in doslej:
        razdalja += 1
        doslej = doslej | sosedi(doslej, zemljevid)
    return razdalja

def najkrajsa_navodila(x, y, zemljevid):
    doslej = set([x])
    koraki = {}
    razdalja = 0
    while y not in doslej:
        razdalja += 1
        vmes = set()
        for i in sosedi(doslej, zemljevid):
            doslej.add(i)
            vmes.add(i)
        koraki[razdalja] = vmes
    trenutni = y
    potka = [y]
    while razdalja != 1:
        razdalja -= 1
        susjedi = sosedi(set([trenutni]), zemljevid)
        blizje = koraki[razdalja]
        mozni = susjedi & blizje
        trenutni = list(mozni)[0]
        potka.append(trenutni)
    potka.append(x)
    potka.reverse()
    return navodila(potka, zemljevid)


