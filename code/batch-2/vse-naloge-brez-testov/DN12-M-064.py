def preberi(ime_datoteke):
    s = {}
    i = 1
    x = open(ime_datoteke)
    for e in x:
        f = e.split()
        t = []
        for w in f:
            t.append(int(w))
        c = min(t)
        q = t.index(c)
        d = t[q::]
        for h in d:
            if h in t:
                t.remove(h)


        t1 = d + t


        s[i] = t1
        i += 1
    x.close()
    return s

def mozna_pot(pot, zemljevid):
    t = zemljevid
    k = zip(pot, pot[1::])


    #povezana krozisca
    for e in k:
        if e[1] not in t[e[0]]:
            return False
    #ne ponovi
    for e in k:
        if e[0] == e[1]:
            return False
    #koncna povezava
    if len(t[pot[0]]) != 1:
        return False
    if len(t[pot[-1]]) != 1:
        return False
    #vmes koncne povezave
    for e in pot[1:-1]:
        if len(t[e]) == 1:
            return False




    return True

def hamiltonova(pot, zemljevid):
    t = zemljevid
    i = 0



    if mozna_pot(pot, zemljevid) == False:
        return False

    s = []

    for e in t:
        if len(t[e]) == 1:
            i += 1

    if len(pot) != len(t) - i + 2:
        return False





    return True

def navodila(pot, zemljevid):
    s = []
    t = zemljevid


    k = zip(pot, pot[1::], pot[2::])
    for e in k:
        i = 0
        if len(t[e[1]]) != 1:
            d = t[e[1]]
            i = abs(d.index(e[2]) - d.index(e[0]))
            s.append(i)
    return s





