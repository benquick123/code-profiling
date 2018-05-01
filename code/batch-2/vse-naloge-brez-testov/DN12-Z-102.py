def preberi(ime_datoteke):
    a = open(ime_datoteke)
    b = {}
    i = 1
    for x in a:
        x = x.strip()
        x = x.split(' ')
        x = list(map(int,x))
        if x[0] != min(x):
            st = x.index(min(x))
            x = x[st:]+x[:st]
        b[i] = x
        i += 1
    a.close()
    return b

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1: # začne/konča
        return False
    for zac,konc in zip(pot,pot[1:]):
        if zac not in zemljevid[konc]:
            return False
    for x in pot[1:len(pot)-1]:
        if len(zemljevid[x]) == 1:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot,zemljevid):
        x = []
        for y in pot:
            if y not in x:
                x.append(y)
            else:
                return False
        if len(x) <= 6:
            if len(x) != len(zemljevid):
                return False
            else:
                return True
        else:
            if len(x)+1 == len(zemljevid)-1:
                return True
            else:
                return False

    else:
        return False




