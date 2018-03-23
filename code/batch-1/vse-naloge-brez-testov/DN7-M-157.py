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
    st = 0
    for a in mine:
        if a[0] !=x or a[1]!=y:
            if abs(a[0]-x) <= 1 and abs(a[1]-y) <= 1:
                st+=1
    return st


def najvec_sosedov(mine, s, v):
    i = 0
    j = 0
    xNaj = 0
    yNaj = 0
    while i < s:
        j=0
        while j < v:
            if sosedov(i,j,mine) >= sosedov(xNaj,yNaj,mine):
                xNaj = i
                yNaj = j
            j+=1
        i+=1
    return xNaj,yNaj


def brez_sosedov(mine, s, v):
    brezSos = set()
    i=0
    while i < s:
        j=0
        while j < v:
            if sosedov(i,j,mine) == 0:
                brezSos.add((i,j))
            j+=1
        i+=1
    return brezSos


def po_sosedih(mine, s, v):
    sezPoSos = {}
    i=0
    while(i<9):
        sezPoSos[i] = set()
        i += 1
    i=0
    while i < s:
        j = 0
        while j < v:
            stSos = sosedov(i,j,mine)
            sezPoSos[stSos].add((i,j))
            j += 1
        i += 1
    return sezPoSos


########################
# Za oceno 7

def dolzina_poti(pot):
    prviKorak = 0
    dolPoti = 0
    for a, b in pot:
        if prviKorak == 0:
            x = a
            y = b
            prviKorak = 1
        dolPoti += abs(x - a) + abs(y - b)
        x = a
        y = b
    return dolPoti


def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1:
        if y0 > y1:
            y0,y1 = y1,y0
        i = y0
        while i <= y1:
            for x,y in mine:
                if (x0,i) == (x,y):
                    return False
            i += 1
    if y0 == y1:
        if x0 > x1:
            x0,x1 = x1,x0
        i = x0
        while i <= x1:
            for x,y in mine:
                if (i,y0) == (x,y):
                    return False
            i += 1
    return True


def varna_pot(pot, mine):
    if len(pot) == 1:
        if varen_premik(pot[0][0],pot[0][1],pot[0][0],pot[0][1],mine) == False:
            return False
    i = 0
    while i+1 < len(pot):
        if varen_premik(pot[i][0], pot[i][1], pot[i + 1][0], pot[i + 1][1], mine) == False:
            return False
        i += 1
    return True


########################
# Za oceno 8

def polje_v_mine(polje):
    x = 0
    y = 0
    s = 0
    v = 0
    mine = set()
    i = 0
    while i< len(polje):
        if polje[i] == " ":
            x = 0
            y += 1
        if polje[i] == "X":
            mine.add((x,y))
            x += 1
        if polje[i] == ".":
            x += 1
        i += 1
    s = x
    v = y+1
    return mine,s,v

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


