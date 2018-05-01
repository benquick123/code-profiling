def preberi(ime_datoteke):
    dictionary = {}
    stevec = 1
    text = open(ime_datoteke).readlines()
    for i in text:
        line = map(int, i.split())
        linija = list(line)
        naj = min(linija)
        najmanjsi = linija.index(naj)
        dictionary[stevec] = linija[najmanjsi:] + linija[:najmanjsi]
        stevec = stevec + 1
    return dictionary

def mozna_pot(pot, zemljevid):
    lop = pot[len(pot)-1]
    nastroj = len(zemljevid[lop])
    while nastroj != 1:
        return False
    lop = pot[0]
    nastroj = len(zemljevid[lop])
    while nastroj != 1:
        return False
    lop = len(pot) - 1
    for x in range(0, lop):
        if pot[x+1] not in zemljevid[pot[x]]:
            return False
    for x in range(0, lop):
        if pot[x] == pot[x+1]:
            return False
    for x in range(1, lop):
        if len(zemljevid[pot[x]]) == 1:
            return False
    return True

def hamiltonova(pot, zemljevid):
    stevec = 2
    if len(pot) != len(set(pot)) or not mozna_pot(pot, zemljevid):
        return False
    for k, v in zemljevid.items():
        if len(v) != 1:
            stevec+=1
    if stevec == len(pot):
        return True
    elif stevec != len(pot):
        return False
    return True


