# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
import collections

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
    i = 0
    lst = [(x,y-1),(x,y+1),(x+1,y),(x-1,y),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]
    for e in lst:
        if e in mine:
            i += 1
    return i

def najvec_sosedov(mine, s, v):
    max = 0
    rezultat = (0,0)
    for x in range(s):
        for y in range(v):
            terka = (x,y)
            stevilo = sosedov(x,y,mine)
            if stevilo > max:
                max = stevilo
                rezultat = terka
    return rezultat


def brez_sosedov(mine, s, v):
    mnozica = set()
    for x in range(s):
        for y in range(v):
            terka = (x,y)
            stevilo = sosedov(x,y,mine)
            if stevilo == 0:
                mnozica.add(terka)
    return mnozica


def po_sosedih(mine, s, v):
    slovar = collections.defaultdict(set)
    for i in range(0,9):
        slovar[i]
    for x in range(s):
        for y in range(v):
            slovar[(sosedov(x,y,mine))].add((x,y))
    return slovar




########################
# Za oceno 7

def dolzina_poti(pot):
    ...


def varen_premik(x0, y0, x1, y1, mine):
    ...


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


