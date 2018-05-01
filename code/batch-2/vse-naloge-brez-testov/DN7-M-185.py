from math import *
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
    r = 0
    for a,b in mine:
        if abs(x-a) <= 1 and abs(y-b) <= 1 and (a,b) != (x,y):
            r = r + 1
    return r
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
    naj = (0, 0)
    if mine == set():
        return naj

    for y in range(v):
        for x in range(s):
            if sosedov(x,y,mine) > sosedi:
                sosedi = sosedov(x,y,mine)
                naj = (x,y)

    return naj

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
    xs = set()
    for y in range(v):
        for x in range(s):
            if sosedov(x, y, mine) == 0:
                xs.add((x,y))
    return xs
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

    xs = {i: set() for i in range(9)}
    for y in range(v):
        for x in range(s):
            xs[sosedov(x,y,mine)].add((x,y))

    return xs
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
    sestevk=0
    i = 0
    while i < (len(pot) - 1):
        x, y = pot[i]
        x0, y0 = pot[i + 1]
        if x != x0:
            sestevk += abs(x - x0)
        if y != y0:
            sestevk += abs(y - y0)
        i += 1
    return sestevk
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
    if x0==x1 and y0 == y1:
        return False

    elif x0!=x1:
        if x1 > x0:
            while x1 >= x0:
                if (x0, y0) in mine:
                    return False
                else:
                    x0+=1
        elif x0 > x1:
            while x0 >= x1:
                if (x0, y0) in mine:
                    return False
                else:
                    x0-=1
        else:
            return True
    elif y0!=y1:
        if y1 > y0:
            while y1 >= y0:
                if (x0, y0) in mine:
                    return False
                else:
                    y0+=1
        elif y0 > y1:
            while y0 >= y1:
                if (x0, y0) in mine:
                    return False
                else:
                    y0-=1
        else:
            return True
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
    if len(pot) == 1 and (pot[0] in mine):

        return False
    i = 0
    while i < len(pot)-1:
        x0,y0 = pot[i]
        x1,y1 = pot[i+1]
        if varen_premik(x0,y0,x1,y1,mine):
            i+=1
        else:
            return False
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


