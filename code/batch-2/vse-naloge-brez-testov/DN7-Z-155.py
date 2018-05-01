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
    count = 0
    for a in range(y - 1, y + 2):
        for b in range(x - 1, x + 2):
            if (b,a) in mine and (b,a) != (x,y):
                count+=1
    return count


def najvec_sosedov(mine, s, v):
    najvecji_count = 0
    koor_x, koor_y = 0, 0
    for i in range(v):
        for j in range(s):
            count = sosedov(j,i, mine)
            if count > najvecji_count:
                najvecji_count = count
                koor_x, koor_y = j, i
    return (koor_x, koor_y)


def brez_sosedov(mine, s, v):
    mnozica = set()
    for i in range(v):
        for j in range(s):
            count = sosedov(j, i, mine)
            if count == 0:
                mnozica.add((j,i))
    return mnozica


def po_sosedih(mine, s, v):
    slovar = {}
    for i in range(9):
        slovar[i] = set()

    for i in range(v):
        for j in range(s):
            count = sosedov(j,i, mine)
            slovar[count].add((j,i))
    return slovar


########################
# Za oceno 7

def dolzina_poti(pot):
    vsota = 0
    for (e1, e2), (e3, e4) in zip(pot[:len(pot)], pot[1:]):
        razdalja = abs(e4 - e2) + abs(e3 - e1)
        vsota += razdalja
    return vsota

def varen_premik(x0, y0, x1, y1, mine):
    if x0-x1 == 0:
        for i in range(min(y0,y1), max(y1,y0)+1):
            if (x0, i) in mine:
                return False
    else:
        for j in range(min(x1,x0), max(x1, x0)+1):
            if (j, y0) in mine:
                return False
    return True


def varna_pot(pot, mine):
    if len(pot) == 1:
        if pot[0] in mine:
            return False
    else:
        for (e1, e2), (e3, e4) in zip(pot[:len(pot)], pot[1:]):
            if varen_premik(e1, e2, e3, e4, mine) is False:
                return False
    return True

########################
# Za oceno 8

def polje_v_mine(polje):
    mnozica = set()
    seznam = polje.split(" ")
    if '' in seznam:
        seznam.remove('')
    visina = len(seznam)
    sirina = len(seznam[0])
    for i in range(visina):
        for j in range(sirina):
            if seznam[i][j] == "X":
                mnozica.add((j, i))
    return (mnozica, sirina, visina)

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


