def preberi(ime_datoteke):
    s = [line.rstrip('\n') for line in open(ime_datoteke)]
    key = 1
    dict = {}
    for i in s:
        if " " in i:
            z = i.split()
            z2 = [int(x) for x in z]
            najmanjsa = min(z2)
            while z2.index(najmanjsa) != 0 :
                trenutna = z2[0]
                z2.remove(trenutna)
                z2.append(trenutna)
            dict[key] = z2
        else:
            dict[key] = [int(i)]
        key += 1

    return dict

def f_izven(zemljevid):
    s = []
    for i in zemljevid:
        if len(zemljevid[i]) == 1:
            s.append(i)
    return s

def mozna_pot(pot, zemljevid):
    izven = f_izven(zemljevid)
    if pot[0] not in izven:
        return False
    elif pot[-1] not in izven:
        return False
    for i in range(1, len(pot)):
        if (pot[i] == pot[i - 1]):
            return False
    for i in pot:
        if i in izven and i != pot[0] and i != pot[-1]:
            return False

    i=1
    while i >= 0 and i != len(pot):
        if pot[i-1] not in zemljevid[pot[i]]:
            return False
        i += 1

    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid) == False:
        return False

    s=[]
    izven = f_izven(zemljevid)
    for key, value in zemljevid.items():
        s.append(key)
    for i in izven:
        if i in s:
            s.remove(i)

    pot = pot[1:-1]
    if sorted(pot) != sorted(s):
        return False
    else:
        return True



