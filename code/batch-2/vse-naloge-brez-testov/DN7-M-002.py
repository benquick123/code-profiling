# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):

    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):

    sosedi = 0
    for i in mine:
        if (x-1,y) == i:
            sosedi += 1
        elif(x+1,y) == i:
            sosedi += 1
        elif(x,y-1) == i:
            sosedi += 1
        elif(x,y+1) == i:
            sosedi += 1
        elif (x+1, y+1) == i:
            sosedi += 1
        elif(x+1,y-1) == i:
            sosedi += 1
        elif(x-1,y+1) == i:
            sosedi += 1
        elif(x-1,y-1) == i:
            sosedi += 1
    return sosedi


def najvec_sosedov(mine, s, v):
    najmin = 0
    koordinate = (0,0)
    for i,j in vsa_polja(s,v):
        if sosedov(i,j,mine) > najmin:
            najmin += sosedov(i,j,mine)
            koordinate = (i,j)
    return koordinate

def brez_sosedov(mine, s, v):
    nesosedi =  set()
    for x,y in vsa_polja(s,v):
        if sosedov(x,y,mine) == 0:
            nesosedi.add((x,y))
    return nesosedi

def po_sosedih(mine, s, v):
    slovar = {}
    for i in range(9):
        slovar[i] = set()
    for x,y in vsa_polja(s,v):
        for j in range(9):
            if sosedov(x,y,mine) == j:
                slovar[j].add((x,y))
    return slovar


########################
# Za oceno 7

def dolzina_poti(pot):
    dolzina = 0
    i = 0

    while i < len(pot) -1:
        x, y = pot[i]
        x1, y1 = pot[i+1]
        dolzina += abs(x1 - x)
        dolzina += abs(y1 - y)
        i += 1
    return dolzina





def varen_premik(x0, y0, x1, y1, mine):
    mina = True
    detonation = True
    xx0 = x0
    yy0 = y0
    while detonation == True:
        if (xx0,yy0) in mine:
            detonation = False
            mina = False
            break
        if xx0 != x1 and yy0 != y1:
            if x1 > xx0:
                xx0 += 1
            else:
                xx0 -= 1
            if y1 > yy0:
                yy0 += 1
            else:
                yy0 -= 1

        elif xx0 != x1 and yy0 == y1:
            if x1 > xx0:
                xx0 += 1
            else:
                xx0 -= 1

        elif xx0 == x1 and yy0 != y1:
            if y1 > yy0:
                yy0 += 1
            else:
                yy0 -= 1

        elif xx0 == x1 and yy0 == y1:
            detonation = False

    return mina





def varna_pot(pot, mine):
    i = 0
    jeVarna = False
    if len(pot) == 1:
        x0, y0 = pot[i]
        if (x0,y0) not in mine:
            jeVarna = True
    if len(pot) == 0:
        jeVarna = True
    else:
        while i < len(pot)-1:
            x0,y0 = pot[i]
            x1,y1 = pot[i+1]
            if varen_premik(x0,y0,x1,y1,mine) == True:
                jeVarna = True
            else:
                jeVarna = False
                return jeVarna
            i += 1
    return jeVarna

########################
# Za oceno 8

def polje_v_mine(polje):
    polje2 = polje.split()
    mina = set()
    v = len(polje2)
    s = len(polje2[0])
    x1 = 0
    y1 = 0
    i = 0
    while i < len(polje):
        if polje[i] is " ":
            i+= 1
        else:
            if polje[i] == "X":
                mina.add((x1, y1))
            if x1 == s-1:
                x1 = -1
                y1 += 1
            i += 1
            x1 += 1

    return (mina,s,v)


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


