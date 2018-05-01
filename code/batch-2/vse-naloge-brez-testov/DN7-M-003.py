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

import collections


def sosedov(x, y, mine):
    bomb = 0
    for a in mine:
        if a == (x + 1, y) or a == (x - 1, y) or a == (x, y + 1) or a == (x, y - 1) or a == (x + 1, y + 1) or a == (x + 1, y - 1) or a == (x - 1, y + 1) or a == (x - 1, y - 1):
            bomb += 1
    return bomb


def najvec_sosedov(mine, s, v):
    a, b = 0, 0
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) > sosedov(a, b, mine):
                a, b = x, y
    return a, b


def brez_sosedov(mine, s, v):
    prosta_pot = set()
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) == 0:
                prosta_pot.add((x, y))
    return prosta_pot


def po_sosedih(mine, s, v):
    bojno_stanje = collections.defaultdict(set)
    for n in range(9):
        bojno_stanje[n] = set()
    for x in range(s):
        for y in range(v):
            bojno_stanje[sosedov(x, y, mine)].add((x, y))
    return bojno_stanje



########################
# Za oceno 7



def dolzina_poti(pot):
    koraki = 0
    pot_x, pot_y = [], []
    if pot:
        for x, y in pot:
            pot_x.append(x), pot_y.append(y)
        current_x, current_y = pot_x[0], pot_y[0]
        for x1 in pot_x:
            if x1 != current_x:
                koraki += abs(current_x - x1)
                current_x = x1
        for y1 in pot_y:
            if y1 != current_y:
                koraki += abs(current_y - y1)
                current_y = y1
    return koraki


def varnost(pot, mine):
    varnost = True
    for korak in pot:
        if korak in mine:
            varnost = False
            break
    return varnost

def premik(x0, y0, x1, y1):
    pot = [(x0, y0)]
    if x0 == x1:
        a = y0
        while a != y1:
            if y1 > y0:
                pot.append((x0, a + 1))
                a = a + 1
            else:
                pot.append((x0, a - 1))
                a = a - 1
    if y0 == y1:
        b = x0
        while b != x1:
            if x1 > x0:
                pot.append((b + 1, y0))
                b = b + 1
            else:
                pot.append((b - 1, y0))
                b = b - 1
    return pot

def varen_premik(x0, y0, x1, y1, mine):
    return varnost(premik(x0, y0, x1, y1), mine)

def varna_pot(pot, mine):
    varnost = True
    potovanje = list()
    if pot:
        if len(pot) > 1:
            while pot[-1] not in potovanje:
                for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
                    korak = premik(x0, y0, x1, y1)
                    for a in korak:
                        potovanje.append(a)
                    pot = pot[1 :]
            for step in potovanje:
                if step in mine:
                    varnost = False
                    break
        if len(pot) == 1:
            for z in pot:
                if z in mine:
                    varnost = False
    return varnost





########################
# Za oceno 8


def polje_v_mine(polje):
    if polje.endswith(" "):
        polje = polje[ : -1]
    polje = polje.split(" ")
    koordinate = set()
    s = 0
    v = len(polje)
    x = 0
    for jarek in polje:
        y = polje.index(jarek)
        s = len(jarek)
        valuex = 0
        for crka in jarek:
            if crka == ".":
                valuex += 1
            else:
                x = valuex
                valuex += 1
            koordinate.add((x, y))
    return koordinate, s, v



def sovrazne_koordinate(seznam):
    koordinate = set()
    for podatki in seznam:
        x, y, mina = podatki
        if mina == True:
            koordinate.add((x, y))
    return koordinate

def takticna_ocena(x, y, polje):
    polje1 = polje
    if polje.endswith(" "):
        polje1 = polje[: -1]
    polje1 = polje1.split(" ")
    jarek = polje1[y]
    znak = jarek[x]
    if znak == "X":
        return True
    else:
        return False

def strateski_seznam(polje):
    seznam = []
    polje1 = polje
    if polje.endswith(" "):
        polje1 = polje[ : -1]
    polje1 = polje1.split(" ")
    visina = len(polje1)
    for jarek in polje1:
        sirina = len(jarek)
    map = vsa_polja(sirina, visina)
    for x, y in map:
        pozicija = (x, y, takticna_ocena(x, y, polje))
        seznam.append(pozicija)
    return seznam

