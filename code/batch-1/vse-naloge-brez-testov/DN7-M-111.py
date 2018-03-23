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
    from math import sqrt
    i = 0
    for x1, y1 in mine:
        dist = sqrt((x - x1) ** 2 + (y - y1) ** 2)
        if dist == 1 or dist == sqrt(2):
            i += 1
    return i

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
    naj = 0
    polje = (0, 0)
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) > naj:
                naj = sosedov(x, y, mine)
                polje = (x, y)
    return polje

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
    mnozica = set()
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) == 0:
                mnozica.add((x, y))
    return mnozica

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
    d = {}
    for a in range(9):
        mnozica = set()
        for x in range(s):
            for y in range(v):
                if sosedov(x, y, mine) == a:
                    mnozica.add((x, y))
        d[a] = mnozica
    return d

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
    vsota = 0
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if x1 != x0:
            vsota += abs(x1 - x0)
        if y1 != y0:
            vsota += abs(y1 - y0)
    return vsota

    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    varno = True
    if (x0, y0) in mine:
        varno = False
    if x0 < x1:
        while x0 <= x1:
            if (x0,y0) in mine:
                varno = False
            x0 += 1
        return varno
    if x0 > x1:
        while x0 >= x1:
            if (x0,y0) in mine:
                varno = False
            x0 -= 1
        return varno
    if y0 < y1:
        while y0 <= y1:
            if (x0,y0) in mine:
                varno = False
            y0 += 1
        return varno
    if y0 > y1:
        while y0 >= y1:
            if (x0,y0) in mine:
                varno = False
            y0 -= 1
        return varno
    return varno

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
    #i am so sorry
    """


def varna_pot(pot, mine):
    list = []
    for a in pot:
        if a in mine:
            return False
    for i in range(len(pot)):
        x0, y0 = pot[i]
        if i + 1 < len(pot):
            x1, y1 = pot[i+1]
            list.append(varen_premik(x0, y0, x1, y1, mine))
    return all(list)

#boy im bad at this
#how the hell are you supposed to do these in one line

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
    mnozica = set()
    i = 0
    for a in polje.split():
        j = 0
        for b in a:
            if b == "X":
                mnozica.add((j, i))
            j += 1
        i += 1
    return (mnozica, j, i)

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


