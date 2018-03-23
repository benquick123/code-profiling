# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.

def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

from math import *

def sosedov(x, y, mine):
    sosed = 0
    xkoor = [x-1, x, x+1]
    ykoor = [y-1, y, y+1]
    preveri = [(a, b) for a in xkoor for b in ykoor if a != x or b != y]
    for polje in preveri:
        if polje in mine:
            sosed +=1
    return sosed



def najvec_sosedov(mine, s, v):
    najvec_min = 0
    koor_najvec = ()
    for x, y in vsa_polja(s, v):
        nekaj = sosedov(x, y, mine)
        if nekaj >= najvec_min:
            najvec_min = nekaj
            koor_najvec = (x, y)
    return koor_najvec



def brez_sosedov(mine, s, v):
    polja_brez_min = set()
    for x, y in vsa_polja(s, v):
        ima_mine = sosedov(x, y, mine)
        if ima_mine == 0:
            polje = (x, y)
            polja_brez_min.add(polje)
    return polja_brez_min


from collections import *

def po_sosedih(mine, s, v):
    slovar_sosedov = {8: set(), 7: set(), 6: set(), 5: set(), 4: set(), 3: set(), 2: set(), 1: set(), 0: set(),}
    for x, y in vsa_polja(s, v):
        stevilo = sosedov(x, y, mine)
        polje = (x, y)
        slovar_sosedov[stevilo].add(polje)
    return slovar_sosedov




########################
# Za oceno 7

def dolzina_poti(pot):
    dolzina = 0
    if not pot:
        return 0
    x1, y1 = pot[0]
    for x, y in pot:
        dolzina += abs(x1 - x) + abs(y1 - y)
        x1, y1 = x, y
    return dolzina



def varen_premik(x0, y0, x1, y1, mine):
    koraki = [(x0, y0)]
    while x0 != x1:
        if x0 > x1:
            x0 -= 1
            koraki += [(x0, y0)]
        else:
            x0 += 1
            koraki += [(x0, y0)]
    while y0 != y1:
        if y0 > y1:
            y0 -= 1
            koraki += [(x0, y0)]
        else:
            y0 += 1
            koraki += [(x0, y0)]
    for pozicija in koraki:
        if pozicija in mine:
            return False
    return True




def varna_pot(pot, mine):
    dvojice = zip(pot, pot[1:])
    varno = 0
    for nekaj in pot:
        if nekaj in mine:
            return False
    for (x0, y0), (x1, y1) in dvojice:
        if not varen_premik(x0, y0, x1, y1, mine):
            return False
    return True



########################
# Za oceno 8

def polje_v_mine(polje):
    kje_so_mine = set()
    s = polje.split(" ")
    if s[-1] == "":
        del s[-1]
    y = 0
    for vrstica in s:
        for i in range(len(vrstica)):
            if vrstica[i] == "X":
                x = i
                mina = (x, y)
                kje_so_mine.add(mina)
        y += 1


    return kje_so_mine, len(vrstica) or 1, y






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