def polje_v_mine(polje):
    koordinate = set()
    karta = strateski_seznam(polje)
    karta1 = sovrazne_koordinate(karta)
    polje1 = polje
    if polje.endswith(" "):
        polje1 = polje[ : -1]
    polje1 = polje1.split(" ")
    visina = len(polje1)
    for jarek in polje1:
        sirina = len(jarek)
    return karta1, sirina, visina

########################
# Za oceno 9

def sosedov(x,y, mine):
    return len([a for a in mine if a == (x + 1, y) or a == (x - 1, y) or a == (x, y + 1) or a == (x, y - 1) or a == (x + 1, y + 1) or a == (x + 1, y - 1) or a == (x - 1, y + 1) or a == (x - 1, y - 1)])

def najvec_sosedov(mine, s, v):
    return max([(a, b) for a, b, c in [(x, y, sosedov(x, y, mine)) for x, y in vsa_polja(s, v)] if c == (max(c for a, b, c in [(x, y, sosedov(x, y, mine)) for x, y in vsa_polja(s, v)]))])

def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine, s, v):
    return {n :  {koordinate for koordinate, mine in [((x, y), z) for x, y, z in [koordinate for koordinate in[(x, y, sosedov(x, y, mine)) for x, y in vsa_polja(s, v)]]] if mine == n} for n in range(9)}

def dolzina_poti(pot):
    return sum([w + z for w, z in [(abs(a2 - a1), abs(b2 - b1)) for (a1, b1), (a2, b2) in [((x0, y0), (x1, y1)) for (x0, y0), (x1, y1) in zip(pot, pot[1: ])]]])

def varen_premik(x0, y0, x1, y1, mine):
    return all([bomba not in mine for bomba in [[[(x0, z) for z in range(y0, y1 + 1)] if y0 < y1 else [(x0, z) for z in range(y0, y1 - 1, -1)]][0] if x0 == x1 else [[(z, y0) for z in range(x0, x1 + 1)] if x0 < x1 else [(z, y0) for z in range(x0, x1 - 1, -1)]][0]][0]])

def varna_pot(pot, mine):
    return all([all([all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in [((x0, y0), (x1, y1)) for (x0, y0), (x1, y1) in zip(pot, pot[1:])]]) if len(pot) > 1 else pot[0] not in mine]) if len(pot) > 0 else True])


########################
# Za oceno 10

def preberi_pot(ukaz):
    ukaz = ukaz.split("\n")
    pot, orientacija = [(0, 0)], "gor"
    usmeritve = ["gor", "desno", "dol", "levo"]
    x, y = 0, 0
    for command in ukaz:
        if command == "DESNO":
            orientacija = usmeritve[(usmeritve.index(orientacija) + 1)%4]
        elif command == "LEVO":
            orientacija = usmeritve[(usmeritve.index(orientacija) - 1)%4]
        else:
            command = int(command)
            if orientacija == "gor":
                x1, y1 = x, (y - command)
                x, y = x1, y1
                pot.append((x, y))
            elif orientacija == "dol":
                x1, y1 = x, (y + command)
                x, y = x1, y1
                pot.append((x, y))
            elif orientacija == "desno":
                x1, y1 = (x + command), y
                x, y = x1, y1
                pot.append((x, y))
            elif orientacija == "levo":
                x1, y1 = (x - command), y
                x, y = x1, y1
                pot.append((x, y))
    return pot



def zapisi_pot(ukazi):
    pot = ""
    ukazi1 = zip(ukazi, ukazi[1 :])
    usmeritve_desno = ["gor", "desno", "dol", "levo"]
    trenutna_orientacija = "gor"
    for (x0, y0), (x1, y1) in ukazi1:
        if x1 - x0 == 0:
            gibov = abs(y1 - y0)
            if y1 - y0 < 0:
                orientacija = "gor"
            if y1 - y0 > 0:
                orientacija = "dol"
        if y1 - y0 == 0:
            gibov = abs(x1 - x0)
            if x1 - x0 < 0:
                orientacija = "levo"
            if x1 - x0 > 0:
                orientacija = "desno"
        gibov_v_desno = 0
        while trenutna_orientacija != orientacija:
            trenutna_orientacija = usmeritve_desno[(usmeritve_desno.index(trenutna_orientacija) + 1)%4]
            gibov_v_desno += 1
        pot = pot + (gibov_v_desno * "\nDESNO") + "\n" + str(gibov)
    pot = pot.rstrip()
    pot = pot.lstrip()
    return pot


