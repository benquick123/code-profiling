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

    stevec = 0
    for mina in mine:
        if -1 <= x-mina[0] <= 1 and -1 <= y-mina[1] <=1 and (x,y) != mina:
            stevec+=1
    return stevec




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

    maks = 0
    k1 = k2 = 0
    for (x, y) in vsa_polja(s, v):
        if sosedov(x, y, mine)>maks:
            maks = sosedov(x,y, mine)
            k1 = x
            k2 = y
    return k1, k2



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

    m = set()
    for x,y in vsa_polja(s, v):
        if sosedov(x,y, mine) == 0:
            m.add((x,y))

    return m



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
    d={}
    i = 0
    while i < 9:
        d[i]=set()
        i+=1

    for x,y in vsa_polja(s,v):
        d[sosedov(x, y, mine)].add((x, y))

    return d


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

    vsota=0
    i=0
    j=1
    while j<len(pot):
        x1, y1 = pot[i]
        x2, y2 = pot[j]
        vsota += sqrt((x2-x1)**2 + (y2-y1)**2)
        i+=1
        j+=1

    return vsota



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
    if x0 == x1:
        ky0 = y0 #kopiji koordinat y0, y1
        ky1 = y1
        while True:
            if (x0, ky0) in mine:
                return False
            if ky0>ky1:
                ky0-=1
            if ky0<ky1:
                ky0+=1
            if ky0 == ky1:
                if (x0, ky0) in mine:
                    return False
                else:
                    break

    if y0 == y1:
        kx0 = x0 #kopiji koordinat x0, x1
        kx1 = x1
        while True:
            if (kx0, y0) in mine:
                return False
            if kx0>kx1:
                kx0-=1
            if kx0<kx1:
                kx0+=1
            if kx0 == kx1:
                if (kx0, y0) in mine:
                    return False
                else:
                    break

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
    if len(pot)==1:
        x, y = pot[0]
        if (x, y) in mine:
            return False

    j=1
    i=0
    while j<len(pot):
        x0, y0 = pot[i]
        x1, y1 = pot[j]
        if not varen_premik(x0, y0, x1, y1, mine):
            return False
        j+=1
        i+=1

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

    x = 0
    y = 0
    m = set()
    for znak in polje:
        if znak == "X":
            m.add((x,y))
        x+=1

        if znak == " ":
            y+=1
            x=0
    s = 0
    for znak in polje:
        if znak == " ":
            break
        s+=1
    v=ceil(len(polje)/(s+1))
    terka = (m, s, v)
    return terka




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


