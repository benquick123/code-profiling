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
    stevec=0
    if (x-1, y-1) in mine:
        stevec+=1
    if (x-1, y) in mine:
        stevec+=1
    if (x-1, y+1) in mine:
        stevec+=1
    if (x, y-1) in mine:
        stevec+=1
    if (x, y+1) in mine:
        stevec+=1
    if (x+1, y-1) in mine:
        stevec+=1
    if (x+1, y) in mine:
        stevec+=1
    if (x+1, y+1) in mine:
        stevec+=1
    return stevec


def najvec_sosedov(mine, s, v):
    trenutni_rezultat=0
    koordinate=(0,0)
    for x in range(s):
        for y in range(v):
            stevilo_min=sosedov(x,y,mine)
            if stevilo_min>trenutni_rezultat:
                trenutni_rezultat=stevilo_min
                koordinate=(x,y)
    return koordinate



def brez_sosedov(mine, s, v):
    rezultati=set()
    for x in range(s):
        for y in range(v):
            if sosedov(x,y,mine)==0:
                rezultati.add((x,y))
    return rezultati

import collections
import math

def po_sosedih(mine, s, v):
    slovar=collections.defaultdict(set)
    for x in range(9):
        slovar[x]=set()
    for x in range(s):
        for y in range(v):
            z=sosedov(x,y,mine)
            slovar[z].add((x,y))
    return slovar



########################
# Za oceno 7

def dolzina_poti(pot):
    for x, y in pot:
        a=x
        b=y
        break
    dolzina=0
    for x, y in pot:
        if x!=a:
            pot1=a-x
            pot1=abs(pot1)
            dolzina=dolzina+pot1
        if y!=b:
            pot2=b-y
            pot2=abs(pot2)
            dolzina=dolzina+pot2
        a=x
        b=y
    return dolzina




def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1:
        if y0<y1:
            for a in range(y0,y1+1):
                if (x0,a) in mine:
                    return False
        if y0>y1:
            for a in range(y1,y0+1):
                if (x0,a) in mine:
                    return False
    if y0 == y1:
        if x0<x1:
            for a in range(x0,x1+1):
                if (a,y0) in mine:
                    return False
        if x0>x1:
            for a in range(x1,x0+1):
                if (a,y0) in mine:
                    return False
    if x0==x1==y0==y1:
        return False
    return True


def varna_pot(pot, mine):
    for x,y in pot:
        if (x,y) in mine:
            return False
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if varen_premik(x0,y0,x1,y1,mine) == False:
            return False
    return True



########################
# Za oceno 8

def polje_v_mine(polje):
    x = polje.split()
    visina = len(x)
    sirina = 0
    koordinate = []
    for a in enumerate(x):
        sirina =len(a[1])
        for i,j in list(enumerate(a[1])):
            if j=="X":
                koordinate.append((i, a[0]))
    return set(koordinate), sirina, visina



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


