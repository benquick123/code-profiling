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


#######################
# Za oceno 6

def sosedov(x, y, mine):
    i = 0
    y1 = y - 1
    while y1 - y <= 1:
        x1 = x - 1
        while x1 - x <= 1:
            if (x1, y1) in mine and not (x1 == x and y1 == y):
                i = i + 1
            x1 = x1 + 1
        y1 = y1 + 1
    return(i)


def najvec_sosedov(mine, s, v):
    i=0
    x=0
    y=0
    naj = 0
    while i < s:
        j=0
        while j<v:
            if sosedov(i,j, mine)>naj:
                naj=sosedov(i,j, mine)
                x=i
                y=j
            j=j+1
        i=i+1
    return (x,y)

def brez_sosedov(mine, s, v):
    i = 0
    seznam = set()
    while i < s:
        j = 0
        while j < v:
            if sosedov(i, j, mine) == 0:
                seznam.add((i,j))
            j = j + 1
        i = i + 1
    return (seznam)

def po_sosedih(mine, s, v):
    slovar = {}
    i=0
    while i < 9:
        slovar[i]=set()
        i+=1

    i = 0
    while i < s:
        j = 0
        while j < v:
            slovar[sosedov(i,j,mine)].add((i,j))
            j = j + 1
        i = i + 1
    return (slovar)

########################
# Za oceno 7

def dolzina_poti(pot):
    i=0
    if len(pot) <1 :
        return 0
    x1, y1 = pot[0]
    for x, y in pot[1:]:
        i = abs((x + y) - (x1 + y1)) + i
        x1 = x
        y1 = y
    return(i)

def varen_premik(x1, y1, x2, y2, mine):
    if (x1, y1) in mine:
        return False
    while not (x1 == x2 and y1 == y2):
        if x1 == x2 and y1 > y2:
            y1 -= 1
        if x1 == x2 and y1 < y2:
            y1 += 1
        if y1 == y2 and x1 > x2:
            x1 -= 1
        if y1 == y2 and x1 < x2:
            x1 += 1
        if (x1, y1) in mine:
            return False
    return True

def varna_pot(pot, mine):
    if len(pot) > 0:
        x1,y1=pot[0]
        for x,y in pot:
            if varen_premik(x1,y1,x,y,mine) == False:
                return False
            x1,y1=x,y
        return True
    else:
        return True

########################
# Za oceno 8

def polje_v_mine(polje):
    koord = set()
    x, y = 0, 0

    for vrstica in polje.split():
        x = 0
        for znak in vrstica:
            if znak == 'X':
                koord.add((x, y))
            x += 1
        y += 1

    return((koord, len(vrstica), y))


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


