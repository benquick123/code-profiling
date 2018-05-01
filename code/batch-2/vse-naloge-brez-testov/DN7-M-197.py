minex = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}

def vsa_polja(s, v):
    """
    Generiraj vse koordinate (x, y) za polje s podano širino in višino
    """
    return ((x, y) for x in range(s) for y in range(v))
from collections import  defaultdict
import itertools
from math import sqrt
import string

def sosedov(x, y, mine):
    return sum([1
            for sosed in [(x-1, y), (x+1, y), (x, y-1), (x, y +1), (x-1, y-1), (x-1, y+1), (x+1, y+1), (x+1, y-1)]
                if sosed in mine])


def najvec_sosedov(mine, s, v):
    return (max([[polje, sosedov(polje[0], polje[1], mine)] for polje in vsa_polja(s, v)], key=lambda x: x[1])[0])

def brez_sosedov(mine, s, v):
    return set([polje for polje in vsa_polja(s, v) if sosedov(polje[0], polje[1], mine) == 0])

def po_sosedih(mine, s, v):
    return {i: set((x, y)for x, y in vsa_polja(s, v) if i == sosedov(x, y, mine)) for i in range(9)}


########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([sqrt((x0-x1)**2 + (y0-y1)**2) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])

def varen_premik(x0, y0, x1, y1, mine):


# najprej generira korake, nato preverei, ali so varni
    return all ([premik not in mine
           for situacija in [[(x0, y0+i) for i in range(0, x1 - x0 + y1 - y0 + 1)]
                        if x1 - x0 == 0 and y1 - y0 > 0
                  else [(x0, y0 - i) for i in range(0, abs(x1 - x0 + y1 - y0) + 1)]
                        if x1 - x0 == 0 and y1 - y0 < 0
                  else [(x0+i, y0) for i in range(0, x1 - x0 + y1 - y0 + 1)]
                        if y1 - y0 == 0 and x1 - x0 > 0
                  else [(x0 - i, y0) for i in range(0, abs(x1 - x0 + y1 - y0) + 1)]
                        if y1 - y0 == 0 and x1 - x0 < 0
                  else [(x0, y0)]
                        if y1 - y0 == 0 and x1 - x0 == 0
                  else "nekaj ne štima"]
           for premik in situacija])

def varna_pot(pot, mine):
    return all([
        all([varen_premik(x0, y0, x1, y1, mine)
            for (x0, y0), (x1, y1) in zip(pot, pot[1:])])
            if (len(pot) > 1)
            else (pot[0] not in mine) if len(pot) == 1
            else True
            ])
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
    out = set()
    max_y = []
    max_x = []
    for y_indeks, vrstica in enumerate(polje.split()):
        max_y.append(y_indeks)
        for x_indeks, crka in enumerate(vrstica):
            max_x.append(x_indeks)
            if crka == "X":
                out |= {(x_indeks, y_indeks)}
    return (out, max(max_x)+1, max(max_y)+1)

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
    smer_count = 0
    pot = [(0,0)]
    for beseda in ukazi.split():
        if beseda == "DESNO":
            smer_count +=1
        if beseda == "LEVO":
            smer_count += -1
        if beseda.isdigit():
            orientacija = smer_count%4
            trenutni_x, trenutni_y = pot[-1][0], pot[-1][1]
            premik = int(beseda)
            if orientacija == 0:
                pot.append((trenutni_x, trenutni_y-premik))
            if orientacija == 1:
                pot.append((trenutni_x + premik, trenutni_y))
            if orientacija == 2:
                pot.append((trenutni_x, trenutni_y + premik))
            if orientacija == 3:
                pot.append((trenutni_x - premik, trenutni_y))
    return pot
def zapisi_pot(pot):
    out_navodila = ""
    orientacija = 0

    cene_premikov = {
            (0, 1) : 1,
            (0, 2) : 2,
            (0, 3) : 3,
            (1, 0) : 3,
            (1, 2) : 1,
            (1, 3) : 2,
            (2, 0) : 2,
            (2, 1) : 3,
            (2, 3) : 1,
            (3, 0) : 1,
            (3, 1) : 2,
            (3, 2) : 3,
                    }


    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        dx = x1 -x0
        dy = y1- y0
        #print (dx, dy, "to sta dx in dy")
        if dx == 0 and dy > 0:
            orientacija_cilj = 2

        if dx == 0 and dy < 0:
            orientacija_cilj = 0

        if dy == 0 and dx > 0:
            orientacija_cilj = 1

        if dy == 0 and dx < 0:
            orientacija_cilj = 3
        if orientacija_cilj != orientacija:
            out_navodila += ("DESNO \n"*cene_premikov[(orientacija, orientacija_cilj)])
        out_navodila += str((max(abs(dy), abs(dx)))) + "\n"
        orientacija = orientacija_cilj
    return out_navodila

