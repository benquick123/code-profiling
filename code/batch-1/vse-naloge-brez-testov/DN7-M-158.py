import collections
import math
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

    i=0
    for yTMP in range(y-1,y+2):
        for xTMP in range(x-1,x+2):
            if (xTMP,yTMP) in mine-{(x,y)}:
                i=i+1
    return i



def najvec_sosedov(mine, s, v):
    i = 0
    najMin=0
    xMax=0
    yMax=0
    for y in range(0,v):
        for x in range(0,s):
            i=sosedov(x,y,mine)
            if i > najMin:
                najMin=i
                xMax=x
                yMax=y
    return (xMax,yMax)



def brez_sosedov(mine, s, v):

    mnoBrez=set()
    for y in range(0,v):
        for x in range(0,s):
           i=sosedov(x,y,mine)
           if i == 0:
               mnoBrez.add((x,y))
    return mnoBrez




def po_sosedih(mine, s, v):

    slov= collections.defaultdict(set)
    for nastavi in range(0, 9):
        slov[nastavi] = set()
    for y in range(0,v):
        for x in range(0,s):
            i = sosedov(x, y, mine)
            slov[i].add((x,y))
    return slov


########################
# Za oceno 7

def dolzina_poti(pot):

    dolPot=0
    for (x, y), (x2, y2) in zip(pot, pot[1:]):
        dolPot+=math.sqrt((x - x2)**2 + (y - y2)**2)
    return int(dolPot)




def varen_premik(x0, y0, x1, y1, mine):

    if x0 == x1:
        if y0 > y1:
            tmp=y0
            y0=y1
            y1=tmp
        for vred in range(y0,y1+1):
            if (x0,vred) in mine:
                return False
        return True
    else:
        if x0 > x1:
            tmp=x0
            x0=x1
            x1=tmp
        for vred in range(x0,x1+1):
            if (vred,y0) in mine:
                return False
        return True



def varna_pot(pot, mine):

    if len(pot) == 1:
        if pot[0] in mine:
            return False
        return True
    for (x, y), (x2, y2) in zip(pot, pot[1:]):
        if not varen_premik(x, y, x2, y2, mine):
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
    listic=polje.split()
    s=len(listic[0])
    y=0
    mnozica=set()
    for vred in listic:
        for vred2, char in enumerate(vred):
            if char == "X":
                mnozica.add((vred2,y))
        y+=1
    return mnozica,s,y


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


