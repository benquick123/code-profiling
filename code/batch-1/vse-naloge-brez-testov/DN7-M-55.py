# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
from math import *

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
    return len([sosede for sosede in mine if abs(x-sosede[0]) <= 1 and abs(y-sosede[1]) <= 1 and not (x-sosede[0] == 0 and y-sosede[1] == 0)])

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
    return max((sosedov(x,y, mine),(x, y)) for x, y  in vsa_polja(s, v))[1]
    """y, x = 0, 0
    min = 0
    for m, n in vsa_polja(s, v):
        if min < sosedov(m, n, mine):
            min = sosedov(m, n, mine)
            x, y = m, n
    return (x, y)"""
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
    return {(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine) == 0}
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
    return {n:{(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine) == n} for n in range(9)}
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
    return sum(sqrt((x[0]-y[0])**2+(x[1]-y[1])**2) for x,y in zip(pot, pot[1::]))
    """rez1 = 0
    for x,y in zip(pot, pot[1::]):
        rez = sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
        rez1 +=rez
    return rez1"""
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    return False if False in [False for x,y in mine if(x in range(min(x0, x1), max(x0, x1)+1) and y1 == y0 == y) or (y in range(min(y0, y1), max(y0, y1)+1) and x1 == x0 == x)] else True

    """
    for x,y in mine:
        if x in range(min(x0, x1), max(x0, x1)+1) and y1 == y0 == y:
            return False
        if y in range(min(y0, y1), max(y0, y1)+1) and x1 == x0 == x:
            return False
    return True
"""





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

    return True if len(pot) == 0\
                   or (len(pot) == 1 and varen_premik(pot[0][0],pot[0][1],pot[0][0],pot[0][1],mine))\
                   or len(pot) > 1 and False not in (varen_premik(a[0],a[1],b[0],b[1],mine) for a,b in zip(pot, pot[1::]))\
                else False
    """
    if len(pot) == 1 and not varen_premik(pot[0][0],pot[0][1],pot[0][0],pot[0][1],mine):
        return False
    for a,b in zip(pot, pot[1::]):
        if not varen_premik(a[0],a[1],b[0],b[1],mine):
            return False
    return True"""

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
    list = set()
    y=0
    while y < len(polje.split()):
        x = 0
        while x < len(polje.split()[0]):
            if polje.split(" ")[y][x] == 'X':
                list.add((x,y))
            x+=1
        y+=1
    return list,len(polje.split()[0]),len(polje.split())

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
    x = 0
    y = 0
    smer = 0 #0 = gor, 1 = desno, 2 = dol, 3= levo
    store = [(x,y)]
    for a in ukazi.split():
        if a == "DESNO":
            if smer == 3:
                smer =-1
            smer +=1
        elif a == "LEVO":
            if smer == 0:
                smer =4
            smer -=1
        else:
            if smer == 0:
                y -= int(a)
                store.append((x,y))
            if smer == 1:
                x += int(a)
                store.append((x, y))
            if smer == 2:
                y += int(a)
                store.append((x, y))
            if smer == 3:
                x -= int(a)
                store.append((x, y))
    return store

    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """


def zapisi_pot(pot):
    koda = ""
    smer = 0  # 0 = gor, 1 = desno, 2 = dol, 3= levo
    for a,b in zip(pot, pot[1::]):
        x,y = a
        razx = a[0] - b[0]
        razy = a[1] - b[1]
        if razx < 0:
            while smer != 1:
                koda += "DESNO "
                smer+=1
                if smer > 3:
                    smer = 0
        if razx > 0:
            while smer != 3:
                koda += "DESNO "
                smer+=1
                if smer > 3:
                    smer = 0
        if razy < 0:
            while smer != 2:
                koda += "DESNO "
                smer+=1
                if smer > 3:
                    smer = 0
        if razy > 0:
            while smer != 0:
                koda += "DESNO "
                smer+=1
                if smer > 3:
                    smer = 0

        if razx:
            koda += str(abs(razx))+" "
        if razy:
            koda += str(abs(razy))+" "
    return koda






    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """


