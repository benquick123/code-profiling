from collections import defaultdict


def preberi(ime_datoteke):
    a = 1
    b = []
    slovar = defaultdict(list)
    datoteka = open(ime_datoteke)
    for s in datoteka:
        s = s.strip()
        s = s.split(" ")
        for n in s:
                b.append(int(n))
        najmanj = min(b)
        while najmanj != b[0]:
            b.append(b[0])
            b = b[1:]
        slovar[a] = b
        b = []
        a += 1
    datoteka.close()
    return slovar

def mozna_pot(pot, zemljevid):
    i = 1
    if 1 != len(zemljevid[pot[0]]):
        return False
    if 1 != len(zemljevid[pot[len(pot)-1]]):
        return False
    else:
        for h in pot[1:-1]:
            if 1 == len(zemljevid[h]):
                return False
        a = pot[0]
        for s in pot[1:]:
            if s == a:
                return False
            a = s
        for m in pot:
            p = zemljevid[m]
            for n in pot[i:]:
                if n not in p:
                    return False
                i += 1
                break
    return True

def hamiltonova(pot, zemljevid):
    b = 0
    a = len(pot)
    if mozna_pot(pot, zemljevid):
        for i in pot:
            if pot.count(i) > 1:
                return False
        for e in zemljevid:
            if len(zemljevid[e]) > 1:
                b += 1
        if a-2 != b:
            return False
        return True
    return False



