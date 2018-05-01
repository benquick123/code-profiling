def preberi(ime_datoteke):
    file = open(ime_datoteke).read()
    slovar = {}
    stevec_vrstic = 1
    for vrstica in file.split("\n"):
        seznam = []
        for stevilka in vrstica.split(" "):
            if stevilka:
                seznam.append(int(stevilka))
        if seznam:
            i = seznam.index(min(seznam))
            nov_seznam = seznam[i:] + seznam[:i]
        else:
            break
        slovar[stevec_vrstic] = nov_seznam
        stevec_vrstic += 1
    return slovar


def mozna_pot(pot, zemljevid):
    skupaj = zip(pot, pot[1:])
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1:
        brez = pot[1:-1]
        for element in brez:
            if not len(zemljevid[element]) > 1:
                return False
        for original, primerjava in skupaj:
            if primerjava in zemljevid[original]:
                continue
            else:
                return False
        return True
    else:
        return False


def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):
        for i in range(len(pot)):
            if pot[i] not in pot[:i]:
                continue
            else:
                return False
        for kraj in zemljevid:
            seznam = []
            for krozisce in zemljevid[kraj]:
                if krozisce in pot or len(zemljevid[krozisce]) == 1:
                    seznam.append(True)
                else:
                    seznam.append(False)
            if not all(seznam):
                return False
        return True
    return False


def navodila(pot, zemljevid):
    navodilo = []
    stevec = 1
    for cifra in pot:
        if not len(zemljevid[cifra]) == 1:
            razlika = zemljevid[cifra].index(pot[stevec]) - zemljevid[cifra].index(stara)
            if razlika < 0:
                razlika = razlika % len(zemljevid[cifra])
            navodilo.append(razlika)
        stara = cifra
        stevec += 1
    return navodilo


def prevozi(zacetek, navodila, zemljevid):
    stanje = zemljevid[zacetek][0]
    pot = [zacetek, stanje]
    staro = zacetek
    for korak in navodila:
        stev = zemljevid[stanje].index(staro) + korak
        if stev >= len(zemljevid[stanje]):
            stev = stev - len(zemljevid[stanje])
        staro = stanje
        stanje = zemljevid[stanje][stev]
        pot.append(stanje)
    return pot


