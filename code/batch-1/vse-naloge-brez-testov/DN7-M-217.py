# -*- coding: utf-8 -*-
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
    return len(set([(xa, ya) for xa in range(x - 1, x + 2) for ya in range(y - 1, y + 2) if ((xa, ya) != (x, y))]).intersection(mine))
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
    return [(x, y) for x, y in vsa_polja(s, v) if(sosedov(x, y, mine) >= max(set([sosedov(xx, yy, mine) for xx, yy in vsa_polja(s, v)])))][0]
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
    return set([(x, y) for x, y in vsa_polja(s, v) if (sosedov(x, y, mine) == 0)])
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
    return {i: set([(x, y) for x, y in vsa_polja(s, v) if (sosedov(x, y, mine) == i)]) for i in range(0, 9)}
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
    return sum([abs(pot[i][0] - abs(pot[i - 1][0])) for i in range(1, len(pot)) if ((i - 1 <= len(pot)))] + [abs(pot[i][1] - abs(pot[i - 1][1])) for i in range(1, len(pot)) if ((i - 1 <= len(pot)))])
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    return (set([(xi,yi) for xi in range(x0,x1+1) for yi in range(y0,y1+1)] + [(xi,yi) for xi in range(x0,x1-1,-1) for yi in range(y0,y1- 1,-1) if(y1<y0) or (x1<x0)]).intersection(set(mine))==set())
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
    return False not in (set([varen_premik(pot[x - 1][0], pot[x - 1][1], pot[x][0], pot[x][1], mine) for x in range(1, len(pot)) if(len(pot) > 1)] + [False for iks, ips in pot if ((iks, ips) in mine)]))
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
    rows = polje.split(" ")
    visina = len(rows)
    sirina = len(rows[0])
    x = 0
    y = 0
    mines = set()
    for row in rows:
        row = list(row)
        x = 0
        for letter in row:
            if (letter == "X"):
                mines.add((x, y))
            x = x + 1
        y = y + 1

    return (mines, sirina, visina)
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
    pot = [(0, 0)]
    sx = 0
    sy = 0
    ipsmin = True
    ipspl = False
    iksmin = False
    ikspl = False
    ukazi_s = ukazi.splitlines()
    for ukaz in ukazi_s:
        if (ukaz == "DESNO"):
            if (ipsmin == True):
                ikspl = True
                ipsmin = False
                continue
            if (ikspl == True):
                ipspl = True
                ikspl = False
                continue
            if (ipspl == True):
                iksmin = True
                ipspl = False
                continue
            if (iksmin == True):
                ipsmin = True
                iksmin = False
                continue
        if (ukaz == "LEVO"):
            if (ipsmin == True):
                iksmin = True
                ipsmin = False
                continue
            if (iksmin == True):
                ipspl = True
                iksmin = False
                continue
            if (ipspl == True):
                ikspl = True
                ipspl = False
                continue
            if (ikspl == True):
                ipsmin = True
                ikspl = False
                continue
        if (ukaz in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            if (ikspl == True):
                sx += int(ukaz)
            if (iksmin == True):
                sx -= int(ukaz)
            if (ipspl == True):
                sy += int(ukaz)
            if (ipsmin == True):
                sy -= int(ukaz)
            pot.append((sx, sy))
    return pot
    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """


def zapisi_pot(pot):
    ukazi = []
    ipsmin = True
    ipspl = False
    iksmin = False
    ikspl = False
    for i in range(1, len(pot)):
        if (pot[i - 1][0] == pot[i][0]) and (pot[i - 1][1] < pot[i][1]):
            if (ikspl == True):
                ukazi.append("DESNO")
            if (iksmin == True):
                ukazi.append("LEVO")
            if (ipsmin == True):
                ukazi.append("DESNO")
                ukazi.append("DESNO")
            ikspl = False
            iksmin = False
            ipsmin = False
            ipspl = True
            ukazi.append(str(pot[i][1] - pot[i - 1][1]))
        if (pot[i - 1][0] == pot[i][0]) and (pot[i - 1][1] > pot[i][1]):
            if (ikspl == True):
                ukazi.append("LEVO")
            if (iksmin == True):
                ukazi.append("DESNO")
            if (ipspl == True):
                ukazi.append("DESNO")
                ukazi.append("DESNO")
            ikspl = False
            iksmin = False
            ipsmin = True
            ipspl = False
            ukazi.append(str(pot[i - 1][1] - pot[i][1]))
        if (pot[i - 1][1] == pot[i][1]) and (pot[i - 1][0] < pot[i][0]):
            if (iksmin == True):
                ukazi.append("DESNO")
                ukazi.append("DESNO")
            if (ipspl == True):
                ukazi.append("LEVO")
            if (ipsmin == True):
                ukazi.append("DESNO")
            ikspl = True
            iksmin = False
            ipsmin = False
            ipspl = False
            ukazi.append(str(pot[i][0] - pot[i - 1][0]))
        if (pot[i - 1][1] == pot[i][1]) and (pot[i - 1][0] > pot[i][0]):
            if (ikspl == True):
                ukazi.append("DESNO")
                ukazi.append("DESNO")
            if (ipspl == True):
                ukazi.append("DESNO")
            if (ipsmin == True):
                ukazi.append("LEVO")
            ikspl = False
            iksmin = True
            ipsmin = False
            ipspl = False
            ukazi.append(str(pot[i - 1][0] - pot[i][0]))

    return "\n".join(ukazi)
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """


