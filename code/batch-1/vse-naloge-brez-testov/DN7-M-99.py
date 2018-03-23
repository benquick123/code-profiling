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

    st_sosedov = 0

    for x1, y1 in mine:
        if x != x1 or y != y1:
            if abs((x-x1)) <= 1 and abs((y-y1)) <= 1:
                st_sosedov += 1

    return st_sosedov



def najvec_sosedov(mine, s, v):

    stevec = 0
    z_najvec = (0, 0)
    for y in range(v):
        for x in range(s):
            if sosedov(x, y, mine) > stevec:
                stevec = sosedov(x, y, mine)
                z_najvec = (x, y)

    return z_najvec

def brez_sosedov(mine, s, v):

    brez = set()

    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) == 0:
                brez.add((i,j))

    return brez

def po_sosedih(mine, s, v):

    d = {i: set() for i in range(9)}
    for x in range(s):
        for y in range(v):
                d[sosedov(x, y, mine)].add((x, y))

    return d

########################
# Za oceno 7

def dolzina_poti(pot):

    dolzina = 0

    if len(pot) > 1:
        x1, y1 = pot[0]

        for x, y in pot:
            if x != x1 or y != y1:
                dolzina += abs((x1 - x) + (y1 - y))

            x1, y1 = x, y

    return dolzina


def varen_premik(x0, y0, x1, y1, mine):


    if x0 == x1:
        if y1 < y0:
            y0, y1 = y1, y0
        for i in range(y0, y1 + 1):
                if (x0, i) in mine:
                    return False
    else:
        if x1 < x0:
            x0, x1 = x1, x0
        for i in range(x0, x1 + 1):
            if (i, y0) in mine:
                return False

    return True



def varna_pot(pot, mine):

    if len(pot) > 0:
        x0, y0 = pot[0]

        if (x0, y0) in mine:
            return False

        for (x0, y0), (x1, y1) in zip(pot,pot[1:]):
            if varen_premik(x0, y0, x1, y1, mine) == False:
                return False

    return True

########################
# Za oceno 8

def polje_v_mine(polje):

    koordinate = set()
    polje = list(polje.split())

    s = len(polje[0])
    v = len(polje)

    y = 0

    for vrstica in polje:
        x = 0
        for znak in list(vrstica):
            if znak == "X":
                koordinate.add((x, y))
            x += 1
        y += 1


    return (koordinate, s, v)


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


