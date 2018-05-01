def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    seznam = [s.strip() for s in datoteka]
    datoteka.close()
    seznam2 = []
    seznam3 = []
    for a in seznam.copy():
        a = a.split(" ")
        seznam2.append(a)
    for b in seznam2:
        seznam3.append([int(i) for i in b])
    for b in seznam3:
        for a in range(len(b)):
           if a + 1 < len(b):
                if b[a] < b[a+1]:
                    break
                elif b[0] == min(b):
                    break
                else:
                    b.insert(0, b.pop(-1))
    return( {i+1 : seznam3[i] for i in range(len(seznam3))})

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[-1]]) != 1 or len(zemljevid[pot[0]]) != 1 or len(pot) == 2:
        return False
    else:
        for a in range(len(pot)):
            if pot[a] != pot[-1] and pot[a] != pot[0]:
                if (zemljevid[pot[a]]) == 1:
                    return False
                elif pot[a] is pot[a+1]:
                    return False
                elif len(zemljevid[pot[a]]) == 1:
                    return False
                elif pot[a+1] not in zemljevid[pot[a]] or pot[a] not in zemljevid[pot[a+1]]:
                    return False
                elif pot[0] not in zemljevid[pot[1]]:
                    return False
    return True


def hamiltonova(pot, zemljevid):
    seznam = [a for a in zemljevid.keys() if a not in [1, 2, 12, 15]]
    if mozna_pot(pot, zemljevid):
        for a in pot:
            if pot.count(a) < 2:
                    if a in seznam:
                        seznam.remove(a)
                    continue
            else:
                return False
        if len(seznam) != 0:
            return False
        return True
    return False

def navodila(pot, zemljevid):
    seznam = []
    for c, a in enumerate(pot):
        if c != 0 and c != len(pot)-1:
            seznam.append((zemljevid[a].index(pot[c+1]) - zemljevid[a].index(pot[c-1])) % len(zemljevid[a]))
    return seznam

