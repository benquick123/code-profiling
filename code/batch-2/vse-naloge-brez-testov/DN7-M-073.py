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
import math
def sosedov(x, y, mine):
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
    a = x
    b = y
    sosedi = 0
    for x, y in mine:
        razdalja = math.sqrt(((a - x) ** 2) + (b - y) ** 2)
        if 0 < razdalja <= math.sqrt(2):
            sosedi += 1
    return sosedi

def najvec_sosedov(mine, s, v):
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """

    sosedi = 0
    a, b= 0, 0
    for x, y in vsa_polja(s, v):
        if sosedov(x, y, mine) > sosedi:
            sosedi = sosedov(x, y, mine)
            a, b= x, y
    return (a, b)

def brez_sosedov(mine, s, v):
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
    a = set()
    for x, y in vsa_polja(s, v):
        if sosedov(x, y, mine) == 0:
            koordinate = (x, y)
            a.add(koordinate)
    return a


def po_sosedih(mine, s, v):
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

    a = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(),
        6: set(), 7: set(), 8: set()}
    for x, y in vsa_polja(s, v):
        koordinate = (x, y)
        if sosedov(x, y, mine) in a:
            a[sosedov(x, y, mine)].add(koordinate)
    return a


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

    s = 0
    if pot == []:
        s = 0
    else:
        a = pot[0][0]
        b = pot[0][1]
        for x, y in pot[1:]:
            if x != a:
                s += abs(a - x)
                a = x
            if y != b:
                s += abs(b - y)
                b = y
    return s



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
    for x, y in mine:
        if x0==x1:
            if x==x0:
                if y1<=y<=y0 or y0<=y<=y1:
                    return False
        if y0==y1:
            if y==y0:
                if x1<=x<=x0 or x0<=x<=x1:
                    return False
    return True

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    if pot==[]:
        return True
    else:
        a=pot[0][0] or 0
        b=pot[0][1] or 0
        for x, y in pot:
            if varen_premik(a, b, x, y, mine)==False:
                return False
            else:
                 a, b=x, y
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
    v, s=0, 0
    x, y = 0, 0
    mnozica = set()
    for a in polje.split():
        a = list(a)
        for b in a:
            if b == "X":
                koordinate = (x, y)
                mnozica.add(koordinate)
            x += 1
            s = a.count("X") + a.count(".")
        x = 0
        y += 1
        v += 1
    return (mnozica, s, v)


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


