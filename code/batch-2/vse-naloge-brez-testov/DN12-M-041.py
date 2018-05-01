def preberi(ime_datoteke):
    slovar = dict()
    counter = 0
    for line in open(ime_datoteke):
        line = line.strip().split()
        line = [int(i) for i in line]
        counter += 1
        slovar[counter] = line
        indx = line.index(min(line))
        temp_list = line[:indx]
        del line[:indx]
        line += temp_list
    return slovar

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) > 1 or len(zemljevid[pot[-1]]) > 1:
        return False
    for i, e in enumerate(pot[1:]):
        i += 1
        if len(zemljevid[e]) == 1 and i < len(pot) - 1:
            return False
        if e == pot[i - 1]:
            return False
        if pot[i - 1] not in zemljevid[e]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False

    lst = []
    for i, e in zip(zemljevid, zemljevid.values()):
        if len(e) > 1:
            lst += [i]

    lst2 = pot[1:-1]
    lst2 = sorted(lst2)

    if lst == lst2:
        return True
    return False








