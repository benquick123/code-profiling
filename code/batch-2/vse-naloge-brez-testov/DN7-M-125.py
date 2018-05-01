# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    stsosedov = 0
    for i in mine:
        if (x+1, y) == i: stsosedov += 1
        elif (x-1, y) == i: stsosedov += 1
        elif (x, y+1) == i: stsosedov += 1
        elif (x, y-1) == i: stsosedov += 1
        elif (x+1, y+1) == i: stsosedov += 1
        elif (x+1, y-1) == i: stsosedov += 1
        elif (x-1, y+1) == i: stsosedov += 1
        elif (x-1, y-1) == i: stsosedov += 1
    return stsosedov


def najvec_sosedov(mine, s, v):
    najsos = 0
    x, y = 0, 0
    for x1, y1 in vsa_polja(s, v):
        sos = sosedov(x1, y1, mine)
        if sos > najsos:
            najsos = sos
            x, y = x1, y1
    return (x, y)




def brez_sosedov(mine, s, v):
    polja = set()
    for x, y in vsa_polja(s, v):
        if sosedov(x, y, mine)>0:
            continue
        else: polja.add((x,y))
    return polja

def po_sosedih(mine, s, v):
    seznam = dict()
    for i in range(9):
        seznam[i] = set()
    for x, y in vsa_polja(s, v):
        for j in range(9):
            if sosedov(x, y, mine) == j:
                seznam[j].add((x, y))
    return seznam



########################
# Za oceno 7

def dolzina_poti(pot):
    dolzina = 0
    i = 0
    while i < len(pot):
        if i == len(pot)-1:
            break
        x, y = pot[i]
        x1, y1 = pot[i+1]
        dolzina += abs(y1-y)
        dolzina += abs(x1-x)
        i += 1
    return dolzina


def varen_premik(x0, y0, x1, y1, mine):
    jevaren = False
    if (x0, y0) not in mine and (x1, y1) not in mine:
        if x0 == x1 and y0 == y1:
            jevaren = True
        else:
            if y0 == y1 and x0 != x1:
                for x in range(min(x0, x1), max(x0, x1)+1):
                    if (x, y0) not in mine:
                        jevaren = True
                    else:
                        jevaren = False
                        break
            if x0 == x1 and y0 != y1:
                for y in range(min(y0, y1), max(y0, y1)+1):
                    if (x0, y) not in mine:
                        jevaren = True
                    else:
                        jevaren = False
                        break
    return jevaren


def varna_pot(pot, mine):
    jevarna = False
    i = 0
    if len(pot) == 1:
        if pot[0] in mine:
            return False
        else:
            return True
    if len(pot) == 0:
        return True
    while i < len(pot):
        if i == len(pot)-1:
            break
        x, y = pot[i]
        x1, y1 = pot[i+1]
        if varen_premik(x, y, x1, y1, mine) == True:
            jevarna = True
            i += 1
        else:
            jevarna = False
            break
    return jevarna


########################
# Za oceno 8

def polje_v_mine(polje):
    mine = set()
    s = len(polje.split()[0])
    v = len(polje.split())
    x = 0
    y = 0
    for i in polje:
        if i == "X":
            mine.add((x, y))
            x += 1
        if i == ".":
            x += 1
        if i == " ":
            x = 0
            y += 1

    return mine, s, v



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


