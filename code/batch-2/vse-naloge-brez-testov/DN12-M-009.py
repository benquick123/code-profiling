def preberi(imedatoteke):
    slovar = {}
    i = 1
    datoteka = open(imedatoteke)
    for vrstica in datoteka:
        vrstica1 = vrstica.split()
        vrstica1 = [int(i) for i in vrstica1]
        while not vrstica1[0] == min(vrstica1):
            a = vrstica1[0]
            vrstica1.pop(0)
            vrstica1.append(a)
        slovar[i] = vrstica1
        i = i + 1
    return slovar

def mozna_pot(pot, zemljevid):
    if not len(zemljevid[pot[0]]) == 1:
        return False
    if not len(zemljevid[pot[-1]]) == 1:
        return False
    i = 1
    while i < len(pot):
        if not pot[i] in zemljevid[pot[i-1]]:
            return False
        if pot[i] == pot[i-1]:
            return False
        if i + 1 != len(pot) and len(zemljevid[pot[i]]) == 1:
            return False
        i = i + 1
    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid) == False:
        return False
    if not len(pot) == len(set(pot)):
        return False
    i = 1
    izhodi = 0
    while i <= len(zemljevid):
        if len(zemljevid[i]) == 1:
            izhodi = izhodi + 1
        i = i + 1
    if not len(pot) == len(zemljevid.keys()) + 2 - izhodi:
        return False
    return True

