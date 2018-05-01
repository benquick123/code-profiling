# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    """
    Generiraj vse koordinate (x, y) za polje s podano širino in višino
    Args:
        s (int): širina
        v (int): višina

    Returns:
        generator parov polj
    """
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    sosedi = [(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x+1,y),(x- 1,y),(x,y+1),(x,y-1)]
    stej_mine = 0
    for sosed in sosedi:
        if sosed in mine:
            stej_mine += 1
    return stej_mine


def najvec_sosedov(mine, s, v):
    polja = vsa_polja(s,v)
    slovar = {}
    for x,y in polja:
        st_min = sosedov(x,y,mine)
        slovar[x,y] = st_min
    return max(slovar, key=slovar.get)


def brez_sosedov(mine, s, v):
    brez = set()
    polja = vsa_polja(s, v)
    for x,y in polja:
        st_min = sosedov(x,y,mine)
        if st_min == 0:
            brez.add((x,y))
    return brez


from collections import defaultdict
def po_sosedih(mine, s, v):
    polja = vsa_polja(s, v)
    slovar = defaultdict(set)
    for n in range(0,9):
        slovar[n] = set()
    for x,y in polja:
        st_min = sosedov(x,y, mine)
        if st_min in slovar:
            slovar[st_min].add((x,y))
    return slovar


########################
# Za oceno 7

def dolzina_poti(pot):
    koraki = 0
    xx = []
    yy = []
    if pot:
        for x,y in pot:
            xx.append(x)
            yy.append(y)
        xzdej = xx[0]
        yzdej = yy[0]
        for x1 in xx:
            if x1 != xzdej:
                koraki += abs(xzdej - x1)
                xzdej = x1
        for y1 in yy:
            if y1 != yzdej:
                koraki += abs(yzdej - y1)
                yzdej = y1
    return koraki

def potka(x0,y0,x1,y1):
    pot = [(x0,y0)]
    if x0 == x1:
        yy = y0
        while yy != y1:
            if y1 > y0:
                pot.append((x0, yy+1))
                yy = yy +1
            else:
                pot.append((x0, yy-1))
                yy = yy -1
    if y0 == y1:
        xx = x0
        while xx != x1:
            if x1 > xx:
                pot.append((xx+1,y0))
                xx = xx +1
            else:
                pot.append((xx-1,y0))
                xx = xx -1
    return pot


def varen_premik(x0, y0, x1, y1, mine):
    varnost = True
    for korak in potka(x0,y0,x1,y1):
        if korak in mine:
            varnost = False
    return varnost

def varna_pot(pot, mine):
    varnost = True
    premiki = []
    if pot:
        if len(pot) == 1:
            for xx in pot:
                if xx in mine:
                    varnost = False
        if len(pot) > 1:
            while pot[-1] not in premiki:
                for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
                    korak = potka(x0, y0, x1, y1)
                    for x in korak:
                        premiki.append(x)
                    pot = pot[1:]
            for e in premiki:
                if e in mine:
                    varnost = False
                    break
    return varnost


########################
# Za oceno 8

def polje_v_mine(polje):
    """
    Vrni koordinate min v podanem polju.

    Niz polje opisuje polje tako, da so vodoravne "vrstice" polja ločene s
    presledki. Prosta polja so označena z znako `.`, mine z `X`.

    Args:
        polje (str): polje

    Returns:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja.
    """


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """


