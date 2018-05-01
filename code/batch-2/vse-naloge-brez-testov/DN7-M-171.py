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
    return sum(1 for terka in mine if terka == (x-1,y-1) in mine or terka == (x,y-1) in mine or terka == (x+1,y-1) in mine or terka == (x-1,y) in mine or terka == (x+1,y) in mine or terka == (x-1,y+1) in mine or terka == (x,y+1) in mine or terka == (x+1,y+1) in mine)

def najvec_sosedov(mine, s, v):
    return max({(x,y): sosedov(x,y,mine) for y in range(v) for x in range(s)}, key={(x,y): sosedov(x,y,mine) for y in range(v) for x in range(s)}.get)

def brez_sosedov(mine, s, v):
    return set((x,y)for y in range(v) for x in range(s) if sosedov(x,y,mine) == 0)

def po_sosedih(mine, s, v):
    return ({i: set((x, y) for y in range(v) for x in range(s) if sosedov(x, y, mine) == i) for i in range(0, 9)})


########################
# Za oceno 7

def dolzina_poti(pot):
    koliko = 0
    if pot != []:
        xp,yp = pot[0]
        for x,y in pot:
            if (x,y) != (xp,yp):
                raz = sqrt((xp - x) ** 2 + (yp - y) ** 2)
                xp,yp = x,y
                koliko += raz
        return koliko
    return 0



def varen_premik(x0, y0, x1, y1, mine):
    if (x0,y0) in mine:
        return False
    if x0 < x1:
        for x in range(x0,x1+1):
            if (x,y0) in mine:
                return False
    if x0 > x1:
        for x in range(x1,x0+1):
            if (x,y0) in mine:
                return False
    if y0 < y1:
        for y in range(y0,y1+1):
            if (x0,y) in mine:
                return False
    if y0 > y1:
        for y in range(y1,y0+1):
            if (x0,y) in mine:
                return False
    return True


def varna_pot(pot, mine):
    if pot != []:
        prej = None
        for kam in pot:
            if prej == None:
                prej = kam
                if kam in mine:
                    return False
            else:
                x0,y0 = prej
                x1,y1 = kam
                preveri = varen_premik(x0, y0, x1, y1, mine)
                prej = kam
                if preveri == False or kam in mine:
                    return False
    return True


########################
# Za oceno 8

def polje_v_mine(polje):
    seznam = polje.split()
    mnozica = set()
    visina = 0
    sirina = None
    for vrstica in seznam:
        sirina = len(vrstica)
        i = 0
        for znak in vrstica:
            if znak == "X":
                mnozica.add((i,visina))
            i += 1
        visina += 1
    return (mnozica,sirina,visina)



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


