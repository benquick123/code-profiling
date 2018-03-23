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
    mineST=0
    for xM,yM in mine:
        if (abs(xM-x)+abs(yM-y))<=2 and (abs(xM-x)==1 or abs(yM-y)==1):
            mineST+=1
    return mineST

def najvec_sosedov(mine, s, v):
    sosedi=0
    kor=(0,0)
    for xM in range(s):
        for yM in range(v):
            if sosedov(xM,yM,mine)>sosedi:
                kor=xM,yM
                sosedi=sosedov(xM,yM,mine)
    return kor


def brez_sosedov(mine, s, v):
    kor = set()
    for xM in range(s):
        for yM in range(v):
            if sosedov(xM, yM, mine) ==0:
                kor.add((xM, yM))

    return kor


import collections
def po_sosedih(mine, s, v):
    knj=collections.defaultdict(set)
    for st in range(9):
        knj[st] = set()
        for xM in range(s):
            for yM in range(v):
                if sosedov(xM, yM, mine) == st:
                    knj[st].add((xM,yM))
    return dict(knj)


########################
# Za oceno 7

def dolzina_poti(pot):
   K1=pot
   K2=pot[1:]
   totalPot=0
   for i in range(len(K2)):
        x1,y1=K1[i]
        x2,y2 =K2[i]
        totalPot+=abs(x1-x2)+abs(y1-y2)
   return totalPot

def dejanska_pot(x0, y0, x1, y1):
    pot = []
    negx = 1
    negy = 1
    if y0 > y1:
        negy = -1
    if x0 > x1:
        negx = -1
    for i in range(x0, x1 , negx):
        pot.append((i, y0))

    for i in range(y0, y1 , negy):
        pot.append((x1, i))
    pot.append((x0,y0))
    pot.append((x1, y1))
    return pot

def varen_premik(x0, y0, x1, y1, mine):
    pot=dejanska_pot(x0, y0, x1, y1)
    for mina in mine:
        if mina in pot:
            return False
    return True





def varna_pot(pot, mine):
   for i in range(0,len(pot)-1):
       x0,y0=pot[i]
       x1,y1=pot[i+1]
       if not varen_premik(x0, y0, x1, y1, mine):
           return False
   if len(pot)==1:
       x, y = pot[0]
       if not varen_premik(x, y, x, y, mine):
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


