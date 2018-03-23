from collections import *
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
    s= []

    a=(x+1,y)
    b=(x-1,y)
    c=(x - 1, y-1)
    d=(x + 1, y-1)
    e=(x , y-1)
    f=(x-1 , y+1)
    g=(x , y+1)
    h=(x +1, y+1)
    s.append(a)
    s.append(b)
    s.append(c)
    s.append(d)
    s.append(e)
    s.append(f)
    s.append(g)
    s.append(h)
    stevilo=0
    for x1, y1 in s:
        for (x2, y2) in mine:
            if (x1, y1) == (x2, y2):
                stevilo += 1
    return stevilo

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



def najvec_sosedov(mine, s , v):

    naj = 0
    najkoord=(0,0)
    for x,y in vsa_polja (s, v):
        x1= x
        y1= y
        if sosedov(x1 , y1 , mine) > naj:
            najkoord = (x1 , y1)
            naj = sosedov(x1 , y1, mine)

    return najkoord


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
    p = set()

    for x, y in vsa_polja(s, v):
        y1 =y
        x1= x
        if sosedov(x1, y1, mine) == 0:
            o= (x,y)
            p.add(o)
    return p



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
    p = [[],[],[],[],[],[],[],[],[]]
    for i in range(0,9):
        for x, y in vsa_polja(s, v):
             if sosedov(x, y, mine)== i:
                 p[i].append((x,y))


    return {i:{(x,y)for (x,y) in p[i] }for i in range (0,9)}





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
    path=0
    for x,y in pot:
        prevx= x
        prevy=y
        break

    for x,y in pot:

        path += abs(x - prevx)
        path += abs(y - prevy)
        prevx=x
        prevy=y


    return path



    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
     s=[]
     if x0== x1 and y0== y1:
         se = [x0,y0]
         s.append(se)

     if x0 > x1:
         se=[x0,y0]
         s.append(se)
         while x0!= x1:
             x0= x0-1
             se = [x0, y0]
             s.append(se)



     if x0 < x1:
         se = [x0,y0]
         s.append(se)
         while x0!= x1:
             x0= x0+1
             se = [x0,y0]
             s.append(se)

     if y0 < y1:
         se = [x0,y0]
         s.append(se)
         while y0!= y1:
              y0= y0+1
              se = [x0, y0]
              s.append(se)

     if y0 > y1:
         se = [x0,y0]
         s.append(se)
         while y0 != y1:
             y0 = y0 - 1
             se=[x0,y0]
             s.append(se)



     for x5, y5 in s:
         for x,y in mine:
             if x == x5 and y == y5:
                 return False

     return True





def varna_pot(pot, mine):
    for x,y in pot:
        prevx= x
        prevy= y
        break

    for x , y in pot:
        if varen_premik(prevx, prevy, x, y, mine)!=True:
            return False
        prevx=x
        prevy=y
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


