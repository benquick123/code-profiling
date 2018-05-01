def preberi(ime_datoteke):
    t = open(ime_datoteke, "r", encoding="utf-8")
    st = 1
    slovar = {}
    for vrstica in t:
        vrstica = vrstica.rstrip()
        seznam = []
        for stevilka in vrstica.split(" "):
            seznam.append(int(stevilka))
        #print(seznam)
        seznam = preobrni(seznam)
        #print(seznam)
        slovar[st] = seznam

        st += 1
    t.close()
    return slovar

def preobrni(seznam):
    najmanjse = min (zip(seznam, range(0,len(seznam))))
    #print(list(zip(seznam, range(0,len(seznam)))))
    #print(najmanjse)
    st = 0
    nov_seznam = []
    while st < len(seznam):
        nov_seznam.append(seznam[(st+najmanjse[1])%len(seznam)])
        st += 1
    return nov_seznam

def mozna_pot(pot, zemljevid):
    #print("\n",zemljevid)
    #print(pot)

    def my_rek(pot,prejsen):
        #print(pot)
        if not pot:
            return True
        e = pot[0]
        pot = pot[1:]
        if len(zemljevid[e]) == 1:
            return False
        if prejsen in zemljevid[e]:
            if my_rek(pot,e):
                return True
        else:
            #print("hello ", prejsen , zemljevid[e])
            return False

    return len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1 and my_rek(pot[1:-1],pot[0]) and pot[0] in zemljevid[pot[1]]

def hamiltonova(pot, zemljevid):
    return mozna_pot(pot,zemljevid) and len(pot) == len(set(pot)) and all(len(zemljevid[e]) == 1 for e in list(set(list(zemljevid.keys())) - set(pot)))

def navodila(pot, zemljevid):
    return list(((zemljevid[krozisce].index(izhod)-zemljevid[krozisce].index(vhod))%len(zemljevid[krozisce])) for (vhod,krozisce,izhod) in zip(pot,pot[1:],pot[2:]))

def prevozi(zacetek, navodila, zemljevid):
    trenutni = zemljevid[zacetek][0]
    prejsen = zacetek
    #print(trenutni)
    seznam = []
    seznam.append(zacetek)
    seznam.append(trenutni)
    for st in navodila:
        x = zemljevid[trenutni][(zemljevid[trenutni].index(prejsen) + st) % len(zemljevid[trenutni])]
        prejsen = trenutni
        trenutni = x
        seznam.append(trenutni)
    return seznam

def sosedi(doslej, zemljevid):
    #print("Doslej:",doslej)
    mnozica = set()
    for e in doslej:
        for i in zemljevid[e]:
            if i not in doslej:
                mnozica.add(i)
    #print(mnozica)
    return mnozica

def razdalja(x, y, zemljevid):
    globina = 0
    x = [x]
    while y not in x:
        x = sosedi(x, zemljevid)
        globina += 1
    return globina

def najkrajsa_navodila(x, y, zemljevid):
    x = [x]
    seznam_slovarjev = []
    while y not in x:
        x = podobno_sosedi(x,zemljevid)
        seznam_slovarjev.append(x)
    pot = []
    for e in seznam_slovarjev[::-1]:
        #print(y)
        pot.append(y)
        y = e[y]
    pot.append(y)
    return navodila(pot[::-1],zemljevid)

def podobno_sosedi(doslej, zemljevid):
    seznam = {}
    for e in doslej:
        for i in zemljevid[e]:
            if i not in doslej:
                seznam[i] = e
    return seznam




