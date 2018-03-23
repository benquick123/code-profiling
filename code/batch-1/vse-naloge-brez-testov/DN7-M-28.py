# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
import collections

def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    return sum([1 for xm, ym in mine if (xm+1 == x or xm == x or xm-1 == x) and (ym+1 == y or ym == y or ym-1 == y) and not (xm == x and ym == y)])


def najvec_sosedov(mine, s, v):
    return max({key: sosedov(key[0], key[1], mine) for key in vsa_polja(s, v)}, key={key: sosedov(key[0], key[1], mine) for key in vsa_polja(s, v)}.get)


def brez_sosedov(mine, s, v):
    return {key for key in vsa_polja(s, v) if sosedov(key[0], key[1], mine) == 0}


def po_sosedih(mine, s, v):
    return {key: {(i, j) for i in range(s) for j in range(v) if sosedov(i, j, mine) == key} for key in range(9)}


########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([abs(x1 - x0) + abs(y1 - y0) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])


def varen_premik(x0, y0, x1, y1, mine):
    return all([True if ((x, y) not in mine) else False for x in range(min(x0, x1), max(x0, x1)+1) for y in range(min(y0, y1), max(y0, y1)+1)])


def varna_pot(pot, mine):
    return all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:] or pot)])


########################
# Za oceno 8

def polje_v_mine(polje):
    polje = polje.strip().split(" ")
    mine = set()
    y = 0
    for vrstica in polje:
        x = 0
        for m in vrstica:
            if m == 'X':
                mine.add((x, y))
            x += 1
        y += 1
    return (mine, len(polje[0]), len(polje))


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    pot = [(0, 0)]
    smeri = ["gor", "desno", "dol", "levo"]
    smer = 0
    for ukaz in ukazi.split("\n"):
        if ukaz == "DESNO" or ukaz == "LEVO":
            if ukaz == "DESNO":
                smer += 1
                if smer > 3:
                    smer = 0
            else:
                smer -= 1
                if smer < 0:
                    smer = 3
        else:
            if smeri[smer] == "gor":
                pot.append((pot[-1][0], pot[-1][1] - int(ukaz)))
            elif smeri[smer] == "desno":
                pot.append((pot[-1][0] + int(ukaz), pot[-1][1]))
            elif smeri[smer] == "dol":
                pot.append((pot[-1][0], pot[-1][1] + int(ukaz)))
            elif smeri[smer] == "levo":
                pot.append((pot[-1][0] - int(ukaz), pot[-1][1]))
    return pot


def zapisi_pot(pot):
    ukaz = []
    smer = 0
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if y0 > y1:
            smer2 = 0
        elif x0 < x1:
            smer2 = 1
        elif y0 < y1:
            smer2 = 2
        elif x0 > x1:
            smer2 = 3
        while smer != smer2:
            ukaz.append("DESNO")
            smer += 1
            if smer > 3:
                smer = 0
        ukaz.append(str(abs(x0 - x1) + abs(y0 - y1)))
    return "\n".join(ukaz)


