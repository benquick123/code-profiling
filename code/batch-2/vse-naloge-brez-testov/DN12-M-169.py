def obrni(s):
    for i in range(5):
        if s[0] == min(s):
            break
        else:
            prva = s[0]
            s = s[1:]
            s.append(prva)
    return s

def preberi(ime_datoteke):
    slovar = {}
    d = open(ime_datoteke)
    i = 1
    sez = []
    for e in d:
        if len(e) <= 2:
            if i not in slovar:
                slovar[i] = []
                slovar[i].append(int(e))
            else:
                slovar[i].append(int(e))
        else:
            e = e.split(" ")
            for ee in e:
                if ee != '\n':
                    if i not in slovar:
                        slovar[i] = []
                        slovar[i].append(int(ee))
                    else:
                        slovar[i].append(int(ee))
        i += 1
    for f in slovar:
        slovar[f] = obrni(slovar[f])
    return slovar


def mozna_pot(pot, zemljevid):
    slovar = zemljevid
    for e in pot[1:-1]:
        if len(slovar[e]) == 1:
            return False
    for f, d in zip(pot, pot[1:]):
        if f == d:
            return False
        if f not in slovar[d] or d not in slovar[f]:
            return  False
    p = pot[0]
    z = pot[-1]
    if len(slovar[p]) != 1:
        return False
    if len(slovar[z]) != 1:
        return False
    else:
        return True

def unikati(s):
    xs = []
    for e in s:
        if e not in xs:
            xs.append(e)
    return xs


def hamiltonova(pot, zemljevid):
    s = zemljevid
    if not mozna_pot(pot, zemljevid) or not (unikati(pot) == pot):
        return False
    for el in s:
        if len(s[el]) > 2:
            if el not in pot:
                return False
    else:
        return True

def navodila(pot, z):
    s = []
    st = 0
    for e, f, g in zip(pot,pot[1:],pot[2:]):
        for i in range(len(z[f])):
            if g == z[f][i] and z[f][0] == e:
                s.append(i + st)
                continue
            elif g == z[f][i]:
                st = z[f].index(e)
                r = i - st
                if r < 0:
                    r = len(z[f]) + r
                    s.append(r)
                else:
                    s.append(r)
    return s
def prevozi(zacetek, navodila, z):
    s = [zacetek]
    p = z[zacetek][0]
    if len(z[zacetek]) == 1:
        s.append(p)
    for e in navodila:
        if len(z[p]) < 2:
            break
        if z[p][0] == zacetek:
            s.append(z[p][e])
            zacetek = p
            p = z[p][e]
        else:
            i = z[p].index(zacetek)
            r = i + e
            if r >= len(z[p]):
                r = r - len(z[p])
            s.append(z[p][r])
            zacetek = p
            p = z[p][r]
    return s

def sosedi(doslej, z):
    s = []
    for e in doslej:
        for f in z[e]:
            if f in doslej:
                continue
            elif f not in s:
                s.append(f)
    return set(sorted(s))

def razdalja(x, y, z):
    m = set()
    if type(x) == int:
        s = sosedi({x}, z)
        m = m | s | {x}
    else:
        s = sosedi(x, z)
        m = m | s | x
    if y in m:
        return 1
    return 1 + razdalja(m,y,z)

