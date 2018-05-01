def obrni(seznam):
        pravi_seznam = []
        seznam2 = []
        stevec = seznam.index(min(seznam))
        for i in seznam:
            seznam2.append(i)
            seznam2.sort()
        for j in seznam2:
            if min(seznam) == seznam[0]:
                pravi_seznam = seznam
                break
            if j == seznam2[0]:
                pravi_seznam.append(j)
            else:
                if stevec == len(seznam):
                    stevec = 0
                if seznam[stevec] not in pravi_seznam:
                    pravi_seznam.append(seznam[stevec])
                stevec += 1
        for k in seznam:
            if k not in pravi_seznam:
                pravi_seznam.append(k)
        return pravi_seznam


def preberi(ime_datoteke):
    datoteka = open(ime_datoteke, encoding="UTF-8")
    stevec = 1
    slovar = {}
    for vrstica in datoteka:
        vrstica = vrstica.rstrip().split()
        vrstica = [int(i) for i in vrstica]
        slovar[stevec] = obrni(vrstica)
        stevec += 1
    datoteka.close()
    return slovar

def mozna_pot(pot, zemljevid):
    i = 1
    if len(zemljevid[pot[0]]) > 1:
        return False
    for x in pot[1:-1]:
        if len(zemljevid[x]) == 1:
            return False
    while i < len(pot):
        if pot[i - 1] == pot[i]:
            return False
        i += 1
    i = 1
    while i < len(pot):
        if pot[i-1] not in zemljevid[pot[i]]:
            return False
        i += 1
    if len(zemljevid[pot[-1]]) == 1:
        return True
    return False

def hamiltonova(pot, zemljevid):
    i = 1
    seznam_kraj = []
    if len(pot) > len(set(pot)):
        return False
    for x in pot:
        if len(zemljevid[x]) == 1:
            seznam_kraj.append(x)
    while i < len(zemljevid):
        if i not in pot and len(zemljevid[i]) != 1:
            return False
        i += 1
    if len(zemljevid[pot[-1]]) != 1:
        return False
    return True


