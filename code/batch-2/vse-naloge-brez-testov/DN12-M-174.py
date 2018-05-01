import collections


def preberi(ime_datoteke):
    d = open(ime_datoteke).read()
    o = collections.defaultdict(list)
    s = 1
    d = d.split("\n")
    if d[-1] == '':
        d = d[:-1]
    for x in d:
        x = x.split(" ")
        x = [int(m) for m in x]
        if len(x) > 1:
            p = 0
            for f in range(1, len(x)):
                if x[f] < x[p]:
                    p = f
            for f in range(0, len(x)):
                if p > len(x) - 1:
                    p = 0
                o[s].append((x[p]))
                p += 1
        else:
            x = int(x[0])
            o[s].append(x)
        s += 1
    return o


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[-1]]) == 1 and len(zemljevid[pot[0]]) == 1:
        for x in range(len(pot) - 1):
            if x != 0 and x != len(pot) - 1:
                if len(zemljevid[pot[x]]) == 1:
                    return False
            if pot[x + 1] not in zemljevid[pot[x]]:
                return False
        else:
            return True


def hamiltonova(pot, zemljevid):
    p = collections.defaultdict(int)
    if mozna_pot(pot, zemljevid):
        for x in pot:
            p[x] += 1
    return all([True if p[x] == 1 else False for x in range(1, sorted(zemljevid.keys())[-1]) if len(zemljevid[x]) != 1])


def navodila(pot, zemljevid):
    n = []
    print(pot)
    for x in range(1, len(pot) - 1):
        print(len(zemljevid[pot[x]]))
        vhod = zemljevid[pot[x]].index(pot[x - 1])
        izhod = zemljevid[pot[x]].index(pot[x + 1])
        n.append(abs(vhod-izhod) % len(zemljevid[pot[x]]))
    return n


