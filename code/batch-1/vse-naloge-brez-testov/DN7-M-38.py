# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.

def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))

########################
# Za oceno 6
def sosedov(x, y, mine): 
    return len(mine & {(x-1+i, y-1+j) for i in range(3) for j in range(3) if (i, j) != (1,1)})

def najvec_sosedov(mine, s, v):
    return [(x, y) for x, y in vsa_polja(s, v) \
    if max({sosedov(x, y, mine) for x, y in vsa_polja(s, v)}) == sosedov(x, y, mine)][0]

def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine, s, v):
    return {i : {(x, y) for x, y in vsa_polja(s, v) if i == sosedov(x, y, mine)} for i in range(0, 9)}

########################
# Za oceno 7
def dolzina_poti(pot):
    return sum([abs((x2 - x1) + (y2 - y1)) for (x1, y1), (x2, y2) in zip(pot, pot[1:])])

def varen_premik(x0, y0, x1, y1, mine):
    return not (mine & {(x,y) for x in range(min(x0,x1),max(x0,x1)+1) for y in range(min(y0,y1),max(y0,y1)+1)})

def varna_pot(pot, mine):
    return all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])]) if len(pot) > 1 else all([(x0,y0) not in mine for (x0, y0) in pot])

########################
# Za oceno 8
def polje_v_mine(polje):
    return ({(x,y) for y, vrstica in enumerate(polje.split(" ")) for x, crka in enumerate(vrstica) if crka == "X"}, len(polje.split(" ")[0]), len(list(filter(None, polje.split(" ")))))

########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.

########################
# Za oceno 10

def orentacija(usmerjen, ukaz):
    smeri = ["GOR", "DESNO", "DOL", "LEVO", "GOR"]
    if ukaz == "DESNO":
        return [potem for trenutna, potem in zip(smeri, smeri[1:]) if trenutna == usmerjen]
    else:
        return [potem for trenutna, potem in zip(smeri[1:], smeri) if trenutna == usmerjen]
    return usmerjen
def preberi_pot(ukazi):
    smeri = {"GOR": (0, -1), "DESNO": (1, 0), "DOL": (0, 1), "LEVO": (-1, 0)}
    pot = [(0, 0)]
    usmerjen = "GOR"
    for ukaz in ukazi.split("\n"):
        if ukaz == "DESNO" or ukaz == "LEVO":
            usmerjen = ''.join(orentacija(usmerjen, ukaz))
        else:
            pot.append((pot[-1][0]+(int(ukaz)*smeri[usmerjen][0]), pot[-1][1]+(int(ukaz)*smeri[usmerjen][1])))
    return pot

from math import *
def zapisi_pot(pot):
    usmerjen = "GOR"
    ukazi = list()
    for (trenutn_x, trenutn_y), (nasledn_x, nasledn_y) in zip(pot, pot[1:]):
        premik_x = nasledn_x - trenutn_x
        premik_y = nasledn_y - trenutn_y
        moral = ("DESNO" if premik_x > 0 else "LEVO") if premik_x != 0 else ("DOL" if premik_y > 0 else "GOR")
        while True:
            if usmerjen == moral:
                break
            else:
                ukazi.append("DESNO")
                usmerjen = ''.join(orentacija(usmerjen, "DESNO"))
        ukazi.append(str(abs(premik_x) + abs(premik_y)))
    return "\n".join(ukazi)

