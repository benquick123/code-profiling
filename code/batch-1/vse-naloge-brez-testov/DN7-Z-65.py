# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6
import math

def sosedov(x, y, mine):
    return len([(k1,k2) for (k1, k2) in mine if math.sqrt((x - k1) ** 2 + (y - k2) ** 2) <= math.sqrt(2) and math.sqrt((x - k1) ** 2 + (y - k2) ** 2) != 0])

def najvec_sosedov(mine, s, v):
    return max({(x,y): sosedov(x,y,mine) for (x,y) in vsa_polja(s,v)}, key={(x,y): sosedov(x,y,mine) for (x,y) in vsa_polja(s,v)}.get)

def brez_sosedov(mine, s, v):
    return {(x,y) for (x,y) in vsa_polja(s,v) if sosedov(x,y,mine)==0}

def po_sosedih(mine, s, v):
    return {i: {(x,y) for (x,y) in vsa_polja(s,v) if sosedov(x,y,mine)==i}for i in range(9)}


########################
# Za oceno 7
def dolzina_poti(pot):
    return sum((abs(pot[i][0] - pot[i - 1][0])) + (abs(pot[i][1] - pot[i - 1][1])) for i in range (1, len(pot)))



def varen_premik(x0, y0, x1, y1, mine):
    return not len([(k1, k2) for k1, k2 in mine if (x1 == x0 == k1 and (y0 <= k2 <= y1 or y1 <= k2 <= y0) or
                                                    (y1 ==y0 == k2 and (x0 <= k1 <= x1 or x1 <= k1 <= x0)))]) > 0

def varna_pot(pot, mine):
    return all(varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot[:1] + pot, pot))

# Za oceno 8
def polje_v_mine(polje):
    polja=set()
    v = len(polje.split())
    s=len(polje.split()[0])
    for y in range(v):
        for x in range(len(polje.split()[y])):
           if polje.split()[y][x]=="X":
               polja.add((x, y))
    return (polja, s, v)


########################
# Za oceno 10
from math import*

def preberi_pot(ukazi):
    pot=[(0,0)]
    nahajalisce=(0, 0)
    smer=(0,-1)
    kot=atan((smery- y)/(smerx- x))
    for e in ukazi.split():
        if e=="DESNO":
            kot+=radians(90)
        elif e=="LEVO":
            kot-=radians(90)







def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """


