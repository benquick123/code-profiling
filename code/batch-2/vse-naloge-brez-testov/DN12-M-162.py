def preberi(ime_datoteke):
    slovarij_krozisca = {}
    m = open(ime_datoteke)
    i = 1
    for ms in m:
        lista_krozisca = []
        b = [int(x) for x in ms.strip().split(" ")]
        c = min(b)
        g = b.index(c)
        if b[0] != c:
            for nesto in b[g:]:
                lista_krozisca.append(nesto)
            for nesto in b[:g]:
                lista_krozisca.append(nesto)
        else:
            for nesto in b:
                lista_krozisca.append(nesto)
        slovarij_krozisca[i] = lista_krozisca
        i += 1
    m.close()
    return slovarij_krozisca


def mozna_pot(pot, zemljevid):
    potanja = zip(pot, pot[1:])
    for a, b in potanja:
        if b not in zemljevid[a] or a == b:
            return False
    if len(zemljevid[pot[0]]) > 1 or len(zemljevid[pot[-1]]) > 1:
        return False
    for a in pot[1:-1]:
        if len(zemljevid[a]) == 1:
            return False
    return True


def hamiltonova(pot, zemljevid):
    for a in zemljevid:
        if not len(zemljevid[a]) == 1 and (a != pot[0] or a != pot[-1]):
            if a not in pot:
                return False
    if len(pot) > len(set(pot)):
        return False
    return mozna_pot(pot, zemljevid)


def navodila(pot, zemljevid):
    ruta = []
    potanja = zip(pot, pot[1:], pot[2:])
    for a, b, c in potanja:
        rutina = zemljevid[b]
        while rutina[0] != a:
            prva = rutina[0]
            rutina.remove(prva)
            rutina.append(prva)
        ci = rutina.index(c)
        ruta.append(len(rutina[:ci]))
    return ruta


def prevozi(zacetek, navodila, zemljevid):
    tocka_zacetka = zemljevid[zacetek][0]
    finalna_ruta = [zacetek, zemljevid[zacetek][0]]
    for nav in navodila:
        lista = zemljevid[tocka_zacetka]
        while lista[0] != finalna_ruta[-2]:
            prva = lista[0]
            lista.remove(prva)
            lista.append(prva)
        finalna_ruta.append(lista[nav])
        tocka_zacetka = zemljevid[tocka_zacetka][nav]
    return finalna_ruta


def sosedi(doslej, zemljevid):
    finalni_slovarij_povezava = []
    for krozisce in doslej:
        lista = zemljevid[krozisce]
        for uvozov in lista:
            if uvozov not in doslej:
                finalni_slovarij_povezava.append(uvozov)
    return set(finalni_slovarij_povezava)


def razdalja(x, y, zemljevid):
    t = list(sosedi({x}, zemljevid))
    finalna_povezava = 1
    while y not in t:
        for x1 in t:
            t = t + list(sosedi({x1}, zemljevid))
        finalna_povezava += 1
    return finalna_povezava


def sosedi_slovarij(slovarij, zemljevid):
    slovarijx = {}
    for x in slovarij:
        for nesto in zemljevid[x]:
            if nesto not in slovarijx:
                slovarijx[nesto] = x
    slovarij.update(slovarijx)


def najkrajsa_navodila(x, y, zemljevid):
    slovarij_poteva = {x: None}
    lista_neka = [y]
    while y not in slovarij_poteva:
        sosedi_slovarij(slovarij_poteva, zemljevid)
    while x not in lista_neka:
        lista_neka.append(slovarij_poteva[y])
        y = slovarij_poteva[y]
    return navodila(lista_neka[::-1], zemljevid)


