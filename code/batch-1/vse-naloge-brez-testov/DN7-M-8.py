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
def izracun_razlike(x, y):
    if x >= y:
        rezultat = x - y
    else:
        rezultat = y - x
    return rezultat

def sosedov(x, y, mine):
    števec = 0
    if (x-1,y-1) in mine:
        števec += 1
    if (x-1,y) in mine:
        števec += 1
    if (x-1,y+1) in mine:
        števec += 1
    if (x,y-1) in mine:
        števec += 1
    if (x,y+1) in mine:
        števec += 1
    if (x+1,y-1) in mine:
        števec += 1
    if (x+1,y) in mine:
        števec += 1
    if (x+1,y+1) in mine:
        števec += 1
    return števec


def ni_sosedov(x,y, mine):

    if sosedov(x,y,mine) == 0:
        return False
    if (x,y) in mine:
        return False
    else:
        return True


def najvec_sosedov(mine, s, v):
    trenutno_najvecji = 0
    trenutno_polje = (0,0)
    if len(mine) == 1:
        return (0,0)
    for x in range(s+1):
        for y in range(v+1):
            sosedi = sosedov(x,y,mine)
            if sosedi > trenutno_najvecji:
                trenutno_najvecji = sosedi
                trenutno_polje = (x,y)
    return trenutno_polje

def brez_sosedov(mine, s, v):
    množica = set()

    for x in range(s):
        for y in range(v):
            if sosedov(x,y,mine) == 0:
                množica.add((x,y))
    return množica



def po_sosedih(mine, s, v):
    nic = set()
    ena = set()
    dva = set()
    tri = set()
    stiri = set()
    pet = set()
    sest = set()
    sedem = set()
    osem = set()
    slovar = dict()


    for x in range(s):
        for y in range(v):
            if sosedov(x,y,mine) == 0:
                nic.add((x,y))
            if sosedov(x,y,mine) == 1:
                ena.add((x,y))
            if sosedov(x,y,mine) == 2:
                dva.add((x,y))
            if sosedov(x,y,mine) == 3:
                tri.add((x,y))
            if sosedov(x,y,mine) == 4:
                stiri.add((x,y))
            if sosedov(x,y,mine) == 5:
                pet.add((x,y))
            if sosedov(x,y,mine) == 6:
                sest.add((x,y))
            if sosedov(x,y,mine) == 7:
                sedem.add((x,y))
            if sosedov(x,y,mine) == 8:
                osem.add((x,y))
    slovar[0] = nic
    slovar[1] = ena
    slovar[2] = dva
    slovar[3] = tri
    slovar[4] = stiri
    slovar[5] = pet
    slovar[6] = sest
    slovar[7] = sedem
    slovar[8] = osem

    return slovar


#mine3 = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
#print(sosedov(8,2,mine3))


########################
# Za oceno 7

def dolzina_poti(pot):
    dolzina = 0
    if len(pot) == 0:
        return 0
    x1 = pot[0][0]
    y1 = pot[0][1]
    for x,y in pot:
        if x == x1 and y == y1:
            dolzina += 0
            x1 = x
            y1 = y
        elif x == x1 and y != y1:
            dolzina += izracun_razlike(y,y1)
            x1 = x
            y1 = y
        elif x != x1 and y == y1:
            dolzina += izracun_razlike(x,x1)
            x1 = x
            y1 = y
    return dolzina


def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1 and y0 == y1:
        return False
    if x0 == x1 and y0 != y1:
        if y0 < y1:
            while y0 <= y1:
                if (x0,y0) in mine:
                    return False
                y0 += 1
        else:
            while y1 <= y0:
                if (x0,y0) in mine:
                    return False
                y0 -= 1
        return True
    if x0 != x1 and y0 == y1:
        if x0 < x1:
            while x0 <= x1:
                if (x0,y0) in mine:
                    return False
                x0 += 1
        else:
            while x1 <= x0:
                if (x0,y0) in mine:
                    return False
                x0 -= 1
        return True


def varna_pot(pot, mine):
    if len(pot) == 0:
        return True
    if len(pot) == 1:
        if (pot[0][0],pot[0][1]) in mine:
            return False
        return True
    x0 = pot[0][0]
    y0 = pot[0][1]
    for x,y in pot[1:]:
        if varen_premik(x0, y0, x, y, mine) is False:
            return False
        x0 = x
        y0 = y
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


