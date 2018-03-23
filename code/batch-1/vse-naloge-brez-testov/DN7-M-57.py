# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    stevilo_sosedov = 0
    if (x + 1, y) in mine:
        stevilo_sosedov += 1
    if (x - 1, y) in mine:
        stevilo_sosedov += 1
    if (x, y + 1) in mine:
        stevilo_sosedov += 1
    if (x, y - 1) in mine:
        stevilo_sosedov += 1
    if (x + 1, y + 1) in mine:
        stevilo_sosedov += 1
    if (x - 1, y - 1) in mine:
        stevilo_sosedov += 1
    if (x - 1, y + 1) in mine:
        stevilo_sosedov += 1
    if (x + 1, y - 1) in mine:
        stevilo_sosedov += 1
    return stevilo_sosedov


def najvec_sosedov(mine, s, v):
    maxi = -1
    for polje in vsa_polja(s, v):
        if sosedov(polje[0], polje[1], mine) > maxi:
            maxi = sosedov(polje[0], polje[1], mine)
            koordinate_max = polje
    return koordinate_max


def brez_sosedov(mine, s, v):
    mnozica = set([])
    for koordinate in vsa_polja(s, v):
        if sosedov(koordinate[0], koordinate[1], mine) == 0:
            mnozica.update([koordinate])
    return mnozica


def po_sosedih(mine, s, v):
    def x_sosedov(mine, s, v, x):
        mnozica = set([])
        for koordinate in vsa_polja(s, v):
            if sosedov(koordinate[0], koordinate[1], mine) == x:
                mnozica.update([koordinate])
        return mnozica
    return {i : x_sosedov(mine, s, v, i) for i in range(9)}


########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([max(abs(pot[i][0] - pot[i+1][0]), abs(pot[i][1] - pot[i+1][1])) for i in range(len(pot) - 1)])


def varen_premik(x0, y0, x1, y1, mine):
    dx = x1 - x0
    dy = y1 - y0
    if dx != 0:
        for i in range(dx + 1):
            if (x0 + i, y0) in mine:
                return False
    else:
        for i in range(dy + 1):
            if (x0, y0 + i) in mine:
                return False
    return True



def varna_pot(pot, mine):
    for i in range(len(pot) - 1):
        if varen_premik(pot[i][0], pot[i][1], pot[i+1][0], pot[i+1][1], mine) == False:
            return False
    else:
        return True


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


