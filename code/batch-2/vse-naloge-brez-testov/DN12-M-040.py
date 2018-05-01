from collections import defaultdict

def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    s = {}
    i = 1
    for vrstica in datoteka:
        s[i] = list(map(int, vrstica.split()))
        i+=1
    for k in s:
        zacasni = s[k]
        indeks = zacasni.index(min(zacasni))
        if zacasni[:indeks] != []:
            delcek = zacasni[:indeks]
            del zacasni[:indeks]
            for i in delcek:
                zacasni.append(i)
    return s

def mozna_pot(pot, zemljevid):
    koncne = []
    for kljuc in zemljevid:
        if len(zemljevid[kljuc]) == 1:
            koncne.append(kljuc)
    vmesne = pot[1:-1]
    a = True
    if pot[0] not in koncne or pot[-1] not in koncne:
            a = False
    for i in vmesne:
        if i in koncne:
            a = False
            break
    for i in pot:
        soseda = pot[pot.index(i): pot.index(i) + 2]
        if len(soseda) > 1 and soseda[0] == soseda[1]:
            a = False
            break
    for i in pot:
        soseda = pot[pot.index(i): pot.index(i) + 2]
        if len(soseda) > 1 and soseda[1] not in zemljevid[soseda[0]]:
            a = False
            break
    return a

def hamiltonova(pot, zemljevid):
    vsa = []
    for k in zemljevid:
        if len(zemljevid[k]) > 1:
            vsa.append(k)
    if not mozna_pot(pot, zemljevid):
        return False
    elif sorted(pot[1:-1]) != sorted(vsa):
        return False
    else:
        return True

def navodila(pot, zemljevid):
    navodila = []
    for i in range(1, len(pot) - 1):
        s = zemljevid[pot[i]]
        prejsnji = pot[i - 1]
        naslednji = pot[i + 1]
        rez = (s.index(naslednji) - s.index(prejsnji)) % len(s)
        navodila.append(rez) 
    return navodila


    

