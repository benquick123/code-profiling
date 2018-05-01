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
from math import sqrt

def sosedov(x, y, mine):
    return len([(x1,y1) for x1,y1 in mine
                if 0 < sqrt((x1 - x) ** 2 + (y1 - y) ** 2) < 2])

def najvec_sosedov(mine, s, v):
    maxsos = 0
    koor = (0, 0)
    for x, y in vsa_polja(s, v):
        if maxsos < sosedov(x, y, mine):
            maxsos = sosedov(x, y, mine)
            koor = (x, y)
    return koor


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
    return set((x, y) for (x,y) in vsa_polja(s, v) if sosedov(x,y,mine) == 0)

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

from collections import defaultdict
def po_sosedih(mine, s, v):
    imenik = {}
    for keys in range(9):
        imenik.setdefault(keys, set())
    for x, y in vsa_polja(s, v):
        imenik[sosedov(x, y, mine)].add((x, y))
    return imenik


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
    return sum([sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2) for (x0, y0),(x1, y1) in zip(pot, pot[1:])])
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    for x,y in mine:
        if x0 == x1 == x and  (y0 <= y <= y1 or y0 >= y >= y1):
            return False
        elif y0 == y1 == y and (x0 <= x <= x1 or x0 >= x >= x1):
            return False
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
    varnost = []

    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
            varnost.append(varen_premik(x0,y0,x1,y1, mine))
    for x0,y0 in pot:
        if len(pot) == 1:
            varnost.append(varen_premik(x0,y0,x0,y0,mine))
    return all(varnost)
    #return all([varen_premik(x0,y0,x1,y1, mine) for (x0,y0),(x1,y1) in zip(pot, pot[1:])])


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
    mine = set()
    v = len(polje.split())
    for iv,vrstica in enumerate(polje.split()):
        for i,e in enumerate(vrstica):
            if e == 'X':
                mine.add((i,iv))
    s = len(vrstica)

    return mine, s, v



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


