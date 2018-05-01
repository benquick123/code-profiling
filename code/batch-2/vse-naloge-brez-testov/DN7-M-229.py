# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
import math

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
    return len([(x1,y1) for x1, y1 in mine
            if (abs(x-x1) < 2 and abs(y-y1) < 2) and (abs(x-x1) > 0 or abs(y-y1) > 0)])


def najvec_sosedov(mine, s, v):
    return {sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)}[max({sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)})]

def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x,y,mine) == 0}


def po_sosedih(mine, s, v):
    return {i:{(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine) == i} for i in range(0,9)}


########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([math.sqrt((x1-x0)**2 + (y1-y0)**2) for (x0,y0),(x1,y1) in zip(pot,pot[1:])])


def varen_premik(x0, y0, x1, y1, mine):
    return [({(x0, y) for y in range(min(y0, y1), max(y0, y1)+1)} & mine) == set() and {(x, y0) for x in range(min(x0, x1), max(x0, x1)+1)} & mine == set()][0]

def varna_pot(pot, mine):
    return [all([varen_premik(x0,y0,x1,y1,mine) for (x0,y0),(x1,y1) in zip(pot,pot[1:])]) and all([(x0,y0) not in mine for x0,y0 in pot])][0]


########################
# Za oceno 8

def polje_v_mine(polje):
    polje = polje.rstrip()
    polje = polje.lstrip()
    polje = polje.split(" ")
    koordinate = set()
    v = 0
    for vrsta in polje:
        z = 0
        for znak in vrsta:
            if znak == "X":
                koordinate.add((z, v))
            z += 1
        v += 1
    return koordinate, len(polje[0]), len(polje)


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    ukazi = ukazi.split()
    x = 0
    y = 0
    seznam = [(x,y)]
    smer = 0
    for n in ukazi:
        if n == "DESNO":
            smer = smer+1
            if smer > 3:
                smer = 0
        elif n == "LEVO":
            smer = smer-1
            if smer < 0:
                smer = 3
        else:
            if smer == 0:
                y = y-int(n)
            elif smer == 1:
                x = x + int(n)
            elif smer == 2:
                y = y + int(n)
            else:
                x = x - int(n)
            seznam.append((x, y))
    return seznam




def zapisi_pot(pot):
    smer = ["smer0", "smer1", "smer2", "smer3"]
    start = "smer0"
    ukazi = ""
    for (x1, y1), (x2, y2) in zip(pot, pot[1:]):
        if x2 > x1:
            end = "smer1"
        elif x2 < x1:
            end = "smer3"
        elif y2 > y1:
            end = "smer2"
        else:
            end = "smer0"
        zamik = smer.index(end) - smer.index(start)
        for n in range(0, zamik):
            ukazi = ukazi + " " + "DESNO"
        if x1 == x2:
            ukazi = ukazi + " " + str(abs(y2 - y1))
        else:
            ukazi = ukazi + " " + str(abs(x2 - x1))
        smer = smer[smer.index(end):] + smer[:smer.index(end)]
        start = end
    return ukazi

