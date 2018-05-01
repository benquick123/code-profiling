__author__ = 'Haris'
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
    output=0
    for par in mine:
        if (x+1,y) == par:
            output+=1
        elif (x-1,y) == par:
            output+=1
        elif (x+1,y) == par:
            output+=1
        elif (x+1,y+1) == par:
            output+=1
        elif (x+1,y-1) == par:
            output+=1
        elif (x-1,y+1) == par:
            output+=1
        elif (x-1,y-1) == par:
            output+=1
        elif (x,y+1) == par:
            output+=1
        elif (x,y-1) == par:
            output+=1
    return output

def najvec_sosedov(mine, s, v):
    najvec_x=najvec_y=naj_sosedov=0
    for x in range(0,s):
        for y in range(0,v):
            if sosedov(x,y,mine)>naj_sosedov:
                naj_sosedov=sosedov(x,y,mine)
                najvec_x=x
                najvec_y=y
    return (najvec_x,najvec_y)

def brez_sosedov(mine, s, v):
    output=set()
    for x in range(0,s):
        for y in range(0,v):
            if sosedov(x,y,mine)==0:
                par=(x,y)
                output.add(par)
    return output



def stevilo_sosedov(mine,s,v,p):
    output = set()
    for x in range(0, s):
        for y in range(0, v):
            if sosedov(x, y, mine) == p:
                par = (x, y)
                output.add(par)
    return output

def po_sosedih(mine, s, v):
    output = {}
    for element in range(0, 9):
        output[element] = stevilo_sosedov(mine, s, v, element)
    return output

########################
# Za oceno 7

def dolzina_poti(pot):
    output=0
    for (a,b),(c,d) in zip(pot,pot[1:]):
        output+=abs(a-c+b-d)
    return output



def varen_premik(x0, y0, x1, y1, mine):
    for x_mine,y_mine in mine:
        return 6

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


