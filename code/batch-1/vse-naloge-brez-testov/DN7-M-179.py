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

# def sosedov(x, y, mine):
#     # if x != 0 and y != 0:
#     sosedi = {(x+1,y+1),(x-1,y-1),(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y-1),(x-1,y+1)}
#     st_min = 0
#     for sosed in sosedi:
#         if sosed in mine:
#             st_min += 1
#         return st_min

# def sosedov(x, y, mine):
#     s = [(x-1, y+1), (x, y+1), (x+1, y+1), (x-1, y), (x+1, y), (x-1, y-1), (x, y-1), (x+1, y-1)]
#     m = []
#     for e in s:
#         if e in mine:
#             m.append(e)
#     return len(m)


def sosedov(x, y, mine):
    sosedi = {(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
              (x - 1, y), (x + 1, y),
              (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)}
    stevilo_min = 0
    for sosed in sosedi:
        if sosed in mine:
            stevilo_min += 1
    return stevilo_min

print(sosedov(2, 1, mine))
print(sosedov(3, 0, mine))

    # """
    # Vrni število sosedov polja s koordinatami `(x, y)` na katerih je mina.
    # Polje samo ne šteje.
    #
    # Args:
    #     x (int): koordinata x
    #     y (int): koordinata y
    #     mine (set of tuple of int): koordinate min
    #
    # Returns:
    #     int: število sosedov
    # """


def najvec_sosedov(mine, s, v):
    i = {}
    for x in range(s):
        for y in range(v):
            i[sosedov(x, y, mine)] = (x, y)
    return i[max(i)]

print(najvec_sosedov(mine, 8, 4))

    # """
    # Vrni koordinati polja z največ sosednjih min
    #
    # Args:
    #     mine (set of (int, int)): koordinate min
    #     s (int): širina polja
    #     v (int): višina polja
    #
    # Returns:
    #     tuple of int: koordinati polja
    #
    # """


def brez_sosedov(mine, s, v):
    brez = set()
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) == 0:
                brez.add((x,y))
    return brez


print(brez_sosedov(mine, 8, 4))

    # """
    # Vrni množico koordinat polj brez min na sosednjih poljih. Polje samo lahko
    # vsebuje mino.
    #
    # Args:
    #     mine (set of tuple of int): koordinate min
    #     s (int): širina polja
    #     v (int): višina polja
    #
    # Returns:
    #     set of tuple: polja brez min na sosednjih poljih
    # """


# def po_sosedih(mine, s, v):
#     i = 0
#     slovar = {}
#     for k in range(0, 9):
#         slovar[k] = {}
#     for x in range(s):
#         for y in range(v):
#            for a in sosedov(x, y, mine):
#                c = set()
#                if sosedov(x, y, mine) == k:
#                    c.add((x,y))
#     return slovar

def po_sosedih(mine, s, v):
    i = 0
    slovar = {}
    for k in range(0, 9):                 # kreiranje slovarjev
        slovar[k] = set()
    for x in range(s):
        for y in range(v):
            k = sosedov(x, y, mine)       # dodajanje
            slovar[k].add((x, y))
    return slovar


print(po_sosedih(mine, 8, 4))

    # """
    # Vrni slovar, katerega ključi so možna števila sosednjih polj z minami
    # (torej števila od 0 do 8), vrednosti pa množice koordinat polj s toliko
    # sosedami.
    #
    # Args:
    #     mine (set of tuple of int): koordinate min
    #     s (int): širina polja
    #     v (int): višina polja
    #
    # Returns:
    #     dict: (glej zgoraj)
    # """


########################
# Za oceno 7

pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]

from math import *

def dolzina_poti(pot):
    dol_poti = 0
    for tocka in pot:
        if tocka == pot[0]:
            prejsna = tocka
            continue
        dolzina = abs(prejsna[0]-tocka[0]) + abs(prejsna[1]-tocka[1])
        dol_poti += dolzina
        prejsna = tocka
    return dol_poti

print(dolzina_poti(pot))

    # """
    # Vrni dolžino podane poti, vključno z vmesnimi polji.
    #
    # Args:
    #     pot (list of tuple): seznam koordinat polj
    #
    # Returns:
    #     int: dolžina poti
    # """


def varen_premik(x0, y0, x1, y1, mine):
    if (x0, y0) in mine:
        return False
    elif x0 == x1:
        while y0 < y1:
            y0 += 1
            if (x0, y0) in mine: return False
        while y0 > y1:
            y0 -= 1
            if (x0, y0) in mine: return False
        return True
    elif y0 == y1:
        while x0 < x1:
            x0 += 1
            if (x0, y0) in mine: return False
        while x0 > x1:
            x0 -= 1
            if (x0, y0) in mine: return False
        return True
    else:
        return True

print(varen_premik(2, 1, 5, 1, mine))

    # """
    # Vrni `True`, če je pomik z (x0, y0) and (x1, y1) varen, `False`, če ni.
    #
    # Args:
    #     x0 (int): koordinata x začetnega polja
    #     y0 (int): koordinata y začetnega polja
    #     x1 (int): koordinata x končnega polja
    #     y1 (int): koordinata y končnega polja
    #     mine (set of tuple of int): koordinate min
    #
    # Returns:
    #     bool: `True`, če je premik varen, `False`, če ni.
    # """


def varna_pot(pot, mine):
    for koord in pot:
        if koord == pot[0]:
            if koord in mine: return False
            pred = koord
            print(pred)
            continue
        elif varen_premik(pred[0], pred[1], koord[0], koord[1], mine):
            print(pred, koord)
            pred = koord
            continue
        else:
            return False
    return True

mine1 = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}

print(varna_pot([(1, 1)], mine1))

    # """
    # Vrni `True`, če je podana pot varna, `False`, če ni.
    #
    # Args:
    #     pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
    #     mine (set of tuple of int): koordinate min
    #
    # Returns:
    #     bool: `True`, če je pot varna, `False`, če ni.
    # """


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


