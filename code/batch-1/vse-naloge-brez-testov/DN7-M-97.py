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
    stevec = 0
    primerjava = sqrt(2)
    for tocke in mine:
        x2, y2 = tocke
        razdalja = sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
        if razdalja <= primerjava and razdalja != 0:
            stevec = stevec + 1
    return (stevec)


def najvec_sosedov(mine, s, v):
    x = 0
    najvec_bomb = 0
    tocka = (0,0)
    while(x < s):
        y = 0
        while(y < v):
            if(najvec_bomb < sosedov(x,y,mine)):
                najvec_bomb = sosedov(x,y,mine)
                tocka = x,y
            y += 1
        x += 1
    return(tocka)


def brez_sosedov(mine, s, v):
    x = 0
    seznam =set()
    tocka = (0,0)
    while (x < s):
        y = 0
        while (y < v):
            if (sosedov(x,y,mine)==0):
                seznam.add((x,y))
            y += 1
        x += 1
    return (seznam)


def po_sosedih(mine, s, v):
    slovar = {0:set(),
              1:set(),
              2: set(),
              3: set(),
              4: set(),
              5: set(),
              6: set(),
              7: set(),
              8: set(),}
    x = 0
    najvec_bomb = 0
    tocka = (0, 0)
    while (x < s):
        y = 0
        while (y < v):
            slovar[sosedov(x,y,mine)].add((x,y))
            y += 1
        x += 1
    return (slovar)

########################
# Za oceno 7


def dolzina_poti(pot):
    dolzina = 0
    for (x1,y1),(x2,y2) in zip(pot,pot[1:]):
           vrednost = abs(x1 - x2) + abs(y1 - y2)
           dolzina = dolzina + vrednost
    return(dolzina)

def varen_premik(x0,y0,x1,y1,mine):
    x0basis =x0
    y0basis =y0
    x1basis =x1
    y1basis =y1
    for vse in mine:
        MineX,MineY = vse
        x0 = x0basis
        y0 = y0basis
        x1 =x1basis
        y1 = y1basis
        if(x0 == x1):
            PrimerY1 = y1 +1
            while(y0 != PrimerY1 and y0 < 10):
                if((x0,y0) == (MineX,MineY)):
                    return(False)
                    break
                if(y0 > y1):
                    y0 -= 1
                else:
                    y0 += y0
        if(y0 == y1):
            PrimerX1 = x1 +1
            while(x0 != PrimerX1 and x0 < 10):
                if((x0,y0) == (MineX,MineY)):
                    return(False)
                    break
                if(x0 > x1):
                    x0 -= 1
                else:
                    x0 += 1
    return(True)

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


