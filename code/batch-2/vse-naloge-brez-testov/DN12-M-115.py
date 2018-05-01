def preberi(ime_datoteke):
    data = open(ime_datoteke)
    stevec = 0
    slovar = {}
    for i in data:
        stevec += 1
        k = i.strip()
        sez = []
        for strin in k.split():
            sez.append(int(strin))
        idx = sez.index(min(sez))
        sez1 = (sez[idx:]+sez[:idx])
        slovar[stevec] = sez1
    return slovar

def mozna_pot(pot, zemljevid):
    prvo = pot[0]
    zadnji = pot[len(pot)-1]
    #print(prvo, zadnji)
    if len(zemljevid[prvo]) == 1 and len(zemljevid[zadnji]) == 1:
        for i in pot[1:-1]:
            if len(zemljevid[i]) == 1:
                return False
        pot1 = pot
        for i in pot1:
            pot2 = pot1[:1]
            #print(pot1[1:2])
            if pot2 == pot1[1:2]:
                return False
            pot1 = pot1[1:]
        p1 = pot
        for i in p1:
            p2 = p1[:1] #prvi el
            #print(p2)
            p3 = p1[1:2] #naslednji
            if p3 != []:
                for i in p2:
                    z = i
                for i in p3:
                    z1 = i
                if z1 not in zemljevid[z]:
                    return False
                p1 = p1[1:]
                #print(p1)
        return True
    return False

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot,zemljevid) == True:
        pot1 = []
        for i in zemljevid:
            if len(zemljevid[i]) > 1:
                pot1.append(i)
        for i in pot1:
            if i not in pot or pot.count(i)>1:
                return False
        return True
    return False



