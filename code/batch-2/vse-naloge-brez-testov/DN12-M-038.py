
def preberi(ime_datoteke):
    dat= open(ime_datoteke)
    s={}
    i=1
    for all in dat:
        vrsta = all.strip()
        vrsta = vrsta.split(" ")
        vrsta = map(int,vrsta)
        vrsta = list(vrsta)
        najmanj = 100
        for al in vrsta:
            if najmanj > al:
                najmanj = al

        if vrsta[0]!= najmanj:
            presledek= vrsta.index(najmanj)
            vrsta= vrsta[presledek:]+vrsta[:presledek]



        s[i] = vrsta
        i += 1
    dat.close()

    return s

def mozna_pot(pot, zemljevid):

    if len(zemljevid[pot[0]])!=1 or len(zemljevid[pot[-1]])!=1:
        return False

    for x,y in zip(pot, pot[1:]):
        if x not in zemljevid[y]:
            return False

    for x in pot[1:-2]:
        if len(zemljevid[x]) == 1:
            return False



    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):
        repeat=[]
        for x in pot:
            if x not in repeat:
                repeat.append(x)
            else:
                return False
        if len(repeat)>= 6:
            if len(repeat)+1 != len(zemljevid)-1:
                return False
            else:
                return True
        else:
            if len(repeat) != len(zemljevid):
                return False
            else:
                return True
    else:
        return False








