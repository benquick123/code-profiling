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
mine = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}

def sosedov(x, y, mine):
    stevec = 0
    for xm,ym in mine:
        if (x-1 <= xm <= x+1) and (y-1 <= ym <= y+1) and (x,y) != (xm, ym):
            stevec += 1
    return stevec
print(sosedov(2, 1, mine))


def najvec_sosedov(mine, s, v):
    koliko = 0
    katero = (0, 0)
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) > koliko:
                koliko = sosedov(i, j, mine)
                katero = (i, j)
    return katero
print(najvec_sosedov(mine, 8, 4))


def brez_sosedov(mine, s, v):
    kateri = set()
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) == 0:
                kateri.add((i, j))
    return kateri
print(brez_sosedov(mine, 8, 4))


def po_sosedih(mine, s, v):
    slovar = {}
    for i in range(9):
        slovar[i] = set()
    for st in slovar:
        for i in range(s):
            for j in range(v):
                if sosedov(i, j, mine) == st:
                    slovar[st].add((i, j))
    return slovar
print(po_sosedih(mine, 8, 4))


########################
# Za oceno 7
pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]

def dolzina_poti(pot):
    dolzina = 0
    skok = list(zip(pot, pot[1:]))
    for ena,dva in skok:
        dolzina += abs(ena[0] - dva[0]) + abs(ena[1] - dva[1])
    return dolzina
print(dolzina_poti(pot))


def varen_premik(x0, y0, x1, y1, mine):
    vse = {(x0, y0)}
    if x0 < x1:
        for i in range(x0,x1+1):
            vse.add((i, y0))
    elif x0 > x1:
        for i in range(x1,x0+1):
            vse.add((i, y0))
    elif y0 < y1:
        for i in range(y0,y1+1):
            vse.add((x0, i))
    elif y0 > y1:
        for i in range(y1,y0+1):
            vse.add((x0, i))
    for vsak in vse:
        if vsak in mine:
            return False
    return True
print(varen_premik(2, 3, 2, 6, mine))


def varna_pot(pot, mine):
    if len(pot) == 1:
        if pot[0] in mine:
            return False
        else:
            return True
    skok = list(zip(pot, pot[1:]))
    for prvi,drugi in skok:
        if ((varen_premik(prvi[0], prvi[1], drugi[0], drugi[1], mine) != True)):
            return False
    return True
print(varna_pot(pot, mine))


########################
# Za oceno 8

def polje_v_mine(polje):
    polja = set()
    seznam = polje.split()
    for i in range(len(seznam)):
        for j in range(len(seznam[i])):
            if seznam[i][j] == "X":
                polja.add((j, i))
    izpis = (polja, len(seznam[0]), len(seznam))
    return izpis
print(polje_v_mine("...X.... .X....X. .XX..... ......X."))
#({(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}, 8, 4)


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


