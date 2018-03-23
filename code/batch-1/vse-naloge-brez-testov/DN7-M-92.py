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
    stevec = 0
    for x2 in range(x-1, x+2):
        for y2 in range(y-1, y+2):
            if (x2, y2) in mine and (x2, y2) != (x, y):
                stevec += 1
    return stevec

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
    maks = [(0, 0), 0]
    for x in range(s):
        for y in range(v):
            trenutno = sosedov(x, y, mine)
            if trenutno > maks[1]:
                maks[1] = trenutno
                maks[0] = (x, y)
    return maks[0]
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
    osamljeni = set()
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) == 0:
                osamljeni.add((x, y))
    return osamljeni
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


def po_sosedih(mine, s, v):
    from collections import defaultdict
    slovar = {st: set() for st in range(9)}

    for x in range(s):
        for y in range(v):
            sosednjih = sosedov(x, y, mine)
            slovar[sosednjih].add((x, y))
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
    razdalja = 0
    for (x, y), (xp, yp) in zip(pot, pot[1:]):
        razdalja += abs(xp - x) + abs(yp - y)
    return razdalja
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    polja = set()
    if x0 != x1:
        if x0 - x1 == 0:
            smer = 1
        else:
            smer = (x1 - x0) // abs(x1 - x0)
        for i in range(0, abs(x1 - x0) + 1):
            polja.add((x0 + i * smer, y0))
    else:
        if y0 - y1 == 0:
            smer = 1
        else:
            smer = (y1 - y0) // abs(y1 - y0)
        for i in range(0, abs(y1 - y0) + 1):
            polja.add((x0, y0 + i * smer))

    if polja & mine != set():
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
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if not varen_premik(x0, y0, x1, y1, mine):
            return False
    if len(pot) == 0:
        return True
    elif pot[0] in mine:
        return False
    return True
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
    lokacije = set()
    vrstice = polje.split()
    s = len(vrstice)
    v = len(vrstice[0])
    for i in range(s):
        for j in range(v):
            if vrstice[i][j] == "X":
                lokacije.add((j, i))
    return (lokacije, v, s)
    
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


