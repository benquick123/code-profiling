def preberi(datoteka):
    a = {}
    b = open(datoteka)
    c = 1
    for i in b:
        j = i.split()
        n = []
        for k in j:
            k = int(k)
            n.append(k)
        l = min(n)
        while 1:
            if n[0] != l:
                o = n.pop(0)
                n.append(o)
            else:
                break
        a[c] = n
        c = c + 1
    b.close()
    return a



def mozna_pot(pot, zemljevid):
    a = pot[0]
    b = pot[-1]
    if len(zemljevid[a]) != 1 or len(zemljevid[b]) != 1:
        return False
    d = 0
    for i in pot:
        if d != 0 and d != len(pot) - 1:
            if len(zemljevid[i]) == 1:
                return False
        d = d + 1
    c = 0
    for i in pot:
        if i != pot[-1] and pot[c + 1] not in zemljevid[i]:
            return False
        c = c + 1
    return True



def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False
    for i in pot:
        if pot.count(i) != 1:
            return False
    for i in zemljevid:
        if len(zemljevid[i]) != 1:
            if i not in pot:
                return False
    return True


#TESTI:
