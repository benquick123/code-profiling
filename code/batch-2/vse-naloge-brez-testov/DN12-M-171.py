def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    slovar = {}
    i = 1
    for vrstica in datoteka:
        s = vrstica.split()
        s1 = list(map(int, s))
        mini = min(s1)
        while s1[0] != mini:
            s1.append(s1[0])
            s1.remove(s1[0])
        slovar[i] = s1
        i += 1
    datoteka.close()
    return slovar


def mozna_pot(pot, zemljevid):
    for i,e in enumerate(pot):
        if len(pot) <= 2:
            if pot[1] not in zemljevid[e]:
                return False
        if i == len(pot) - 1:
            if len(zemljevid[pot[len(pot)-1]]) > 1:
                return False
        if i == 0:
            if len(zemljevid[pot[0]]) > 1 or pot[i+1] not in zemljevid[pot[i]]:
                return False
        if pot[i-1] == e and i > 0:
            return False
        if 0 < i < len(pot) - 2:
            if pot[i+1] not in zemljevid[pot[i]] or len(zemljevid[pot[i]]) < 2 or e not in zemljevid:
                return False
    return True


def hamiltonova(pot, zemljevid):
    sez = []
    koliko = 0
    for k,sosedi in zemljevid.items():
        if k not in sez:
            preveri = mozna_pot(pot,zemljevid)
            if len(sosedi) > 1 and k not in pot[1:len(pot)-1:1]:
                return False
            if preveri == False:
                return False
            sez.append(k)
            for i,element in enumerate(pot):
                if k == element:
                    koliko += 1
                    if koliko == 2:
                        return False
            koliko = 0

    return True


def navodila(pot, zemljevid):
    star = pot[0]
    vrni = []
    koliko = 0
    for i,e in enumerate(pot[1:-1]):
        nov = zemljevid[e]
        while nov[0] != star:
            nov.append(nov[0])
            nov.remove(nov[0])
        for vsak in nov:
            if vsak == pot[i+2]:
                vrni.append(koliko)
                koliko = 0
                break
            koliko += 1
        star = e
    return vrni


def prevozi(zacetek, navodila, zemljevid):
    pot = navodila
    seznam = [zacetek]
    pozicija = zacetek
    prejsna = zacetek
    reseno = False

    while reseno != True:
        for k,v in zemljevid.items():
            if k == pozicija:
                if len(v) == 1:
                    pozicija = v[0]
                    seznam.append(v[0])
                    pozicija = v[0]
                    continue
                for l, stej in enumerate(pot):
                    if k == pozicija:
                        while prejsna != v[0]:
                            v.append(v[0])
                            v.remove(v[0])
                        prejsna = pozicija
                        pozicija = v[stej]
                        seznam.append(pozicija)
                        continue
                pot.remove(pot[0])
            if pot == []:
                return seznam
    return seznam











