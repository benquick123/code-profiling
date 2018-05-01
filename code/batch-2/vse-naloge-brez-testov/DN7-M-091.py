# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))

########################
# Za oceno 6
from math import hypot

def sosedov(x, y, mine):
    return sum([True for mina in mine if 0 < hypot(x-mina[0], y-mina[1]) < 2])

def najvec_sosedov(mine, s, v):
    return max({polje: sosedov(*polje, mine) for polje in vsa_polja(s, v)}, key = {polje: sosedov(*polje, mine) for polje in vsa_polja(s, v)}.get)

def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine, s, v):
    return {st_sosedov: {(x,y) for x,y in vsa_polja(s, v) if sosedov(x,y,mine) == st_sosedov} for st_sosedov in range(9)}

########################
# Za oceno 7

def dolzina_poti(pot):
    return int(sum([hypot(x0 - x1, y0 - y1) for (x0, y0), (x1, y1) in zip(pot, pot[1:])]))

def varen_premik(x0, y0, x1, y1, mine):
    return not any({(x, y) for x in range(min(x0, x1), max(x0, x1) + 1) for y in range(min(y0, y1), max(y0, y1) + 1)} & mine)

def varna_pot(pot, mine):
    return True if len(pot) == 0 else all([varen_premik(x0 , y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip([pot[0]] + pot, pot)])

########################
# Za oceno 8

def polje_v_mine(polje):
    seznam = polje.split()
    v, s = len(seznam), len(seznam[0])
    mine = set()
    y = 0
    for terka in seznam:
        x = 0
        for crka in terka:
            if crka == "X":
                mine.add((x, y))
            x += 1
        y += 1
    return(mine, s, v)

########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.

# ✓ ✓ ✓

########################
# Za oceno 10

def preberi_pot(ukazi):
    pot = [(0,0)]
    polozaj = [0,0]
    ukazi = ukazi.split()
    smeri = ["gor", "desno", "dol", "levo"] * len(ukazi)*8
    smer = len(ukazi)*4
    for ukaz in ukazi:
        if ukaz == "DESNO":
            smer += 1
        elif ukaz == "LEVO":
            smer -= 1
        else:
            if smeri[smer] == "gor":
                polozaj[1] -= int(ukaz)
            elif smeri[smer] == "desno":
                polozaj[0] += int(ukaz)
            elif smeri[smer] == "dol":
                polozaj[1] += int(ukaz)
            elif smeri[smer] == "levo":
                polozaj[0] -= int(ukaz)
            pot.append(tuple(polozaj))
    return pot

def zapisi_pot(pot):
    zeljena_smer = ukaz = ""
    smeri = ["gor", "desno", "dol", "levo"] * len(pot)*8
    smer = len(pot)*4
    for i in range(len(pot)-1):
        (x0, y0), (x1, y1) = pot[i], pot[i+1]
        if y0 < y1:
            zeljena_smer = "dol"
        elif y0 > y1:
            zeljena_smer = "gor"
        elif x0 < x1:
            zeljena_smer = "desno"
        elif x0 > x1:
            zeljena_smer = "levo"
        while smeri[smer] != zeljena_smer:
            ukaz += "DESNO "
            smer += 1
        ukaz += str(abs(x0 - x1 + y0 - y1)) + " "
    return ukaz

