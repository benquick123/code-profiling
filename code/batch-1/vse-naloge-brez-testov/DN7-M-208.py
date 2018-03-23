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
    if (x + 1, y + 1) in mine:
        st_sosedov += 1
    if (x, y + 1) in mine:
        st_sosedov += 1
    if (x - 1, y + 1) in mine:
        st_sosedov += 1
    if (x - 1, y) in mine:
        st_sosedov += 1
    if (x - 1, y - 1) in mine:
        st_sosedov += 1
    if (x, y - 1) in mine:
        st_sosedov += 1
    if (x + 1, y - 1) in mine:
        st_sosedov += 1
    if (x + 1, y) in mine:
        st_sosedov += 1
    return st_sosedov


def najvec_sosedov(mine, s, v):
    max = 0
    res = (0, 0)
    for (x, y) in vsa_polja(s, v):
        tmp_max = sosedov(x, y, mine)
        if tmp_max > max:
            max = tmp_max
            res = (x, y)
    return res


def brez_sosedov(mine, s, v):
    brez = set()
    for (x, y) in vsa_polja(s, v):
        if sosedov(x, y, mine) == 0:
            brez.add((x, y))
    return brez


def po_sosedih(mine, s, v):
    res = {
        0: set(),
        1: set(),
        2: set(),
        3: set(),
        4: set(),
        5: set(),
        6: set(),
        7: set(),
        8: set()
    }
    for (x, y) in vsa_polja(s, v):
        st_sosedov = sosedov(x, y, mine)
        res[st_sosedov].add((x, y))
    return res


########################
# Za oceno 7

def dolzina_poti(pot):
    dolzina = 0
    for i in range(len(pot) - 1):
        x1, y1 = pot[i]
        x2, y2 = pot[i + 1]
        dolzina += abs(x1 - x2)
        dolzina += abs(y1 - y2)
    return dolzina


def varen_premik(x0, y0, x1, y1, mine):
    x = x0 - x1
    y = y0 - y1
    smer = True  # true za x, false za y
    negative = False
    dolzina = x
    if abs(x) < abs(y):
        smer = False
        dolzina = y
    if dolzina < 0:
        negative = True
    if (x0, y0) in mine:
        return False
    for i in range(abs(dolzina) + 1):
        if (x0, y0) in mine:
            return False
        if smer:
            if negative == True:
                x0 += 1
            else:
                x0 -= 1
        else:
            if negative == True:
                y0 += 1
            else:
                y0 -= 1
    return True


def varna_pot(pot, mine):
    if len(pot) > 0:
        if pot[0] in mine:
            return False
    for i in range(len(pot) - 1):
        x0, y0 = pot[i]
        x1, y1 = pot[i + 1]
        if varen_premik(x0, y0, x1, y1, mine) == False:
            return False
    return True


########################
# Za oceno 8

def polje_v_mine(polje):
    mine = set()
    polje = polje.split(" ")
    for y in range(len(polje)):
        vrstica = polje[y]
        for x in range(len(vrstica)):
            if vrstica[x] == "X":
                mine.add((x, y))
    return mine, len(polje[0]), len(polje)


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


