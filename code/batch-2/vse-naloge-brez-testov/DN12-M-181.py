def preberi(ime_datoteke):
    datoteka = open(ime_datoteke).read().split('\n')
    s = {}
    i = 1

    for el in datoteka:
        if el != "":
            s[i] = []
            i += 1
    i = 1
    for el in datoteka:
        if el != "":
            pomozni = el.split(" ")
            for st in pomozni:
                s[i].append(int(st))
            i += 1
    for i in range(1, len(datoteka)):
        for j in range(0, len(s[i])):
            if s[i][0] != min(s[i]):
                s[i].append(s[i].pop(0))
    return s




def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[len(pot)-1]]) != 1:
        return False
    if len(pot) <= 2:
        return False
    if pot[1] not in zemljevid[pot[0]]:
        return False
    for i in range(1, len(pot)-1):
        if pot[i+1] not in zemljevid[pot[i]] or len(zemljevid[pot[i]]) == 1:
            return False
    return True


def hamiltonova(pot, zemljevid):
    st = 0
    for i in range(1, len(zemljevid)+1):
        if len(zemljevid[i]) == 1:
            st += 1
    st = st - 2
    if mozna_pot(pot, zemljevid) and len(pot) == len(set(pot)) and len(pot) == len(zemljevid) - st:
        return True
    return False


def navodila(pot, zemljevid):
    s = []
    for i in range(1, len(pot)-1):
        krozisce = zemljevid[pot[i]]
        razlika = (krozisce.index(pot[i+1]) - krozisce.index(pot[i-1])) % len(krozisce)
        s.append(razlika)
    return s



def prevozi(zacetek, navodila, zemljevid):
    s = [zacetek, zemljevid[zacetek][0]]
    for izvoz in navodila:
        t = []
        for c, vrednost in enumerate(zemljevid[s[-1]]):
            if vrednost == s[-2]:
                t.append(c)
        najvecji = max(t)
        s.append(zemljevid[s[-1]][(najvecji + izvoz) % len(zemljevid[s[-1]])])
    return s


def prevozi(zacetek, navodila, zemljevid):
    s = [zacetek, zemljevid[zacetek][0]]
    for izvoz in navodila:
        t = []
        for i in range(0, len(zemljevid[s[-1]])):
            if zemljevid[s[-1]][i] == s[-2]:
                t.append(i)
        najvecji = max(t)
        s.append(zemljevid[s[-1]][(izvoz + najvecji) % len(zemljevid[s[-1]])])
    return s


def sosedi(doslej, zemljevid):
    s = set()
    for krozisce in doslej:
        for izvoz in zemljevid[krozisce]:
            if izvoz not in doslej:
                s.add(izvoz)
    return s


def razdalja(x, y, zemljevid):
    s = {x}
    st = len(s)
    while True:
        if y not in sosedi(s, zemljevid):
            s.update(sosedi(s, zemljevid))
            st += 1
        else:
            break
    return st



