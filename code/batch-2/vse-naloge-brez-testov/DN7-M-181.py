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
    st = 0
    if (x-1, y-1) in mine:
        st = st + 1
    if (x-1, y) in mine:
        st = st + 1
    if (x-1, y+1) in mine:
        st = st + 1
    if (x, y-1) in mine:
        st = st + 1
    if (x, y+1) in mine:
        st = st + 1
    if (x+1, y-1) in mine:
        st = st + 1
    if (x+1, y) in mine:
        st = st + 1
    if (x+1, y+1) in mine:
        st = st + 1
    return st


def najvec_sosedov(mine, s, v):
    max = (0, 0)
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) > sosedov(max[0], max[1], mine):
                max = (i, j)
    return max




def brez_sosedov(mine, s, v):
    par = set()
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) == 0:
                par.add((i, j))
    return par




def po_sosedih(mine, s, v):
    d = {}
    for i in range(9):
        d[i] = set()
    for a in range(9):
        for i in range(s):
            for j in range(v):
                if a == sosedov(i, j, mine):
                    d[a].add((i, j))
    return d


########################
# Za oceno 7


def dolzina_poti(pot):
    razdalja = 0
    for i in range(1, len(pot)):
        razdalja = razdalja + abs(pot[i][0] - pot[i-1][0])
        razdalja = razdalja + abs(pot[i][1] - pot[i-1][1])
    return razdalja


def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1:
        for i in range(abs(y1-y0)+1):
            if y0 < y1:
                if (x0, y0+i) in mine:
                    return False
            else:
                if (x0, y0-i) in mine:
                    return False
    else:
        for i in range(abs(x1-x0)+1):
            if x0 < x1:
                if (x0+i, y0) in mine:
                    return False
            else:
                if (x0-i, y0) in mine:
                    return False
    return True



def varna_pot(pot, mine):
    if len(pot) == 1:
        if (pot[0][0], pot[0][1]) in mine:
            return False
    for i in range(len(pot)-1):
        if varen_premik(pot[i][0], pot[i][1], pot[i+1][0], pot[i+1][1], mine) == False:
            return False

    return True


########################
# Za oceno 8

def polje_v_mine(polje):
    vrstice = polje.split(" ")
    if vrstice[len(vrstice) - 1] == "":
        vrstice.remove(vrstice[len(vrstice) - 1])
    v = len(vrstice)
    polj = list(vrstice[0])
    s = len(vrstice[0])
    seznam = set()
    for i in range(v):
        for j in range(s):
            if vrstice[i][j] == 'X':
                seznam.add((j, i))
    return seznam, s, v

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


