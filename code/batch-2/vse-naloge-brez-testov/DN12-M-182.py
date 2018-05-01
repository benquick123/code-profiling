import collections

def preberi(ime_datoteke):
    f = open(ime_datoteke)
    s = collections.defaultdict(list)
    c = 1
    nov = []
    for i in f.read().split("\n"):
        j = i.split()
        for e in j:
            nov.append(int(e))
            mini = nov.index(min(nov))
            a = nov[mini:] + nov[:mini]
            s[c] = a
        c += 1
        nov.clear()
    f.close()
    return s

def mozna_pot(pot, zemljevid):
    a = False
    c = -1
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1:
        for i, j in zip(pot, pot[1:]):
            if j not in zemljevid[i] and c == -1:
                a = False
                break
            if j in zemljevid[i] and len(zemljevid[i]) > 1 and c == 0:
                a = True
            else:
                a = False
                c += 1
    return a

def hamiltonova(pot, zemljevid):
    a = False
    c = 0
    for e in zemljevid:
        if len(zemljevid[e]) == 1:
            c += 1
    if mozna_pot(pot, zemljevid) and len(zemljevid) - c + 2  == len(pot):
        a = True
    return a

def navodila(pot, zemljevid):
    navodila = []
    for a, b, c in zip(pot, pot[1:], pot[2:]):
        g = (zemljevid[b].index(c) - zemljevid[b].index(a)) % len(zemljevid[b])
        navodila.append(abs(g))
    return navodila


