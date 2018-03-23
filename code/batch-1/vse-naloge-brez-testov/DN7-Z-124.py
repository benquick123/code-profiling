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

for x, y in vsa_polja(5, 3):
    print(x, y)
########################
# Za oceno 6

def sosedov(x, y, mine):
    return sum((x == s or x == s -1 or x == s + 1) and (y == v or y == v+1 or y == v-1) for s, v in mine if not (x == s and y == v))

    """
    Vrni število sosedov polja s koordinatami `(x, y)` na katerih je mina.
    Polje samo ne šteje.

    Args:
        x (int): koordinata x
        y (int): koordinata y
        mine (set of tuple of int): koordinate min

    Returns:
        int: število sosedov
    """


def najvec_sosedov(mine, s, v):
    maks = 0
    maksx = 0
    maksy = 0
    for x, y in vsa_polja(s, v):
        s = sosedov(x, y, mine)
        if s > maks:
            maks = s
            maksx = x
            maksy = y
    return maksx, maksy

    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """


def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

    """
    Vrni množico koordinat polj brez min na sosednjih poljih. Polje samo lahko
    vsebuje mino.

    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        set of tuple: polja brez min na sosednjih poljih
    """
import collections

def po_sosedih(mine, s, v):
    slovar = {i: set() for i in range(9)}
    sosed = 0
    for x, y in vsa_polja(s, v):
        sosed = sosedov(x, y, mine)
        slovar[sosed].add((x, y))
    return slovar

    """
    Vrni slovar, katerega ključi so možna števila sosednjih polj z minami
    (torej števila od 0 do 8), vrednosti pa množice koordinat polj s toliko
    sosedami.

    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        dict: (glej zgoraj)
    """


########################
# Za oceno 7

def dolzina_poti(pot):
    dolzina = 0
    for (x1, y1), (x2, y2) in zip(pot, pot[1:]):
                dolzina += abs(x1 - x2) + abs(y1 - y2)
    return dolzina
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1:
        if y0 < y1:
            while y0 <= y1:
                if (x0, y0) in mine:
                    return False
                y0 += 1
        else:
            while y1 <= y0:
                if (x1, y1) in mine:
                    return False
                y1 += 1
    if y1 == y0:
        if x0 < x1:
            while x0 <= x1:
                if (x0, y0) in mine:
                    return False
                x0 += 1
        else:
            while x1 <= x0:
                if (x1, y1) in mine:
                    return False
                x1 += 1
    return True


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
    if len(pot) == 1 and pot[0] in mine:
        return False
    return all(varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:]))
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
    p = (polje.strip()).split(" ")
    sirina = len(p[0])
    visina = len(p)
    mine = set()
    for i, y in enumerate(p):
        for j, x in enumerate(y):
            if x == "X":
                mine.add((j, i))
    return mine, sirina, visina


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


