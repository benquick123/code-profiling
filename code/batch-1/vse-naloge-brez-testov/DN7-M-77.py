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
    sosedje = 0
    for xMina,yMina in mine:
        if sqrt((xMina - x)**2 + (yMina - y)**2) <= sqrt(2) and sqrt((xMina - x)**2 + (yMina - y)**2) != 0:
            sosedje += 1
    return sosedje


def najvec_sosedov(mine, s, v):
    najvec = 0
    koordinate = (0, 0)
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) > najvec:
                najvec = sosedov(x, y, mine)
                koordinate = (x, y)
    return koordinate


def brez_sosedov(mine, s, v):
    brez = set()
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) == 0:
                brez.add((x, y))
    return brez


def po_sosedih(mine, s, v):
    seznamSosednjihMin = { el: set() for el in range(0,9) }
    for x in range(s):
        for y in range(v):
            seznamSosednjihMin[sosedov(x,y,mine)].add((x,y))
    return seznamSosednjihMin

########################
# Za oceno 7

def dolzina_poti(pot):
    dolzina = 0
    for prvi in range(0, len(pot)-1):
        x1,y1 = pot[prvi]
        x2,y2 = pot[prvi+1]
        dolzina = dolzina + sqrt((x2-x1)**2+(y2-y1)**2)
    return dolzina



def varen_premik(x0, y0, x1, y1, mine):
    if y0 == y1:
        if x1>=x0:
            for x in range(x0, x1+1):
                if (x,y0) in mine:
                    return False
            return True
        if x0>x1:
            for x in range(x0, x1-1,-1):
                if (x,y0) in mine:
                    return False
            return True
    if x0 == x1:
        if y1>=y0:
            for y in range(y0, y1+1):
                if (x0,y) in mine:
                    return False
            return True
        if y0>y1:
            for y in range(y0, y1-1,-1):
                if (x0,y) in mine:
                    return False
            return True


def varna_pot(pot, mine):
    for x0,y0 in pot:
        for x1,y1 in pot:
            if varen_premik(x0,y0,x1,y1,mine) == False:
                return False
            x0,y0 = x1,y1
        return True
    return True



########################
# Za oceno 8

def polje_v_mine(polje):
    mine = set()
    polje = polje.strip().split(" ")
    v = 0
    for y in range(0, len(polje)):
        v += 1
        for x in range(0,len(polje[y])):
            if polje[y][x] == "X":
                mine.add((x,y))
    return (mine,len(polje[y]),v)




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


