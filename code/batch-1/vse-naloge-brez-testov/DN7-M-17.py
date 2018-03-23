# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
from collections import*
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
    counter = 0
    uzyn = range(x-1, x+2)
    gapdal = range(y-1, y+2)
    for j in uzyn:
        for k in gapdal:
            if (j,k) in mine:
                if (j,k) != (x,y):
                    counter += 1
    return counter


def najvec_sosedov(mine, s, v):

    max = 0
    kx = 0
    ky = 0
    uzyn = range(s)
    gapdal = range(v)

    for j in uzyn:
        for k in gapdal:
            counter = sosedov(j,k, mine)
            while counter > max:
                max = counter
                kx = j
                ky = k
    return (kx, ky)

def brez_sosedov(mine, s, v):
    lop = set()
    uzyn = range(s)
    gapdal = range(v)
    nol = 0

    for j in uzyn:
        for k in gapdal:
            counter = sosedov(j, k, mine)
            if counter == nol:
                lop.add((j,k))
    return lop

def po_sosedih(mine, s, v):
    neigh = defaultdict(set)
    lis = []
    uzyn = range(s)
    gapdal = range(v)
    total = range(0, 9)

    for j in uzyn:
        for k in gapdal:
            lis.append((j,k))

            for a in total:
                neigh[a]
            for one, two in lis:
                num = sosedov(one, two, mine)
                neigh[num].add((one, two))
    return dict(neigh)


########################
# Za oceno 7

def dolzina_poti(pot):
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    """
    Vrni `True`, če je pomik z (x0, y0) and (x1, y1) varen, `False`, če ni.

    Args:
        x0 (int): koordinata x začetnega polja
        y0 (int): koordinata y začetnega polja
        x1 (int): koordinata x končnega polja
        y1 (int): koordinata y končnega polja
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je premik varen, `False`, če ni.
    """


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """


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


