def preberi(ime_datoteke):
    dat = open(ime_datoteke)
    s = {}
    st = 1
    for vrstica in dat:
        ls = []
        vrstica = vrstica.split(" ")
        naj = min(int(x) for x in vrstica)
        pisem = False
        for xx in vrstica:
            if int(xx) == naj:
                pisem = True

            if pisem == True:
                ls.append(int(xx))

        for xy in vrstica:
            if int(xy) == naj:
                break

            ls.append(int(xy))
        s[st] = ls
        st += 1
    return s


def mozna_pot(pot, zemljevid):
    l = len(pot)
    res = True
    st = 0
    for korak in pot:
        if st == 0:
            # ce smo na prvem preveri ali si na izvozu
            if (len(zemljevid[korak]) != 1):
                res = False

        elif st == (len(pot) - 1):
            # isto, preveri ali je zadnji izvoz
            if (len(zemljevid[korak]) != 1):
                res = False
            if (pot[st - 1] not in zemljevid[korak]):
                return False
        else:
            if (len(zemljevid[korak]) == 1):
                res = False
            if (pot[st - 1] not in zemljevid[pot[st]]):
                res = False
        st += 1
    return res


def hamiltonova(pot, zemljevid):
    if (mozna_pot(pot, zemljevid)):
        ls = []
        vsi = []
        por = []
        for el in zemljevid:
            if (len(zemljevid[el]) > 1):
                vsi.append(el)
        for korak in pot:
            if (korak not in ls):
                ls.append(korak)
                por.append(korak)
            else:
                return False
        for en in vsi:
            if (en not in por):
                return False
        return True


def navodila(pot,
             zemljevid):  # [zemljevid[pot[korak-1]].index(pot[korak])-zemljevid[pot[korak-1]].index(pot[korak-2]))%len(zemljevid[pot[korak-1]] for korak in range(2, len(pot))]
    return [(zemljevid[pot[korak - 1]].index(pot[korak]) - zemljevid[pot[korak - 1]].index(pot[korak - 2])) % len(
        zemljevid[pot[korak - 1]]) for korak in range(2, len(pot))]


def prevozi(zacetek, navodila, zemljevid):
    ls = [zacetek, zemljevid[zacetek][0]]
    pos = zemljevid[zacetek][0]
    for navodilo in navodila:
        x = zemljevid[pos][(zemljevid[pos].index(zacetek) + navodilo) % len(zemljevid[pos])]
        print(x)
        zacetek = pos
        pos = x

        ls.append(x)

    return ls


def sosedi(doslej, zemljevid):
    res = set()
    for neki in doslej:
        for a in zemljevid[neki]:
            if (a not in doslej):
                res.add(a)

    return res


def razdalja(x, y, zemljevid):
    r = 0
    f = {x}
    x = True
    while x == True:
        s = sosedi(f, zemljevid)
        r += 1
        if (y in s):
            x = False
        f = s
    return r


def sosedi_slovar(slovar_vozlisc, zemljevid):
    dict = {}
    for vozlisce in slovar_vozlisc:
        for sosed_vozlisca in zemljevid[vozlisce]:
            dict[sosed_vozlisca] = vozlisce
    return {**dict, **slovar_vozlisc}


def najkrajsa_navodila(x, y, zemljevid):
    start = zemljevid[x][0]
    run = True
    n = 0
    found = False
    pot = [y]
    slovar_bliznjih = {start: x}
    while run == True:
        s = sosedi_slovar(slovar_bliznjih, zemljevid)
        n += 1
        for sosed in s:
            if sosed == y:
                found = True

        if found == True:
            xa = 0
            while xa < 15:
                print(s)
                for korak in s:
                    if korak == y:
                        pot.append(s[korak])
                        y = s[korak]
                        xa += 1
                        if x in pot:
                            xa = 100
            obrnjen = []
            for xxx in pot[::-1]:
                obrnjen.append(xxx)
            konec = navodila(obrnjen, zemljevid)
            if (0 in konec):
                konec.remove(0)
            return konec
        slovar_bliznjih = s
