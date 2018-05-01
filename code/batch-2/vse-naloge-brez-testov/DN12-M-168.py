def preberi(ime_datoteke):
    slovar = {}
    g = 1
    zemljevid = open(ime_datoteke)
    for vrstica in zemljevid:
        seznam = []
        vrstica = vrstica.strip().split()
        for znak in vrstica:
            znak = int(znak)
            seznam.append(znak)
        seznam = seznam*2
        for i,a in enumerate(seznam):
            if a == min(seznam):
                seznam = seznam[i: i + len(seznam)//2]
                break
        slovar[g] = seznam
        g += 1
    return slovar
def mozna_pot(pot,zemljevid):
    prav = True
    prav1 = []
    for x in pot:
        if len(zemljevid[x]) != 1:
            prav1.append(True)
        else:
            prav1.append(False)
    if sum([1 for x in prav1 if x]) == len(pot) -2 and not prav1[0] and not prav1[-1]:
        for k1,k2 in zip(pot,pot[1:]):
            if k2 in zemljevid[k1]:
                continue
            else:
                return False
    else:
        return False

    return True





def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid) == True:
        if len(pot) != len(set(pot)):
            if len(pot) == 12:
                return True
    return False




